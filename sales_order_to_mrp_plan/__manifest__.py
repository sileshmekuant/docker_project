{
    "name": "Sales Order To MRP Plan",
    "version":'1.0',
    "author":"Yeab A. (Yoraki)",
    "website":"www.yoraki.com",
    'depends': ['base', 'stock','sale_management','hr','mrp'],
    "data":[
        'security/ir.model.access.csv',
        "security/group.xml",
        'data/sequence.xml',
        "views/mrp_plan.xml",
        'views/product_category.xml',

        "views/sale_order.xml",
        "views/menu.xml",
        "wizard/create_mo.xml",

        'report/mrp_planing_report_templates.xml',
       'report/mrp_planing_report.xml',

    ],
    "application":True,
    "installable":True

}