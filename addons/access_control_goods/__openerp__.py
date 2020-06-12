# -*- coding: utf-8 -*-
{
    'name': "NanguERP Access Control Goods 模块",
    'author': "尹彬",
    'website': "http://www.yinbin.ink",
    'category': 'gooderp',
    'summary': 'NanguERP 商品 读写建删权限控制',
    "description":
    '''
该模块添加了 创建商品组，该组成员可以对商品进行增删改查，普通用户只能查看。
    ''',
    'version': '11.11',
    'application': True,
    'depends': ['core'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
    ],
}
