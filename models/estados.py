# -*- coding: utf-8 -*-
from openerp.osv import fields, osv

class estados(osv.osv):
    _name='prueba.estados'
    _rec_name='nombre'

    _columns={
        'nombre':fields.char('Nombre del estado',size=80,required=True,help='Aqui se coloca el nombre del estado'),
        'active':fields.boolean('Active'),
    }

    _defaults={
        'active': True
    }