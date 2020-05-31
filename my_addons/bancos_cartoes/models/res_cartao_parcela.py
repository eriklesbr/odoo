# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResCartaoParcela(models.Model):
    """Model Cartao Parcela."""

    _name = 'res.cartao_parcela'
    _description = 'res.cartao_parcela'
    _rec_name = 'qtde_parcela'

    qtde_parcela = fields.Char(string='Qtde. Parcelas')
    comissao = fields.Float(string='Comissão/Juros (%)')
    tipo_ressarcimento = fields.Selection(string='Tipo de Ressarcimento', selection=[
                                          ('1', '1 - De acordo a parcela'), ('2', '2 - Tudo de uma vez'), ])
    dias_ressarcimento = fields.Integer(
        string='Dias/Intervalo p/ Ressarcimento')
    banco_id = fields.Many2one(comodel_name='res.bancos', string='Banco', ondelete="cascade")
