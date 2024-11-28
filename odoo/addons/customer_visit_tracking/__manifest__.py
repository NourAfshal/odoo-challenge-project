{
    'name': 'Customer Visit Tracking',
    'version': '1.0',
    'summary': 'Schedule, track, and report customer visits.',
    'description': 'This module allows sales reps to schedule visits, check in at customer locations, and report visit outcomes.',
    'author': 'Nour',
    'category': 'Sales',
    'depends': ['sale', 'crm'],
    'data': [
        'views/visit_views.xml',
        'views/actions.xml',
        'views/menuitems.xml',
    ],
    'installable': True,
    'application': True,
}
