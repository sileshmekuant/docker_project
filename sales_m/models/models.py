from odoo import models, fields

class SaleOrderInherit(models.Model):
    _inherit = "sale.order"

    active = fields.Boolean(default=True)

# def toggle_active(self):
#         for order in self:
#             order.active = not order.active 
