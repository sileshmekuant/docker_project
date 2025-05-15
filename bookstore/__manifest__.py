{
   'name': 'Bookstore',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        
        'security/bookstore_security.xml',
        'security/ir.model.access.csv',
        #  'views/author_wizard_view.xml',
        'views/author_wizard_menu.xml',
        'views/book_stor.xml',
        'wizard/author_wizard_view.xml',
    ],
    'application':True,
    "installable":True
}

