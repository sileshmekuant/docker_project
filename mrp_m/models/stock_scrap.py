from odoo import models, fields

class StockScrap(models.Model):
    _inherit = 'stock.scrap'

    reason = fields.Many2one('scrap.reason', string='Reason')
