import logging
from odoo import models, fields, api
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)

class ProductAsset(models.Model):
    _inherit = 'product.product'

    asset_name = fields.Char(string="Asset Name", required=True)
    serial_number = fields.Char(string="Serial Number", required=True)
    description = fields.Text(string="Description")
    is_asset = fields.Boolean(string="Is an Asset", default=True)
    category_id = fields.Many2one('asset.category', string="Asset Category")  # Ensure category exists

    sql_constraints = [
        ('unique_serial_number', 'unique(serial_number)', 'Serial Number must be unique!')
    ]


class AssetAssignment(models.Model):
    _name = 'asset.assignment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Asset Assignment'

    name = fields.Char(string="Assignment Name", required=True, default="New")
    image = fields.Image(string="Image")
    asset_id = fields.Many2one('product.product', string="Asset", domain=[('is_asset', '=', True)], required=True)
    category_id = fields.Many2one('product.category',related='asset_id.categ_id', string="Category")  
    employee_id = fields.Many2one('hr.employee', string="Assigned To", required=True)
    assignment_date = fields.Date(string="Assignment Date", default=fields.Date.today, required=True)
    return_deadline = fields.Date(string="Return Deadline", help="The date by which the asset should be returned.")
    return_date = fields.Date(string="Return Date")

    state = fields.Selection([
        ('assigned', 'Assigned'),
        ('return_requested', 'Return Requested'),
        ('return_verified', 'Return Verified'),
        ('returned', 'Returned'),
        ('overdue', 'Overdue')
    ], string="Status", default="assigned", tracking=True)

    @api.depends('asset_id')
    def _compute_category(self):
        """ Auto-set category from asset. """
        for record in self:
            if record.asset_id and record.asset_id.category_id:
                record.category_id = record.asset_id.category_id.id
            else:
                record.category_id = False  # Ensure field is set properly

    @api.constrains('assignment_date', 'return_deadline', 'return_date')
    def _check_assignment_dates(self):
        for record in self:
            if record.return_deadline and record.assignment_date > record.return_deadline:
                raise ValidationError("Assignment Date cannot be after the Return Deadline.")
            if record.return_date and record.assignment_date > record.return_date:
                raise ValidationError("Assignment Date cannot be after the Return Date.")
            if record.return_deadline and record.return_deadline < record.assignment_date:
                raise ValidationError("Return Deadline cannot be before the Assignment Date.")
            if record.return_date and record.return_date < record.assignment_date:
                raise ValidationError("Return Date cannot be before the Assignment Date.")

    @api.depends('return_deadline', 'return_date', 'state')
    def _compute_status(self):
        today = fields.Date.today()
        for record in self:
            if record.state in ['returned', 'return_verified']:
                continue
            if record.state == 'return_requested' and record.return_date:
                record.state = 'return_verified'
            elif record.return_date:
                record.state = 'returned'
            elif record.return_deadline and today > record.return_deadline:
                record.state = 'overdue'

    def action_request_return(self):
        for record in self:
            if record.state == 'assigned':
                _logger.info(f"Action Request Return triggered for {record.name}.")
                record.state = 'return_requested'

    def action_verify_return(self):
        for record in self:
            if record.state == 'return_requested':
                _logger.info(f"Action Verify Return triggered for {record.name}.")
                record.state = 'return_verified'

    def action_return_asset(self):
        for record in self:
            if record.state == 'return_verified':
                _logger.info(f"Returning asset {record.asset_id.name if record.asset_id else 'Unknown'} assigned to {record.employee_id.name if record.employee_id else 'Unknown'}.")
                record.write({'state': 'returned', 'return_date': fields.Date.today()})

    def action_mark_overdue(self):
        for record in self:
            if record.state in ['assigned', 'return_requested', 'return_verified']:
                _logger.info(f"Manually marking {record.asset_id.name if record.asset_id else 'Unknown'} assigned to {record.employee_id.name if record.employee_id else 'Unknown'} as overdue.")
                record.state = 'overdue'

    def action_check_overdue(self):
        today = fields.Date.today()
        overdue_records = self.search([
            ('state', 'in', ['assigned', 'return_requested', 'return_verified']),
            ('return_deadline', '<', today),
        ])

        for record in overdue_records:
            _logger.info(f"Marking asset {record.asset_id.name if record.asset_id else 'Unknown'} assigned to {record.employee_id.name if record.employee_id else 'Unknown'} as overdue.")
            record.state = 'overdue'

    def name_get(self):
        result = []
        for record in self:
            asset_name = record.asset_id.name if record.asset_id else "Unknown Asset"
            employee_name = record.employee_id.name if record.employee_id else "Unknown Employee"
            result.append((record.id, f"{asset_name} - {employee_name}"))
        return result

    @api.model
    def create(self, vals):
        """ Auto-assign category when creating an assignment. """
        asset = self.env['product.product'].browse(vals.get('asset_id')) if vals.get('asset_id') else None
        employee = self.env['hr.employee'].browse(vals.get('employee_id')) if vals.get('employee_id') else None
        asset_name = asset.name if asset else "Unknown Asset"
        employee_name = employee.name if employee else "Unknown Employee"
        if asset:
            vals['category_id'] = asset.category_id.id  # Auto-fill category
        vals['name'] = f"{asset_name} - {employee_name}"
        return super(AssetAssignment, self).create(vals)
    # def toggle_action_buttons(self):
    #     # This is a dummy method just to trigger JS toggle from the form
    #     return {
    #             'type': 'ir.actions.client',
    #             'tag': 'reload',  # optional, or use JS directly
                #}
