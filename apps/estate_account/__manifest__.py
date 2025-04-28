{
    'name': 'Real Estate Account',
    'version': '1.0',
    'category': 'Real Estate',
    'summary': 'Real Estate Account Integration',
    'description': """
        This module integrates the Real Estate module with the Accounting module.
    """,
    'depends': ['estate', 'account'],
    'data': [
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
} 