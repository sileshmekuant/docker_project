from odoo import models , api,fields
class sales_m(models.Model):
        _inherit="sale.order"


        payment_date = fields.Date(string="payment.date")
