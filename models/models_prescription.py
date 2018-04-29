# -*- coding: utf-8 -*-

from odoo import models, fields

class resep_obat(models.Model):
    _name = 'basic_hms.resep_obat'

    nama_pasien = fields.Char('Nama pasien',required=True)
    tgl_resep = fields.Date('Tanggal')
    nama_dokter = fields.Char('Nama pasien',required=True)
    obat = fields.Many2many('basic_hms.detail_resep_obat')
