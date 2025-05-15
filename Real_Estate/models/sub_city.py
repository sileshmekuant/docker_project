from odoo import models, fields,api

class SubCity(models.Model):
    _name = "sub_city"
    _description = "Sub City"

    name = fields.Char(string="Sub City Name", required=True)
    city_id = fields.Many2one('new.city',string='city')
    
    region_id = fields.Many2one('region.model', string="Region")
    # region= fields.Many2one('new.region',string="Region")
    country_id = fields.Many2one('res.country',string="Country")

    get_country = fields.Many2many('new.region',compute="_get_regions")

@api.depends('country_id')
def _get_regions(self):
                  for rec in self:
                    if rec.country_id:
                              rec.get_country = self.env['new.region'].search([('country', '=', rec.country_id.id)])
                    else:
                            rec.get_country=False
@api.depends('city_id')
def _get_regions(self):
                  for rec in self:
                    if rec.city_id:
                              rec.get_city = self.env['new.subcity'].search([('city', '=', rec.city_id.id)])
                    else:
                            rec.get_city=False




















# class SiteModel(models.Model):
#     _name='estate.site'
#     _description="Site desctiption"

#     name=fields.Char(string="Site")
#     address = fields.Many2one('estate.sub.city')
    