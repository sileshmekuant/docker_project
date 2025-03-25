from odoo import models, fields, api

class ParkingSpaceWizard(models.TransientModel):
    _name = 'parking.space.wizard'
    _description = 'Parking Space Assignment Wizard'

    property_id = fields.Many2one('estate.property', string="Property", required=True)
    parking_space_ids = fields.Many2many('parking.space', string="Parking Spaces")

    def assign_parking_spaces(self):
        """Assign selected parking spaces to the property"""
        if self.property_id:
            self.property_id.parking_space_ids = [(6, 0, self.parking_space_ids.ids)]
            for space in self.parking_space_ids:
                space.property_id = self.property_id
        return {'type': 'ir.actions.act_window_close'}  # Close wizard after action
