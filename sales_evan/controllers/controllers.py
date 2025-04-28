# -*- coding: utf-8 -*-
# from odoo import http


# class SalesEvan(http.Controller):
#     @http.route('/sales_evan/sales_evan', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sales_evan/sales_evan/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sales_evan.listing', {
#             'root': '/sales_evan/sales_evan',
#             'objects': http.request.env['sales_evan.sales_evan'].search([]),
#         })

#     @http.route('/sales_evan/sales_evan/objects/<model("sales_evan.sales_evan"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sales_evan.object', {
#             'object': obj
#         })

