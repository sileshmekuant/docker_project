from odoo import models,fields,api


class ProductCategory(models.Model):
    _inherit='product.category'


    is_raw_material  = fields.Boolean(string="Raw Material",default=False)