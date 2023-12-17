# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Demo Data Pos',
    'version' : '1',
    'summary': 'Demo data sudoerp',
    'sequence': 10,
    'description': """ """,
    'category': '',
    'website': '',
    'depends' : ['base_setup', 'point_of_sale'],
    'data': ['data/pos_demo.xml'],
    'demo': [
        'demo/pos_demo.xml',
    ],

    'installable': True,
    'application': True,
    'post_init_hook': '',
    'license': 'LGPL-3',
}
