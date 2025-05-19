# -*- coding: utf-8 -*-
from email.policy import default

from odoo import models, fields


class DamagedGoods(models.Model):
    _name = 'damaged.goods'
    _description = 'Damaged Goods'
    _inherit = ['mail.thread']

    name=fields.Char(string="Ref.", default="New")
    department = fields.Many2one('hr.department', string="Department",tracking=True)
    source_location = fields.Many2one('stock.location',string="From",tracking=True)
    destination_location = fields.Many2one('stock.location',string="To",tracking=True)
    reason = fields.Char(string="Reason", size=50, unique=True,tracking=True)
    received_by = fields.Many2one('hr.employee', string="Received By", size=50, unique=True,tracking=True)
    delivered_by = fields.Many2one('hr.employee', string="Delivered By",tracking=True)
    damaged_goods_receiving_ids = fields.One2many(
        'damaged.goods.receiving.notes',
        'damaged_goods_id',
        string="Receiving Notes"
    ,tracking=True)

    state = fields.Selection([
        ('draft', 'Draft'),
        ('received', 'Received'),
        ('delivered', 'Delivered'),
    ],
        default='draft',
        string="State")

    def action_set_draft(self):
        for record in self:
            record.state = 'draft'
            # self.action_set_received()
    def action_set_received(self):
        for record in self:
            record.state = 'received'
            record.received_by = self.env.user.employee_id.id
            # self.action_set_delivered()

    def action_set_delivered(self):
        for record in self:
            record.state = 'delivered'
            record.delivered_by = self.env.user.employee_id.id

    
class DamagedGoodsReceivingNotes(models.Model):
    _name = 'damaged.goods.receiving.notes'
    _description = 'Damaged Goods Receiving Notes'

    damaged_goods_id = fields.Many2one('damaged.goods', string="Damaged Goods")
    ref = fields.Integer(string='Ref No', required=True)
    voucher_no = fields.Integer(string='Transfer Voucher No', required=True)
    description = fields.Text(string='Description')
    unit_measure = fields.Many2one('uom.uom',string="Unit of Measure")
    quantity = fields.Float(string='Quantity')
    remark = fields.Html(string="Remark")
