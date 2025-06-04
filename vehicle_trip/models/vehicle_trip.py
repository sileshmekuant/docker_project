from odoo import models, fields, api
from odoo.exceptions import UserError
from datetime import date


class VehicleTrip(models.Model):
    _name = "vehicle.trip"
    _description = "Vehicle Trip"

    # Vehicle Info
    vehicle = fields.Many2one('fleet.vehicle', string="Vehicle")
    plate_number = fields.Char("Plate Number",related='vehicle.license_plate')
    driver_name = fields.Many2one('res.partner',related="vehicle.driver_id", string="driver")

    # Trip Start Info
    name = fields.Char(string="Reference", readonly=True, default="New")
    date = fields.Date("Date",default=fields.Date.today())
    start_location = fields.Char("Start Location")
    start_date = fields.Date("Start Time")
    odoo_meter = fields.Float("Odometer Start")

    # Trip End Info
    destination_location = fields.Char("Destination location")
    end_date = fields.Date("End date")
    # current_odoo_meter = fields.Float("Odometer End")
    fuel_consumption = fields.Float("Fuel Consumption")
    dispense_fuel = fields.Float(string="Dispensed Fuel (Litres)")
    end_odometer = fields.Float(string="End Odometer")


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
    def action_request(self):
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
            # if trip.start_time and trip.end_date:
            #     duration = trip.end_date - trip.start_time
            #     total_duration = str(duration)
            # else:
            #     total_duration = ''

        # Create related printout and store in variable
        printout = self.env['vehicle.trip.printout'].create({
            'trip_id': trip.id,
            'vehicle': trip.vehicle.id,
            # 'plate_number': trip.plate_number,
            'driver_name': trip.driver_name.id,
            'start_location': trip.start_location,
            'date': trip.date,
            'destination_location': trip.destination_location,
            'start_date': trip.start_date,
            'end_date': trip.end_date,
            #'total_duration': total_duration,
            'reason': '',
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
    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('vehicle.trip') or 'New'
        return super().create(vals)