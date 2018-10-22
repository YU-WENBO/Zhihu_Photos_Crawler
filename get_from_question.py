#coding=utf-8

from __future__ import print_function # 使用python3的print方法
from zhihu_oauth import ZhihuClient
from zhihu_oauth.exception import NeedCaptchaException


#use this part when you run the code at the first time

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


#第二次以后执行时请将上面的部分注释掉

from zhihu_oauth import ZhihuClient
import re
import os
import urllib


def auto_down(url,filename):
    try:
        urllib.urlretrieve(url,filename)
    except urllib.ContentTooShortError:
        print ('Network conditions is not good.Reloading.')
        auto_down(url,filename)


client = ZhihuClient()
# 登录
# 加载token文件
client.load_token('token.pkl')

# 例如知乎链接为：https://www.zhihu.com/question/68592527/answer/516076246 则id请填入 68592527
id = 68592527

question = client.question(id)
print(u"问题:",question.title)
print(u"回答数量:",question.answer_count)
# 建立存放图片的文件夹
os.mkdir(question.title + u"(图片)")
path = question.title + u"(图片)"
index = 1 # 图片序号
answer_num = 0
for answer in question.answers:
    answer_num = answer_num +1
    print('')
    print('第',answer_num,'/',question.answer_count,'回答')
    content = answer.content # 回答内容
    re_compile = re.compile(r'<img.*?src="(https://pic\d\.zhimg\.com/.*?\.(jpg|png))".*?>')
    img_lists = re.findall(re_compile,content)
    #print('img_lists = ', img_lists)
    if(img_lists):
        for img in img_lists:
            img_url = img[0] # 图片url
            #urllib.urlretrieve(img_url,path+u"/%d.jpg" % index)
            auto_down(img_url,path+u"/%d.jpg" % index)
            print(u"成功保存第%d张图片" % index)
            index += 1


