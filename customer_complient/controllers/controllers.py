# -*- coding: utf-8 -*-
# from odoo import http


# class Azpip(http.Controller):
#     @http.route('/azpip/azpip', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/azpip/azpip/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('azpip.listing', {
#             'root': '/azpip/azpip',
#             'objects': http.request.env['azpip.azpip'].search([]),
#         })

#     @http.route('/azpip/azpip/objects/<model("azpip.azpip"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('azpip.object', {
#             'object': obj
#         })

