from odoo import models, fields

class book(models.Model):
    _name = 'book.module'
    _description = 'modul untuk buku'

    name = fields.Char('Judul Buku')
    active = fields.Boolean('active',default=True)
    isbn = fields.Char('No. isbn')
    genre = fields.Char('genre')
    summary = fields.Text('summary')
    author = fields.Char('author')
    format = fields.Selection([
                                    ('paperback', 'Paperback'),
                                    ('hardcover', 'hardcover'),
                                    ('audiobook', 'audiobook'),
                                    ('e-book', 'e-book'),
                                ], string='format')
    language = fields.Selection([
                                    ('en', 'en'),
                                    ('es', 'es'),
                                    ('fr', 'fr'),
                                    ('de', 'de'),
                                ], string='Language')
    edition = fields.Integer('edition')
    publisher = fields.Char('publisher')
    publish_date = fields.Date('publish date')
    price = fields.Monetary('price')

    
    