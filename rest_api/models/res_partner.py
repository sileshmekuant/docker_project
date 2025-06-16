from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo.tools import logging

_logger = logging.getLogger(__name__)

class ResPartner(models.Model):
    _inherit = 'res.partner'

    synced_to_crm = fields.Boolean(string="Synced to External CRM", default=False)

    @api.model
    def create(self, vals):
        partner = super().create(vals)
        if partner.customer_rank > 0:
            partner.sync_with_external_crm()
        return partner

    def write(self, vals):
        res = super().write(vals)
        for partner in self:
            if partner.customer_rank > 0:
                partner.sync_with_external_crm()
        return res

    def sync_with_external_crm(self):
        for partner in self:
            if not partner.email:
                continue
            try:
                self.env['crm.sync.service']._send_to_crm(partner)
                partner.synced_to_crm = True
            except Exception as e:
                _logger.error(f"Failed to sync partner {partner.id}: {str(e)}")
                raise UserError("Error syncing with external CRM")
