from odoo import models, fields, api

class EstateProperty(models.Model):
    _name = "estate.property"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Property"

    listed_date = fields.Date(string="Listed Date", default=fields.Date.context_today)
    available_from = fields.Datetime(string="Available From", default=fields.Datetime.now)
    sale_deadline = fields.Datetime(string="Sale Deadline")
    name = fields.Char(string="Property Name", required=True,tracking=True)
    image = fields.Image(string="Property Image",required=True)
    country_id = fields.Many2one('res.country', string="Country")
    region_ids = fields.Many2many('new.region', string="Regions", compute="_get_regions", store=False)

    region_id = fields.Many2one('new.region', string="Region")
    city = fields.Many2one('new.city', string="City")
    sub_city_id = fields.Many2one("sub_city", string="Sub Cities")

    property_type = fields.Many2one('estate.property.type', string="Property Type")
    price_per_sq_m = fields.Float(string="Price per sq.m", related="property_type.price_per_area")
    area = fields.Float(string="Area (sq.m)", related="property_type.area")
    price = fields.Float(string="Total Price", related="property_type.price")
    
    year_built = fields.Datetime(string="Year Built")
    parking_space = fields.Boolean(string="Parking", default=False)
    parking_space_id = fields.Many2one('parking.space', string="Parking Space")

    grand_total = fields.Float(string="Grand Total", compute="_compute_grand_total")
    total_price = fields.Float(string="Total Price", compute="_compute_total_price")
    sold = fields.Boolean(string="Sold", default=False)
    # Fix: Define missing fields
    address_id = fields.Many2one('estate.sub.city', string="Address")
    site_id = fields.Many2one('estate.site', string="Site")

    @api.depends('country_id')
    def _get_regions(self):
        for rec in self:
            rec.region_ids = self.env['new.region'].search([('country', '=', rec.country_id.id)]).ids if rec.country_id else []

    @api.depends('city')
    def _get_sub_city(self):
        for rec in self:
            rec.sub_city_ids = self.env['sub_city'].search([('city_id', '=', rec.city.id)]).ids if rec.city else []

    @api.depends('address_id')
    def _compute_site(self):
        for record in self:
            site = self.env['estate.site'].search([('partner_id', '=', record.address_id.id)], limit=1)
            record.site_id = site.id if site else False

    @api.depends('price_per_sq_m', 'area')
    def _compute_price(self):
        for record in self:
            record.price = record.price_per_sq_m * record.area if record.area and record.price_per_sq_m else 0.0

    @api.depends('area', 'price_per_sq_m', 'parking_space')
    def _compute_total_price(self):
        for record in self:
            record.total_price = record.area * record.price_per_sq_m if record.area and record.price_per_sq_m else 0.0

    @api.depends('price', 'parking_space', 'parking_space_id')
    def _compute_grand_total(self):
        for record in self:
            parking_fee = record.parking_space_id.price_per_month if record.parking_space else 0
            record.grand_total = record.price + parking_fee

    def confirm_wizard(self):
        """Method to create an offer for the selected property"""
        self.ensure_one()
        offer = self.env['estate.property'].create({
            'name': "Offer for " + self.name,
            'price': self.price,  
        })
    def action_sold(self):
        """Method to mark property as sold and show rainbow effect"""
        self.ensure_one()
        self.sold = True
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'Congratulations! The property is sold!',
                'type': 'rainbow_man',
            }
        }

    