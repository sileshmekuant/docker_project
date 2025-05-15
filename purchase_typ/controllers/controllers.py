# -*- coding: utf-8 -*-
# from odoo import http


# class PurchaseTyp(http.Controller):
#     @http.route('/purchase_typ/purchase_typ', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/purchase_typ/purchase_typ/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('purchase_typ.listing', {
#             'root': '/purchase_typ/purchase_typ',
#             'objects': http.request.env['purchase_typ.purchase_typ'].search([]),
#         })

#     @http.route('/purchase_typ/purchase_typ/objects/<model("purchase_typ.purchase_typ"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('purchase_typ.object', {
#             'object': obj
#         })

