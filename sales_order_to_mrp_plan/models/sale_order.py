from odoo import models,fields

class SaleOrder(models.Model):
    _inherit="sale.order"

    job_order_created=fields.Boolean(string="Job Order Created",default=False)
    # def action_confirm(self):
    #     res = super().action_confirm()

    #         if not line.product_id.categ_id.is_raw_material:
    #             self.env['mrp.planing'].create({
    #                 'product':line.product_template_id.id,
    #                 'customer_id':self.partner_id.id,
    #                 'quantity':line.product_uom_qty,
    #                 'sales_order':self.id
    #             })
            
    def action_create_job_order(self):

        for line in self.order_line:
            if not line.product_id.categ_id.is_raw_material:
                self.env['mrp.planing'].create({
                    'product':line.product_template_id.id,
                    'customer_id':self.partner_id.id,
                    'quantity':line.product_uom_qty,
                    'sales_order':self.id
                })
        self.job_order_created=True
        
