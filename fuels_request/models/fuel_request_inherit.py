# -*- coding: utf-8 -*-

from odoo import models, fields, api


class FuelsRequest(models.Model):
    _name = 'fleet.fuel.request'


    name = fields.Char(string="Reference", default="New", tracking=True)
    date = fields.Date(string="Date", default=fields.Date.today, tracking=True)
    requested_by = fields.Many2one('hr.employee', string="Requested By", tracking=True)
    # requester_job_title = fields.Many2one('hr.job', string="Requester Job Title", related="requested_by.job_id", store=True)
    vehicle = fields.Many2one('fleet.vehicle', string="Vehicle", required=True, tracking=True)
    current_fuel_level = fields.Float(string="Current Fuel Level", tracking=True)
    current_milage = fields.Float(string="Current Mileage", tracking=True)
    previous_milage = fields.Float(string="Previous Mileage", compute="_get_prev_milage", store=True)
    qty_requested = fields.Float(string="Quantity Requested", tracking=True)
    reason_for_request = fields.Text(string='Reason For Request', tracking=True)
    remark = fields.Text(string="Remark", tracking=True)
    approved_by = fields.Many2one('hr.employee', string="Approved By", tracking=True)
    approved_on = fields.Datetime(string="Approved On", tracking=True)
    dispensed_by = fields.Many2one('hr.employee', string="Dispensed By", tracking=True)
    dispensed_on = fields.Datetime(string="Dispensed On", tracking=True)
    qty_dispensed = fields.Float(string="Quantity Dispensed", tracking=True)

    STATES =[(i, i.capitalize()) for i in ['draft','request', 'checked', 'authorized']]   
    state = fields.Selection(STATES, default='draft', string='Process Status')

    store_issue = fields.Char(string="Store Center")
    plate_no = fields.Char(string="Plate Number",related="vehicle.license_plate")
    driver_name = fields.Many2one('res.partner', related="vehicle.driver_id",string="Driver Name")

    starting_km=fields.Char(string="Starting KM/Engine per Hour")
    date=fields.Date(string="Date", default=fields.date.today())
    starting_place = fields.Char(string="Place of Starting")
    destination_place = fields.Char(string="Place of Destination")
    request_department = fields.Many2one('hr.department', string="Requesting Department")
    fuel_id = fields.One2many('oil.form.lubricant', 'lubricant_id', string="Delivery Items")

    requested_by = fields.Many2one('res.users', string="Requested By")
    request_date=fields.Date(string="Request Date")
    checked_by = fields.Many2one('hr.employee', string="Checked By")
    checked_date=fields.Date(string="Checked Date")
    authorized_by = fields.Many2one('hr.employee', string="Authorized By")
    authorized_date=fields.Date(string="Authorized Date")
    reason_for_receive=fields.Text(string="Reason of Receive")
    request_fuel=fields.Float(string="Request Fuel")
    current_odometer=fields.Float(string="Current Odometer")
    request_time=fields.Float(string="Request Time")

    dispense_fuel=fields.Float(string="Dispense Fuel")

    vehicle_type=fields.Selection([
        ('car','Car'),
        ('machine','Machine')
    ])

    fuel_siv=fields.Many2one('order.receipt',string="Fuel SIV")

    fuel_siv_count=fields.Integer(string="Fuel SIV",compute="_compute_siv_count")

    is_inventory=fields.Boolean(string="Inventory")
    warehouse_id = fields.Many2one('stock.warehouse', string="Warehouse")

    @api.depends('fuel_siv')
    def _compute_siv_count(self):
        return
        for record in self:
            total_siv=self.env['order.receipt'].search([
                ('requistion_number','=',record.id)
            ])
            record.fuel_siv_count=len(total_siv)
            for rec in total_siv:
                if rec.state=='received':
                    record.warehouse_id=rec.warehouse.id
                    record.dispense_fuel=rec.total_littre

    def action_view_fuel_siv(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Fuel SIV',
            'res_model': 'order.receipt',
            'view_mode': 'tree,form',
            'domain': [('requistion_number', '=', self.name)],
            'views': [
                (self.env.ref('asset_warehous.view_order_receipt_tree').id, 'tree'),
                (self.env.ref('asset_warehous.view_order_receipt_form').id, 'form'),
            ],
            'target': 'current',
        }

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('fleet.fuel.request') or 'New'
        return super().create(vals)

    def user_request_by(self):
        self.ensure_one()
        self.state = 'request'
        self.requested_by = self.env.user.id
        self.request_date=fields.Date.today()
    def employe_checked_by(self):
        self.write({'state':'checked'})
        self.checked_by=self.env.user.employee_id.id
        self.checked_date=fields.Date.today()



    def employe_authorized_by(self):
        for record in self:  # Iterate over the records in the recordset
            record.state = 'authorized'  # Update the state for the current record
            record.authorized_by = self.env.user.employee_id.id
            record.authorized_date=fields.Date.today()
            if record.is_inventory:
                receipt_vals = {
                    'requistion_number':record.id,
                    'dept': record.request_department.id,
                    'plate_no': record.plate_no, # Access the id
                    'total_km':record.starting_km,
                    'request_fuel':record.request_fuel,
                    'vehicle':record.vehicle.id,
                    'dept':record.request_department.id,
                    'order_id': [(0, 0, {
                        'serial_no': line.item_no.id,
                        'unit': line.unit.id,
                        'qty': line.qty,
                        'description': line.description,

                    }) for line in record.fuel_id]
                }
                siv_fuel=self.env['order.receipt'].create(receipt_vals)
                record.fuel_siv=siv_fuel.id
class DeliveryInfo(models.Model):
    _name = 'oil.form.lubricant'
    _description = 'Delivery Information'

    item_no = fields.Many2one("product.product", string="Item No")
    description = fields.Html(string="Description")
    unit = fields.Many2one('uom.uom',related="item_no.uom_id" ,string="Unit")
    qty = fields.Integer(string="Quantity")
    total_price=fields.Float(string="Total Amount",compute="_compute_amount")
    approved_qty = fields.Integer(string="Approved Quantity", store=True)
    remark = fields.Html(string="Remark")
    lubricant_id = fields.Many2one('fleet.fuel.request', string="Fleet Reference")
   
    @api.depends('approved_qty','item_no','qty')
    def _compute_amount(self):
        for record in self:
            if record.approved_qty>0:
                record.total_price=record.approved_qty*record.item_no.lst_price
            else:
                record.total_price=record.qty*record.item_no.lst_price