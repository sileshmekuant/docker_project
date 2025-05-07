from odoo import models, api, fields

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    def action_send_email(self):
        sender_email = self.env

        # Use hardcoded recipient or fetch dynamically
        recipient_email = "sileshmekuant@gmail.com"

        # Fetch email template
        template = self.env.ref("purchase_m.email_template_purchase_request")

        # You can pass any object here; using self[0] or a dummy employee if needed
        context_obj = self[0] if self else self.env['purchase.order']

        # Render email content
        body_html = template.with_context(object=context_obj)._render_field('body_html', [template.id])[template.id]
        subject = template.with_context(object=context_obj)._render_field('subject', [template.id])[template.id]

        # Send email to the target address
        mail_values = {
            'email_from': sender_email,
            'email_to': recipient_email,
            'subject': subject,
            'body_html': body_html,
        }

        mail = self.env['mail.mail'].create(mail_values)
        mail.send()
