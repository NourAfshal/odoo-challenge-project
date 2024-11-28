{
    'name': 'Sales Dashboard for Real-Time Monitoring',
    'version': '1.0',
    'summary': 'Monitor sales routes, activities, and inventory in real time.',
    'description': 'This module provides a dashboard for sales managers to oversee sales rep activities, routes, customer visits, and inventory levels.',
    'author': 'Nour',
    'category': 'Sales',
    'depends': ['sale', 'stock', 'crm', 'web_dashboard'],
    'data': [
        'views/sales_dashboard_views.xml',
        'views/actions.xml',
        'views/menuitems.xml',
    ],
    'installable': True,
    'application': True,
}
