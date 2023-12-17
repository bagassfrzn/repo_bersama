from odoo import models, fields


class TrainingModels(models.Model):
    _name = 'training.module'
    _description = 'Training Course'
    
    #create fields
    name = fields.Char(string=' ')
    registration_amount = fields.Float(string='Registration Amount')
    date = fields.Date(string='Training Date')
    description = fields.Text(string='Description')
    state = fields.Selection([('draft', 'Draft'), ('inprogress', 'In Progress'), ('done', 'Done')], string='Status')
    total_attendees = fields.Integer(string='Total Attendees')
    trainer_id = fields.Many2one('trainer.module',string='Trainer')
    # trainer_phone = fields.Char('trainer_id.phone',string='Trainer')
    # assistant_ids = fields.Many2one('res.users',string='Assistant')
    asisten = fields.Many2many('res.users',string='asisten')

class TrainerModels(models.Model):
    _name = 'trainer.module'
    _description = 'trainer master data'
    
    name = fields.Char(string=' ')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    description = fields.Text(string='Description')
    
    