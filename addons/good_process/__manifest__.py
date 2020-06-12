# -*- coding: utf-8 -*-
{
    "name": "good_process",
    "version": '11.11',
    "author": '尹彬',
    "website": "http://www.yinbin.ink",
    "category": "gooderp",
    "description": """
    可配置的审批流程
    """,
    "data": [
        'data/data.xml',
        'views/good_process.xml',
        'security/ir.model.access.csv',
    ],
    "depends": [
        'core',
    ],
    'qweb': [
        'static/src/xml/approver.xml',
    ],
}
