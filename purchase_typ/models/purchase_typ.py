from odoo import models, fields

class PurchaseRequest(models.Model):
    
    _inherit = 'purchase.request'   

    purchase_type = fields.Selection([
        ('direct', 'Direct'),
        ('fixed', 'Fixed'),
        ('limited', 'Limited'),
        ('national_competitive', 'National Competitive'),
        ('competitive', 'Competitive'),
        ('proforma', 'Proforma'),
    ], string="Purchase Type", required=True, default='direct')
