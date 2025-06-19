# File: models/raw_material_inspection.py
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class RawMaterialInspection(models.Model):
    _name = 'raw.material.inspection'
    _description = 'Raw Material Inspection Record'
    _order = 'date desc'


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


    # General Info
    material_type = fields.Char(string='Type of Raw Material', required=True)
    supplier = fields.Char(string='Supplier', required=True)
    grn_no = fields.Char(string='GRN No.', required=True)
    batch_no = fields.Char(string='Batch No.', required=True)
    prepared_by = fields.Many2one('res.users', string='prepared By', default=lambda self: self.env.user,
                                   readonly=True, ondelete='restrict')
    approved_by = fields.Many2one('res.users', string='approved By', required=True, ondelete='restrict')
    date = fields.Date(string='Date', required=True, default=fields.Date.today)
    date_received = fields.Date(string='Date Received', required=True)
    quantity_received = fields.Float(string='Quantity Received (kg)', required=True, digits=(12, 2))
    mfg_date = fields.Date(string='Manufacturing Date')
    expiry_date = fields.Date(string='Expiry Date')

    # Inspection Parameters
    packaging_condition = fields.Selection([
        ('good', 'Good'),
        ('damaged', 'Damaged')
    ], string='Packaging Condition', required=True)
    weight_per_package = fields.Float(string='Weight per Package (kg)', digits=(12, 2))
    coa_available = fields.Selection([
        ('available', 'Available'),
        ('not_available', 'Not Available')
    ], string='Certificate of Analysis', required=True)
    load_on_machine = fields.Selection([
        ('bad', 'Bad'),
        ('good', 'Good'),
        ('v_good', 'Very Good'),
        ('excellent', 'Excellent')
    ], string='Load on Machine', required=True)

    # Remarks and Status
    remark = fields.Text(string='Remarks')
    

   

    @api.constrains('quantity_received', 'weight_per_package')
    def _check_positive_numbers(self):
        for rec in self:
            if rec.quantity_received <= 0:
                raise ValidationError("Quantity Received (kg) must be greater than 0.")
            if rec.weight_per_package and rec.weight_per_package <= 0:
                raise ValidationError("Weight per Package (kg) must be greater than 0.")

    @api.constrains('mfg_date', 'expiry_date')
    def _check_dates(self):
        for rec in self:
            if rec.mfg_date and rec.expiry_date and rec.mfg_date > rec.expiry_date:
                raise ValidationError("Manufacturing Date cannot be later than Expiry Date.")