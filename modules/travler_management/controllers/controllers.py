# -*- coding: utf-8 -*-
# from odoo import http


# class TravlerManagement(http.Controller):
#     @http.route('/travler_management/travler_management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/travler_management/travler_management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('travler_management.listing', {
#             'root': '/travler_management/travler_management',
#             'objects': http.request.env['travler_management.travler_management'].search([]),
#         })

#     @http.route('/travler_management/travler_management/objects/<model("travler_management.travler_management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('travler_management.object', {
#             'object': obj
#         })

