# -*- coding: utf-8 -*-
from openerp.osv import fields, osv

class re_company(osv.osv):
    _name='res.company'
    _inherit=['res.company']
    
    _columns={
        'rif':fields.char('Rif',size=80,required=True,help='Aqui se coloca el Rif de la uni')
    }