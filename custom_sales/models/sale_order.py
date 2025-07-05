from odoo import models, fields, api

class CustomSaleOrder(models.Model):
    _inherit = 'sale.order'
    property_id = fields.Many2one('estate.property', string="Property", tracking=True)

    
    # Workflow State Field
    custom_state = fields.Selection([
        ('quotation', 'Quotation'),
        ('reserved', 'Reserved'),
        ('contract_signed', 'Contract Signed'),
        ('deposit_paid', 'Deposit Paid'),
        ('full_payment', 'Full Payment'),
        ('handover', 'Handover')
    ], string='Workflow State', default='quotation', tracking=True)
    
    deadline_date = fields.Date(string="Contract Deadline")
    payment_terms = fields.Text(string="Payment Terms")
    
    # Dynamic pricing update
    def update_dynamic_prices(self):
        for order in self:
            if order.state in ['draft', 'sent']:  # Only update unconfirmed quotes
                for line in order.order_line:
                    line.price_unit = line.product_id.lst_price
    
    # State progression
    def action_next_state(self):
        state_order = dict(self.fields_get()['custom_state']['selection'])
        states = list(state_order.keys())
        current_index = states.index(self.custom_state)
        if current_index < len(states) - 1:
            self.custom_state = states[current_index + 1]
    
    # Document generation
    def generate_custom_report(self):
        return self.env.ref('sale.action_report_saleorder').report_action(self)

    def action_batch_processing_wizard(self):
        return {
            'name': 'Batch Add Products',
            'type': 'ir.actions.act_window',
            'res_model': 'batch.processing.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_order_id': self.id,
            },
        }