from odoo import models, fields

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    register_by_id = fields.Many2one('hr.employee', string='Register By')
    approved_by_id = fields.Many2one('hr.employee', string='Approved By')
    certified_by_id = fields.Many2one('hr.employee', string='Certified By')
