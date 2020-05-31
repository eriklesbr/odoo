# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResBancos(models.Model):
    """Model Bancos."""

    _name = 'res.bancos'
    _description = 'res.bancos'
    _rec_name = 'nome'

    numero = fields.Char(string='Número/Código')
    nome = fields.Char(string='Nome')
    financeira = fields.Boolean(string='Financeira')
    administradora = fields.Boolean(string='Administradora/Operadora de cartões')
    hab_debito = fields.Boolean(string='Habilitar venda no cartão de débito')
    hab_credito = fields.Boolean(string='Habilitar venda no cartão de crédito')
    comissao_debito = fields.Float(string='Comissão débito)')
    comissao_credito = fields.Float(string='Comissão crédito')
    int_dias_deb = fields.Integer(string='Intervalo de dias débito')
    int_dias_cre = fields.Integer(string='Intervalo de dias crédito')
    taxa_deb = fields.Float(string='Taxa débito')
    taxa_cre = fields.Float(string='Taxa crédito')
    qtde_parcelas = fields.Integer(string='Qtde.')
    parcelas_id = fields.One2many(comodel_name='res.cartao_parcela', inverse_name='banco_id', string='Parcelas')

    def gerar_parcelas(self):

        # Gera parcelas de acordo o número e intervalo de dias.
        # Exclui as parcelas antigas
        self.parcelas_id.unlink()
        # Gera novas parcelas
        for n_parcela in range(1, (self.qtde_parcelas + 1)):
            self.env['res.cartao_parcela'].create(
                {
                    'banco_id': self.id,
                    'qtde_parcela': str(n_parcela) + 'x',
                    'comissao': self.comissao_credito,
                    'tipo_ressarcimento': '1',
                    'dias_ressarcimento': self.int_dias_cre
                })
