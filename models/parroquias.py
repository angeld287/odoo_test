# -*- coding: utf-8 -*-
from openerp.osv import fields, osv

class parroquias(osv.osv):
    _name='prueba.parroquias'
    _rec_name='nombre'

    _columns={
        'nombre':fields.char('Nombre del parroquias',size=80,required=True,help='Aqui se coloca el nombre del parroquias'),
        'municipio_id': fields.many2one('prueba.municipios','Nombre del Municipio'),
        'active':fields.boolean('Active'),
    }

    _defaults={
        'active': True
    }