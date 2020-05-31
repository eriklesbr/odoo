# -*- coding: utf-8 -*-
{
    'name': "Bancos/Cartões/Financeiras",

    'summary': """
        CRUD Bancos/Cartões/Financeiras""",

    'description': """
        Módulo para gerenciar Bancos/Cartões/Financeiras:
            Cadastrar.
            Listar.
            Editar.
            Excluir.
    """,

    'author': "Sismais",
    'website': "https://www.maxproerp.com.br",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Cadastros',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/res_bancos.xml',
        'views/res_cartoes_parcela.xml',
        'views/templates.xml',
    ],
    'demo': False,
    'application': True,
}
