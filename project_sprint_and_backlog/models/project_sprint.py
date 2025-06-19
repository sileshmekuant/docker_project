from odoo import models, fields, api

class ProjectSprint(models.Model):
    _name = 'project.sprint'
    _description = 'Sprint'
     

    project_id = fields.Many2one('project.project', string='Project', required=True)
    sprint_ids = fields.One2many('project.sprint', 'project_id', string='Sprints')
    name = fields.Char(string='Sprint Name', required=True)
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    task_ids = fields.One2many('project.task', 'sprint_id', string='Sprint Tasks')
