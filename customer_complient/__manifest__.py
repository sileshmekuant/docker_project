# -*- coding: utf-8 -*-
{
    'name': "Customer Complaint",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr','stock','mail','sale_management'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security_view.xml',

        'views/views.xml',
        'views/name_store.xml',
        'views/damaged_goods.xml',
        'views/good_pass.xml',
        'views/templates.xml',

        'report/report_menu.xml',
        'report/report_template.xml',

        'report/order_report_menu.xml',  
        'report/order_report_template.xml',
        'report/damaged_good.xml',
        'report/good_pass.xml',

        'data/sequence.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
