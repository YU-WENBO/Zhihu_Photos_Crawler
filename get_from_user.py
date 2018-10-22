#coding=utf-8

from __future__ import print_function # 使用python3的print方法
from zhihu_oauth import ZhihuClient
from zhihu_oauth.exception import NeedCaptchaException


client = ZhihuClient()

try:
    client.login('account', 'password')
except NeedCaptchaException:
    # 保存验证码并提示输入，重新登录
    with open('a.gif', 'wb') as f:
        f.write(client.get_captcha())
    captcha = raw_input('please input captcha:')
    client.login('account', 'password', captcha)


client.save_token('token.pkl') # 保存token
#有了token之后，下次登录就可以直接加载token文件了
# client.load_token('filename')



from zhihu_oauth import ZhihuClient
import re
import os
import urllib

client = ZhihuClient()
# 登录
# 加载token文件
client.load_token('token.pkl')

#例如目标user的主页url为https://www.zhihu.com/people/leng-zhe/activities，则id为leng-zhe
id = str('leng-zhe')

people = client.people(id)

#question = client.people.question(id)
index = 1  # 图片序号

os.mkdir(id)
path = id

for answer in people.answers:
    #print('answer.question.title = ',answer.question.title)

    #path = 'people'

    content = answer.content  # 回答内容
    #print('answer.content = ',answer.content)

    re_compile = re.compile(r'<img.*?src="(https://pic\d\.zhimg\.com/.*?\.(jpg|png))".*?>')
    img_lists = re.findall(re_compile, content)

    #print('img_lists = ',img_lists)
    if (img_lists):
        for img in img_lists:
            img_url = img[0]  # 图片url
            urllib.urlretrieve(img_url, path + u"/%d.jpg" % index)
            print(u"成功保存第%d张图片" % index)
            index += 1



