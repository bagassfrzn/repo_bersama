{
    'name' : "training",
    'summary' : """ringkasan info modul odoo training""",
    'description' : """
        Training module for managing training : 
                - Training course
    """,
    'author' : "bagas",
    'website' : "https://www.bagas.com",
    'category' : 'Test',
    'version' : '1.0',
    
    #any module needed for this modul work correctly
    'depends' : [
        'base',
    ],
    
    #always loaded
    'data' : [
        'views/training.xml',
        'security/ir.model.access.csv',
    ],
    
    #only loaded in demo mode
    'demo' : [
        
    ],
}