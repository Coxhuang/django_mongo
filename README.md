[TOC]


# django-mongodb

## #0 Blog

```
https://blog.csdn.net/Coxhuang
```

## #1 环境

> 前提: 已经安装MongoDB

```
Python3.7.3
Django==2.0.7
mongoengine==0.17.0
```

## #2 开始

### #2.1 安装 mongoengine


```
pip3 install mongoengine
```

### #2.2 新建django项目

### #2.3 在MongoDB新建一个数据库

```
use django_mongo
```

![20190426155828-image.png](https://raw.githubusercontent.com/Coxhuang/yosoro/master/20190426155828-image.png)


### #2.4 修改settings.py配置


```
DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE':None,
    }
}
from mongoengine import connect
connect('django_mongo') # 链接刚刚新建的MongoDB数据库 
```

### #2.5 models.py


```
from django.db import models
import mongoengine


class Test(mongoengine.Document):

    name = mongoengine.StringField(
        max_length=128,
    )
    age = mongoengine.IntField(
        default=10,
    )
```

### #2.6 不需要数据库迁移

### #2.7 新建视图函数

views.py


```
from django.shortcuts import HttpResponse
from app.models import Test
def test(request):

    Test.objects.create(
        name = "cox",
        age = 12,
    )
    return HttpResponse("hello mongodb")
```

### #2.8 访问接口

![20190426161020-image.png](https://raw.githubusercontent.com/Coxhuang/yosoro/master/20190426161020-image.png)


## #3 注意

- models中不会像使用MySQL那样,有智能补全
- models不需要数据库迁移
- models的增删改查和mysql的ORM一样,都是使用同样的ORM,只是数据库不同













