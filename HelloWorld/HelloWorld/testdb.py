from django.http import HttpResponse
from TestModel.models import Test


# 数据库操作
def testdb(request):
    ####################################################
    # # 1.向数据库添加内容
    # test1 = Test(name='runoob')
    # test1.save()
    # return HttpResponse("<p>数据添加成功</p>")

    ####################################################
    # # 2.获取数据库的内容
    # # 初始化
    # response = ""
    # response1 = ""
    #
    # # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    # _list = Test.objects.all()
    #
    # # filter相当于SQL中的WHERE，可设置条件过滤结果
    # response2 = Test.objects.filter(id=1)
    #
    # # 获取单个对象
    # response3 = Test.objects.get(id=1)
    #
    # # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
    # Test.objects.order_by("name")[0:2]
    #
    # # 数据排序
    # Test.objects.order_by("id")
    #
    # # 上面的方法可以连锁使用
    # Test.objects.filter(name="runoob").order_by("id")
    #
    # # 输出所有数据
    # for var in _list:
    #     response1 += var.name + " "
    # response = response1
    # print("-"*50)
    # print(response)
    # print("-"*50)
    # return HttpResponse("<p>" + response + "</p>")

    ####################################################
    # # 3.修改数据库的内容
    # # 修改数据可以使用 save() 或 update()
    # # 修改其中一个id=1的name字段，再save，相当于SQL中的UPDATE
    # # test1 = Test.objects.get(id=1)
    # # test1.name = 'Google'
    # # test1.save()
    #
    # # 另外一种方式
    # # Test.objects.filter(id=1).update(name="google")
    #
    # # 修改所有的列
    # Test.objects.all().update(name="Google")
    #
    # return HttpResponse("<p>修改成功</p>")

    ####################################################
    # # 4.删除数据
    # # 删除id=1的数据
    # test1 = Test.objects.get(id=1)
    # test1.delete()

    # # 另外一种方式
    # Test.objects.filter(id=2).delete()

    # 删除所有数据
    Test.objects.all().delete()
    return HttpResponse("<p>删除成功")
