from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Appointment(models.Model):
    _name = 'appointment.appointment'
    _description = 'Appointment'

    name = fields.Char(string='Subject', required=True)
    patient_id = fields.Many2one('res.partner', string='Patient', required=True)
    appointment_date = fields.Datetime(string='Appointment Date', required=True)
    notes = fields.Text(string='Notes')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='draft')

    @api.constrains('appointment_date')
    def _check_appointment_date(self):
        for record in self:
            if record.appointment_date < fields.Datetime.now():
                raise ValidationError("Appointment date must be in the future.")

    def action_confirm(self):
        for record in self:
            record.state = 'confirmed'

    def action_done(self):
        for record in self:
            record.state = 'done'

    def action_cancel(self):
        for record in self:
            record.state = 'cancelled'
