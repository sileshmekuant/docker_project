{
    'name': 'Planning train',
    'version': '1.0',
    'depends': ['base','mail'],
    'data': [
         'data/cron_jobs.xml',
         'security/ir.model.access.csv',
        'views/plan.xml',
         'views/task.xml', 
   
        'report/plan_report_template.xml',
             'report/plan_report.xml',
    ],
    'installable': True,
    'application': True,
}
