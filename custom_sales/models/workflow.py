from odoo import models, fields, api

class WorkflowRule(models.Model):
    _name = 'custom.workflow.rule'
    _description = 'Workflow Automation Rules'
    
    name = fields.Char(required=True)
    trigger_state = fields.Selection([
        ('quotation', 'Quotation'),
        ('reserved', 'Reserved'),
        ('contract_signed', 'Contract Signed'),
        ('deposit_paid', 'Deposit Paid'),
        ('full_payment', 'Full Payment'),
    ], string="Trigger On")
    
    action = fields.Selection([
        ('send_email', 'Send Email'),
        ('create_activity', 'Schedule Activity'),
        ('update_field', 'Update Field'),
    ], string="Action")
    
    email_template_id = fields.Many2one('mail.template')
    activity_type_id = fields.Many2one('mail.activity.type')
    field_id = fields.Many2one('ir.model.fields', domain="[('model_id.model', '=', 'sale.order')]")
    field_value = fields.Char()
    
    # Document checklist
    document_template_ids = fields.Many2many('ir.attachment', string="Required Documents")
    