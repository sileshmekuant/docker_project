# -*- coding: utf-8 -*-
from odoo import models, fields, api


class OrderRegistration(models.Model):
    _name = 'order.registration'
    _description = 'Order Registration and Review'

    # SECTION A: Order Register, Review, and Communication
    date_registered = fields.Date(
        string='Date Order Registered',
        default=fields.Date.today
    )
    order_number = fields.Many2one(
        "sale.order",
        string='Order No.',
        required=True
    )
    entered_by = fields.Many2one(
        'res.users',
        string='Order Entered By',
        default=lambda self: self.env.user.id
    )
    order_type = fields.Selection([
        ('oral', 'Oral'),
        ('written', 'Written')
    ], string='Order Type', required=True)

    customer_name = fields.Many2one(
        'res.partner',
        string='Customer Name',
        required=True,
        related="order_number.partner_id"
    )
    customer_requirements = fields.Text(
        string='Customer Requirements (Attendance/Parallels)'
    )

    review_result = fields.Boolean(
       string='Order Review Result', default=False)

    # Fields visible only when review_result is 'accepted'
    technical_spec_attachment = fields.Binary(string='Technical Specification Document')
    technical_spec_filename = fields.Char(string='Filename')

    # Fields visible only when review_result is 'rejected'
    send_sorry_report = fields.Boolean(string='Send Sorry Report')
    rejection_reason = fields.Html(string='Rejection Reason')

    # SECTION B: Technical Specification Verification Results
    customer_verification_result = fields.Selection([
        ('accepted', 'Accept as it is'),
        ('amendment', 'Amendment Required'),
        ('rejected', 'Rejected')
    ], string='Customer Verification Result')

    date_confirmed = fields.Date(string='Date Confirmed')
    amendment_details = fields.Html(string='Amendment Details')

    amendment_accepted = fields.Selection([
        ('yes', 'YES'),
        ('no', 'NO')
    ], string='Is the new amendment accepted by AZ?')

    communicated_to_om = fields.Boolean(string='Communicated to OM')
    communicated_to_others = fields.Many2one('name.store', string='Communicated to Others')

    # Automatically reset communication flags based on review result
    @api.onchange('review_result')
    def _onchange_review_result(self):
        if self.review_result == 'rejected':
            self.send_technical_spec = False
        else:
            self.send_sorry_report = False

    # Action to simulate sending a technical specification
    def action_send_technical_spec(self):
        self.ensure_one()
        if self.review_result == 'accepted':
            self.send_technical_spec = True
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': 'Success',
                    'message': 'Technical specification has been sent to the customer.',
                    'type': 'success',
                    'sticky': False,
                }
            }

    # Action to simulate sending a sorry report
    def action_send_sorry_report(self):
        self.ensure_one()
        if self.review_result == 'rejected':
            self.send_sorry_report = True
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': 'Success',
                    'message': 'Sorry report has been sent to the customer.',
                    'type': 'success',
                    'sticky': False,
                }
            }
