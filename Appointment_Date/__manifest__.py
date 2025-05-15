{
    'name': "appointment_date",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "for pharmacy",
    

    
    'category': 'Uncategorized',
    'version': '0.1',

    
    'depends': ['base'],

    # always loaded
    'data': [
         'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    
    'demo': [
        'demo/demo.xml',
    ],
}

