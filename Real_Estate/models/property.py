from odoo import models, fields, api

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Property"

    name = fields.Char(string="Property Name", required=True)
    site_id = fields.Many2one('estate.site', string="Site",)
    #address_id = fields.Many2one('estate.sub.city', string="address")
    region_id = fields.Many2one('estate.region', string="Region")  
    property_type = fields.Many2one('estate.property.type',string="property_type")
    sub_city_id = fields.Many2one("estate.sub.city", string="Sub Cities")
    price_per_sq_m = fields.Float(string="Price per_sq_m", compute="_compute_total_price", related="property_type.price_per_area")
    area = fields.Float(string="Area (sq.m)", related="property_type.area")
    price = fields.Float(string="Total Price", related="property_type.price" )
    
    year_built = fields.Datetime(string="Year Built")
    parking_space = fields.Boolean(string="Parking",default=False) 
    parking_space_id = fields.Many2one('parking.space', string="Parking Space")
    #parking_name = fields.Char(related='parking_space_id.name', string="Parking Space Name", store=True)
    grand_total = fields.Float(string="Grand Total", compute="_compute_grand_total")

    # @api.onchange('region_id')
    # def _onchange_region_id(self):
    #     if self.region_id:
    #         return {'domain': {'sub_city_id': [('region_id', '=', self.region_id.id)]}}
    #     return {'domain': {'sub_city_id': []}}
    @api.depends('price')
    def _compute_grand_total(self):
        for record in self:
            record.grand_total = record.price 
    @api.depends('address_id')
    def _compute_site(self):
        for record in self:
            if record.address_id:
                
                site = self.env['estate.site'].search([('partner_id', '=', record.address_id.id)], limit=1)
                record.site_id = site.id if site else False
            else:
                record.site_id = False

    @api.depends('price_per_area', 'area')
    def _compute_price(self):
        for record in self:
            record.price = record.price_per_area * record.area if record.area and record.price_per_area else 0.0
     
    

    @api.depends('area', 'price_per_area', 'parking_space')
    def _compute_total_price(self):
        for record in self:
            record.total_price = record.area * record.price_per_area if record.area and record.price_per_area else 0.0
    @api.depends('price', 'parking_space','parking_space_id')
    def _compute_grand_total(self):
        for record in self:
            parking_fee = record.parking_space_id.price_per_month if record.parking_space else 0  # Example parking fee
            record.grand_total = record.price + parking_fee