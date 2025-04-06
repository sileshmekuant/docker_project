from odoo import models, fields

class EstateCountry(models.Model):
    _name = "estate.country"
    _description = "Country"

    name = fields.Char(string="Country Name", required=True)
    code = fields.Char(string="Country Code", size=3)
    country_id = fields.Many2one("res.country", string="Country Reference")
    region_id = fields.One2many("estate.region", "country_id", string="Regions")
