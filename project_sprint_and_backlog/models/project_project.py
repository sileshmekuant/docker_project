from odoo import models, fields, api

class ProjectProject(models.Model):
    _inherit = 'project.project'

    sprint_ids = fields.One2many('project.sprint', 'project_id', string='Sprints')
