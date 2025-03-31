from odoo import models, fields

class RealEstateWizard(models.TransientModel):
    _name = 'real.estate.wizard'
    _description = 'Real Estate Wizard'

    name = fields.Char(string="Name", required=True, default="New Offer")
    propertytype = fields.Many2one('estate.property.type', string="Property Type")
    sale_deadline = fields.Datetime(string="Sale Deadline")
    city = fields.Many2one('new.city', string="City")

    def confirm_wizard(self):
        """Method to create an offer for the selected property"""
        self.ensure_one()
        offer = self.env['estate.property'].create({
            'name': self.name,
            'property_type':self.propertytype.id,
            'sale_deadline':self.sale_deadline ,
            "city":self.city.id
        })
        return {'type': 'ir.actions.act_window_close'}
  
  