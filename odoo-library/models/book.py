class book(models.Model):
    _name = 'book.module'
    _description = 'modul untuk buku'

    name = fields.Char('Judul Buku')
    active = fields.Boolean('active',default=True)
    isbn = fields.Char('No. isbn')
    genre = fields.Char('genre')
    summary = fields.Text('summary')
    author = fields.Char('author')
    field_name = fields.Selection([
                                    ('key', 'value')
                                ], string='field_name')
    
    