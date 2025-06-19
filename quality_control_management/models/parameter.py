from odoo import models, fields, api

class Parameter(models.Model):
    _name = 'parameter.parameter'
    _description = 'parameters Log'
   

    # General Info
    name = fields.Char(string='name')
    # active = fields.Boolean(default=True)