from odoo import models, fields,api

class ProjectBacklog(models.Model):
    _name = 'project.backlog'
    _description = 'Project Backlog'

    name = fields.Char(string="Backlog Name", required=True)
    project_id = fields.Many2one('project.project', string="Project", required=True)
    task_ids = fields.One2many('project.task', 'backlog_id', string="Backlog Tasks")
 
    backlog_task_ids = fields.One2many(
    'project.task', 
    'sprint_id', 
    string="Backlog Tasks",
    compute='_compute_backlog_tasks',
    store=False
    )

    @api.depends('task_ids.is_backlog')
    def _compute_backlog_tasks(self):
        for sprint in self:
            sprint.backlog_task_ids = sprint.task_ids.filtered(lambda t: t.is_backlog)
