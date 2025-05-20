from odoo import models, fields

class VehicleStock(models.Model):
    _name = 'vehicle.stock'
    _description = 'Vehicle Stock Report'

    date = fields.Date(string='Date')
    receiving_note = fields.Char(string='Receiving Note')
    vehicle_exit = fields.Char(string='Vehicle Exit')
    description = fields.Char(string='Description')
    chassis_no = fields.Char(string='Chassis No')
    engine_no = fields.Char(string='Engine No')
    model_year = fields.Char(string='Model Year')
    plate_no = fields.Char(string='Plate No')
    sold_date = fields.Date(string='Sold Date')
    remark = fields.Char(string='Remark')
    beginning_balance = fields.Integer(string='Beginning Balance')
    stock_in = fields.Integer(string='Stock In')
    stock_out = fields.Integer(string='Stock Out')
    ending_balance = fields.Integer(string='Ending Balance')
    team_code = fields.Char(string='Team Code')
    year = fields.Char(string='Year')
    location = fields.Char(string='Location')
