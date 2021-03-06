# -*- coding: utf-8 -*-
{
    'name': "Condições de Pagamento",

    'summary': """
        Gerenciar Condições de Pagamento e Parcelas""",

    'description': """
        Módulo para Gerenciar as Condições de Pagamento e Parcelas:
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
        'views/res_condicao_pagamento_parcela.xml',
        'views/res_condicao_pagamento.xml',
        'views/res_tipo_pagamento.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
    'demo': False,
    'application': True,
}