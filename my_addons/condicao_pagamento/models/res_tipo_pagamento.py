# -*- coding: utf-8 -*-

from odoo import models, fields, api


class TipoPagamento(models.Model):
    """Model tipo de pagamento."""

    _name = 'res.tipo_pagamento'
    _description = 'res.tipo_pagamento'
    _order = 'ordem asc'
    _rec_name = 'forma'

    forma = fields.Char(string='Forma de Pagamento')
    ordem = fields.Integer(string='Ordem')
