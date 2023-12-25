from odoo import api, models, fields

class Course(models.Model):
    _name = 'academy.course'
    _description = 'Course Info'

    name = fields.Char('Title', required=True)
    active = fields.Boolean('Active', default=True)
    description = fields.Text()
    level = fields.Selection([
                                ('beginner', 'Beginner'),
                                ('intermediate', 'Intermediate'),
                                ('advanced', 'Advanced')
                            ], 
                            string='Level',
                            copy=False)
    
    session_ids = fields.One2many('academy.session', 'course_id', string='Sessions')
    currency_id = fields.Many2one('res.currency', string='currency',default= lambda self:self.env.company.currency_id.id)
    base_price = fields.Monetary(string="Base Price", currency_fields="currency_id")
    additional_fee = fields.Monetary(string="additional fee", currency_fields="currency_id")
    total_price = fields.Monetary(string="total Price", currency_fields="currency_id", compute="_compute_total_price")

    @api.depends("base_price","additional_fee")
    def _compute_total_price(self):
        for record in self:
            if(record.base_price < 0):
                raise ValidationError(("Base Price tidak boleh bernilai negatif"))
            record.total_price = record.base_price + record.additional_fee
