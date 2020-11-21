# -*- coding: utf-8 -*-
"""
Montecarlo simulation:
    
    三个玩家相互比赛每个人赢的概率是0.5，每场比赛后，剩下的那个玩家代替输的人
    求每个人都赢其他人一次所需要的场次期望
    
result = 12.4
"""

import numpy as np
import matplotlib.pyplot as plt

def MonteCarlo(N, simulation):
    results = np.zeros(N)
    for i in range(N):
        results[i] = simulation()
    
    arrN = np.arange(1,N+1)
    mc = np.cumsum(results)/arrN
    # print(mc)
    plt.figure()
    plt.plot(arrN, mc)
    plt.show()
    return mc[-1]

def simulation():
    board = np.zeros([3,3])
    final = np.array([[0,1,1],[1,0,1],[1,1,0]])
    
    host = 0
    guest = 1
    wait = 2
    Nturns = 0
    
    while (not np.array_equal(board,final)):
        host_win = versus(board, host, guest)
        # print(Nturns)
        # print(host_win, board)
        if host_win:
            tmp = guest
            guest = wait; wait = tmp
        else:
            tmp = host
            host = guest; guest = wait; wait = tmp
        # print(host, guest, wait)
        Nturns += 1
        
    return Nturns

def versus(board, host, guest):
    
    ber = np.random.binomial(1,0.5)
    if ber==0:
        board[guest, host] = 1
    else:
        board[host, guest] = 1
    return ber
            

print(MonteCarlo(10000, simulation))
