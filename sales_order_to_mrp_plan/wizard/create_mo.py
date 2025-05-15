from odoo import models, fields, api,_

from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)

from datetime import datetime

class CreateManufacturingOrder(models.TransientModel):
    _name = "create.manufacturing.order"
    _description = "create manufacturing order"

    product = fields.Many2one('product.template', string="Product")
    start_date = fields.Datetime(string="Start Date")
    end_date = fields.Datetime(string="End Date")
    quantity = fields.Float(string="Quantity")
    
    shift = fields.Selection([
        ('day','Day'),
        ('night','Night')
    ],string="Shift")

    duration = fields.Float(
        string="Duration (Hours)",
        compute="_compute_duration",
        store=False,
        readonly=True,
        help="Duration between Start Date and End Date in hours."
    )

    @api.depends('start_date', 'end_date')
    def _compute_duration(self):
        for record in self:
            if record.start_date and record.end_date:
                delta = record.end_date - record.start_date
                record.duration = delta.total_seconds() / 3600  # Convert to hours
            else:
                record.duration = 0.0

    
    @api.model
    def default_get(self, fields_list):
        _logger.info("########################################## list 88888888888888")
        res = super(CreateManufacturingOrder, self).default_get(fields_list)
        active_id = self.env.context.get('active_id')
        if active_id:
            mrp_plan = self.env['mrp.planing'].browse(active_id)
            res.update({
                'product': mrp_plan.product.id,
                'quantity': mrp_plan.quantity,
            })
        return res
    
    def action_create(self):
        self.ensure_one()
        mrp_plan = self.env['mrp.planing'].browse(self.env.context.get('active_id'))
        bom = self.env['mrp.bom'].search([
            ('product_tmpl_id', '=', self.product.id)
        ], limit=1)

        if not bom:
            raise ValueError("No Bill of Materials found for the selected product.")

        move_raw_ids = [
            (0, 0, {
                'product_id': line.product_id.id,
                'product_uom_qty': line.product_qty * self.quantity / bom.product_qty,
                'product_uom': line.product_uom_id.id,
                'name': line.product_id.display_name,
                'location_id': self.env['stock.location'].search([('usage', '=', 'internal')], limit=1).id,
                'location_dest_id': self.env['stock.location'].search([('usage', '=', 'production')], limit=1).id,
            })
            for line in bom.bom_line_ids
        ]

        product_product = self.env['product.product'].search(
            [('product_tmpl_id', '=', self.product.id)], limit=1
        )
        if self.quantity>mrp_plan.quantity:
           raise ValidationError(_("Please Check Quantity"))

        production = self.env['mrp.production'].create({
            'product_id': product_product.id,
            'product_uom_id': self.product.uom_id.id,
            'product_qty': self.quantity,
            'date_start': self.start_date,
            'bom_id': bom.id,
            'move_raw_ids': move_raw_ids,
            'state': 'draft',
            'mrp_plan': mrp_plan.id,
            'shift': self.shift,
        })
        mrp_plan.quantity-=self.quantity
        production.write({'date_finished': self.end_date})
        mrp_plan.write({
                'production_ids': [(4, production.id)]
            })
        if production.workorder_ids:
            for workorder in production.workorder_ids:
                workorder.duration_expected = float(self.duration)*60

        return {'type': 'ir.actions.act_window_close'}

