from odoo import models, fields, api

class TravelBooking(models.Model):
    _name = 'travel.booking'
    _description = 'Travel Booking'

    name = fields.Char(string="Booking Reference", required=True, default=lambda self: self.env['ir.sequence'].next_by_code('travel.booking'))
    employee_id = fields.Many2one('hr.employee', string="Employee", required=True)
    destination = fields.Char(string="Destination", required=True)
    start_date = fields.Date(string="Start Date", required=True)
    end_date = fields.Date(string="End Date", required=True)
    travel_mode = fields.Selection([('flight', 'Flight'), ('train', 'Train'), ('car', 'Car')], string="Travel Mode")
    state = fields.Selection([('draft', 'Draft'), ('submitted', 'Submitted'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='draft')

    def action_submit(self):
        self.state = 'submitted'

    def action_approve(self):
        self.state = 'approved'

    def action_reject(self):
        self.state = 'rejected'
