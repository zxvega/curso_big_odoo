# -*- coding: utf-8 -*-
{
    'name': "Inmobiliario",
    'summary': 'Modulo de Capacitacion para Desarrollo Odoo',
    'description': 'Modulo de Capacitacion para Desarrollo Odoo',
    'author': "Giovanni Vega",
    'license': 'Other proprietary',
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'version': '0.1',
    # any module necessary for this one to work correctly
    'depends': ['base'],
    "data":[
        "securitic/res.groups.xml",
        "securitic/ir.model.access.xml",
        "demo/inmuebles.xml",
        "data/sg_tipo_inmueble.xml",
        "views/sg_inmueble.xml",
    ]
    
}