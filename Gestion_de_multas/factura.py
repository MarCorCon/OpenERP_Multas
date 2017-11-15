
# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (http://tiny.be). All Rights Reserved
#    
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################
from osv import osv
from osv import fields

class factura(osv.osv):
    _name = 'factura'
    _description = 'esta es una factura'
 
    _columns = {
            'name': fields.char('Identificador', size=30, required=True, readonly=False),
            'fecha': fields.datetime('Fecha', required=True, autodate=True),
            'importe':fields.float('Importe', required=True),
            'state': fields.selection([
            ('no', 'No pagada'),
            ('si', 'Pagada'),
            ], '¿Factura pagada?'),
        }
    _sql_constraints = [('id_factura_uniq','unique(name)', 'ID factura ya utilizado.')]
    _defaults = {  
        'state': 'no',  
        }    
factura()