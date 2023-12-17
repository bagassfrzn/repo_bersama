{
    'name' : "modul baru",
    'summary' : """modul dibuat untuk nambah field di absensi""",
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
        'absensi'
        ],
    
    # always loaded
    'data' : [
        'views/fieldbaru.xml',
        ],
    
    'demo' : [
        
    ],
} 