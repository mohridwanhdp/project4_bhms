# -*- coding: utf-8 -*-

from odoo import models, fields

class obat(models.Model):
    _name = 'basic_hms.obat'

    nama_obat = fields.Char('Nama Obat', required=True)
    jenis_obat = fields.Selection([
            ('obat','Obat'),
            ('alkes','Alat Kesehatan'),
            ('pkrt','PKRT')
        ], default='obat')
    stok = fields.Integer('Stok')
    satuan = fields.Selection([
            ('strip','Strip'),
            ('kaplet','Kaplet'),
            ('botol','Botol')
        ], default = 'strip')
