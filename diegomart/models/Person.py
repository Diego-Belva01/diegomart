from odoo import api, fields, models


class Person(models.Model):
    _name = 'diegomart.person'
    _description = 'New Description'

    name = fields.Char(string='Nama')
    alamat = fields.Char(string='Alamat')
    tgl_lahir = fields.Datetime(string='Tanggal Lahir')


class Kasir(models.Model):
    _name = 'diegomart.kasir'
    _inherit = 'diegomart.person'
    _description = 'New Description'

    id_kasir = fields.Char(string='ID Kasir')


class CleaningService(models.Model):
    _name = 'diegomart.cleaningservice'
    _inherit = 'diegomart.person'
    _description = 'New Description'

    id_cln = fields.Char(string='ID Cleaning Service')