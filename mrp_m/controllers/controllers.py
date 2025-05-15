# -*- coding: utf-8 -*-
# from odoo import http


# class MrpM(http.Controller):
#     @http.route('/mrp_m/mrp_m', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mrp_m/mrp_m/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('mrp_m.listing', {
#             'root': '/mrp_m/mrp_m',
#             'objects': http.request.env['mrp_m.mrp_m'].search([]),
#         })

#     @http.route('/mrp_m/mrp_m/objects/<model("mrp_m.mrp_m"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mrp_m.object', {
#             'object': obj
#         })

