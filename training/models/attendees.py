# from odoo import models, fields

# class TrainingAttendees(models,Model):
#     _name = 'training.attendees'
#     _description = 'Training Attendees'
    
#     attendee_id = fields.Many2one('res.partner',string='Attendee')
#     presence = fields.Boolean(string='Presence')
#     training_id = fields.Many2one('training.module',string='Training')
#     attendees_ids = fields.One2many('training.attendees','training_id',string='Attendees')
#     phone = fields.related('attendee_id.phone',string='Phone')
    
    
