from odoo import models, fields,api

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
    
    @api.model
    def _get_stage_mapping(self):
       return {
        'draft': self.env.ref('maintenance.stage_new').id,  # Example ID
        'request': self.env.ref('maintenance.stage_in_progress').id,
        'approved': self.env.ref('maintenance.stage_done').id,
      }
    
    
    def action_approve(self):
        self.write({'state': 'approved'})
        return True

    def action_draft(self):
        self.write({'state': 'draft'})
        return True

    def action_request(self):
        self.write({'state': 'request'})
        return True
