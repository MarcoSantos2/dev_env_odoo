{
    'name': "Marco's estate app 2",
    'version': '1.0',
    'author': 'Marco',
    'depends': ['base'],
    'application': True,
    'category': 'Real Estate',
    'description': 'Real estate management module',
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_menus.xml'      
    ],
}