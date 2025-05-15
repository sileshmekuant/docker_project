# -*- coding: utf-8 -*-
# from odoo import http


# class MaintenanceReq(http.Controller):
#     @http.route('/maintenance_req/maintenance_req', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/maintenance_req/maintenance_req/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('maintenance_req.listing', {
#             'root': '/maintenance_req/maintenance_req',
#             'objects': http.request.env['maintenance_req.maintenance_req'].search([]),
#         })

#     @http.route('/maintenance_req/maintenance_req/objects/<model("maintenance_req.maintenance_req"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('maintenance_req.object', {
#             'object': obj
#         })

