{
    'name' : "absensi",
    'summary' : """modul dibuat untuk absensi""",
    'description' : """
                        ini adalaah modul absen. data yang dibutuhkan :
                                        - data diri
                    """, 
    'author' : "Bagas Safrizan Fadilah",
    'website' : "",
    'category' : 'test',
    'version' : '1.0',
    
    #any module needed for this modul work correctly
    'depends' : [
        'base','training',
        ],
    
    # always loaded
    'data' : [
        'views/absensi.xml',
        'security/ir.model.access.csv',
        ],
    
    'demo' : [
        
    ],
} 