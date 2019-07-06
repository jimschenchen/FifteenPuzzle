#coding=utf-8

from array2d import Array2D
from pathway import Pathway
import sys

sys.setrecursionlimit(100000)
#创建array
row0 = [8, 7, 6 ,5]
row1 = [1, 2, 3, 4]
row2 = [9, 10, 11, 12]
row3 = [13, 14, 15, 0]

rowt0 = [1, 2, 3 ,4]
rowt1 = [6, 5, 7, 8]
rowt2 = [9, 10, 11, 12]
rowt3 = [13, 14, 15, 0]

array_origin = Array2D(row0, row1, row2, row3)
array_1 = Array2D(row0, row1, row2, row3)
array_target = Array2D(rowt0, rowt1, rowt2, rowt3)

pathway = Pathway()
pathways = []
step_limit = 9999


array_origin.recursion2(array_origin, array_target, pathway, pathways, step_limit)

for pathway in pathways:
    print('\nResult:', pathway.getPathway())

#main:

