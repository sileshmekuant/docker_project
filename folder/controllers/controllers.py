# -*- coding: utf-8 -*-
# from odoo import http


# class Folder(http.Controller):
#     @http.route('/folder/folder', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/folder/folder/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('folder.listing', {
#             'root': '/folder/folder',
#             'objects': http.request.env['folder.folder'].search([]),
#         })

#     @http.route('/folder/folder/objects/<model("folder.folder"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('folder.object', {
#             'object': obj
#         })

