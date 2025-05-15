from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ForeignPurchaseWorkflow(models.Model):
    _name = 'foreign.purchase.workflow'
    _description = 'Foreign Purchase Workflow'
    state = fields.Selection([
        ('invoice', 'Invoice'),
        ('lt_form', 'LT Form'),
        ('currency', 'Currency'),
        ('bank_import', 'Bank Import'),
        ('bill', 'Bill'),
        ('clearance', 'Clearance'),
    ], default='invoice', string="State")



    proforma_invoice = fields.Binary(string="Attach proforma invoice")
    lt_form = fields.Binary(string="Attach LT form")
    currency_approval = fields.Binary(string="Attach single window (foreign currency approval)")
    import_permit = fields.Binary(string="Attach single window (bank import permit)")
    awb = fields.Binary(string="Attach AWB/bill of landing")
    clearance_form = fields.Binary(string="Attach custom clearance form")

    proforma_invoice_cost = fields.Float(string="Proforma Invoice Cost")
    lt_form_cost = fields.Float(string="LT Form Cost")
    currency_approval_cost = fields.Float(string="Currency Approval Cost")
    import_permit_cost = fields.Float(string="Import Permit Cost")
    awb_cost = fields.Float(string="AWB Cost")
    clearance_form_cost = fields.Float(string="Clearance Form Cost")



    @api.constrains('cost')
    def _check_cost_positive(self):
        for rec in self:
            if rec.cost <= 0:
                raise ValidationError("Cost must be greater than 0.")
    
    
    def set_state_invoice(self):
        self.ensure_one()
        self.state = 'lt_form'

    def set_state_lt_form(self):
         self.write({'state': 'lt_form'})
         self.state = 'currency'

    def set_state_currency(self):
        self.write({'state': 'currency'})
        self.state = 'bank_import'

    def set_state_bank_import(self):
        self.write({'state': 'bank_import'})
        self.state = 'bill'

    def set_state_bill(self):
        self.write({'state': 'bank_import'})
        self.state = 'clearance'

    def set_state_clearance(self):
        self.write({'state': 'bank_imclearanceport'})
