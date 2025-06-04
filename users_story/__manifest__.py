{
    'name': 'User story',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Automatically assign leads to regional teams based on location',
    'depends': ['base','sale','crm','website'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/sale_order_views.xml',
        'views/res_partner_view.xml',
        'views/website_form.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': False,
}