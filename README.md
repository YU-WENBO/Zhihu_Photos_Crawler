# 知乎照片爬虫 Zhihu_Photos_Crawler
提供两个python文件，分别可以实现获取某个知乎问题下所有用户回答的照片以及获取某个知乎用户的所有回答的照片

Usage：

1两者在使用时均需要将 account 和 password 改成自己的知乎账号和密码（如果账号是手机号的请在最前面加上+86）
2在第二次使用之后，登录部分的代码可以注释掉。#有了token之后，下次登录就可以直接加载token文件了

获取某个知乎问题下所有用户回答的照片：
get_from_question.py 

获取某个知乎用户的所有回答的照片：
get_from_user.py 
