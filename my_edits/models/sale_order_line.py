# models/sale_order_line.py
from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    property_id = fields.Many2one(
        'real.estate.property',
        string='Property'
    )

    @api.onchange('property_id')
    def _onchange_property_id(self):
        for line in self:
            if line.property_id:
                line.name = line.property_id.name
                line.price_unit = line.property_id.price
