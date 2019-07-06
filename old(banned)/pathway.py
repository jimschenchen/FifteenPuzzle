#coding=utf-8

class Pathway():
    '''
    储存路径
    格式为： 一个数组包含多个元组 [(1, 'UP'), (2, 'UP')， (5, 'Down')]
    '''
    
    
    def __init__(self):
        self.array = [(0, 'start')]
        
    def addPath(self, number, direction):
        '''添加一个路径， 格式为要移动的数字+方向'''
        self.array.append((number, direction))
        
    def delLast(self):
        #删除最后一项
        del self.array[-1]
    
    def delAll(self):
        self.array = []
        
    def getPathway(self):
        return self.array
    
    def getLast(self):
        if self.array:
            return self.array[-1]

