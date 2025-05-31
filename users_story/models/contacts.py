from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    
    regional_team_id = fields.Many2one('crm.team', string='Regional Team')
