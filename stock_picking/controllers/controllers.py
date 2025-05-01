# -*- coding: utf-8 -*-
# from odoo import http


# class StockPicking(http.Controller):
#     @http.route('/stock_picking/stock_picking', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/stock_picking/stock_picking/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('stock_picking.listing', {
#             'root': '/stock_picking/stock_picking',
#             'objects': http.request.env['stock_picking.stock_picking'].search([]),
#         })

#     @http.route('/stock_picking/stock_picking/objects/<model("stock_picking.stock_picking"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('stock_picking.object', {
#             'object': obj
#         })

