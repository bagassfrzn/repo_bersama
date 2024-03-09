from odoo import models,fields

class regist_model(models.Model):
    _name = 'itclub.regist'
    _description = 'model itclub regist'

    nama = fields.Char('Nama Siswa')
    nis = fields.Integer('Nis Siswa')
    nisn = fields.Integer('Nisn Siswa')
    kelas = fields.Selection([
                                ('x', 'Kelas X'),
                                ('xi','kelas XI'),
                                ('xii','kelas XII')
                            ], string='Kelas Siswa')
    jurusan = fields.Selection([
                                ('bdp', 'BISNIS DARING PEMASARAN'),
                                ('otkp','OTOMATISASI TATA KELOLA PERKANTORAN'),
                                ('akl','AKUNTANSI KEUANGAN LEMBAGA'),
                                ('rpl','REKAYASA PERANGKAT LUNAK')
                            ], string='Program keahlian')
    


    