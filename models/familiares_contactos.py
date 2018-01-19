# -*- coding: utf-8 -*-
from openerp.osv import fields, osv

class familiares_contactos(osv.osv):
    _name='prueba.familiares_contactos'
    _rec_name='nombre'

    _columns={
        'nombre':fields.char('Nombre',size=80,required=True,help='Aqui se coloca el nombre del estudiante'),
        'apellido':fields.char('Apellido',size=80,required=True,help='Aqui se coloca el apellido del estudiante'),
        'cedula':fields.char('Cedula',size=80,required=True,help='Aqui se coloca la cedula del estudiante'),
        'active':fields.boolean('Active'),
        'estado_id': fields.many2one('prueba.estados','Nombre del Estado', ondelete="restrict"),
        'municipio_id': fields.many2one('prueba.municipios','Nombre del Municipio', ondelete="restrict"),
        'parroquia_id': fields.many2one('prueba.parroquias','Nombre de la Parroquia', ondelete="restrict"),
        'sector': fields.char('Sector',size=100),
        'calle': fields.char('Calle/Avenida',size=100),
        'estudiante_id': fields.many2one('prueba.estudiantes','Estudiante'),
        
    }

    def pulsar_estado(self,cr,ids,context=None):
        return {'value':{'municipio_id':'', 'parroquia_id':''}}