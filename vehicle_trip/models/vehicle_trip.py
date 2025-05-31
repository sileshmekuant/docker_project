from odoo import models, fields, api
from odoo.exceptions import UserError
from datetime import date


class VehicleTrip(models.Model):
    _name = "vehicle.trip"
    _description = "Vehicle Trip"

    # Vehicle Info
    vehicle_type = fields.Many2one('fleet.vehicle', string="Vehicle")
    plate_number = fields.Char("Plate Number",related='vehicle_type.license_plate')
    driver_name = fields.Many2one('res.partner',related="vehicle_type.driver_id", string="driver")

    # Trip Start Info
    date = fields.Date("Trip Date")
    start_location = fields.Char("Start Location")
    start_time = fields.Date("Start Time")
    odoo_meter = fields.Float("Odometer Start")

    # Trip End Info
    destination = fields.Char("Destination")
    end_date = fields.Date("End Date")
    current_odoo_meter = fields.Float("Odometer End")
    fuel_consumption = fields.Float("Fuel Consumption (L)")

    # Status Workflow
    state = fields.Selection([
        ('draft', 'Draft'),
        ('request', 'request'),
        ('confirmed', 'Confirmed'),
        ('approved', 'Approved'),
    ], string="Status", default='draft', tracking=True)

    request_by = fields.Many2one('res.users', string="request By", readonly=True)
    request_date = fields.Date(string="request Date", readonly=True)

    confirmed_by = fields.Many2one('res.users', string="Confirmed By", readonly=True)
    confirmed_date = fields.Date(string="Confirmed Date", readonly=True)

    approved_by = fields.Many2one('res.users', string="Approved By", readonly=True)
    approved_date = fields.Date(string="Approved Date", readonly=True)

    #Action buttons
    def action_prepare(self):
        for rec in self:
            if rec.state != 'draft':
                raise UserError("Only draft records can be request.")
            rec.state = 'request'
            rec.request_by = self.env.user
            rec.request_date = date.today()

    def action_confirm(self):
        for rec in self:
            if rec.state != 'request':
                raise UserError("Only request records can be confirmed.")
            rec.state = 'confirmed'
            rec.confirmed_by = self.env.user
            rec.confirmed_date = date.today()

    # def action_approve(self):
    #     for rec in self:
    #         if rec.state != 'confirmed':
    #             raise UserError("Only confirmed records can be approved.")
    #         rec.state = 'approved'
    #         rec.approved_by = self.env.user
    #         rec.approved_date = date.today()
    


    # Approve method
    def action_approve(self):
        for trip in self:
            if trip.state != 'confirmed':
                raise UserError("Only confirmed records can be approved.")

            trip.state = 'approved'
            trip.approved_by = self.env.user
            trip.approved_date = date.today()

            # Compute total duration
            if trip.start_time and trip.end_date:
                duration = trip.end_date - trip.start_time
                total_duration = str(duration)
            else:
                total_duration = ''

        # Create related printout and store in variable
        printout = self.env['vehicle.trip.printout'].create({
            'trip_id': trip.id,
            'vehicle_type': trip.vehicle_type.id,
            # 'plate_number': trip.plate_number,
            'driver_name': trip.driver_name.id,
            'date': trip.date,
            'destination': trip.destination,
            'duration_from': trip.start_time,
            'duration_to': trip.end_date,
            'total_duration': total_duration,
            'reason': 'Trip approved and ready',
            'requester_name': trip.request_by.id if trip.request_by else '',
            'authorizer_name': trip.approved_by.id if trip.approved_by else '',
        })

        # Return action to open the form view of the printout
        return {
            'type': 'ir.actions.act_window',
            'name': 'Trip Printout',
            'res_model': 'vehicle.trip.printout',
            'res_id': printout.id,
            'view_mode': 'form',
            'target': 'current',
        }
