from odoo import models, fields

class ScrapReason(models.Model):
    _name = 'scrap.reason'
    _description = 'Scrap Reason'

    name = fields.Char(string='Reason', required=True)
    
