
from odoo import models, fields


class StoredNames(models.Model):
    _name = 'name.store'
    _description = 'Name Store'

    name = fields.Char(string="Stored Name")