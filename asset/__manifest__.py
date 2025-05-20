{
    'name': 'Asset Manage',
    'version': '1.0',
    'summary': 'Manage company assets assigned to employees',
    'description': 'A module to track and manage company asset properties assigned to employees.',
    'author': 'Silesh',
    'depends': ['base', 'product', 'hr', 'mail'],  
    'data': [
        'views/asset.xml',
        'views/employee.xml',
        'security/ir.model.access.csv',
        'report/asset_report.xml',
        'report/asset_report_template.xml',
        'report/asset_report_xlsx.xml',
        'data/cron_jobs.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'asset/static/src/js/asset_dashboard.js',
            'asset/static/src/xml/asset_dashboard.xml',
        ],
    },
    'installable': True,
    'application': True,
    'license': 'LGPL-3',  
}
