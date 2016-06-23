#!/usr/bin/python
import unittest

def dpGetChange(denomination,change):
    minCoins =[0]*(change+1)
    coinedUsed =[0]*(change+1)
    coin =1
    for cents in range(change+1):
        numCoins =cents
        for deno in [c for c in denomination if c <= cents]:
            if minCoins[cents-deno]+1  < numCoins:
               numCoins = minCoins[cents-deno]+1
               coin =deno
        minCoins[cents] = numCoins
        coinedUsed[cents] =coin
    return (minCoins[change],coinedUsed)      


def print_coin_used(coinedUsed,change):
    coin = change
    while coin >0:
         thisCoin = coinedUsed[coin]
         print thisCoin
         coin = coin -thisCoin



class Test(unittest.TestCase):
      data = [([1,5,10,25],90,5)]
      def  test_coin_change_dp(self):
           for testDeno,testChange,expected in self.data:
               actual,coin_used = dpGetChange(testDeno,testChange)
               self.assertEqual(actual,expected)


if __name__ =="__main__":
   unittest.main()  




