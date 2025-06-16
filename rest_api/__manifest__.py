{
    'name': 'rest api',
    'version': '1.0',
    'summary': 'Sync Odoo customers with external CRM via REST API',
    'category': 'Sales',
    'author': 'sis',
    'depends': ['base', 'contacts'],
    'data': [
        'views/res_partner_views.xml',
    ],
    'installable': True,
    'application': True,
}
