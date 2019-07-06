#coding=utf-8
from pathway import Pathway

class Array2D():
    '''二维数组'''
    
    def __init__(self, row0, row1, row2, row3):
        self.rows = [row0, row1, row2, row3]
        self.sample_rows = [row0, row1, row2, row3]
        
    def printArray(self):
        print()
        for rowNum in range(4):
            print(self.rows[rowNum])
            
    def reset(self):
        self.rows == self.sample_rows
            
    def getNumber(self, row, col):
        '''参数：位置 返回：该位置的数字'''
        return self.rows[row][col]    
    def getPosition(self, number):
        '''参数：数字 返回：该数字位置'''
        for row in range(len(self.rows)):
            for col in range(len(self.rows[row])):
                if number == self.rows[row][col]:
                    return (row, col)
    def changeNumber(self, position, number):
        '''position -> (int, int); number -> int'''
        self.rows[position[0]][position[1]] = number
        
    def checkBound(self, number, direction):
        swapNum = number
        number_row = self.getPosition(number)[0]
        number_col = self.getPosition(number)[1]
        
        len_col = len(self.rows[0])
        len_row = len(self.rows)

        if direction == 'up' and number_row > 0:
            row_value = -1
            col_value = 0
        elif direction == 'down' and number_row < len_row - 1:
            row_value = 1
            col_value = 0
        elif direction == 'left' and number_col > 0:
            row_value = 0
            col_value = -1
        elif direction == 'right' and number_col < len_col - 1:
            row_value = 0
            col_value = 1
        else:
            return False   
        
        return True
    
    def swapNum(self, number, direction):
        '''移动数字 将数字number向着direction方向移动 成功移动返回True 移动失败（碰到边界）返回False'''
        swapNum = number
        number_row = self.getPosition(number)[0]
        number_col = self.getPosition(number)[1]
        
        len_col = len(self.rows[0])
        len_row = len(self.rows)

        if direction == 'up' and number_row > 0:
            row_value = -1
            col_value = 0
        elif direction == 'down' and number_row < len_row - 1:
            row_value = 1
            col_value = 0
        elif direction == 'left' and number_col > 0:
            row_value = 0
            col_value = -1
        elif direction == 'right' and number_col < len_col - 1:
            row_value = 0
            col_value = 1
        else:
            return False
        
        #交换两个数
        self.rows[number_row][number_col] = self.rows[number_row + row_value][number_col + col_value]
        self.rows[number_row + row_value][number_col + col_value] = swapNum
        return True
    
    def compareArray(self, array_target):
        '''一样返回True 不相同返回False'''
        array_len = len(self.rows)
        confirmedNum = 0
        
        for row in range(array_len):
            if self.rows[row] == array_target.rows[row]:
                confirmedNum += 1

        if confirmedNum == array_len:
            return True
        else:
            return False
    
    def comprehension(self, pathway):
        #根据pathway 重置rows并模拟到pathway最后一步
        self.reset()
        for path in pathway:
            if path[1] == 'up':
                self.swapNum(0, 'up')
            elif path[1] == 'down':
                self.swapNum(0, 'down')
            elif path[1] == 'left':
                self.swapNum(0, 'left')
            elif path[1] == 'right':
                self.swapNum(0, 'right')            
        
        
        
        
        
        
        
        
    def recursion2(self, array_origin, array_target, pathway, pathways, step_limit):
        #每层减少一次
        step_limit -= 1
        print('step:', step_limit, pathway.getPathway())
        print(self.getPosition(0))
        
        #如过相同 储存pathway并返回上一层
        if self.compareArray(array_target):
            pathways.append(pathway)
            print("check1")
            return
        elif step_limit <= 0:
            #如果次数用完 直接向上返回
            print("check2")
            return
        
        #Sub-problem：
        for positionNum in range(4):
            if positionNum == 0:
                #up 向上走 并且 之前一步不为 向下走 以免重复
                if self.checkBound(0, 'up') and pathway.getLast()[1] != 'down':
                    self.swapNum(0, 'up')
                    pathway.addPath(0, 'up')
                    print('up add')
                    return self.recursion2(array_origin, array_target, pathway, pathways, step_limit)
                else:
                    #碰到头 则删除 直接向上返回
                    #pathway.delLast()
                    print('up del')
            if positionNum == 1 and pathway.getLast()[1] != 'up':
                #down
                if self.checkBound(0, 'down'):
                    self.swapNum(0, 'down')
                    pathway.addPath(0, 'down')
                    print('down add')
                    return self.recursion2(array_origin, array_target, pathway, pathways, step_limit)
                else:
                    #碰到头 则删除 直接向上返回
                    #pathway.delLast()
                    print('down del')
            if positionNum == 2 and pathway.getLast()[1] != 'right':
                #down
                if self.checkBound(0, 'left'):
                    self.swapNum(0, 'left')
                    pathway.addPath(0, 'left')
                    print('left add')
                    return self.recursion2(array_origin, array_target, pathway, pathways, step_limit)
                else:
                    #碰到头 则删除 直接向上返回
                    #pathway.delLast()
                    print('left del')
            if positionNum == 3 and pathway.getLast()[1] != 'left':
                #down
                if self.checkBound(0, 'right'):
                    self.checkBound(0, 'right')
                    pathway.addPath(0, 'right')
                    print('rigth add')
                    return self.recursion2(array_origin, array_target, pathway, pathways, step_limit)
                else:
                    #碰到头 则删除 直接向上返回
                    #pathway.delLast()
                    print('right del')