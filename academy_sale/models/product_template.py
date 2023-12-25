from odoo import api, fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    detailed_type = fields.Selection(selection_add=[('course','Course')], ondelete={'course': 'set service'})
    course_ids = fields.One2many('academy.course', 'product_id', string='course')

    def _detailed_type_mapping(self):
        type_mapping = super()._detailed_type_mapping()
        type_mapping['course'] = 'service'
        return type_mapping
    