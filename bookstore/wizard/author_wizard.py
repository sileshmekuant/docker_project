from odoo import models, fields, api

class AuthorWizard(models.TransientModel):
    _name = 'author.wizard'
    _description = 'Author Wizard'

    name = fields.Char(string="Author Name", required=True)
    birth_date = fields.Date(string="Date of Birth")
    biography = fields.Text(string="Biography")

    def action_create_author(author):
        """ Create an author record and close the wizard """
        author.env['bookstore.author'].create({
            'name': author.name,
            'birth_date': author.birth_date,
            'biography': author.biography,
        })
        return {'type': 'ir.actions.act_window_close'}
