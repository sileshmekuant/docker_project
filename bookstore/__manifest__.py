{
   'name': 'Bookstore',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'views/book_stor.xml',
        'security/bookstore_security.xml',
         'views/author_wizard_view.xml',
        'views/author_wizard_menu.xml',
        'wizard/author_wizard_view.xml',
    ],
    'application':True,
    "installable":True
}

