from odoo import models, api,fields
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = "sale.order"

    sale_type= fields.Selection([(i,i.capitalize()) for i in ['bid','proforma','whole sale','direct']],string="Sale Type",default="direct")


    def action_confirm(self):
        for order in self:
            if not self.env.user.has_group('sales_evan.group_sale_order_approver'):
                raise UserError("Only Sales Approvers can confirm quotations.")
        return super(SaleOrder, self).action_confirm()
