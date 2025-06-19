from odoo import models, fields


class PipeDimensionSheet(models.Model):
    _name = 'pipe.dimension.sheet'
    _description = 'Pipe Dimension Sheet'

    name = fields.Char(string="Name", required=True)
    line_ids = fields.One2many('pipe.dimension.line', 'sheet_id', string='Dimensions')


class PipeDimensionLine(models.Model):
    _name = 'pipe.dimension.line'
    _description = 'Pipe Dimension Line'

    sheet_id = fields.Many2one('pipe.dimension.sheet', string='Sheet', required=True, ondelete='cascade')

    od_mm = fields.Float(string='OD (mm)', required=True)

    sdr26_min = fields.Float(string='SDR26 Min')
    sdr26_max = fields.Float(string='SDR26 Max')

    sdr21_min = fields.Float(string='SDR21 Min')
    sdr21_max = fields.Float(string='SDR21 Max')

    sdr17_min = fields.Float(string='SDR17 Min')
    sdr17_max = fields.Float(string='SDR17 Max')

    sdr136_min = fields.Float(string='SDR13.6 Min')
    sdr136_max = fields.Float(string='SDR13.6 Max')

    sdr11_min = fields.Float(string='SDR11 Min')
    sdr11_max = fields.Float(string='SDR11 Max')

    sdr9_min = fields.Float(string='SDR9 Min')
    sdr9_max = fields.Float(string='SDR9 Max')
