from odoo import models, fields, api
from datetime import timedelta

class StockMove(models.Model):
    _inherit = 'stock.move'

    start_date = fields.Date(string='Start Date', store=False)
    end_date = fields.Date(string='End Date', store=False)
    
    def _compute_dummy(self):
        pass