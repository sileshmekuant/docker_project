from odoo import models, fields, api
from datetime import date

class BookDetails(models.Model):
    _name = 'book.detail'
    _description = 'Book Details'

    title = fields.Char(string='Title', required=True)
    author = fields.Char(string='Author', required=True)
    publisher = fields.Char(string='Publisher')
    published_date = fields.Date(string='Published Date')
    book_age = fields.Integer(string='Book Age', compute='_compute_book_age', store=True)

    @api.depends('published_date')
    def _compute_book_age(self):
        for record in self:
            if record.published_date:
                current_year = date.today().year
                published_year = record.published_date.year
                record.book_age = current_year - published_year
            else:
                record.book_age = 0

    

