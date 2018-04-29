# -*- coding: utf-8 -*-

from odoo import models, fields

class detail_resep_obat(models.Model):
    _name = 'basic_hms.detail_resep_obat'

    nama_obat = fields.Many2one('basic_hms.obat')
    dosis = fields.Char('Dosis')
    aturan_obat = fields.Selection([
        ('setelah', 'Setelah Makan'),
        ('sebelum', 'Sebelum Makan')
    ], default='sebelum')
    keterangan = fields.Char('Keterangan')