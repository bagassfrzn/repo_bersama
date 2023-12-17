{
    'name': 'Tilabs Academy',
    'version': '1.0',
    'description': """ This module can manage some features like : 
        - Course
        - Sessions
        - Attendees """,
    'summary': 'Tilabs Academy is testing modul for learning',
    'author': 'Bagas Sfrzn',
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
    ],
    'demo': [
        'demo/course_demo.xml', 
    ],
    'auto_install': False,
    'application': True,
    
}