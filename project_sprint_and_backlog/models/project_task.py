from odoo import models, fields

class ProjectTask(models.Model):
    _inherit = 'project.task'

    sprint_id = fields.Many2one('project.sprint', string='Sprint')
    is_backlog = fields.Boolean(string='Backlog Item', default=True)
    backlog_id = fields.Many2one('project.backlog', string="Backlog")
