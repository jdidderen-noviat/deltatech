# ©  2015-2019 Deltatech
#              Dorin Hongu <dhongu(@)gmail(.)com
# See README.rst file on addons root folder for license details

{
    "name": "Stock Reports",
    "version": "11.0.2.0.0",
    "author": "Terrabit, Dorin Hongu",
    "website": "https://www.terrabit.ro",
    "category": "Generic Modules",
    "depends": ["base", "stock", "stock_account", "date_range"],
    "license": "AGPL-3",
    "data": [
        "security/ir.model.access.csv",
        "report/stock_picking_report.xml",
        "report/monthly_stock_report_view.xml",
        "report/stock_balance_view.xml",
    ],
    "images": ["images/main_screenshot.png"],
    "installable": True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
