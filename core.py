#coding=utf-8
import function as f

class Settings():
    
    def __init__(self):
        self.path_found = False


#初始数组
array = [[1,2,3,4],
         [5,6,7,8],
         [9,10,11,12],
         [13,14,15,0]]
#目标数组
array_target = [[1,2,3,4],[5,6,8,7],[9,10,0,11],[13,14,15,12]]
#array_target = [[1,2,3,4],[5,6,7,8],[9,0,10,12],[13,14,11,15]]

#初始化检测变量
settings = Settings()

#初始化
array_origin = array
path = []
path_saves = []

#递归深度 / 模拟步数
limits = 30

#开始递归
for limit in range(limits):
    if not settings.path_found:
        print("--------------------", limit)
        f.recursion(array, array_target, limit, path, path_saves, settings, direction_last = -1)
        
    
#路径文件检测
f.final(path_saves)

#模拟路径
f.drawStep(array_origin, path_saves, index = 0)