# -*- coding: utf-8 -*-

from odoo import models, fields


class GoodsPass(models.Model):
    _name = 'good.pass'
    _description = 'Damaged Goods'

    client_name = fields.Many2one('res.partner', string="Client Name")
    date = fields.Date(string="Date")
    inspected_by = fields.Many2one('hr.employee', string='Description')
    approved_by = fields.Many2one('hr.employee', string='Approved By')
    damaged_goods_pass_ids = fields.One2many(
        'damaged.goods.pass',
        'damaged_goods_ids',
        string="Receiving Notes"
    )
    state = fields.Selection([
        ('draft', 'Draft'),
        ('inspectedby', 'Inspected By'),
        ('approved', 'Approved'),
    ],
        default='draft',
        string="State")
    def action_set_draft(self):
        for record in self:
            record.state = 'draft'
            # self.action_set_received()
    def action_set_received(self):
        for record in self:
            record.state = 'inspectedby'
            record.inspected_by = self.env.user.employee_id.id
            # self.action_set_delivered()

    def action_set_delivered(self):
        for record in self:
            record.state = 'approved'
            record.approved_by = self.env.user.employee_id.id



class DamagedGoodsPass(models.Model):
    _name = 'damaged.goods.pass'
    _description = 'Damaged Goods Receiving Notes'

    damaged_goods_ids = fields.Many2one('good.pass', string="Damaged Goods")
    product_no = fields.Integer(string='Product No', required=True)
    description = fields.Html(string='Description')
    quantity = fields.Float(string='Quantity')
    isue_no = fields.Integer(string='Issue No', required=True)
    remark = fields.Html(string="Remark")


