from odoo import models , api,fields
class inventory_m(models.Model):
        _inherit="stock.picking"


        payment_date = fields.Date(string="payment.date")
