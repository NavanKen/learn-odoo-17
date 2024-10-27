from odoo import models, fields, api

class EstateProperty(models.Model):
    _name = "siswa_property"
    _description = "Siswa Property"
    _order = "tanggal_lahir desc"

    name = fields.Char(string="Nama Siswa", required=True)
    alamat = fields.Char(string="Alamat", required=True)  # Pastikan ini adalah field yang benar
    nis = fields.Integer(string="NIS Siswa", required=True)
    tanggal_lahir = fields.Date(string="Tanggal Lahir", required=True)  
    age = fields.Integer(string="Umur", required=True)
    asal_sekolah = fields.Char(string="Asal Sekolah", required=True)
    gender = fields.Selection([
        ('male', 'Laki-laki'),
        ('female', 'Perempuan'),
    ], string="Jenis Kelamin", required=True)

    tahun_lahir = fields.Integer(string="Tahun Lahir", compute="_compute_tahun_lahir", store=True)

    @api.depends('tanggal_lahir')
    def _compute_tahun_lahir(self):
        for record in self:
            if record.tanggal_lahir:
                record.tahun_lahir = record.tanggal_lahir.year
            else:
                record.tahun_lahir = 0
