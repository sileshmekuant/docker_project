from odoo import fields,models,api 


class NewCity(models.Model):
          _name="new.city"

          name=fields.Char(string="City")
          region= fields.Many2one('new.region',string="Region")
          country_id = fields.Many2one('res.country',string="Country")

          get_country = fields.Many2many('new.region',compute="_get_regions")

          @api.depends('country_id')
          def _get_regions(self):
                  for rec in self:
                    if rec.country_id:
                              rec.get_country = self.env['new.region'].search([('country', '=', rec.country_id.id)])
                    else:
                            rec.get_country=False