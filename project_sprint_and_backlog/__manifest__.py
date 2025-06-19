{
    'name': 'project sprint and backlog',
    'version': "1.0",
    'depends': ['base', 'project'],
    'data': [
        'security/ir.model.access.csv',
        'views/project_sprint_views.xml',
        'views/project_project_views.xml',
        'views/project_backlog_veiws.xml',
        'views/project_task_views.xml',
        
    ],
    'installable': True,
    'application': True,
}
