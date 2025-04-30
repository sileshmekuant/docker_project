from odoo import models, api, fields

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

   

    def action_send_email(self):
        # Replace with your actual template's external ID
        template = self.env.ref('purchase_m.email_template_purchase_request')

        for record in self:
            if template:
                template.send_mail(record.id, force_send=True)
