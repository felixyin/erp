# -*- coding: utf-8 -*-
{
    'name': "NanguERP Sell Quotation模块",
    'author': "尹彬",
    'website': "http://www.yinbin.ink",
    'category': 'gooderp',
    'summary': 'NanguERP报价单',
    "description":
    '''
                        该模块实现了 NanguERP 给客户报价的功能。
    ''',
    'version': '11.11',
    'application': True,
    'depends': ['sell','good_crm'],
    'data': [
        'security/ir.model.access.csv',
        'views/sell_quotation_view.xml',
        'data/sell_quotation_data.xml',
        'report/report_data.xml',
    ],
    'demo': [
        'data/demo.xml',
    ]
}
