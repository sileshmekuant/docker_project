# -*- coding: utf-8 -*-
{
    'name': "fuels_request",

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
    'depends': ['base','hr','fleet','stock','product'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/fuel_request_inherit.xml',
        'views/templates.xml',
        # 'views/fuel_report_views.xml',
        'views/fuel_consumption.xml',
        'views/fuel_request_report.xml',
        'security/security_group.xml',
        "data/sequence.xml"
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

