# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ResRegion(models.Model):

    _name = "res.region"
    _description = "res.region"
    _rec_name = "nome"

    nome = fields.Char(string='Região')
