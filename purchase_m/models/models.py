from odoo import models , api,fields
class purchase_m(models.Model):
        _inherit="purchase.order"


        payment_date = fields.Date(string="payment.date")
