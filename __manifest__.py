# -*- coding: utf-8 -*-
{
    'name': "Construction Project",

    'summary': """
          Construction Management System
           """,

    'description': """
          Construction Management System
          1-Job Order 
          2- Project have multiple task
    """,

    'author': "Dynexcel",
    'website': "http://www.dynexcel.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/construction_materials_boq_view.xml',
        'views/construction_job_order_view.xml',
        'views/construction_vendor.xml',
        'views/construction_configuration_view.xml',
        'views/construction_project_views.xml',
        'views/menu_item.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
