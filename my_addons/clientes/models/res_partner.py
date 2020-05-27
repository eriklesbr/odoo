# -*- coding: utf-8 -*-
import re

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class ResPartner(models.Model):
    _inherit = ['res.partner']

    tipo_pessoa = fields.Selection(string='Tipo Pessoa', selection=[
                                   ('1', 'Física'), ('2', 'Jurídica')], default='1')
    cpf = fields.Char(string='CPF', size=18, copy=False)
    rg = fields.Char(string='RG')
    rg_orgao = fields.Selection(string='ORG', selection=[('SSP', 'SSP')])
    rg_estado = fields.Selection(string='UF', selection=[('BA', 'BA')])
    rg_emissao = fields.Date(string='Emis.')
    apelido = fields.Char(string="Apelido")
    numero = fields.Char(string="Número")
    bairro = fields.Char(string="Bairro")
    cod_mun_ibge = fields.Char(string="Cod. Mun. IBGE")
    telefone1 = fields.Char(string="Residencial")
    telefone2 = fields.Char(string="Comercial")
    telefone3 = fields.Char(string="Telefone3")
    celular = fields.Char(string="Celular")
    tipotel1 = fields.Selection(selection=[
        ('1', 'Trabalho'),
        ('2', 'Casa'),
        ('3', 'Cobrança'),
        ('4', 'Outros')])
    tipooperadora1 = fields.Selection(selection=[
        ('1', 'Oi'),
        ('2', 'Tim'),
        ('3', 'Claro'),
        ('4', 'Vivo'),
        ('5', 'Embratel'),
        ('6', 'Net'),
        ('7', 'Nbt'),
        ('8', 'Outros')])
    tipotel2 = fields.Selection(selection=[
        ('1', 'Trabalho'),
        ('2', 'Casa'),
        ('3', 'Cobrança'),
        ('4', 'Outros')])
    tipooperadora2 = fields.Selection(selection=[
        ('1', 'Oi'),
        ('2', 'Tim'),
        ('3', 'Claro'),
        ('4', 'Vivo'),
        ('5', 'Embratel'),
        ('6', 'Net'),
        ('7', 'Nbt'),
        ('8', 'Outros')])
    tipotel3 = fields.Selection(selection=[
        ('1', 'Trabalho'),
        ('2', 'Casa'),
        ('3', 'Cobrança'),
        ('4', 'Outros')])
    tipooperadora3 = fields.Selection(selection=[
        ('1', 'Oi'),
        ('2', 'Tim'),
        ('3', 'Claro'),
        ('4', 'Vivo'),
        ('5', 'Embratel'),
        ('6', 'Net'),
        ('7', 'Nbt'),
        ('8', 'Outros')])
    tipotel4 = fields.Selection(selection=[
        ('1', 'Trabalho'),
        ('2', 'Casa'),
        ('3', 'Cobrança'),
        ('4', 'Outros')])
    tipooperadora4 = fields.Selection(selection=[
        ('1', 'Oi'),
        ('2', 'Tim'),
        ('3', 'Claro'),
        ('4', 'Vivo'),
        ('5', 'Embratel'),
        ('6', 'Net'),
        ('7', 'Nbt'),
        ('8', 'Outros')])
    email = fields.Char(string="Email")
    site = fields.Char(string="Site")
    obs1 = fields.Char()
    obs2 = fields.Char()
    obs3 = fields.Char()
    obs4 = fields.Char()
    historico = fields.Text()
    contato_id = fields.One2many(
        comodel_name="res.contact", inverse_name="id", string=" Contatos Autorizados")
    crt = fields.Selection(
        string='CRT', selection=[
            ('1', '1 - Simples Nacional'),
            ('2', '2 - Simples Nacional - Excesso de Receita Bruta'),
            ('3', '3 - Regime Normal')])
    tipo_cliente = fields.Selection(
        string='Tipo Cliente', selection=[
            ('1', '1 - Indústria'),
            ('2', '2 - Distribuidora'),
            ('3', '3 - Distribuidora e Varejo'),
            ('4', '4 - Varejo'),
            ('5', '5 - Produtor Rural'),
            ('6', '6 - Consumidor Final')])
    id_estrangeiro = fields.Char(string='ID Estrangeiro')
    cnae = fields.Char(string='CNAE')
    res1_nome = fields.Char(string='Nome')
    res1_estado_civil = fields.Selection(
        string='Estado Civil', selection=[
            ('1', 'CASADO(A)'),
            ('2', 'SOLTEIRO(A)'),
            ('3', 'VIÚVO(A)'),
            ('4', 'AMASIADO(A)'),
            ('5', 'DESQUITADO(A)')])
    res1_profissao = fields.Char(string='Profissão')
    res1_endereco = fields.Char(string='Endereço')
    res1_bairro = fields.Char(string='Bairro')
    res1_cidade = fields.Char(string='Cidade')
    res1_uf = fields.Selection(
        string='UF', selection=[
            ('BA', 'BA'),
            ('SP', 'SP')])
    res1_cep = fields.Char(string='CEP')
    res1_rg = fields.Char(string='RG')
    res1_cpf = fields.Char(string='CPF')
    res2_nome = fields.Char(string='Nome')
    res2_estado_civil = fields.Selection(
        string='Estado Civil', selection=[
            ('1', 'CASADO(A)'),
            ('2', 'SOLTEIRO(A)'),
            ('3', 'VIÚVO(A)'),
            ('4', 'AMASIADO(A)'),
            ('5', 'DESQUITADO(A)')])
    res2_profissao = fields.Char(string='Profissão')
    res2_endereco = fields.Char(string='Endereço')
    res2_bairro = fields.Char(string='Bairro')
    res2_cidade = fields.Char(string='Cidade')
    res2_uf = fields.Selection(
        string='UF', selection=[
            ('BA', 'BA'),
            ('SP', 'SP')])
    res2_cep = fields.Char(string='CEP')
    res2_rg = fields.Char(string='RG')
    res2_cpf = fields.Char(string='CPF')
    regiao_id = fields.Many2one(
        comodel_name="res.region",
        ondelete='set null',
        string="Região")
    vendedor_id = fields.Char(string='Vendedor')
    nome_pai = fields.Char(string='Nome do Pai')
    nome_mae = fields.Char(string='Nome da Mãe')
    estado_civil = fields.Selection(
        string='Estado Civil', selection=[
            ('1', 'CASADO(A)'),
            ('2', 'SOLTEIRO(A)'),
            ('3', 'VIÚVO(A)'),
            ('4', 'AMASIADO(A)'),
            ('5', 'DESQUITADO(A)')])
    conjuge = fields.Char(string='Cônjuge')
    sexo = fields.Selection(string='Sexo', selection=[('M', 'M'), ('F', 'F'), ('I', 'I')])
    nascimento = fields.Date(string='Nascimento')
    moradia = fields.Boolean(string='Moradia')
    ref1 = fields.Char()
    ref2 = fields.Char()
    ref3 = fields.Char()
    profissao = fields.Char(string='Profissão')
    empresa = fields.Char(string='Empresa')
    aquisitivo_renda = fields.Selection(
        string='Aquisitivo/Renda',
        selection=[
            ('1', 'Até 1 salário mínimo'),
            ('2', 'De 1 até 2 salários mínimos'),
            ('3', 'De 5 até 10 salários mínimos'),
            ('4', 'Acima de 10 salários mínimos')])

    @api.onchange('cpf')
    def _onchange_cpf(self):
        if self.cpf:
            val = re.sub('[^0-9]', '', self.cpf)
            if len(val) == 14 and self.tipo_pessoa == '2':
                cpf = "%s.%s.%s/%s-%s"\
                    % (val[0:2], val[2:5], val[5:8], val[8:12], val[12:14])
                self.cpf = cpf
            elif len(val) == 11 and self.tipo_pessoa == '1':
                cpf = "%s.%s.%s-%s"\
                    % (val[0:3], val[3:6], val[6:9], val[9:11])
                self.cpf = cpf
            else:
                if self.tipo_pessoa == '1':
                    raise UserError('Verifique seu número de CPF!')
                else:
                    raise UserError('Verifique seu número de CNPJ!')
