# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Contact(models.Model):
    """Contatos autorizados de clientes"""

    _name = "res.contact"
    _description = "res.contact"

    nome = fields.Char(string='Nome')
    parentesco = fields.Selection(
        string='Parentesco/Função',
        selection=[('', ''), ('', ''), ])
    email = fields.Char(string='E-mail')
    celular = fields.Char(string='Celular')
    telefone1 = fields.Char(string='Telefone 1')
    telefone2 = fields.Char(string='Telefone 2')
    autorizado_comprar = fields.Boolean(string='Autorizado a comprar')
    observacao = fields.Char(string='Observação sobre o contato')
    cliente_id = fields.Many2one(
        comodel_name="res.partner",
        ondelete='cascade',
        required=True,
        string="Cliente")
