#coding=utf-8
import sys
'''function'''

#输出信息
debug = False

def getNumberPosition(array, number):
    '''参数：数组，数字 返回：该数字位置'''
    for row in range(len(array)):
        for col in range(len(array[row])):
            if number == array[row][col]:
                return (row, col)
            
def printArray(array):
    '''输出数组'''
    print('----- ----- -----')
    for row in array:
            print(row)
    print('----- ----- -----')
            
            
def moveNumber(array, direction, direction_last, number = 0):
    '''参数1 数组， 参数二： 方向 0 = up， 参数三：移动数字'''
    swapNum = number
    num_x = getNumberPosition(array, number)[0]
    num_y = getNumberPosition(array, number)[1]
    if debug:
        print('移动前判定：', num_x, ',', num_y)
    
    if direction == 0 and num_x > 0 and direction_last != 1:
        '''up'''
        array[num_x][num_y] = array[num_x - 1][num_y]
        array[num_x - 1][num_y] = swapNum
        if debug:
            print('##成功向上移动')
            print('现在位置：', num_x - 1, ',', num_y)
    elif direction == 1 and num_x < len(array) - 1 and direction_last != 0:
        '''down'''
        array[num_x][num_y] = array[num_x + 1][num_y]
        array[num_x + 1][num_y] = swapNum        
        if debug:
            print('##成功向下移动')
            print('现在位置：', num_x + 1, ',', num_y)
    elif direction == 2 and num_y > 0 and direction_last != 3:
        '''left'''
        array[num_x][num_y] = array[num_x][num_y - 1]
        array[num_x][num_y - 1] = swapNum  
        if debug:
            print('##成功向左移动')
            print('现在位置：', num_x, ',', num_y - 1)
    elif direction == 3 and num_y < len(array[num_x]) - 1 and direction_last != 2:
        '''right'''
        array[num_x][num_y] = array[num_x][num_y + 1]
        array[num_x][num_y + 1] = swapNum      
        if debug:
            print('##成功向右移动')
            print('现在位置：', num_x, ',', num_y + 1)
    else:
        if debug:
            print('##失败： 到头， 方向： ', direction)
            print('现在位置：', num_x, ',', num_y)


def checkBound(array, direction, direction_last, number = 0):
    '''参数1 数组， 参数二： 方向 0 = up， 参数三：移动数字'''
    num_x = getNumberPosition(array, number)[0]
    num_y = getNumberPosition(array, number)[1]
    
    if direction == 0 and num_x > 0 and direction_last != 1:
        '''up'''
        if debug:
            print('向上边界判定成功')
    elif direction == 1 and num_x < len(array) - 1 and direction_last != 0:
        '''down'''  
        if debug:
            print('向下边界判定成功')
    elif direction == 2 and num_y > 0 and direction_last != 3:
        '''left''' 
        if debug:
            print('向左边界判定成功')
    elif direction == 3 and num_y < len(array[num_x]) - 1 and direction_last != 2:
        '''right'''  
        if debug:
            print('向右边界判定成功')
    else:
        if debug:
            print('向', direction, '边界判定失败')
        return False
    return True

def compareArray(array, array_target):
    '''一样返回True 不相同返回False'''
    array_len = len(array)
    confirmedNum = 0
    
    for row in range(array_len):
        if array[row] == array_target[row]:
            confirmedNum += 1

    if confirmedNum == array_len:
        return True
    else:
        return False

def assignValue(path, path_saves):
    #将path的值保存在path_saves列表里
    path_saves.append([])
    for step in path:
        path_saves[-1].append(step)
    

def recursion(array, array_target, limit, path, path_saves, settings, direction_last = -1):
    '''核心 递归'''
    
    '''开始'''
    limit -= 1
    if debug:
        print('进入', limit, '层')
        print(limit, ':::', path_saves)
    
    '''base case'''
    if(compareArray(array, array_target)):
        print("成功判定 结束工作 退出系统")
        assignValue(path, path_saves)
        print(path_saves)
        #sys.exit()
        limit = 0
        settings.path_found = True
        
    if limit <= 0:
        if debug:
            print('到达底层 结束 返回第一层移动')
        #print('*', end='')
    else:
        
        #向上移动
        if debug:
            print('层数： ', limit, '准备向上移动')
        if checkBound(array, 0, direction_last):
            #移动
            moveNumber(array, 0, direction_last)
            path.append(0)
            recursion(array, array_target, limit, path, path_saves, settings, direction_last = -1)
            
            #回滚
            if debug:
                print('层数： ', limit, '完成向上移动, 回滚：')
            moveNumber(array, 1, -1)
            del path[-1]
        else:
            if debug:
                print('层数： ', limit, '无法向上移动')
        
        #向下移动 
        if debug:
            print('层数： ', limit, '准备向下移动') 
        if checkBound(array, 1, direction_last):
            #移动
            moveNumber(array, 1, direction_last)
            path.append(1)
            recursion(array, array_target, limit, path, path_saves, settings, direction_last = 1)
            
            #回滚
            if debug:
                print('层数： ', limit, '完成向下移动, 回滚：')
            moveNumber(array, 0, -1)
            del path[-1]
        else:
            if debug:
                print('层数： ', limit, '无法向上移动')
        
        #向左移动   
        if debug:
            print('层数： ', limit, '准备向左移动')   
        if checkBound(array, 2, direction_last):
            #移动
            moveNumber(array, 2, direction_last)
            path.append(2)
            recursion(array, array_target, limit, path, path_saves, settings, direction_last = 2)
            
            #回滚
            if debug:
                print('层数： ', limit, '完成向左移动, 回滚：')
            moveNumber(array, 3, -1)
            del path[-1]
        else:
            if debug:
                print('层数： ', limit, '无法向上移动')
        
        #向右移动    
        if debug:
            print('层数： ', limit, '准备向右移动')
        if checkBound(array, 3, direction_last):
            #移动
            moveNumber(array, 3, direction_last)
            path.append(3)
            recursion(array, array_target, limit, path, path_saves, settings, direction_last = 3)
            
            #回滚
            if debug:
                print('层数： ', limit, '完成向右移动, 回滚：')
            moveNumber(array, 2, -1)         
            del path[-1]
        else:
            if debug:
                print('层数： ', limit, '无法向上移动')
            

def drawStep(array, path, index):
    '''根据路径 输出路径每一幅图'''
    try:
        for step in path[index]:
            print('step: ', step)
            moveNumber(array, step, direction_last = -1)
            printArray(array)
    except IndexError:
        print("没有路径文件")
        
def final(path_saves):
    #检测路径文件
    print('部署完毕:')
    if path_saves:
        print(path_saves)
    else:
        print('未能找到方法， 请增加限定值')
        