from odoo import api, fields, models
from odoo.exceptions import ValidationError 

class Session(models.Model):
    _name = 'academy.session'
    _description = 'Session Info'
    
    name = fields.Char('Title')
    # session_number = fields.Char('Session Number', 
    #                              default=lambda self:self.env['ir.sequence'].next_by_code('session.number'))
    session_number = fields.Char('Session Number', 
                                 default="S000", copy=False, required=True, readonly=True)
    # @api.model
    # def create(self, vals):
    #     if vals.get('session_number',('S000'))==('S000'):
    #         vals['session_number'] = self.env['ir.sequence'].next_by_code('session.number')
    #     return super().create(vals)
    date_start = fields.Datetime('date start', required=True)
    date_end = fields.Datetime('date end', required=True)
    course_id = fields.Many2one('academy.course', string='Course',ondelete='cascade',required=True)
    instructor_id = fields.Many2one('res.users', string='Instructor',ondelete='restrict')
    student_ids = fields.Many2many('res.partner', string='Students')

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('session_number',('S000'))==('S000'):
                vals['session_number'] = self.env['ir.sequence'].next_by_code('session.number')
        return super().create(vals_list)

    @api.constrains('date_start','date_end')
    def _check_end_date(self):
        for session in self:
            if(session.date_start > session.date_end):
                raise ValidationError('Tanggal berakhir tidak bisa sebelum tanggal mulai')
