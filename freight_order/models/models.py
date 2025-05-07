from odoo import models, fields

class FreightOrder(models.Model):
    _name = 'freight_order.freight_order'
    _description = 'Freight Order'

    type_of_machinery = fields.Char(string="Type of Machinery")
    plate_no = fields.Char(string="Plate No")
    driver_name = fields.Char(string="Driver Name")
    
    starting_km = fields.Float(string="Starting KM")
    place_of_starting = fields.Char(string="Place of Starting")
    place_of_destination = fields.Char(string="Place of Destination")

    purpose_of_receive = fields.Text(string="Purpose of Receive")
    request_by = fields.Many2one('res.users', string="Requested By")
    checked_by = fields.Many2one('res.users', string="Checked By")
    authorized_by = fields.Many2one('res.users', string="Authorized By")

    material_tracking_line_ids = fields.One2many(
        'freight_order.material_tracking_line',
        'freight_order_id',
        string="Material Tracking Lines"
    )
class MaterialTrackingLine(models.Model):
    _name = 'freight_order.material_tracking_line'
    _description = 'Material Tracking Line'

    freight_order_id = fields.Many2one(
        'freight_order.freight_order',
        string="Freight Order",
        ondelete='cascade',
        required=True
    )

    item_no = fields.Char(string="Item No")
    description = fields.Text(string="Description")
    unit = fields.Char(string="Unit")
    quantity = fields.Float(string="Quantity")
    approved_qty = fields.Float(string="Approved Quantity")
    total_price = fields.Float(string="Total Price")
    remark = fields.Text(string="Remark")