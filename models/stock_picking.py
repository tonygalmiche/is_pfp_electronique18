# -*- coding: utf-8 -*-
from odoo import api, fields, models            # type: ignore


class StockPicking(models.Model):
    _inherit = "stock.picking"

    is_info_complementaire = fields.Text("Conditions de livraison")


    def recopier_description_commande_action(self):
        for obj in self:
            print(obj)
            for move in obj.move_ids:
                if move.sale_line_id:
                    move.description_picking = move.sale_line_id.name