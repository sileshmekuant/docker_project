from odoo import models, fields

class MaintenanceRequestCustom(models.Model):
    _inherit = 'maintenance.request'


     
    state = fields.Selection([
        ('draft', 'Draft'),
        ('request', 'Requested'),
        ('approved', 'Approved'),
    ], string='Status', default='draft', readonly=True, tracking=True)
   
    request_for=fields.Selection([
        ('pm_servece', 'pm servece'),
        ('repaire', 'repaire'),
        ('warranty', 'warranty'),
        
    ], string='request for', default='pm_servece',  tracking=True)
   
    MAINTENANCE_REQUEST_PRIORITY = fields.Selection([
        ('URGENT', 'URGENT'),
        ('HIGH', 'HIGH'),
        ('MEDIUM', 'MEDIUM'),
        ('LOW', 'LOW'),
    ], string='maintenance request', default='URGENT',  tracking=True)
    
    
    asset_code = fields.Char(string='Asset Code')
    comment = fields.Text(string='Comment')
    approved_by = fields.Many2one('res.users', string='Approved By', ondelete='set null')
    # signature = fields.Binary(string='Signature')
    date = fields.Date(string='Approval Date')
    
    
    def action_approve(self):
        for record in self:
            record.state = 'approved'

    def action_draft(self):
        for record in self:
            record.state = 'draft'

    def action_request(self):
        for record in self:
            record.state = 'request'
