from odoo import http
from odoo.http import request
import logging

_logger = logging.getLogger(__name__)


class LeadsFormController(http.Controller):

    @http.route(['/leads/form'], type='http', auth="public", website=True)
    def leads_form(self, **kwargs):
        return request.render("users_story.leads_form_template")

    @http.route(['/submit/leads'], type='http', auth="public", methods=["POST"], website=True, csrf=False)
    def submit_leads_form(self, **post):
        _logger = http.logging.getLogger(__name__)
        _logger.info("Form submitted: %s", post)

        name = post.get('name')
        email = post.get('email')
        region_input = post.get('regional_team')

        # Try to find a Sales Team matching the input region
        team = request.env['crm.team'].sudo().search([
            ('name', 'ilike', region_input)
        ], limit=1)

        # Create the lead
        request.env['crm.lead'].sudo().create({
            'name': name,
            'email_from': email,
            'team_id': team.id if team else False,
            'description': f"Submitted via website form. Region: {region_input}",
        })

        return request.redirect('/thank-you')


    @http.route('/thank-you', type='http', auth='public', website=True)
    def thank_you(self, **kwargs):
        return "<h1>Thank you for your submission!</h1>"
    
