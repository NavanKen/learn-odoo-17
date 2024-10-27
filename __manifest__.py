{
    'name': "Data Siswa",
    'version': '1.0',
    'depends': ['base'],
    'author': "Nopal",
    'category': 'App',
    'description': """
        modul untuk menyimpan data siswa
    """,
    'application': True,
    'data': [ 
        'security/ir.model.access.csv',

        # Vies
        'views/menu.xml',
        'views/siswa.xml',
],

}
