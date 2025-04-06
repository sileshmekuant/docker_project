from odoo import models, fields, api
from odoo.exceptions import ValidationError
class Estatefloor(models.Model):
    _name = "estate.floor"
    _description = "Estate Floor"
    _inherit = ['mail.thread', 'mail.activity.mixin']  

    property_id = fields.Many2one('real.estate.property', string="Property") 
    total_area = fields.Float(string="Total Area")
    price_per_area = fields.Float(string="Price per Area")
    category = fields.Selection([('residential', 'Residential'), ('commercial', 'Commercial')], string="Category",  tracking=True)
    room_ids = fields.One2many('estate.room', 'floor_id', string="Rooms")
    room_count = fields.Integer(string="Room Count", compute="_compute_room_count")
    image = fields.Binary(string="Floor Image")
    rent_id = fields.Many2one('estate.rent', string="Rent")
    floor_ids = fields.One2many('estate.floor', 'property_id', string="Floors")

    @api.depends('room_ids')
    def _compute_room_count(self):
        for record in self:
            record.room_count = len(record.room_ids)
        # floors = self.env['estate.floor'].search([])
        # for floor in floors:
        #     print(floor.category)   # Check if values exist
        #     floor.category = 'residential'  # Manually update if needed


class EstateRent(models.Model):
    _name="estate.rent"
    _description = "Estate rent"

    name = fields.Char(string="Name")