# -*- coding: utf-8 -*-
# from odoo import http


# class Hosipital(http.Controller):
#     @http.route('/hosipital/hosipital', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hosipital/hosipital/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hosipital.listing', {
#             'root': '/hosipital/hosipital',
#             'objects': http.request.env['hosipital.hosipital'].search([]),
#         })

#     @http.route('/hosipital/hosipital/objects/<model("hosipital.hosipital"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hosipital.object', {
#             'object': obj
#         })

