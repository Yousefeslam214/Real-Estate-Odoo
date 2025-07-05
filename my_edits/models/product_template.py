# models/product_template.py

from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    new_field = fields.Char(string="New Field")
    # type = fields.Selection(selection_add=[], string='Product Type', required=True)

    # def _get_selection_type(self):
    #     return [
    #         ('product', 'Inventory Item'),   # change label
    #         ('consu', 'Disposable Item'),    # change label
    #         ('service', 'Service'),          # keep same
    #     ]