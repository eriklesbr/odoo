# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class CondicaoPagamento(models.Model):
    _name = 'res.condicao_pagamento'
    _description = 'res.condicao_pagamento'
    _rec_name = 'descricao'

    ativo = fields.Boolean(string='Ativo')
    descricao = fields.Char(string='Descrição', required=True)
    acrescimo = fields.Float(string='Acréscimo %')
    entrada_rec = fields.Float(string='Recomendada %')
    entrada_min = fields.Float(string='Mínima %')
    qtde_parcelas = fields.Integer(string='Quantidade de Parcelas (dias)')
    int_dias = fields.Integer(string='Intervalo de dias', default=30)
    parcelas_id = fields.One2many(comodel_name='res.condicao_pagamento_parcela',
                                  inverse_name='condicao_pagamento_id', string='Parcelas')

    def gerar_parcelas(self):
        # Gera parcelas de acordo o número e intervalo de dias.

        if self.qtde_parcelas <= 0:
            raise UserError('Informe o número de parcelas!')
        # Exclui as parcelas antigas
        self.parcelas_id.unlink()
        # Gera novas parcelas
        i_dias = 0
        p_percentual = 100 / self.qtde_parcelas
        for n_parcela in range(1, (self.qtde_parcelas + 1)):
            i_dias = i_dias + self.int_dias
            self.env['res.condicao_pagamento_parcela'].create(
                {'condicao_pagamento_id': self.id, 'numero': n_parcela, 'qtde_dias': i_dias, 'percentual': p_percentual})
