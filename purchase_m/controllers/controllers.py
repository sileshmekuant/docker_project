# -*- coding: utf-8 -*-
# from odoo import http


# class PurchaseM(http.Controller):
#     @http.route('/purchase_m/purchase_m', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/purchase_m/purchase_m/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('purchase_m.listing', {
#             'root': '/purchase_m/purchase_m',
#             'objects': http.request.env['purchase_m.purchase_m'].search([]),
#         })

#     @http.route('/purchase_m/purchase_m/objects/<model("purchase_m.purchase_m"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('purchase_m.object', {
#             'object': obj
#         })

