{
    'name': 'Asset manage',
    'version': '1.0',
    'summary': 'Manage company assets assigned to employees',
    'description': 'A module to track and manage company asset properties assigned to employees.',
    'author': 'silesh',
    'depends': ['base', 'product', 'hr'],
    'data': [
        'views/asset.xml',
        'views/employee.xml',
        'security/ir.model.access.csv',
        'report/asset_report.xml',
        'report/asset_report_template.xml',
        'report/asset_report_xlsx.xml',
        'data/cron_jobs.xml',
    ],
    
    'installable': True,
    'application': True,
}
