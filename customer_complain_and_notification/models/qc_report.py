from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class QCReport(models.Model):
    _name = 'qc.report'
    _description = 'Quality Control Report'
    _order = 'date desc'

    name = fields.Char(string='Reference', readonly=True, required=True, copy=False, default='New')
    to = fields.Char(string="To", default="Managing Director")
    from_field = fields.Char(string="From", default="Quality Control")
    product_type = fields.Many2one('product.product',string="Product Type")
    date = fields.Date(string="Date", default=fields.Date.context_today)
    rec_no = fields.Char(string="Rec. No", required=True) 
    machine_line = fields.Char(string="Machine Line")
    remark = fields.Text(string="Remark")
    line_ids = fields.One2many('qc.report.line', 'report_id', string='Components')

    @api.constrains('rec_no')
    def _check_rec_no(self):
        for record in self:
            if not record.rec_no.strip():
                raise ValidationError(_("Recipe Number cannot be empty!"))

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('qc.report') or 'New'
        return super().create(vals)

class QCReportLine(models.Model):
    _name = 'qc.report.line'
    _description = 'QC Report Line'

    report_id = fields.Many2one('qc.report', string="Report Ref", ondelete="cascade")
    component = fields.Char(string="Component", required=True)
    weight = fields.Float(string="Weight (Kg.)/Batch 1")
    sequence = fields.Integer(string='S/N', compute='_compute_sequence', store=True)

    @api.constrains('component')
    def _check_component(self):
        for record in self:
            if not record.component.strip():
                raise ValidationError(_("Component name cannot be empty!"))

    @api.constrains('weight')
    def _check_weight(self):
        for record in self:
            if record.weight <= 0:
                raise ValidationError(_("Weight must be greater than 0!"))

    @api.depends('report_id.line_ids')
    def _compute_sequence(self):
        for rec in self:
            if rec.report_id:
                for idx, line in enumerate(rec.report_id.line_ids, start=1):
                    if line == rec:
                        rec.sequence = idx