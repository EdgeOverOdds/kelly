#Viusalization of the kelly criteria

#import packages
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


'''
f = (p(b + 1) -1)/b
f = fraction of bankroll to wager
p = probability of winning
b = net odds received on the wager ("b to 1")
f = probability of bankroll
'''

#wagering function
def kelly_wager(p, b):
    f = ((p*(b+1)-1)/b)
    #print(f' f is {f}')
    return f

def outcome(p):
    roll = (np.random.rand(1))
    if p > roll:
        return(1)
    else:
        return(-1)

def bet(wager, bankroll):
    return (wager * bankroll)

def main(bankroll,  outcome, multiplier = 1):
    amount = kelly_wager(p, b)
    winnings = bet(amount, bankroll) * multiplier * outcome
    bankroll = bankroll + winnings
    return bankroll

#starting bankrolls
bankroll_kelly = 100
bankroll_half_kelly = 100
bankroll_twokelly = 100

legend = ['kelly', '1/2 kelly', '2x kelly']

if __name__ == '__main__':
    k_profit = []
    hk_profit = []
    tk_profit = []

    p = float(input('enter probability : ' ))
    b = float(input('enter net odds (b to 1) : '))
    #p = .52
    #b = 1

    for i in range(0,100):
        result = outcome(p)
        bankroll_kelly = main(bankroll_kelly, result)
        k_profit.append(bankroll_kelly)

        bankroll_half_kelly = main(bankroll_half_kelly, result, multiplier= .5)
        hk_profit.append(bankroll_half_kelly)


        bankroll_twokelly = main(bankroll_twokelly, result, multiplier= 2)
        tk_profit.append(bankroll_twokelly)

    plt.plot(k_profit)
    plt.plot(hk_profit)
    plt.plot(tk_profit)
    plt.legend(legend)
    plt.show()


