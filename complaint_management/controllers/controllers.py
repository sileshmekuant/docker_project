# -*- coding: utf-8 -*-
# from odoo import http


# class ComplaintManagement(http.Controller):
#     @http.route('/complaint_management/complaint_management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/complaint_management/complaint_management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('complaint_management.listing', {
#             'root': '/complaint_management/complaint_management',
#             'objects': http.request.env['complaint_management.complaint_management'].search([]),
#         })

#     @http.route('/complaint_management/complaint_management/objects/<model("complaint_management.complaint_management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('complaint_management.object', {
#             'object': obj
#         })

