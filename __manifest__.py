# -*- coding: utf-8 -*-

#TODO : 
#- Rapport PDF
#- Mettre sur Gihub et sur VPS
#- https sur VPS (Domaine à créer)
#- Importer les données (clients)
#- Créer les utilisateurs
#- Configurer l'envoi de mails depuis le serveur
#- Sauvegardes du serveur


{
    'name'     : 'InfoSaône - Module Odoo 18 pour PFP Electronique',
    'version'  : '0.1',
    'author'   : 'InfoSaône',
    'category' : 'InfoSaône',


    'description': """
InfoSaône - Module Odoo 18 pour PFP Electronique
===================================================
""",
    'maintainer' : 'InfoSaône',
    'website'    : 'http://www.infosaone.com',
    'depends'    : [
        'base',
        'stock',
        'sale_management',
        'mail',
        'account',
        'purchase',
],
    'data' : [
        'security/ir.model.access.csv',
        'views/partner_view.xml',
        'views/product_view.xml',
        'views/is_account_invoice_line.xml',
        'views/sale_view.xml',
        'views/account_invoice_view.xml',
        # 'report/layouts.xml',
        # 'report/report_invoice.xml',
        # 'report/sale_report_templates.xml',
        'views/menu.xml',
    ],
    'license': 'AGPL-3',
    'installable': True,
    'application': True,
}

