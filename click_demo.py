from pygameauto import Obj,PyGameAuto


obj = Obj()
res = obj.register(r"E:\\python_work_speace\\test\DmReg.dll", 
             r"E:\\python_work_speace\\test\\dm.dll")
print("注册结果是：" , res)

res = obj.create()

print("创建结果是： " , res)

print("大漠版本号: ",obj.Ver())

# obj = Obj()
# obj.register(r".\DmReg.dll", r".\dm.dll")
# obj.create()
# 1 导入大漠模块

# 2 导入PY操作框架,以及初始化操作
py = PyGameAuto()

# 设置操作路径，保存图片资源的操作路径
path = PyGameAuto.get_path()
print("当前路径",path)
obj.SetPath(path)

# 这里的obj是大漠对象
py.set_win(obj)

hwnd = 1180052
# 设置窗口句柄,在大漠综合工具中绑定窗口可以看到16进制的值
py.set_hwnd(hwnd)
# 3 设置大漠的操作路径

# 设置日志级别，1打印所有内容
py.set_level(1)

# 绑定窗口
# res = obj.BindWindow(hwnd,"gdi","windows","windows",0)
res = obj.BindWindowEx(hwnd,"normal","normal","normal","",0)
# res = obj.BindWindow(hwnd,"dx","dx","dx",1) 
# res = obj.BindWindow(hwnd,"normal","normal","normal",0)
print("绑定窗口结果：",res)
# 查看调用失败的错误码
# print(obj.GetLastError())

# obj.MoveTo(100,100)
