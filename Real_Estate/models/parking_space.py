from odoo import models, fields

class ParkingSpace(models.Model):
    _name = "parking.space"
    _description = "Parking Space"

    name = fields.Char(string="Parking Space Name", required=True)
    location = fields.Char(string="Location")
    size = fields.Float(string="Size (sq meters)")
    # is_occupied = fields.Boolean(string="Occupied?", default=False)
    property_id = fields.Many2one("estate.property", string="Related Property")
    price_per_month = fields.Float(string="Monthly Price")
    vehicle_type = fields.Selection([
        ('small', 'Small Car'),
        ('medium', 'Medium Car'),
        ('large', 'Large Vehicle'),
        ('motorcycle', 'Motorcycle'),
    ], string="Vehicle Type")
#     notes = fields.Text(string="Additional Notes")
