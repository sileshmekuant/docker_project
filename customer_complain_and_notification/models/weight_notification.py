from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class WeightNotification(models.Model):
    _name = 'weight.notification'
    _description = 'Weight Notification'

    to_person = fields.Char(string="To", default="Managing Director")
    from_person = fields.Char(string="From", default="Quality Control")
    date = fields.Date(string="Date")
    recipe_no = fields.Char(string="Recipe No.", required=True) 
    product_type = fields.Char(string="Product Type")
    machine_line = fields.Char(string="Machine Line")
    line_ids = fields.One2many('weight.notification.line', 'notification_id', string="Notification Lines")

    @api.constrains('recipe_no')
    def _check_recipe_no(self):
        for record in self:
            if not record.recipe_no.strip():
                raise ValidationError(_("Recipe No. cannot be empty!"))

class WeightNotificationLine(models.Model):
    _name = 'weight.notification.line'
    _description = 'Weight Notification Line'

    notification_id = fields.Many2one('weight.notification', string="Notification")
    diameter = fields.Float(string="Diameter (mm)", required=True)  # Mandatory field
    thickness = fields.Float(string="Thickness (mm)")
    weight = fields.Float(string="Weight (Kg/PCS)")
    length = fields.Float(string="Length (m)")


    @api.constrains('diameter')
    def _check_diameter(self):
      for record in self:
         if record.diameter:
            try:
                float(record.diameter)
            except ValueError:
                raise ValidationError(_("Diameter must be a numeric value!"))

    @api.constrains('thickness', 'weight', 'length')
    def _check_positive_values(self):
        for record in self:
            if record.thickness <= 0:
                raise ValidationError(_("Thickness must be greater than 0!"))
            if record.weight <= 0:
                raise ValidationError(_("Weight must be greater than 0!"))
            if record.length <= 0:
                raise ValidationError(_("Length must be greater than 0!"))