# -*- coding: utf-8 -*-
{
    'name': "Complaint",
    'version': '0.1',
    'category': 'Tools',
    'summary': "Anonymous complaint form with limited access chatter",
    'author': "Your Name",
    'depends': ['base', 'mail'],
    'data': [
            'security/groups.xml',
            'security/ir.model.access.csv',
            'data/sequence.xml',
            'views/complaint_views.xml',

    ],
    'installable': True,
    'application': True,
}
