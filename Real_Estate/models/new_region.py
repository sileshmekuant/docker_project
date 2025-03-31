from odoo import models,fields,api

class NewRegion(models.Model):
          _name="new.region"

          name=fields.Char(string="Region")
          country = fields.Many2one('res.country',string="Country")