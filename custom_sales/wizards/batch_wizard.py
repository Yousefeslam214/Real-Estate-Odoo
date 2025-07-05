from odoo import models, fields, api

class BatchProcessingWizard(models.TransientModel):
    _name = 'batch.processing.wizard'
    _description = 'Batch Processing Wizard'
    
    order_id = fields.Many2one('sale.order', required=True)
    product_ids = fields.Many2many('product.product', string="Products")
    discount_value = fields.Float(string="Discount Value")
    discount_type = fields.Selection([
        ('fixed', 'Fixed Amount'),
        ('percentage', 'Percentage')
    ], string="Discount Type")
    batch_reference = fields.Char(string="Batch Reference")
    
    def apply_batch_processing(self):
        for product in self.product_ids:
            self.env['sale.order.line'].create({
                'order_id': self.order_id.id,
                'product_id': product.id,
                'name': product.name,
                'price_unit': product.lst_price,
                'batch_reference': self.batch_reference,
                'discount_policy': self.discount_type,
                'product_uom_qty': 1,
            })
        
        # Apply discounts
        if self.discount_value:
            lines = self.order_id.order_line.filtered(
                lambda l: l.batch_reference == self.batch_reference
            )
            
            for line in lines:
                if self.discount_type == 'fixed':
                    line.price_unit -= self.discount_value
                elif self.discount_type == 'percentage':
                    line.price_unit *= (1 - self.discount_value / 100.0)