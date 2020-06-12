# -*- coding: utf-8 -*-
# Copyright 2018 上海尹彬 ((http://www.yinbin.ink).)

{
    'name': 'GOODERP 招聘',
    'version': '11.11',
    'author': '上海尹彬',
    'website': 'http://www.yinbin.ink',
    'category': 'gooderp',
    'summary': '员工招聘，工作申请，求职',
    'description': """管理招聘流程""",
    'depends': [
        'staff', 'calendar',
    ],
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/hire_data.xml',
        'views/hire_view.xml',
        'views/staff_job_view.xml',
        'report/hire_report_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'tests/demo.xml',
    ],
    'installable': True,
    'application': False,
}
