# -*- coding: utf-8 -*-
from odoo import models, fields, api


class City(models.Model):
    """Cidades com código IBGE"""

    _name = "res.city"
    _description = "res.city"
    _rec_name = "cidade"

    cidade = fields.Char(string='Cidade')
    uf = fields.Char(string='UF')
    estado = fields.Char(string="Estado")
    cod_ibge = fields.Char(string='Código do Município no IBGE')
