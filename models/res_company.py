# -*- coding: utf-8 -*-
from odoo import api, fields, models, _  # type: ignore


class ResCompany(models.Model):
    _inherit = 'res.company'

    is_report_header = fields.Char("Entête")
   