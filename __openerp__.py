{
	'name':'prueba',
	'author': 'Angel Angeles',
	'version': '1.0',
	'depends': ['base_setup'],
	'category': '',
	'description': """
	Mi primera prueba en ODOO
	""",
	'update_xml': [],
	'data': [
		'views/estudiantes_view.xml',
		'views/estados_view.xml',
		'views/municipios_view.xml',
		'views/parroquias_view.xml'
	],
	'installable': True,
	'auto_install': False,
}