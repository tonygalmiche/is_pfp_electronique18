# -*- coding: utf-8 -*-
from odoo import api, fields, models              # type: ignore


class IsTypeArticle(models.Model):
    _name='is.type.article'
    _description = "Type article"
    _order='name'
    name = fields.Char("Type d'article", required=True)

class IsFamille(models.Model):
    _name='is.famille'
    _description = "Famille"
    _order='name'
    name = fields.Char("Famille", required=True)

class IsSousFamille1(models.Model):
    _name='is.sous.famille1'
    _description = "Sous-famille"
    _order='name'
    name = fields.Char("Sous-famille 1", required=True)

class IsSousFamille2(models.Model):
    _name='is.sous.famille2'
    _description = "Sous-famille 2"
    _order='name'
    name = fields.Char("Sous-famille 2", required=True)

class IsEmplacementStock(models.Model):
    _name='is.emplacement.stock'
    _description = "Emplacement de stock"
    _order='name'
    name = fields.Char("Emplacement de stock", required=True)


class ProductTemplate(models.Model):
    _inherit = "product.template"

    _sql_constraints = [('is_default_code_uniq','UNIQUE(default_code)', 'Ce code existe déjà')]


    @api.depends('is_stock_mini', 'qty_available')
    def _is_qt_cde(self):
        for obj in self:
            qt=obj.is_stock_mini-obj.qty_available
            if qt<0:
                qt=0
            obj.is_qt_cde=-qt


    is_lien_documentation   = fields.Char('Lien documentation')
    is_stock_mini           = fields.Integer('Stock mini')
    is_lot_reappro          = fields.Integer('Lot de réappro')
    is_type_article_id      = fields.Many2one('is.type.article', "Type d'article")
    is_famille_id           = fields.Many2one('is.famille', 'Famille')
    is_sous_famille1_id     = fields.Many2one('is.sous.famille1', 'Sous-famille 1')
    is_sous_famille2_id     = fields.Many2one('is.sous.famille2', 'Sous-famille 2')
    is_emplacement_stock_id = fields.Many2one('is.emplacement.stock', 'Emplacement de stock')
    is_qt_cde               = fields.Float('Signal de commande', compute=_is_qt_cde, store=False, digits='Product Unit of Measure')
    is_note                 = fields.Text('Note')


class ProductSupplierinfo(models.Model):
    _inherit = "product.supplierinfo"

    is_fabriquant     = fields.Char('Fabricant')
    is_ref_fabriquant = fields.Char('Référence fabricant')





