# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ProductQualityCheck(models.Model):
    _name = 'product.quality.check'
    _description = 'Physical Testing Parameters'
    _order = 'date desc, product_type'

    # Header Fields
    date = fields.Date(string='Date', required=True, default=fields.Date.today)
    product_type = fields.Many2one('product.product', string='Product Type', required=True)
    order_code = fields.Char(string='Order Code', required=True)
    inspector = fields.Many2one(
        'res.users',
        string='Inspector',
        default=lambda self: self.env.user,
        required=True
    )

    # Quality Parameters
    quality_line_ids = fields.One2many(
        'product.quality.check.line',
        'check_id',
        string='Quality Parameters',
        copy=True
    )

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


    # Authorization
    prepared_by = fields.Many2one(
        'res.users',
        string='Prepared By',
        default=lambda self: self.env.user
    )
    approved_by = fields.Many2one('res.users', string='Approved By')
    

    @api.constrains('quality_line_ids')
    def _check_quality_lines(self):
        for record in self:
            if not record.quality_line_ids:
                raise ValidationError("At least one quality parameter must be specified.")


class ProductQualityCheckLine(models.Model):
    _name = 'product.quality.check.line'
    _description = 'Physical Testing Parameter Line'
    _order = 'sequence,id'

    sequence = fields.Integer(string='Sequence', default=1)
    check_id = fields.Many2one(
        'product.quality.check',
        string='Quality Check',
        ondelete='cascade',
        required=True
    )

    # Changed from Selection to Char field for free input
    parameter = fields.Many2one('parameter.parameter', 
            string='Parameter', 
            required=True,
            )

    # Changed to regular Char field (not computed)
    equipment_name = fields.Many2one('maintenance.request',string='Equipment Name')

    standard = fields.Char(string='Standard', required=True)
    actual = fields.Char(string='Actual', required=True)
    remark = fields.Char(string='Remark')

    @api.constrains('actual', 'standard')
    def _check_values(self):
        for record in self:
            if not record.actual:
                raise ValidationError("Actual value must be provided for all parameters.")
            if not record.standard:
                raise ValidationError("Standard value must be provided for all parameters.")