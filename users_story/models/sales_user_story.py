from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    region_team_id = fields.Many2one('crm.team', string='Regional Team')

    @api.model
    def create(self, vals):
        # Call the parent create method
        record = super(SaleOrder, self).create(vals)
        
        # Automatically assign regional team based on customer location
        if record.partner_id and not record.region_team_id:
            location = record.partner_id.state_id  # Using state as location
            if location:
                team = self.env['crm.team'].search([('name', 'ilike', location.name)], limit=1)
                if team:
                    record.region_team_id = team.id
        
        return record
