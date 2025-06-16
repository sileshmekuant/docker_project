from odoo import models, fields, api

class HrAttendance(models.Model):
    _inherit = 'hr.attendance'

    extra_hours = fields.Float(
        string='Extra Hours',
        compute='_compute_extra_hours',
        store=True
    )

    @api.depends('check_in', 'check_out')
    def _compute_extra_hours(self):
        for record in self:
            if record.check_in and record.check_out:
                # Total worked hours
                worked_hours = (record.check_out - record.check_in).total_seconds() / 3600.0

                # Extra hours over 8
                record.extra_hours = max(0.0, worked_hours - 8.0)
            else:
                record.extra_hours = 0.0
