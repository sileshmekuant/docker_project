from odoo import models, fields, api, exceptions
import logging

_logger = logging.getLogger(__name__)

class Plan(models.Model):
    _name = 'plan.plan'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Plan'

    name = fields.Char(string="Plan Name", required=True)
    description = fields.Text(string="Description")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('approved', 'Approved'),
    ], string="Status", default="draft", tracking=True)
    task_ids = fields.One2many('plan.task', 'plan_id', string="Tasks")
    
    # 🔹 Add these two computed fields
    is_readonly = fields.Boolean(string="Is Readonly", compute="_compute_is_readonly", store=True)
    is_editable = fields.Boolean(string="Is Editable", compute="_compute_is_editable", store=True)
    # state_color = fields.Char(string="State Color", compute="_compute_state_color", store=True)
    image =fields.Image(string="image")

    @api.depends('state')
    def _compute_is_readonly(self):
        """Compute readonly field based on state"""
        for record in self:
            record.is_readonly = record.state != 'draft'

    @api.depends('state')
    def _compute_is_editable(self):
        """Compute editable field to disable adding/deleting tasks"""
        for record in self:
            record.is_editable = record.state == 'draft'

    def action_approve(self):
        """Approve the plan"""
        self.write({'state': 'approved'})
    
    def write(self, vals):
        """Prevent editing if plan is approved"""
        for record in self:
            if record.state == 'approved':
                raise exceptions.UserError("You cannot edit an approved plan.")
        return super().write(vals)

    def unlink(self):
        """Prevent deleting approved plans"""
        for record in self:
            if record.state == 'approved':
                raise exceptions.UserError("You cannot delete an approved plan.")
        return super().unlink()
    def auto_approve_plans(self):
        """Cron job to auto-approve plans that are waiting for approval"""
        plans = self.search([('state', '=', 'waiting_approval')])
        for plan in plans:
            plan.state = 'approved'
            _logger.info(f"Plan {plan.name} approved by cron job")



      
    # @api.depends('state')
    # def _compute_state_color(self):
    #     """Compute state color for decoration in tree view"""
    #     for record in self:
    #         if record.state == 'approved':
    #             record.state_color = 'success'
    #         else:
    #             record.state_color = 'muted'


# from odoo import models, fields, api

# class Plan(models.Model):
#     _name = 'plan.plan'
#     _inherit = ['mail.thread', 'mail.activity.mixin']
#     _description = 'Plan'

#     name = fields.Char(string="Plan Name", required=True)
#     description = fields.Text(string="Description")
#     state = fields.Selection([
#         ('draft', 'Draft'),
#         ('approved', 'Approved'),
#     ], string="Status", default="draft")
#     task_ids = fields.One2many('plan.task', 'plan_id', string="Tasks")

#     def action_approve(self):
#         """Approve the plan"""
#         self.write({'state': 'approved'})
