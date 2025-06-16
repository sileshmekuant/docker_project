from odoo import models, fields,api

class ProjectProject(models.Model):
    _inherit = 'project.project'

    department_id = fields.Many2one('hr.department', string='Department',required=True)
   

    