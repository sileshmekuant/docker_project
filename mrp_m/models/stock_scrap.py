from odoo import models, fields

class StockScrap(models.Model):
    _inherit = 'stock.scrap'

    reason = fields.Selection([
        ('perform','Perform Reject'),
        ('label','Label Reject'),
         ('poly','Poly Reject'),
          ('cup','Cup Reject'),
           ('bottle','Bottle Reject'),

    ],string="Reason",default="perform")
