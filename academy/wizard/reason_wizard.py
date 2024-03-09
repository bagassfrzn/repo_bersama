from odoo import models, fields, api

class reason(models.TransientModel):
    _name = 'reason.wizard'
    _description = 'reason'

    reason = fields.Text('reason', required=True)
    
    
    def submit_reason(self):
        # Your code here
        return {'type': 'ir.actions.act_window_close'}