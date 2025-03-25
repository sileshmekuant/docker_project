# -*- coding: utf-8 -*-
# from odoo import http


# class SalesM(http.Controller):
#     @http.route('/sales_m/sales_m', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sales_m/sales_m/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sales_m.listing', {
#             'root': '/sales_m/sales_m',
#             'objects': http.request.env['sales_m.sales_m'].search([]),
#         })

#     @http.route('/sales_m/sales_m/objects/<model("sales_m.sales_m"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sales_m.object', {
#             'object': obj
#         })

