from odoo import models, fields, api

class Task(models.Model):
    _name = 'plan.task'
    _description = 'Task'

    name = fields.Char(string="Task Name", required=True)
    plan_id = fields.Many2one('plan.plan', string="Related Plan", required=True)
    is_verified = fields.Boolean(string="Verified", default=False)

    def action_verify(self):
        """ Verify the task """
        for task in self:
            task.is_verified = True

    def action_print_plan(self):
        """ Print Plan Action """
        return {
            'type': 'ir.actions.report',
            'report_name': 'planing.report_plan_template',  # Replace with actual report name
            'model': 'plan.task',
            'report_type': 'qweb-pdf',
            'ids': self.ids,
        }
