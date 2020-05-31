# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CondicaoPagamentoParcela(models.Model):
    _name = 'res.condicao_pagamento_parcela'
    _description = 'res.condicao_pagamento_parcela'

    numero = fields.Integer(string='Número')
    qtde_dias = fields.Integer(string='Qtde Dias')
    percentual = fields.Float(string='Percentual')
    condicao_pagamento_id = fields.Many2one(comodel_name='res.condicao_pagamento', string='Condição Pagamento', ondelete="cascade")
