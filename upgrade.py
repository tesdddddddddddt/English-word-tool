TotalList=[]
from unit import *
checkinit()
wordlistname=get_all_file()
def upgrade_0(list1):
    list1=[list1,{'version':'v0.1','num_version':1}]
    return list1
        
def Up_start():
    for item in wordlistname:
        list1=loadfileP(item)
        if list1[1]['num_version']!=1:
            list1=upgrade_0(list1)
            savefileP(item,list1)    