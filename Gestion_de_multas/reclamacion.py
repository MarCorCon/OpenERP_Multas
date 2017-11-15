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
from addons.Gestion_de_multas.facturaporservicio import facturaPorServicio
from datetime import date, datetime

class reclamacion(osv.osv):
    _name = 'reclamacion'
    _description = 'reclamacion de una o mas multas'
    
    def en_proceso(self, cr, uid, ids):
        hoy = datetime.today()
        self.write(cr, uid, ids,{'state':'en_proceso'})
        self.write(cr, uid, ids, {'fecha_apertura': hoy})
        
        return True
    def cerrada(self, cr, uid, ids):
        hoy = datetime.today()
        self.write(cr, uid, ids,{'state':'cerrada'})
        self.write(cr, uid, ids, {'fecha_cierre': hoy})
        
        return True
        
    def check_en_proceso(self, cr, uid, ids):
        data = (self.read(cr,uid,ids, ['cliente_id','abogado_ids','multa_ids'])[0])
        if data['cliente_id']!= False and data['abogado_ids']!= [] and data['multa_ids'] != []:
            return True
        else:
            raise osv.except_osv(('Error'), ('Para iniciar la reclamacion tiene que asignar al menos un abogado, un cliente y una multa'))
            return False
        
    _columns = {
        'name': fields.char('ID gestion', size=30, required=True),
        'state': fields.selection([
            ('borrador', 'borrador'),
            ('en_proceso', 'En proceso'),
            ('cerrada', 'Cerrada'),
            ('cancelada', 'Cancelada'),
            ], 'Estado de la reclamacion'),
        'fecha_apertura': fields.datetime('Fecha de inicio'),
        'fecha_cierre': fields.datetime('Fecha de fin'),
        'descripcion': fields.text('descripcion'),
        'abogado_ids': fields.many2many('abogado','abogado_reclamacion_rel','reclamacion_id','abogado_id', 'Abogados asignados'),
        'multa_ids': fields.one2many('multa','reclamacion_id','Multas'),
        'cliente_id':fields.many2one('cliente','Cliente'),
        'facturaporservicio_id':fields.many2one('facturaporservicio','Factura'),
    }
    _sql_constraints = [('id_reclamacion_uniq','unique(name)', 'ID reclamacion ya utilizado.')]
    _defaults = {  
        'state': 'borrador',  
        }
reclamacion()

    
#'contador': fields.function(_dameUno, type='integer', string='Ocupacion total',store = True),