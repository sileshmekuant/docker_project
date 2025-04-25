{
    'name': 'Travel Manag',
    'version': '1.0',
    'summary': 'Manage employee travel bookings, approvals, and expenses',
    'category': 'Human Resources',
    'author': 'ASHEWA SmartERP',
    'depends': ['base', 'hr'],
    'data': [       
        'security/ir.model.access.csv',

        'views/travel_booking_views.xml',
       
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
