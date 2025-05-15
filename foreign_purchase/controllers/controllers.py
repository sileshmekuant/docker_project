# -*- coding: utf-8 -*-
# from odoo import http


# class ForeignPurchase(http.Controller):
#     @http.route('/foreign_purchase/foreign_purchase', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/foreign_purchase/foreign_purchase/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('foreign_purchase.listing', {
#             'root': '/foreign_purchase/foreign_purchase',
#             'objects': http.request.env['foreign_purchase.foreign_purchase'].search([]),
#         })

#     @http.route('/foreign_purchase/foreign_purchase/objects/<model("foreign_purchase.foreign_purchase"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('foreign_purchase.object', {
#             'object': obj
#         })

