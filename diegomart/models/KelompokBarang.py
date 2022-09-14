from odoo import api, fields, models


class KelompokBarang(models.Model):
    _name = 'diegomart.kelompokbarang'
    _description = 'New Description'

    name = fields.Selection([
        ('bahan makanan', 'Bahan Makanan'),
        ('snack/makanan ringan', 'Snack/Makanan Ringan'),
        ('minuman dingin', 'Minuman Dingin'),
        ('air mineral galon', 'Air Mineral Galon'),
        ('peralatan mandi', 'Peralatan Mandi'),
        
        
    ], string='Nama Kelompok')

    kode_kelompok = fields.Char(string='Kode Kelompok')

    @api.onchange('name')
    def _onchange_kode_kelompok(self):
        if self.name == 'Bahan Makanan':
            self.kode_kelompok = 'BAHAN_MAKANAN'
        elif self.name == 'Snack/Makanan Ringan':
            self.kode_kelompok = 'MAK_RINGAN'
        elif self.name == 'Minuman Dingin':
            self.kode_kelompok = 'MINUMAN_DINGIN'
        elif self.name == 'Air Mineral Galon':
            self.kode_kelompok = 'AIR_GALON'
        elif self.name == 'Peralatan Mandi':
            self.kode_kelompok = 'ALAT_MANDI'

    kode_rak = fields.Char(string='Kode Rak')
    barang_id = fields.One2many(comodel_name='diegomart.barang',
                                inverse_name='kelompokbarang_id',
                                string='Daftar Barang')
    jml_item = fields.Char(compute='_compute_jml_item', string='Jml Item')

    @api.depends('barang_id')
    def _compute_jml_item(self):
        for record in self:
            a = self.env['diegomart.barang'].search([('kelompokbarang_id', '=', record.id)]).mapped('name')
            b = len(a)
            record.jml_item = b
            record.daftar = a
    
    daftar = fields.Char(string='Daftar isi')

