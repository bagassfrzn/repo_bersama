from odoo import models, fields
 
class AbsensiModels(models.Model):
    _name = 'absen.modul'
    _description = 'aplikasi absensi'
    
    name = fields.Char(string="Nama Siswa")
    nis = fields.Char(string="No Induk Siswa")
    date = fields.Datetime(string="Tanggal absen")
    grade = fields.Selection([('x', 'X'),('xi','XI'),('xii','XII')], string="Kelas")
    majoring = fields.Selection([('rpl', 'RPL'),('bdp','BDP'),('otkp','OTKP'),('akl','AKL')], string="Jurusan")
    division = fields.Selection([('web development', 'Web Development'),('uiux design','UI/UX Design'),('graphic design','Graphic Design')], string="Divisi")
    trainer = fields.Many2one('res.users',string="Trainer")
    training = fields.Many2one('training.module', string="Course")
    status = fields.Selection(related='training.state',string="status")
    
    
     