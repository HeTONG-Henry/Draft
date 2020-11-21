# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 13:27:06 2020

随机分布的黑白棋开局（8x8），面试官告诉你1-64中一个数，你可以选择一颗子改变它的颜色
你和朋友定好策略，使得他看到棋盘就知道面试官说的数
"""
class keyset(set):
    # def __init__(self,s=[]):
    #     set.__init__(self,s)
    
    def __hash__(self):
        
        h  = 0;i = 0
        p = 67; m = 2**64 # n =64 so we choose nearest prime number
        for s in self:
            h += p**i*s
            s+=1

        return h%m
    
    def __eq__(self, s):  # then you can compare s1==s2
        
        return not (self-s)
    
    def __or__(self,s):
        return keyset(self.union(s)) # self|s is a set not keyset
    
    def __sub__(self, s): # you can use s1-s2， __XX__ is built in operator
        return keyset(self.difference(s))
        #return keyset(self-s) 写法有误，这样会不停呼叫减自己，kernel died
    
    def __and__(self, s):
        return keyset(self.intersection(s))

# S = keyset({1,3,2})
# print(S|keyset({4}),type(S|keyset({4})))



n = 16 # 4x4

# state_dict[keyset({2})]

def subsets(card): # subsets of 1:n, a list is perfered
    l = []    
    return l

def func():
    
    return

def find_state_value(N):  # state_dict = {}
    A = range(1,N+1)
    state_dict = {}
    for i in A:
        state_dicti ={}
        for Ai in subsets(i):
            # call some function..
            func() # what is the equations?
        state_dict.update(state_dicti)
    return state_dict