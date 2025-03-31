from odoo import models, fields

class RealEstateWizard(models.TransientModel):
    _name = 'real.estate.wizard'
    _description = 'Real Estate Wizard'

    name = fields.Char(string="Name", required=True, default="New Offer")
    price = fields.Float(string="Price") 
    property_id = fields.Many2one('real.estate.property', string="Property",required=True)
    offer_price = fields.Float(string="Offer Price", required=True, default=0.0)
    buyer_id = fields.Many2one('res.partner', string="Buyer")

    def confirm_wizard(self):
        """Method to create an offer for the selected property"""
        self.ensure_one()
        offer = self.env['real.estate.property'].create({
            # 'property_id': self.property_id.id,
            'name': "Offer for " + self.buyer_id.name,
            
            'price': self.offer_price,
            'buyer_id': self.buyer_id.id,
        })
        return {'type': 'ir.actions.act_window_close'}
  
  