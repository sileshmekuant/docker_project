import requests
from odoo import models
from odoo.tools import logging

_logger = logging.getLogger(__name__)

class CrmSyncService(models.AbstractModel):
    _name = 'crm.sync.service'
    _description = 'External CRM Sync Service'

    def _send_to_crm(self, partner):
        url = "https://external-crm.example.com/api/customers"
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer YOUR_API_KEY"
        }
        payload = {
            "id": partner.id,
            "name": partner.name,
            "email": partner.email,
            "phone": partner.phone,
            "address": f"{partner.street or ''}, {partner.city or ''}, {partner.country_id.name or ''}"
        }

        response = requests.post(url, json=payload, headers=headers, timeout=10)

        if response.status_code not in [200, 201]:
            _logger.error("CRM Sync Failed: %s - %s", response.status_code, response.text)
            raise Exception("External CRM sync failed")
