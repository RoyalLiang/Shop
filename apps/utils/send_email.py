from django.core.mail import send_mail
from Shop.settings import EMAIL_FROM


def send_goods_email(admin_email, name, user_email, inquire, message):
    email_title = 'Test'
    email_body = '用户名：{}，邮箱：{},对货号{}发送了一个请求,内容:{}，请在第一时间处理。'.format(name, user_email, inquire, message)
    send_status = send_mail(email_title, email_body, EMAIL_FROM, [admin_email])
    if send_status:
        pass
