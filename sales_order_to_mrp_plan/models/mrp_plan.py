from odoo import fields, models, api
from datetime import datetime

class MrpPlaning(models.Model):
    _name = "mrp.planing"
    _description = "MRP Planning"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    @api.model
    def _default_name(self):
        return self.env['ir.sequence'].next_by_code('mrp.planing') or 'New'

    name = fields.Char(string="Reference", readonly=True, required=False, copy=False, default=_default_name)
    date = fields.Date(string="Date", default=lambda self: datetime.today())
    product = fields.Many2one('product.template', string="Product")
    sales_order = fields.Many2one('sale.order', string="Sales Order")
    customer_id = fields.Many2one('res.partner', string="Customer Name", related="sales_order.partner_id")
    expiration_date = fields.Date(string="Dead Line",related="sales_order.validity_date")
    quantity = fields.Float(string="Quantity")
    description = fields.Text(string="Description")
    scheduled_date = fields.Datetime(string="Scheduled Date", tracking=True)
    approval_date = fields.Date(string="Approval Date")
    approved_by = fields.Many2one('hr.employee', string="Approved By")
    recieved_date = fields.Date(string="Recieved Date")
    recieved_by = fields.Many2one('hr.employee', string="Recieved By")
    status = fields.Selection([(i, i.upper()) for i in ['draft', 'confirmed','recieved']], default="draft", tracking=True)
    diameter = fields.Float(string="Diameter")
    thickness = fields.Float(string="Thickness")
    length = fields.Float(string="Length")
    color = fields.Char(string="Color")
    weight = fields.Float(string="Weight")
    socket_type = fields.Selection([('utype', 'U-type'), ('rtype', 'R-type')], default='utype', string="Socket Type")
    note = fields.Html(string="Note")
    prepared_by = fields.Many2one('hr.employee', string="Prepared By")
    signature = fields.Binary( string="Signature")
    production_line = fields.Many2one('mrp.workcenter',string="Production Line")
    product_specification = fields.Html(string="Product Specification")
    # production= fields.Many2one('mrp.production')
    recipie = fields.Many2one('mrp.bom', string="Recipie")
    recipie_domain = fields.Many2many('mrp.bom', compute="_get_recipie")
    production_ids = fields.One2many('mrp.production', 'mrp_plan', string="Manufacturing Orders")
    production_count = fields.Integer(
        string="Production Count",
        compute="_compute_production_count",
        store=False
    )

    @api.depends('production_ids')
    def _compute_production_count(self):
        for record in self:
            record.production_count = len(record.production_ids)

    @api.depends('product')
    def _get_recipie(self):
        for rec in self:
            if rec.product:
                boms = self.env['mrp.bom'].search([
                    ('product_tmpl_id', '=', rec.product.id)
                ])
                rec.recipie_domain = boms.ids
            else:
                rec.recipie_domain = [(5, 0, 0)] 


    def action_recieve(self):
        for rec in self:
            rec.prepared_by= self.env.user.employee_id.id 
            rec.recieved_by= self.env.user.employee_id.id 
            rec.recieved_date=fields.Date.today()
            rec.status='recieved'

    def action_open_create_mo_wizard(self):
        return {
            'name': 'Create Manufacturing Order',
            'type': 'ir.actions.act_window',
            'res_model': 'create.manufacturing.order',
            'view_mode': 'form',
            'view_id': self.env.ref('sales_order_to_mrp_plan.view_create_manufacturing_wizard_form').id,
            'target': 'new',
            'context': {
                'default_user': self.env.uid,
            },
        }
    def action_approve(self):
        for rec in self:
            rec.prepared_by= self.env.user.employee_id.id 
            rec.approved_by= self.env.user.employee_id
            rec.approval_date=fields.Date.today()
            rec.status='confirmed'
           


class MrpProduction(models.Model):
    _inherit="mrp.production"

 
    mrp_plan= fields.Many2one('mrp.planing',string="MRP Plan")
    shift = fields.Selection([
        ('day','Day'),
        ('night','Night')
    ],string="Shift")