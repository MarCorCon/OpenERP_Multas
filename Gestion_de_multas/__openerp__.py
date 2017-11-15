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
{
    "name": "Gestion de multas",
    "version": "1.0",
    "depends": ["base"],
    "author": "Daniel, Emiel, Marco",
    "category": "category",
    "description": """
    This module provide : gestion de multas
    """,
    "init_xml": [],
    'update_xml': ['reclamacion_view.xml', 'multa_view.xml', 'abogado_view.xml','cliente_view.xml','nomiembro_view.xml','miembro_view.xml','factura_view.xml','facturaCuotaAnual_view.xml','facturaPorServicio_view.xml','workflow/reclamacion_workflow.xml','miembro_view.xml','factura_view.xml','facturaCuotaAnual_view.xml','facturaPorServicio_view.xml','workflow/factura_por_servicio_workflow.xml','workflow/factura_cuota_anual_workflow.xml'],
    'demo_xml': ['datos_prueba.xml','datos_prueba2.xml','datos_prueba3.xml'],
    'installable': True,
    'active': False,
#    'certificate': 'certificate',
}