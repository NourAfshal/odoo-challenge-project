{
    'name': 'Inventory Monitoring at Customer Locations',
    'version': '1.0',
    'summary': 'Track inventory levels, stock alerts, and sales metrics at customer sites.',
    'description': 'This module enables sales reps to track inventory levels at customer locations, receive stock alerts, and analyze sales metrics.',
    'author': 'Nour',
    'category': 'Inventory',
    'depends': ['sale', 'stock', 'crm'],
    'data': [
        'views/inventory_views.xml',
        'views/actions.xml',
        'views/menuitems.xml',
    ],
    'installable': True,
    'application': True,
}
