# import ctypes
# from comtypes.client import CreateObject

# try:
#     # 加载 RegDll.dll
#     dms = ctypes.windll.LoadLibrary(r'E:\\python_work_speace\\test\\005\\RegDll.dll')
    
#     # 设置 dm.dll 路径
#     dms.SetDllPathW(r'E:\\python_work_speace\\test\\005\\dm.dll', 0)
    
#     # 创建 COM 对象
#     dm = CreateObject('dm.dmsoft')
    
#     # 获取版本信息并打印
#     print(f"DMSoft Version: {dm.Ver()}")
    
# except Exception as e:
#     print(f"An error occurred: {e}")


import ctypes
from comtypes.client import CreateObject

try:
    # 加载 RegDll.dll
    dms = ctypes.windll.LoadLibrary(r'E:\python_work_speace\test\005\RegDll.dll')
    print(f"RegDll.dll loaded successfully",dms)
    # 设置 dm.dll 路径
    dms.SetDllPathW(r'E:\python_work_speace\test\\005\dm.dll', 0)
    
    # 创建 COM 对象
    dm = CreateObject('dm.dmsoft')
    
    # 获取版本信息并打印
    print(f"DMSoft Version: {dm.Ver()}")
    
except Exception as e:
    print(f"An error occurred: {e}")
