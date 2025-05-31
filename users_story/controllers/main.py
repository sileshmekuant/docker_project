from odoo import http
from odoo.http import request

class LeadsFormController(http.Controller):

    @http.route(['/leads/form'], type='http', auth="public", website=True)
    def leads_form(self, **kwargs):
        return request.render("users_story.leads_form_template")

    @http.route(['/submit/leads'], type='http', auth="public", methods=["POST"], website=True, csrf=True)
    def submit_leads_form(self, **post):
        _logger = http.logging.getLogger(__name__)
        _logger.info("Form submitted: %s", post)
        return request.redirect('/thank-you')
