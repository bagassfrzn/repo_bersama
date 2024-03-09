from odoo import api, models, fields

class dama_purchase(models.Model):
    _name = 'dama.purchase'
    _rec_name = 'status'
    _description = 'model purchase custom'

    name = fields.Char('Nama')
    tanggal = fields.Date('Tanggal')
    status = fields.Selection([
                                # yg masuk db , tampilan
                                ('draft', 'Draft'),
                                ('approve', 'Approve'),
                                ('done', 'Done')
                             ], string='Status')

    status_bar = fields.Selection([
                                # yg masuk db , tampilan
                                ('draft', 'Draft'),
                                ('approve', 'Approve'),
                                ('done', 'Done')
                             ], string='Status')
                            
    @api.onchange('status')
    def _onchange_status(self):
        if not self.status:
            return{}
        else:
            self.status_bar = self.status
        return{}        