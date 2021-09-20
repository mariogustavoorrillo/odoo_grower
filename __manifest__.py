# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Odoo Grower',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Odoo Grower',
    'depends': ['web','base','sale_management','sale','account','crm'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml'
    ],
    'demo': [
    ],
    'css': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
