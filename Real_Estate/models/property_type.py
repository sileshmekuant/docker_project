from odoo import models, fields,api

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Property Type"

    name = fields.Char(string="Property Type Name", required=True)
    area = fields.Float(string="Area (sqft)",default=0.0)
    price_per_area = fields.Float(string="Price per Area (sqft)",default=0.0)
    price =fields.Float(string="Price", compute="_compute_price",store=True)
    bed_room = fields.Integer(string="Bedrooms")
    no_of_room = fields.Integer(string="Total Rooms")
    bath_room = fields.Integer(string="Bathrooms")

    @api.depends('area', 'price_per_area')
    def _compute_price(self):
        for record in self:
          record.price = record.area * record.price_per_area
