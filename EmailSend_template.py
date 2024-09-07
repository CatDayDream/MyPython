import smtplib  # 邮件发送模块
from email.mime.text import MIMEText
from email.header import Header
# import schedule  # 定时运行模块


def email_send():
    # 邮件配置信息
    smtp_server = 'smtp.qq.com'  # 邮箱服务器
    smtp_port = 465
    smtp_ssl = True
    smtp_user = '578750954@qq.com'
    smtp_password = 'qdslqcmqfaynbdga'  # 邮箱授权码，到邮箱网站中查看

    # 发送邮件信息
    sender = '578750954@qq.com'  # 发送者邮箱
    receivers = ['578750954@qq.com']  # 接收者邮箱

    # 邮件正文
    mail_content = 'Python 邮件发送测试...'  # 邮件正文内容
    message = MIMEText(mail_content, 'plain', 'utf-8')  # 邮件正文格式

    # 邮件信息配置
    message['From'] = '578750954@qq.com'  # 邮件标头中发件人，不影响实际发送邮箱
    message['To'] = '2309161554@qq.com'  # 邮件标头中收件人，不影响实际送达邮箱
    message['Subject'] = Header("猜猜我是谁？", 'utf-8')  # 邮件标题

    # 发送邮件
    try:
        smtp_obj = smtplib.SMTP_SSL(smtp_server, smtp_port)  # 连接服务器
        smtp_obj.login(smtp_user, smtp_password)  # 登入发送者邮箱
        smtp_obj.sendmail(sender, receivers, message.as_string())  # 发送邮件指令
        print("邮件发送成功")

    except smtplib.SMTPException as e:
        print("Error: 邮件发送失败: ", e)


# 调用邮件发送函数
# Method-1 #
"""

# 设定邮件发送次数 #
send_times = 5  # 设定邮件发送次数
while send_times > 0:
    email_send()
    send_times = send_times - 1
    
"""

# Method-2
"""

# 设定邮件定时发送时间 #
schedule.every().day.at("08:00").do(email_send)
while True:
    schedule.run_pending()
    
"""