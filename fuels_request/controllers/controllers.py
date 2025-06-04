# -*- coding: utf-8 -*-
# from odoo import http


# class FuelsRequest(http.Controller):
#     @http.route('/fuels_request/fuels_request', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fuels_request/fuels_request/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('fuels_request.listing', {
#             'root': '/fuels_request/fuels_request',
#             'objects': http.request.env['fuels_request.fuels_request'].search([]),
#         })

#     @http.route('/fuels_request/fuels_request/objects/<model("fuels_request.fuels_request"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fuels_request.object', {
#             'object': obj
#         })

