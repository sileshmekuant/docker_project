# models/vehicle_trip_printout.py
from odoo import models, fields,api

class VehicleTripPrintout(models.Model):
    _name = 'vehicle.trip.printout'
    _description = 'Vehicle Trip Printout'

    trip_id = fields.Many2one('vehicle.trip', string="Original Trip", required=True, ondelete='cascade')
    
    vehicle_type = fields.Many2one('fleet.vehicle',string="Vehicle Name/Type")
    plate_number = fields.Char(string="License Plate No.",related="vehicle_type.license_plate")
    driver_name = fields.Many2one('res.partner',related="vehicle_type.driver_id",string="Driver's Name")

    date = fields.Date(string="Date")
    destination = fields.Char(string="Destination/Location")
    duration_from = fields.Datetime(string="Estimated Duration From")
    duration_to = fields.Datetime(string="Estimated Duration To")
    total_duration = fields.Char(string="Total Duration")  # or Float with units

    reason = fields.Text(string="Reason")

    requester_name = fields.Many2one('res.users',string="Requester Name")
    requester_title = fields.Many2one('hr.job', compute="_compute_requester_title",string="Requester Job Title", store=True)

    authorizer_name = fields.Many2one('res.users',string="Authorizer Name")
    authorizer_title = fields.Many2one('hr.job',compute="_compute_requester_title",string="Authorizer Job Title", store=True)

    @api.depends('requester_name','authorizer_name')
    def _compute_requester_title(self):
        for record in self:
            employee = self.env['hr.employee'].search([('user_id', '=', record.requester_name.id)], limit=1)
            record.requester_title = employee.job_id.id if employee.job_id else False

            employee1 = self.env['hr.employee'].search([('user_id', '=', record.authorizer_title.id)], limit=1)
            record.authorizer_title=employee1.job_id.id if employee1.job_id else False

    




    # @api.depends('requester_name')
    # def _compute_requester_title(self):
    #     for record in self:
    #         employee = self.env['hr.employee'].search([('user_id', '=', record.requester_name.id)], limit=1)
    #         record.requester_title = employee.job_id.id if employee and employee.job_id else False


    # requester_signature = fields.Binary(string="Requester Signature")
    # authorizer_signature = fields.Binary(string="Authorizer Signature")
