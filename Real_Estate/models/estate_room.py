from odoo import models, fields, api
from odoo.exceptions import ValidationError
class EstateRoom(models.Model):
    _name = "estate.room"
    _description = "Estate Room"

    name = fields.Char(string="Room Name", required=True)  
    size = fields.Float(string="Room Size") 
    floor_id = fields.Many2one('estate.floor', string="Floor")
