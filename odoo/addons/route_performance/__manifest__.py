{
    'name': 'Route Optimization and Performance Analysis',
    'version': '1.0',
    'summary': 'Optimize sales routes and analyze sales rep performance.',
    'description': 'This module provides route optimization and performance insights for sales reps, including optimal travel suggestions and analytics.',
    'author': 'Nour',
    'category': 'Sales',
    'depends': ['sale', 'stock', 'crm', 'web_dashboard', 'base_geolocalize'],
    'data': [
        'views/route_performance_views.xml',
        'views/actions.xml',
        'views/menuitems.xml',
    ],
    'installable': True,
    'application': True,
}
