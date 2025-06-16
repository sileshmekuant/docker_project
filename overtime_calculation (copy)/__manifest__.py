{
    'name': 'HR Attendance Overtime',
    'version': '1.0',
    'depends': ['base','hr_attendance', 'hr_contract'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/hr_attendance.xml'
    ],
    'installable': True,
    'auto_install': False,
}