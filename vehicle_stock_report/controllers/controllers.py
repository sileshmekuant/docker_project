# -*- coding: utf-8 -*-
# from odoo import http


# class VehicleStockReport(http.Controller):
#     @http.route('/vehicle_stock_report/vehicle_stock_report', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vehicle_stock_report/vehicle_stock_report/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('vehicle_stock_report.listing', {
#             'root': '/vehicle_stock_report/vehicle_stock_report',
#             'objects': http.request.env['vehicle_stock_report.vehicle_stock_report'].search([]),
#         })

#     @http.route('/vehicle_stock_report/vehicle_stock_report/objects/<model("vehicle_stock_report.vehicle_stock_report"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vehicle_stock_report.object', {
#             'object': obj
#         })

