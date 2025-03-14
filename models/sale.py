# -*- coding: utf-8 -*-
from odoo import api, fields, models            # type: ignore


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    @api.depends('product_id', 'linked_line_id', 'linked_line_ids')
    def _compute_name(self):
        for line in self:
            if line.product_id:
                if line.product_id.is_description_devis:
                    name=line.product_id.is_description_devis
                else:
                    name=line.product_id.name
                line.name = name
                    

