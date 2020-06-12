# -*- coding: utf-8 -*-
# Copyright 2018 上海尹彬 ((http://www.yinbin.ink).)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'GOODERP Sell To Buy',
    'version': '11.11',
    'author': '上海尹彬',
    'website': 'http://www.yinbin.ink',
    'category': 'gooderp',
    'summary': '以销订购',
    'description': """根据销售订单创建采购订单""",
    'depends': [
        'buy', 'sell'
    ],
    'data': [
        'views/buy_view.xml',
        'wizard/sell_to_buy_wizard_view.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': False,
}
