# -*- coding: utf-8 -*-
{
    'name': "Azbo Overall",

    'summary': """
        Azbo Overall""",

    'description': """
        Azbo Overall
    """,

    'author': "Musadiq Fiaz Chaudhary",
    'website': "http://www.viltco.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'all',
    'version': '14.0.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mrp', 'sale', 'account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'security/security.xml',
        'views/account_asset_views.xml',
        'views/res_config_setting_view.xml',
        'views/views.xml',
    ],
}
