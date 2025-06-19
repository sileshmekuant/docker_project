from odoo import models, fields, api
from odoo.exceptions import ValidationError
from odoo.tools import ustr

class CustomerComplaint(models.Model):
    _name = 'customer.complaint'
    _description = 'Customer Complaint Report'
    inspected_by_1 = fields.Many2one("res.users", string="Inspected By 1.")
    inspected_by_2 = fields.Many2one("res.users", string="Inspected By 2.")
    approved_by = fields.Many2one("res.users", string="Approved By")
    line_ids = fields.One2many('customer.complaint.line', 'report_id', string="Complaint Lines")

class CustomerComplaintLine(models.Model):
    _name = 'customer.complaint.line'
    _description = 'Customer Complaint Line'

    report_id = fields.Many2one('customer.complaint', string="Report Ref", ondelete="cascade")
    date = fields.Date(string="Date", required=True)  
    complaint_received_by = fields.Char(string="Complaint Received By", required=True)  
    product_type = fields.Many2one('product.product', string="Type of Product")
    complaint_description = fields.Text(string="Complaint Description", required=True)  
    cause_of_complaint = fields.Text(string="Cause of Complaint")
    corrective_action_taken = fields.Text(string="Corrective Action Taken")
    sequence = fields.Integer(string='S/N', compute='_compute_sequence', store=False)

    
    @api.constrains('sequence')
    def _check_sequence(self):
      for record in self:
          if record.sequence < 0:
             raise ValidationError(_("Sequence number cannot be negative!"))
    
    @api.constrains('date')
    def _check_date(self):
        for record in self:
            if record.date > fields.Date.today():
                raise ValidationError(_("Complaint date cannot be in the future!"))

    @api.constrains('complaint_received_by')
    def _check_receiver(self):
        for record in self:
            if not record.complaint_received_by.strip():
                raise ValidationError(_("Complaint receiver cannot be empty!"))

    @api.constrains('complaint_description')
    def _check_description(self):
        for record in self:
            if not record.complaint_description.strip():
                raise ValidationError(_("Complaint description cannot be empty!"))

    @api.depends('report_id.line_ids')
    def _compute_sequence(self):
        for rec in self:
            if rec.report_id:
                for idx, line in enumerate(rec.report_id.line_ids, start=1):
                    if line == rec:
                        rec.sequence = idx