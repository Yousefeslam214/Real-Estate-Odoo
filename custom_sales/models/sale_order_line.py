from odoo import models, fields, api

class CustomSaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    
    batch_reference = fields.Char(string="Batch ID")
    discount_policy = fields.Selection([
        ('fixed', 'Fixed Discount'),
        ('percentage', 'Percentage Discount'),
    ], string="Discount Type")
    
    # Automatic description
    @api.onchange('product_id')
    def _onchange_product_id(self):
        if self.product_id:
            self.name = f"{self.product_id.name} - {self.product_id.description_sale or ''}"