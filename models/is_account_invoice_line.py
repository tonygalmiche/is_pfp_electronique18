# -*- coding: utf-8 -*-
from odoo import models,fields,tools   # type: ignore


class is_account_invoice_line(models.Model):
    _name='is.account.invoice.line'
    _description="Lignes des factures"
    _order='id desc'
    _auto = False

    invoice_id      = fields.Many2one('account.move', 'Facture')
    invoice_type               = fields.Selection([
            ('in_invoice' , 'Facture fournisseur'),
            ('in_refund'  , 'Avoir fournisseur'),
            ('out_invoice', 'Facture client'),
            ('out_refund' , 'Avoir client'),

        ], u"Type", readonly=True, index=True)
    number          = fields.Char('N°Facture')
    invoice_date    = fields.Date("Date facture")
    state           = fields.Char('Etat')
    partner_id      = fields.Many2one('res.partner', 'Client/Fournisseur')
    departement     = fields.Char('Département')
    pays            = fields.Char('Pays')
    type_entreprise = fields.Char("Type d'entreprise")
    secteur         = fields.Char('Secteur')
    source          = fields.Char('Source')
    description     = fields.Char('Description')
    product_id      = fields.Many2one('product.template', 'Article')
    type_article    = fields.Char("Type d'article")
    quantity        = fields.Float('Quantité')
    price_unit      = fields.Float('Prix unitaire')
    montant         = fields.Float('Montant HT')


    def init(self):
        cr=self._cr
        tools.drop_view_if_exists(cr, 'is_account_invoice_line')
        cr.execute("""
            CREATE OR REPLACE view is_account_invoice_line AS (
                select
                    ail.id,
                    ai.id invoice_id,
                    ai.move_type invoice_type,
                    ai.name number,
                    ai.invoice_date,
                    ai.state,
                    rp.id partner_id,
                    substr(rp.zip,1,2) departement,
                    rc.name pays,
                    ite.name type_entreprise,
                    sec.name secteur,
                    sou.name source,
                    ail.name description,
                    pt.id product_id,
                    ita.name type_article,
                    ail.quantity,
                    ail.price_unit,
                    (ail.quantity*ail.price_unit) montant
                from account_move ai inner join res_partner              rp on ai.partner_id=rp.id
                                        left outer join res_country         rc on rp.country_id=rc.id
                                        left outer join is_type_entreprise ite on rp.is_type_entreprise_id=ite.id
                                        left outer join is_secteur         sec on rp.is_secteur_id=sec.id
                                        left outer join is_source          sou on rp.is_source_id=sou.id
                                        inner join account_move_line    ail on ail.move_id=ai.id
                                        inner join product_product          pp on ail.product_id=pp.id
                                        inner join product_template         pt on pp.product_tmpl_id=pt.id
                                        left outer join is_type_article    ita on pt.is_type_article_id=ita.id
            )
        """)

