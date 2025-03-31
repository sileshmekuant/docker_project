from odoo import models, fields

# class ResCountry(models.Model):
#     _inherit = "res.country"
#     region_id = fields.One2many("estate.region", "country_id", string="Regions")

class EstateRegion(models.Model):
    _name = "estate.region"
    _description = "Region"

    name = fields.Char(string="Region Name", required=True)
    code = fields.Char(string="Country Code", size=3)
    country_id = fields.Many2one("res.country", string="Country Reference")
    # sub_city_id = fields.One2many("estate.sub.city", "region_id", string="Sub Cities")
    # region_id = fields.One2many("estate.region", "country_id", string="Regions")
    # parent_id = fields.Many2one("estate.region", string="Parent Region")
    # #child_id = fields.One2many("estate.region", "parent_id", string="Sub Regions")