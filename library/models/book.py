from odoo import models,fields

class book(models.Model):
    _name = 'book.modul'
    _description = 'book.modul'
    _rec_name = 'judul'
    
    judul = fields.Char('judul')
    isbn = fields.Char('isbn')
    penerbit = fields.Char('penerbit')
    penulis = fields.Char('penulis')
    tanggal_terbit = fields.Date('tanggal terbit')
    jumlah_cetak = fields.Integer('jumlah cetak')
    sinopsis = fields.Text('sinopsis')

    vendor = fields.Char('vendor')
    harga = fields.Integer('harga')
    het = fields.Integer('Harga Eceran tertinggi')
    tanggal_beli = fields.Date('tanggal beli')
    jumlah_pembelian = fields.Integer('jumlah pembelian')
    responsible = fields.Char('responsible')

    view_type = fields.Selection([
                                    ('admin', 'View Admin'),
                                    ('user', 'View User')
                                ], string='View Type', required=True, default='user')
