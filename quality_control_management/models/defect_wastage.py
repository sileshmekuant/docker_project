from odoo import models, fields, api
from odoo.exceptions import ValidationError

class DefectWastage(models.Model):
    _name = 'defect.wastage'
    _description = 'Weekly Defect/Wastage Follow Up'
    _order = 'date desc'

    # General Info
    date = fields.Date(string='Date', required=True, default=fields.Date.today)
    shift = fields.Selection([
        ('morning', 'Morning'),
        ('afternoon', 'Afternoon'),
        ('night', 'Night')
    ], string='Shift', required=True)
    product_type = fields.Many2one('product.product', string='Product Type', required=True)
    order_no = fields.Char(string='Order No', required=True)

    # Production and Wastage
    total_product = fields.Float(string='Total Product (kg)', required=True, digits=(12, 2))
    total_wastage = fields.Float(string='Total Wastage (kg)', required=True, digits=(12, 2))
    wastage_percent = fields.Float(string='Wastage (%)', compute='_compute_wastage_percent', store=True, readonly=True)

    # Breakdown Fields
    mixer = fields.Float(string='Mixer', required=True)
    hopper = fields.Float(string='Hopper', required=True)
    extruder = fields.Float(string='Extruder', required=True)
    cooling_system = fields.Float(string='Cooling System', required=True)
    haul_off = fields.Float(string='Haul Off', required=True)
    cutter = fields.Float(string='Cutter', required=True)
    belling = fields.Float(string='Belling', required=True)
    starting_dust = fields.Float(string='Starting', required=True)
    impurity = fields.Float(string='Impurity/Dust', required=True)
    power_off = fields.Float(string='Power Off', required=True)


    state = fields.Selection([
        ('draft', 'Draft'),
        ('prepared', 'prepared'),
        ('approved', 'Approved'),
    ], string='Status', default='draft', tracking=True)


    def action_prepared(self):
        for rec in self:
            rec.state = 'prepared'

    def action_approve(self):
        for rec in self:
            if not rec.approved_by:
                rec.approved_by = self.env.user
                rec.approved_date = fields.Datetime.now()
            rec.state = 'approved'

    # Others
    remark = fields.Text(string='Remark')
    prepared_by = fields.Many2one('res.users', string='Prepared By', default=lambda self: self.env.user, readonly=True)
    approved_by = fields.Many2one('res.users', string='Approved By', required=True)
    
    @api.depends('total_wastage', 'total_product')
    def _compute_wastage_percent(self):
        for rec in self:
            if rec.total_product > 0:
                rec.wastage_percent = round((rec.total_wastage / rec.total_product) * 100, 2)
            else:
                rec.wastage_percent = 0.0

    @api.constrains('total_product', 'total_wastage')
    def _check_positive_numbers(self):
        for rec in self:
            if rec.total_product <= 0:
                raise ValidationError("Total Product (kg) must be greater than 0.")
            if rec.total_wastage < 0:
                raise ValidationError("Total Wastage (kg) cannot be negative.")

    @api.constrains('wastage_percent')
    def _check_wastage_percent(self):
        for rec in self:
            if rec.wastage_percent > 100:
                raise ValidationError("Wastage percentage cannot exceed 100%.")

    @api.constrains('mixer', 'hopper', 'extruder', 'cooling_system', 'haul_off', 'cutter', 'belling', 'starting_dust', 'impurity', 'power_off')
    def _check_breakdown_sum(self):
        for rec in self:
            breakdown_sum = sum([
                rec.mixer, rec.hopper, rec.extruder, rec.cooling_system,
                rec.haul_off, rec.cutter, rec.belling, rec.starting_dust,
                rec.impurity, rec.power_off
            ])
            if round(breakdown_sum, 2) != round(rec.total_wastage, 2):
                raise ValidationError("Sum of breakdown fields must equal Total Wastage.")
