# -*- coding: utf-8 -*-
# from odoo import http


# class CrmM(http.Controller):
#     @http.route('/crm_m/crm_m', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/crm_m/crm_m/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('crm_m.listing', {
#             'root': '/crm_m/crm_m',
#             'objects': http.request.env['crm_m.crm_m'].search([]),
#         })

#     @http.route('/crm_m/crm_m/objects/<model("crm_m.crm_m"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('crm_m.object', {
#             'object': obj
#         })

