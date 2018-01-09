# -*- coding: utf-8 -*-
from openerp.osv import fields, osv

class estudiantes(osv.osv):
    _name='prueba.estudiantes'
    _rec_name='nombre'

    _columns={
        'nombre':fields.char('Nombre',size=80,required=True,help='Aqui se coloca el nombre del estudiante'),
        'apellido':fields.char('Apellido',size=80,required=True,help='Aqui se coloca el apellido del estudiante'),
        'cedula':fields.char('Cedula',size=80,required=True,help='Aqui se coloca la cedula del estudiante'),
        'fecha_nacimiento':fields.date('Fecha de Nacimiento'),
        'direccion':fields.char('Direccion'),
        'active':fields.boolean('Active')
    }