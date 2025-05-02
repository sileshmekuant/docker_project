from odoo import models, fields,api

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    register_by_id = fields.Many2one('hr.employee', string='Register By')
    approved_by_id = fields.Many2one('hr.employee', string='Approved By')
    certified_by_id = fields.Many2one('hr.employee', string='Certified By')
    is_store_fp = fields.Boolean(compute='_compute_type_flags', store=True)
    is_pick_components = fields.Boolean(compute='_compute_type_flags', store=True)

    @api.depends('picking_type_id.name')
    def _compute_type_flags(self):
        for rec in self:
            type_name = rec.picking_type_id.name or ''
            rec.is_store_fp = 'Store Finished Product' in type_name
            rec.is_pick_components = 'Pick Components' in type_name
