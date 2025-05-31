from odoo import models, fields

class RegionTeam(models.Model):
    _name = 'region.team'
    _description = 'Regional Team'

    name = fields.Char(required=True)
