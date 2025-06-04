from odoo import fields, models, api
from odoo.exceptions import ValidationError


class FuelConsumptionReport(models.Model):
    _name = 'fuel.consumption.report'
    _description = 'Fuel Consumption Report'
    _inherit = ['mail.thread', 'mail.activity.mixin']   

    name = fields.Char(string="Reference", readonly=True, default="New")
    start_date = fields.Date(string="Start Date", required=True, tracking=True)
    end_date = fields.Date(string="End Date", required=True, tracking=True)
    vehicle = fields.Many2one('fleet.vehicle', string="Vehicle", tracking=True)
    is_inventory=fields.Boolean(string="Inventory")
    vehicles_consumption = fields.Many2many(
        'fleet.fuel.request',
        string="Vehicles Consumption", 
        compute='_compute_vehicles_consumption'
    )
    fuel_consumption = fields.Float(string="Fuel Consumption", compute="_compute_fuel_consumption")

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', 'New') == 'New':
                vals['name'] = self.env['ir.sequence'].next_by_code('fuel.consumption.report') or 'New'
        return super().create(vals_list)

    @api.depends('start_date', 'end_date', 'vehicle','is_inventory')
    def _compute_vehicles_consumption(self):
        for rec in self:
            domain = [
                ('date', '>=', rec.start_date),
                ('date', '<=', rec.end_date),
                ('state','=','authorized')
            ]
            if rec.vehicle:
                domain.append(('vehicle', '=', rec.vehicle.id))
            if rec.is_inventory:
                domain.append(('is_inventory', '=', True))
            rec.vehicles_consumption = self.env['fleet.fuel.request'].search(domain)

    def _compute_fuel_consumption(self):
        for rec in self:
            total = 0.0
            if rec.start_date and rec.end_date:
                domain = [
                    ('date', '>=', rec.start_date),
                    ('date', '<=', rec.end_date),
                ]
                if rec.vehicle:
                    domain.append(('vehicle', '=', rec.vehicle.id))
                # if rec.is_inventory:
                #      domain.append(('is_inventory', '=', True))
                # requests = self.env['fleet.fuel.request'].search(domain)
                total = sum(request.dispense_fuel or 0.0 for request in requests)
            rec.fuel_consumption = total

    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        for record in self:
            if record.start_date and record.end_date and record.start_date > record.end_date:
                raise ValidationError("End Date must be greater than Start Date")
