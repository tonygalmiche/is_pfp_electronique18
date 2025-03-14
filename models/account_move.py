# -*- coding: utf-8 -*-
from odoo import models,fields, api  # type: ignore

class account_move(models.Model):
    _inherit = 'account.move'
    _order   = 'id desc'
  
    is_description   = fields.Char('Description')
    is_sale_order_id = fields.Many2one('sale.order', 'Commande', store=False, readonly=True, compute='_compute_is_sale_order_id')

    @api.depends('state','invoice_line_ids')
    def _compute_is_sale_order_id(self):
        for obj in self:
            order_id = False
            for line in obj.invoice_line_ids:
                for sale_line in line.sale_line_ids:
                    order_id = sale_line.order_id.id
            obj.is_sale_order_id=order_id


class account_move_line(models.Model):
    _inherit = 'account.move.line'
  
    def _get_journal_items_full_name(self, name, display_name):
        return name 
        #return name if not display_name or display_name in name else f"{display_name} {name}"

