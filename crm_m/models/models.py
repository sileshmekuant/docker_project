from odoo import models , api,fields
class crm_m(models.Model):
        _inherit="crm.lead"


        payment_date = fields.Date(string="payment.date")
