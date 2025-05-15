from odoo import models, api,fields
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = "sale.order"

    sale_type= fields.Selection([(i,i.capitalize()) for i in ['bid','proforma','whole sale','direct']],string="Sale Type",default="direct")

    is_approved = fields.Boolean(default=False)

    def action_approve_order(self):
        for order in self:
            order.is_approved = True
        #  return {
        #      'type': 'ir.actions.client',
        #     'tag': 'reload',
        #  }
    
    # @api.model
    # def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
    #     res = super().fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu)

    #     if view_type == 'form' and self.env.context.get('params', {}).get('id'):
    #         order = self.browse(self.env.context['params']['id'])
    #         if order and not order.is_approved:
    #             custom_view = self.env.ref('your_module.view_sale_order_form_pre_approval')
    #             res = super().fields_view_get(view_id=custom_view.id, view_type='form', toolbar=toolbar, submenu=submenu)
    #     return res
    
    


    def action_confirm(self):
        for order in self:
            if not self.env.user.has_group('sales_evan.group_sale_order_approver'):
                raise UserError("Only Sales Approvers can confirm quotations.")
        return super(SaleOrder, self).action_confirm()
