from odoo import fields, models, api
from odoo.exceptions import ValidationError
import logging 
_logger = logging.getLogger(__name__)

class FuelConsumptionReport(models.Model):
    _name = 'fuel.consump.report'
    _description = 'Fuel Consump Report'
    _inherit = ['mail.thread', 'mail.activity.mixin']   

    name = fields.Char(string="Reference", readonly=True, default="New")
    start_date = fields.Date(string="Start Date", required=True, tracking=True)
    end_date = fields.Date(string="End Date", required=True, tracking=True)
    vehicle = fields.Many2one('fleet.vehicle', string="Vehicle", tracking=True)
    # is_inventory=fields.Boolean(string="Inventory")
    vehicles_consumption = fields.Many2many(
        'vehicle.trip',
        string="Vehicles Consumption", 
        compute='_compute_vehicles_consumption',
        store=True
    )
    fuel_consumption = fields.Float(string="Fuel Consumption", compute="_compute_fuel_consumption")
    last_odometer = fields.Float(string="Last Odometer", compute="_compute_last_odometer")

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', 'New') == 'New':
                vals['name'] = self.env['ir.sequence'].next_by_code('fuel.consump.report') or 'New'
        return super().create(vals_list)

    @api.depends('start_date', 'end_date', 'vehicle')
    def _compute_vehicles_consumption(self):
        for rec in self:
            print(f"Computing for vehicle={rec.vehicle}, date={rec.start_date} to {rec.end_date}")
            domain = [
                ('start_date', '>=', rec.start_date),
                ('end_date', '<=', rec.end_date),
                ('state','=','approved')
            ]
            if rec.vehicle:
                domain.append(('vehicle', '=', rec.vehicle.id))
            trips = self.env['vehicle.trip'].search(domain)
            print(f"Found trips: {trips}")
            rec.vehicles_consumption = trips

    @api.depends('vehicles_consumption.fuel_consumption')
    def _compute_fuel_consumption(self):
        a=0
        for rec in self:
            total = 0.0
            if rec.start_date and rec.end_date:
                for i in rec.vehicles_consumption:
                    a+=i.fuel_consumption
            rec.fuel_consumption = a

    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        for record in self:
            if record.start_date and record.end_date and record.start_date > record.end_date:
                raise ValidationError("End Date must be greater than Start Date")
    
    @api.depends('start_date', 'end_date', 'vehicle')
    def _compute_last_odometer(self):
        for rec in self:
            rec.last_odometer = 0.0
            if rec.start_date and rec.end_date:
                domain = [
                    ('start_date', '>=', rec.start_date),
                    ('end_date', '<=', rec.end_date),
                    ('state', '=', 'approved'),
                ]
                if rec.vehicle:
                    domain.append(('vehicle', '=', rec.vehicle.id))
                last_trip = self.env['vehicle.trip'].search(domain, order='date desc, id desc', limit=1)
                if last_trip:
                    rec.last_odometer = last_trip.end_odometer or 0.0
