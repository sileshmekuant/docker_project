from odoo import models, fields, api
from odoo.exceptions import ValidationError

class CalibrationPlan(models.Model):
    _name = 'calibration.plan'
    _description = 'Calibration Plan'
    _order = 'date desc'

    date = fields.Date(string='Date', required=True, default=fields.Date.today)
    calibration_lines = fields.One2many('calibration.line', 'plan_id', string='Calibration Details')
    prepared_by = fields.Many2one('res.users', string='Prepared By', default=lambda self: self.env.user, readonly=True)
    approved_by = fields.Many2one('res.users', string='Approved By', required=True)
    
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


class CalibrationLine(models.Model):
    _name = 'calibration.line'
    _description = 'Calibration Line'

    plan_id = fields.Many2one('calibration.plan', string='Calibration Plan', required=True, ondelete='cascade')
    equipment_name = fields.Char(string='Equipment Name', required=True)
    serial_no = fields.Char(string='Serial No.', required=True)
    capacity_range = fields.Char(string='Capacity/Range of Measurement', required=True)
    last_calibration = fields.Date(string='Last Calibration')
    calibration_frequency = fields.Char(string='Calibration Frequency')
    calibration_due_date = fields.Date(string='Calibration Due Date')
    calibration_party = fields.Selection([
        ('in_house', 'In-House'),
        ('third_party', '3rd Party')
    ], string='Calibration Source', required=True)
    remarks = fields.Text(string='Remarks')


    @api.constrains('last_calibration', 'calibration_due_date')
    def _check_calibration_dates(self):
        for rec in self:
            if rec.last_calibration and rec.calibration_due_date:
                if rec.last_calibration > rec.calibration_due_date:
                    raise ValidationError("Last Calibration date cannot be after the Calibration Due Date.")
