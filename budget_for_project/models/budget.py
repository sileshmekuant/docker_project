from odoo import models, fields,api

class Project(models.Model):
    _inherit = 'project.project'

    budget = fields.Monetary(string='Budget', currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.company.currency_id)