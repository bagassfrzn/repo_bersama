from odoo import api, fields, models
from odoo.exceptions import ValidationError 
from odoo.tools import date_utils
from datetime import datetime



class Session(models.Model):
    _name = 'academy.session'
    _rec_name = 'test'
    _description = 'Session Info'

    # name = fields.Char('Title')
    name = fields.Char(string="Title", related="course_id.name",readonly=False)
    # session_number = fields.Char('Session Number', 
    #                              default=lambda self:self.env['ir.sequence'].next_by_code('session.number'))
    session_number = fields.Char('Session Number', 
                                 default="S000", copy=False, required=True, readonly=True)
    # @api.model
    # def create(self, vals):
    #     if vals.get('session_number',('S000'))==('S000'):
    #         vals['session_number'] = self.env['ir.sequence'].next_by_code('session.number')
    date_start = fields.Datetime('date start', required=True)
    date_end = fields.Datetime('date end', required=True)
    status = fields.Selection([
                                ('draft', 'Draft'),
                                ('on_progess', 'On Progress'),
                                ('done', 'Done')
                            ], string='status')

    duration = fields.Integer(string="Duration", compute="_compute_session_duration", inverse="_inverse_session_duration",readonly=False)
    course_id = fields.Many2one('academy.course', string='Course',ondelete='cascade',required=True)
    instructor_id = fields.Many2one('res.users', string='Instructor',ondelete='restrict')
    student_ids = fields.Many2many('res.partner', string='Students')
    level_course = fields.Char('Level Course')
    # description = fields.Text(related="course_id.description")
    description = fields.Text(string="Description")
    test = fields.Char('test', default="Lucky")

    @api.constrains('date_start','date_end','status')
    def _check_end_date(self):
        for session in self:
            if session.status == 'done' and datetime.now() <= session.date_end :
                session.status = self._origin.status
                raise ValidationError('Belum waktunya berakhir')
            if(session.date_start > session.date_end):
                raise ValidationError('Tanggal berakhir tidak bisa sebelum tanggal mulai')
                

    
    @api.onchange('course_id')xml_id
    def _onchange_description_course(self):
        if not self.course_id:
            return {}
        else:
            self.description = self.course_id.description
            self.level_course = self.course_id.level
        return {}

    # @api.onchange('status')
    # def onchange_status(self):
    #     if self.status == 'on_progress':
    #         return {
    #                 'name': 'Change Status Reason',
    #                 'type': 'ir.actions.act_window',
    #                 'res_model': 'reason.wizard.view.form',
    #                 'view_mode': 'form',
    #                 'target': 'new',
    #             }
    

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('session_number',('S000'))==('S000'):
                vals['session_number'] = self.env['ir.sequence'].next_by_code('session.number')
        return super().create(vals_list)

    @api.depends("date_start","date_end")
    def _compute_session_duration(self):
        for record in self:
            if record.date_start and record.date_end:
                record.duration = (record.date_end - record.date_start).days + 1

    def _inverse_session_duration(self):
        for record in self:
            if record.date_start and record.duration:
                record.date_end = date_utils.add(record.date_start, days=record.duration-1)
