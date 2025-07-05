from odoo import models, fields

class PropertyBooking(models.Model):
    _name = 'property.booking'
    _description = 'Property Booking'

    customer_id = fields.Many2one('res.partner', string='Customer', required=True)
    property_id = fields.Many2one('property', string='Property', required=True)
    booking_date = fields.Date(string='Booking Date', default=fields.Date.today)
    note = fields.Text(string='Note')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='draft')

    def action_confirm(self):
        for rec in self:
            rec.state = 'confirmed'

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancelled'

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'
