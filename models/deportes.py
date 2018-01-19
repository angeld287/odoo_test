# -*- coding: utf-8 -*-
from openerp.osv import fields, osv

class deportes(osv.osv):
    _name='prueba.deportes'
    _rec_name='nombre'

    _columns={
        'nombre':fields.char('Nombre del deporte',size=80,required=True,help='Aqui se coloca el nombre del deporte'),
        'active':fields.boolean('Active'),
    }

    _defaults={
        'active': True
    }