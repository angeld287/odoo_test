# -*- coding: utf-8 -*-
from openerp.osv import fields, osv

class municipios(osv.osv):
    _name='prueba.municipios'
    _rec_name='nombre'

    _columns={
        'nombre':fields.char('Nombre del municipios',size=80,required=True,help='Aqui se coloca el nombre del municipios'),
        'estado_id': fields.many2one('prueba.estados','Estado'),
        'active':fields.boolean('Active'),
    }

    _defaults={
        'active': True
    }