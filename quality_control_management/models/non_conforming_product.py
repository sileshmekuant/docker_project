from odoo import models, fields, api
from odoo.exceptions import ValidationError

class NonConformingProduct(models.Model):
    _name = 'non.conforming.product'
    _description = 'Non-Conforming Product Log'
    _order = 'date desc'

    # General Info
    date = fields.Date(string='Date', required=True, default=fields.Date.today)
    shift = fields.Selection([
        ('morning', 'Morning'),
        ('afternoon', 'Afternoon'),
        ('night', 'Night')
    ], string='Shift', required=True)
    job_order_no = fields.Char(string='Job Order No', required=True)

    # One2many field for non-conforming product lines
    non_conforming_lines = fields.One2many('non.conforming.product.line', 'non_conforming_id', string='Non-Conforming Lines')

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
    
    prepared_by = fields.Many2one('res.users', string='Prepared By', default=lambda self: self.env.user, readonly=True)
    approved_by = fields.Many2one('res.users', string='Approved By', required=True)
    

    @api.constrains('non_conforming_lines')
    def _check_non_conforming_lines(self):
        for rec in self:
            if not rec.non_conforming_lines:
                raise ValidationError("At least one non-conforming product line must be specified.")


class NonConformingProductLine(models.Model):
    _name = 'non.conforming.product.line'
    _description = 'Non-Conforming Product Line'

    sequence = fields.Integer(string='S/N', default=1, readonly=True)
    non_conforming_id = fields.Many2one('non.conforming.product', string='Non-Conforming Product', required=True, ondelete='cascade')
    product_type = fields.Many2one('product.product', string='Type of Product', required=True)
    quantity = fields.Float(string='Quantity (kg)', required=True, digits=(12, 2))
    defect_type = fields.Char(string='Type of Defect', required=True)
    correction = fields.Text(string='Correction')
    remark = fields.Text(string='remark')

    @api.constrains('quantity')
    def _check_quantity(self):
        for line in self:
            if line.quantity <= 0:
                raise ValidationError("Quantity (kg) must be greater than 0.")

    @api.model
    def create(self, vals):
        if 'sequence' not in vals:
            existing_lines = self.search([('non_conforming_id', '=', vals.get('non_conforming_id'))])
            vals['sequence'] = len(existing_lines) + 1
        return super(NonConformingProductLine, self).create(vals)