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
        'active':fields.boolean('Active'),
        'estado_id': fields.many2one('prueba.estados','Nombre del Estado'),
        'municipio_id': fields.many2one('prueba.municipios','Nombre del Municipio'),
        'parroquia_id': fields.many2one('prueba.parroquias','Nombre de la Parroquia'),
        'sector': fields.char('Sector',size=100),
        'calle': fields.char('Calle/Avenida',size=100),
        'deportes_ids': fields.many2many(
            'prueba.deportes',
            'prueba_estudiantes_deportes_rel',
            'estudiante_id',
            'deporte_id',
            'Deportes',
        ),
        'familiar_contacto_ids': fields.one2many(
            'prueba.familiares_contactos',
            'estudiante_id',
            'Familiar de Contacto'
        ),
        
    }

    def pulsar_estado(self,cr,ids,context=None):
        return {'value':{'municipio_id':'', 'parroquia_id':''}}