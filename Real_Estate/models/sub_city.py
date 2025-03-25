from odoo import models, fields

class EstateSubCity(models.Model):
    _name = "estate.sub.city"
    _description = "Sub City"

    name = fields.Char(string="Sub City Name", required=True)
    region_id = fields.Many2one("estate.region", string="Region", required=True)

class SiteModel(models.Model):
    _name='estate.site'
    _description="Site desctiption"

    name=fields.Char(string="Site")
    address = fields.Many2one('estate.sub.city')
    