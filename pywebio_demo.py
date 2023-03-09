# -*- coding: utf-8 -*-
# @Time    : 2023/3/9 11:06
# @Author  : ZhuGaochao
# @File    : pywebio_demo.py
# @Software: PyCharm
from pywebio.input import input, FLOAT, checkbox
from pywebio.output import put_text, put_scope, put_markdown, put_image
from pywebio.pin import put_checkbox
from pywebio import start_server


def index():
    put_markdown(r""" ## Apsara Clouder云计算专项技能认证：云服务器ECS入门 (试题&答案) """)
    put_markdown(r""" ### 考试入口：https://edu.aliyun.com/certification/cldc15 """)
    put_markdown(r""" ##### NOTE： """)
    put_markdown(r""" > *建议开两个web界面，Ctrl+F 检索查阅* """)
    put_markdown(r""" > *需要登录且没账号的，直接支付宝扫码登录就行，0元支付购买，然后考试* """)
    # put_markdown(r""" *** """)

    put_markdown(r""" # 一、单选题 """)

    # 非正确选项不让勾选
    # options = [{'label': 'A.5*8',
    #            'value': ["A.5*8"],
    #            'selected': False,
    #            'disabled': True},
    #            {'label': 'B.7*8',
    #             'value': ["B.5*8"],
    #             'selected': False,
    #             'disabled': True},
    #            {'label': 'C.7*12',
    #             'value': ["C.5*8"],
    #             'selected': False,
    #             'disabled': True},
    #            {'label': 'D.7*24',
    #             'value': ["D.7*24"],
    #             'selected': True,
    #             'disabled': False},
    #            ]
    # put_checkbox(label='1.云服务器ECS以服务化的方式对客户提供，阿里云产品售后支持的时间段是?', options=options, name='sss')

    put_checkbox(label='1.云服务器ECS以服务化的方式对客户提供，阿里云产品售后支持的时间段是?',
                 options=["A.5*8", "B.7*8", "C.7*12", "D.7*24"],
                 value=["D.7*24"], name='name1')

    put_checkbox(label='2.云服务器ECS的计费方式不含以下哪项?',
                 options=["A.包年包月", "B.按量计费", "C.抢占式实例", "D.网商贷"],
                 value=["D.网商贷"], name='name2')

    put_checkbox(label='3.云服务器ECS产品丰富，以下哪个不是云服务器ECS实例类型？',
                 options=["A.通用计算", "B.异构计算", "C.高性能计算", "D.边缘计算"],
                 value=["D.边缘计算"], name='name3')

    put_checkbox(label='4.云服务器ECS属于云计算SaaS、PaaS、laaS哪一层级的服务？',
                 options=["A. Saas", "B. Paas", "C. laas", "D. Daas"],
                 value=["C. laas"], name='name4')

    put_checkbox(label='5.用户可以在阿里云官网的哪一个页面找到云服务器ECS购买入口?',
                 options=["A.云原生产品白皮书", "B.数据库产品详情页", "C.云服务器ECS产品详情页", "D.阿里云开发者社区"],
                 value=["C.云服务器ECS产品详情页"], name='name5')

    put_checkbox(label='6.阿里云官网(http://aliyun.com)上的内容非常丰富,以下哪一项不是阿里云官网的功能?',
                 options=["A.注册阿里云账号", "B.阿里云平台对外运营的统一平台", "C.存储用户的数据文件",
                          "D.查询阿里云产品目录与功能介绍"],
                 value=["C.存储用户的数据文件"], name='name6')

    put_checkbox(label='7.小明听说在阿里云官网创建一台ECS实例非常方便，他开通ECS所必须的步骤不包括以下哪一项?',
                 options=["A.注册http://aliyun.com的账号", "B.实名认证", "C.备案网站域名",
                          "D.指定操作系统镜像"],
                 value=["C.备案网站域名"], name='name7')

    put_checkbox(label='8.完成云服务器ECS创建以后的第一个步骤是什么？',
                 options=["A.远程连接ECS", "B.重置ECS密码", "C.配置安全组",
                          "D.变更ECS配置"],
                 value=["B.重置ECS密码"], name='name8')

    put_checkbox(label='9.下列哪一个不是重置ECS密码的步骤?',
                 options=["A.查看实例详情", "B.进入控制台", "C.远程连接ECS",
                          "D.点击控制台“概览”"],
                 value=["C.远程连接ECS"], name='name9')

    put_checkbox(label='10.云服务器ECS提供了哪两大主流计算架构？',
                 options=["A.xen和kvm", "B.linux 和windows", "C.X86和ARM",
                          "D.虚拟机和docker"],
                 value=["C.X86和ARM"], name='name10')

    put_checkbox(label='11.开放云服务器ECS安全组里22端口，有什么作用？',
                 options=["A.可以远程访问数据库", "B.支持http访问", "C.支持https访问",
                          "D.支持ssh访问"],
                 value=["D.支持ssh访问"], name='name11')

    put_checkbox(label='12.云服务器ECS的快照功能不具备以下哪个作用?',
                 options=["A.数据备份", "B.数据恢复", "C.制作自定义镜像",
                          "D.更换系统"],
                 value=["D.更换系统"], name='name12')

    put_checkbox(label='13.使用阿里云云监控可以实时监控阿里云ECS的运行情况，其优势不包括哪一项?',
                 options=["A.免费", "B.易用", "C.支持多种报警方式",
                          "D.防DDOS攻击"],
                 value=["D.防DDOS攻击"], name='name13')

    put_checkbox(label='14.以下哪项不属于云服务器ECS基础概念?',
                 options=["A.安全组", "B.ddos高防", "C.镜像",
                          "D.网络"],
                 value=["B.ddos高防"], name='name14')

    put_checkbox(label='15.针对云服务器ECS安全组说法正确的是?',
                 options=["A.是一种物理防火墙", "B.仅用于控制安全组内ECS实例的入流量", "C.具备状态检测和数据包过滤能力",
                          "D.不支持VPC网络"],
                 value=["C.具备状态检测和数据包过滤能力"], name='name15')

    put_checkbox(label='16.云服务器ECS支持的产品形态包括',
                 options=["A.vm虚机和裸金属", "B.仅裸金属形态", "C.仅虚机形态",
                          "D.同时支持vm虚机、裸金属、DDH等多种形态"],
                 value=["D.同时支持vm虚机、裸金属、DDH等多种形态"], name='name16')

    put_checkbox(label='17.使用控制台可以便捷地管理ECS实例，下列哪项操作无法在阿里云控制台完成?',
                 options=["A.查看云磁盘中的数据", "B.查看阿里云ECS挂载的磁盘列表", "C.管理用户拥有的所有ECS实例",
                          "D.修改ECS的登录恋码"],
                 value=["A.查看云磁盘中的数据"], name='name17')

    put_checkbox(label='18.针对专有网络VPC，不可以进行以下哪个操作?',
                 options=["A.选择IP地址范围", "B.配置路由表", "C.配置网关",
                          "D.更改地域"],
                 value=["D.更改地域"], name='name18')

    put_checkbox(label='19.参加阿里云的哪个技术公益项目，可以免费领取学生专享的免费云服务器?',
                 options=["A.云翼计划", "B.中小企业数字化服务节", "C.繁星计划",
                          "D.飞天加速计划"],
                 value=["D.飞天加速计划"], name='name19')

    put_checkbox(label='20.飞天加速计划为以下哪种人群提供免费云服务器领取?',
                 options=["A.学生", "B.医生", "C.公务员",
                          "D.企业管理层"],
                 value=["A.学生"], name='name20')

    put_checkbox(label='21.学生用户免费领取飞天加速计划的云服务器ECS,需要先完成下列哪项动作？',
                 options=["A.学生实名认证", "B.学会编程语言", "C.学会建站",
                          "D.购买过云服务器ECS"],
                 value=["A.学生实名认证"], name='name21')

    put_checkbox(label='22.以下哪些不是云服务器ECS的产品组件？',
                 options=["A.数据库", "B.快照", "C.安全组",
                          "D.镜像"],
                 value=["A.数据库"], name='name22')

    put_markdown(r""" # 二、多选题 """)
    put_checkbox(label='1.云服务器ECS无法远程连接可能是以下哪些选项导致',
                 options=["A.密码不正确", "B.安全组未开放相应端口", "C.云服务器已关机或重启中",
                          "D.有效期还剩1天"],
                 value=["A.密码不正确", "B.安全组未开放相应端口", "C.云服务器已关机或重启中"], name='multi_name1')

    put_checkbox(label='2.远程连接云服务器ECS有哪几种方式?',
                 options=["A. Workbench", "B. VNC", "C.控制台", "D.第三方客户端工具"],
                 value=["A. Workbench", "B. VNC", "D.第三方客户端工具"], name='multi_name2')

    put_checkbox(
        label='3.阿里云云服务器ECS位于“云端”，但是用户可以完全掌控自己的ECS，以下哪几项体现了阿里云支持用户掌控自己的ECS?',
        options=["A.升降配", "B.远程连接ECS", "C.配置安全组", "D.退订"],
        value=["A.升降配", "B.远程连接ECS", "C.配置安全组", "D.退订"], name='multi_name3')

    put_checkbox(
        label='4.阿里云云服务器ECS位于“云端”，但是用户可以完全掌控自己的ECS，以下哪几项体现了阿里云支持用户掌控自己的ECS?',
        options=["A.用户可以自主选定自己的ECS所处的位置，即地域与可用区，阿里云不会擅自更改",
                 "B.用户可以通过控制台实时掌握自己ECS的运行状态",
                 "C.用户可以通过终端远程连接ECS，对ECS所做的所有操作完全自主决定",
                 "D.用户可以自主重置ECS的密码"],
        value=["A.用户可以自主选定自己的ECS所处的位置，即地域与可用区，阿里云不会擅自更改",
               "B.用户可以通过控制台实时掌握自己ECS的运行状态",
               "C.用户可以通过终端远程连接ECS，对ECS所做的所有操作完全自主决定",
               "D.用户可以自主重置ECS的密码"], name='multi_name4')

    put_checkbox(label='5.以下哪些是云服务器ECS的产品组件?',
                 options=["A.实例", "B.镜像", "C.块存储", "D.快照"],
                 value=["A.实例", "B.镜像", "C.块存储", "D.快照"], name='multi_name5')

    put_checkbox(label='6.快照是某一时间点云盘的数据状态文件，常用于以下哪些场景?',
                 options=["A.数据备份", "B.数据恢复", "C.数据制作", "D.自定义镜像"],
                 value=["A.数据备份", "B.数据恢复", "C.数据制作", "D.自定义镜像"], name='multi_name6')

    put_checkbox(
        label='7.云计算已经成为数字化转型的基础设施，作为云计算的基础产品之一，以下哪些是阿里云云服务器ECS的优势?',
        options=["A.产品丰富", "B.弹性灵活", "C.稳定可靠", "D.便捷易用"],
        value=["A.产品丰富", "B.弹性灵活", "C.稳定可靠", "D.便捷易用"], name='multi_name7')

    put_checkbox(label='8.云服务器ECS支持以下哪些运维工具？',
                 options=["A. Terraform", "B.运维编排", "C.资源编排", "D.SMC迁云工具"],
                 value=["A. Terraform", "B.运维编排", "C.资源编排", "D.SMC迁云工具"], name='multi_name8')
    put_checkbox(label='9.用户可以对云服务器ECS进行下列哪些操作？',
                 options=["A.升降配", "B.远程连接ECS", "C.配置安全组", "D.退订"],
                 value=["A.升降配", "B.远程连接ECS", "C.配置安全组", "D.退订"], name='multi_name9')

    put_markdown(r""" *** """)
    put_markdown(r""" > *题目来自网络，不保证题目量最新，误勾选项框可刷新页面复原* """)
    put_markdown(r""" > *feedback：WeChat@gazh1312* """)


if __name__ == '__main__':
    # start_server(applications=index, host='192.168.150.109',port=61157)
    start_server(applications=index)
    # put_image('https://views.whatilearened.today/views/github/evil0ctal/TikTokDownload_PyWebIO.svg', title='访问记录')
