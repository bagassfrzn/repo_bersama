{
    'name': 'Tilabs Academy',
    'version': '1.0',
    'description': """ This module can manage some features like : 
        - Course
        - Sessions
        - Attendees """,
    'summary': 'Tilabs Academy is testing modul for learning',
    'author': 'Bagas Sfrzn',
    'images': ['static/src/img/academy.png'], 
    'website': 'bagas.id',
    'license': 'LGPL-3',
    'category': 'Knowledge',
    'depends': [
        'base'
    ],
    'data': [
        'security/academy_groups.xml',
        'security/ir.model.access.csv',
        'security/academy_security.xml',
        'data/session_data.xml',
        'views/academy_menuitems.xml',
        'views/course_view.xml',
        'views/session_view.xml',
        'demo/course_demo.xml',
        'wizard/reason_wizard_view.xml',
    ],
    'demo': [
        'demo/course_demo.xml', 
    ],
    'auto_install': False,
    'application': True,
    
}