from crypt import methods
import json


import json

from odoo import http, models, fields
from odoo.http import request


class diegomart(http.Controller):
    @http.route('/diegomart/getbarang', auth='public', method=['GET'])
    def getBarang(self, **kw):
        # Mengambil semua barang dari table barang
        barang = request.env['diegomart.barang'].search([])
        items = []

        for item in barang:
            items.append({
                'nama_barang': item.name,
                'harga_jual': item.harga_jual,
                'stok': item.stok
            })
        
        return json.dumps(items)

    @http.route('/diegomart/getsupplier', auth='public', method=['GET'])
    def getSupplier(self, **kw):
        supplier = request.env['diegomart.supplier'].search([])
        items = []

        for item in supplier:
            items.append({
                'nama_perusahaan': item.name,
                'alamat': item.alamat,
                'no_telepon': item.no_telp,
                'barang_id': item.barang_id[0].name
            })
        
        return json.dumps(items)