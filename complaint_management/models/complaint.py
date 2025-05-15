from odoo import models, fields, api

class Complaint(models.Model):
    _name = 'complaint.management'
    _description = 'Complaint Management'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Reference", readonly=True, default="New")
    complaint = fields.Html(string="Complaint", required=True)
    rejection_reason = fields.Html(string="Rejection Reason", readonly=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('sent', 'Sent'),
        ('marked', 'Marked as Issue'),
        ('resolved', 'Resolved'),
        ('rejected', 'Rejected')
    ], default='draft', tracking=True)

    def action_send(self):
        self.write({'state': 'sent'})

    def action_mark(self):
        self.write({'state': 'marked'})

    def action_resolve(self):
        self.write({'state': 'resolved'})

    def action_reject(self):
        self.write({
            'state': 'rejected',
            'rejection_reason': 'Rejected by management',  # You can later replace this with a wizard input
        })

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('complaint.management') or 'New'
        return super().create(vals)
