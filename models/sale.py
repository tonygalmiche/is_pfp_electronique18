# -*- coding: utf-8 -*-
from odoo import api, fields, models            # type: ignore


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"


    # @api.multi
    # @api.onchange('product_id')
    # def product_id_change(self):
    #     if not self.product_id:
    #         return {'domain': {'product_uom': []}}

    #     vals = {}
    #     domain = {'product_uom': [('category_id', '=', self.product_id.uom_id.category_id.id)]}
    #     if not self.product_uom or (self.product_id.uom_id.id != self.product_uom.id):
    #         vals['product_uom'] = self.product_id.uom_id
    #         vals['product_uom_qty'] = 1.0

    #     product = self.product_id.with_context(
    #         lang=self.order_id.partner_id.lang,
    #         partner=self.order_id.partner_id.id,
    #         quantity=vals.get('product_uom_qty') or self.product_uom_qty,
    #         date=self.order_id.date_order,
    #         pricelist=self.order_id.pricelist_id.id,
    #         uom=self.product_uom.id
    #     )

    #     result = {'domain': domain}

    #     title = False
    #     message = False
    #     warning = {}
    #     if product.sale_line_warn != 'no-message':
    #         title = _("Warning for %s") % product.name
    #         message = product.sale_line_warn_msg
    #         warning['title'] = title
    #         warning['message'] = message
    #         result = {'warning': warning}
    #         if product.sale_line_warn == 'block':
    #             self.product_id = False
    #             return result

    #     #TODO : Partie modifiée pour ne mettre que la note de la fiche article
    #     name = product.name_get()[0][1]
    #     if product.description_sale:
    #         name=product.description_sale
    #     vals['name'] = name

    #     self._compute_tax_id()

    #     if self.order_id.pricelist_id and self.order_id.partner_id:
    #         vals['price_unit'] = self.env['account.tax']._fix_tax_included_price_company(self._get_display_price(product), product.taxes_id, self.tax_id, self.company_id)
    #     self.update(vals)

    #     return result


