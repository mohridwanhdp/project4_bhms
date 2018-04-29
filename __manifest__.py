# -*- coding: utf-8 -*-
{
    'name': "Basic Hospital Management System",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': 'Module for organizing basic procceess of hospital',

    'author': "B1",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/basic_hms_obat.xml',
        'views/basic_hms_resep_obat.xml',
    ],

	'application': True,
}
