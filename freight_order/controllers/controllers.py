# -*- coding: utf-8 -*-
# from odoo import http


# class FreightOrder(http.Controller):
#     @http.route('/freight_order/freight_order', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/freight_order/freight_order/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('freight_order.listing', {
#             'root': '/freight_order/freight_order',
#             'objects': http.request.env['freight_order.freight_order'].search([]),
#         })

#     @http.route('/freight_order/freight_order/objects/<model("freight_order.freight_order"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('freight_order.object', {
#             'object': obj
#         })

