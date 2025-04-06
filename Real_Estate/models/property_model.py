from odoo import models, fields, api
from odoo.exceptions import ValidationError
class RealEstateProperty(models.Model):
    _name = "real.estate.property"
    _description = "Real Estate Property"


    name = fields.Many2one('product.product',string="Property Name", required=True)
    description = fields.Text("Description")
    property_type = fields.Selection([
        ('house', 'House'),
        ('apartment', 'Apartment'),
        ('land', 'Land')
    ], string="Type", required=True)
    price = fields.Float("Price", required=True)
    area = fields.Float("Area (sqft)")

    bedrooms = fields.Integer("Bedrooms")
    bathrooms = fields.Integer("Bathrooms")
    state = fields.Selection([
        ('new', 'New'),
        ('offer_received', 'Offer Received'),
        ('sold', 'Sold')
    ], string="State", default="new")
    owner_id = fields.Many2one("res.partner", string="Owner")

    
    tax = fields.Float("Tax", compute="_compute_tax", store=True)
    garden = fields.Boolean(string="Is Garden", default=False)
    garden_orientation = fields.Selection(
        [('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
        string="Garden Orientation"
    )
    garden_area = fields.Float(string="garden_area")
    postcode = fields.Integer(string="postcode")
    available_from = fields.Date(string="Available From")
    # expected_price = fields.Float(string="expected_price")
    selling_price =  fields.Float(string="selling price",compute="_compute_selling")
    owner_id = fields.Many2one('res.partner', string="Owner")
    buyer_id = fields.Many2one('res.partner', string="Buyer")
    salesperson_id = fields.Many2one('res.users', string="Salesperson")
    # New Many2many fields
    agent_ids = fields.Many2many('res.users', string="Agents")
    interested_partner_ids = fields.Many2many('res.partner', string="Interested Buyers")
    floor_ids = fields.One2many('estate.floor', 'property_id', string="Floors")  # Add this field
    total_area = fields.Float(string="Total Area (sqm)", compute="_compute_total_area", store=True)
    @api.depends("price")
    def _compute_tax(self):
            for record in self:
                record.tax = record.price * 0.15 
    @api.depends("price","tax")
    def _compute_selling(self):
        for record in self:
             
            record.selling_price = record.tax + record.price
    @api.depends('garden_area')
    def _compute_total_area(self):
        for property in self:
            property.total_area = property.area + property.garden_area
    def action_mark_as_sold(self):
        for record in self:
            if record.state != 'sold':
                    record.state = 'sold'

                    
    @api.constrains('expected_price', 'price')
    def _check_expected_price(self):
            """Ensure the selling price is at least 90% of the expected price."""
            for record in self:
                if record.price < (0.9 * record.expected_price):
                    raise ValidationError("The selling price must be at least 90% of the expected price.")

class EstateFloor(models.Model):
    _name = 'estate.floor.plan'
    _description = 'Building Floor Plan'
    _rec_name = 'name'

    name = fields.Char(string="Floor Name", required=True)
    floor_id = fields.Char(string="Floor Code")
    image = fields.Image(string="Floor Plan Image")


