from odoo import models,fields

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
    