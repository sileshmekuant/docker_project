# -*- coding: utf-8 -*-

from odoo import models, fields, api


class azpip(models.Model):
    _name = 'compliant.register'
    _description = 'Azpip'

    date = fields.Date(string="Date of Compliant Received", default=fields.Date.today())
    compliant_no = fields.Integer(string="Compliant Number")
    customer_name = fields.Many2one('res.partner', string='Customer Name')
    address = fields.Char(string="Address")
    description = fields.Html(string="Compliant Description")
    compliant_received = fields.Many2one('hr.employee', string="Compliance Received Employe")
    job_position = fields.Many2one('hr.job', string='Job Position')

    ##compliant investigation actionor customer feedback
    reason = fields.Html(string="Reason")
    correction_taken = fields.Many2one('name.store',string="correction Taken")
    correction_date = fields.Date(string="Correction Date")
    corrective_action = fields.Html(string="Corrective Action")
    corrective_dat = fields.Date(string="Corrective Date")
    investigated_by = fields.Many2one('hr.employee', string="Invetigated by")
    issue_status = fields.Selection([
        ('draft','Draft'),
        ('closed', 'Closed'),
        ('outstanding', 'Outstanding'),
        ('action_not_taken', 'Action Not Taken')],
        string="Issue Status",
        default='draft',
        required=True
    )

    is_closed = fields.Boolean(string="Is Closed", compute="_compute_status_flags")
    is_outstanding = fields.Boolean(string="Is Outstanding", compute="_compute_status_flags")
    is_action_not_taken = fields.Boolean(string="Is Action Not Taken", compute="_compute_status_flags")

    @api.depends('issue_status')
    def _compute_status_flags(self):
        for record in self:
            record.is_closed = record.issue_status == 'closed'
            record.is_outstanding = record.issue_status == 'outstanding'
            record.is_action_not_taken = record.issue_status == 'action_not_taken'

    remarks = fields.Html(string="Remarks")

    def action_outstanding(self):
        self.issue_status='outstanding'
        self.compliant_received= self.env.user.employee_id.id 

    def action_closed(self):
        self.issue_status='closed'
        self.investigated_by= self.env.user.employee_id.id 