from odoo import models, fields

class FleetVehicle(models.Model):  
    _inherit = 'fleet.vehicle'

    branch = fields.Many2one('res.users', string='Branch')
