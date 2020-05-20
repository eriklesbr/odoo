# -*- coding: utf-8 -*-

from odoo import models, fields, api


class cliente(models.Model):
    #_name = 'cliente.cliente'
    #_description = 'cliente.cliente'
    _inherit = 'res.partner'

    tipo = fields.Selection(string='Tipo Pessoa', selection=[('1', 'Física'), ('2', 'Jurídica')], default='1')
    cpf = fields.Char(string='CPF')
    rg = fields.Char(string='RG')
    rg_orgao = fields.Selection(string='ORG', selection=[('SSP', 'SSP')])
    rg_estado = fields.Selection(string='UF', selection=[('BA', 'BA')])
    rg_emissao = fields.Date(string='Emis.')
    nickname = fields.Char(string="Apelido")
    numero = fields.Char(string="Número")
    complemento = fields.Char(string="Complemento")
    bairro = fields.Char(string="Bairro")
    cod_mun_ibge = fields.Char(string="Cod. Mun. IBGE")

    telefone1 = fields.Char(string="Residencial")
    telefone2 = fields.Char(string="Comercial")
    tipotel1 = fields.Selection(selection=[('Casa', 'Casa'), ('Cobrança', 'Cobrança'),])
    tipooperadora1 = fields.Selection(selection=[('Tim', 'Tim'), ('Claro', 'Claro'),])

    email = fields.Char(string="Email")
    site = fields.Char(string="Site")
    
    

