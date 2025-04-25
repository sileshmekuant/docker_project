# from odoo import models, fields, api

# class HrEmployee(models.Model):
#     _inherit = 'hr.employee'

#     asset_assignment_count = fields.Integer(
#         string='Asset Assignments',
#         compute='_compute_asset_assignment_count'
#     )

#     def _compute_asset_assignment_count(self):
#         for employee in self:
#             employee.asset_assignment_count = self.env['asset.assignment'].search_count([
#                 ('employee_id', '=', employee.id)
#             ])
