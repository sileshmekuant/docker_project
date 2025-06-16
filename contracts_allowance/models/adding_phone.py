from odoo import models, fields

class HrEmployee(models.Model):
    _inherit = 'hr.contract'

    phone_allowance = fields.Float("Phone/Internet Allowance")
    fuel_allowance = fields.Float("Fuel Allowance")
