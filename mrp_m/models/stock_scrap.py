from odoo import models, fields

class StockScrap(models.Model):
    _inherit = 'stock.scrap'

    reason = fields.Selection([
        ('preform','Preform Reject'),
        ('label','Label Reject'),
         ('poly','Poly Reject'),
          ('cup','Cup Reject'),
           ('bottle','Bottle Reject'),

    ],string="Reason")
    
    reason_id = fields.Many2one('reason.model', string='Reason')
