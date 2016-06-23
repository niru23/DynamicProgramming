#!/usr/bin/python
import unittest
def getChange(denomination,change,knownResults):
    # check the base condition
    print ' Denominations '+str(denomination)
    print ' Change '+str(change)
    print ' Known Results '+str(knownResults)
    if change in denomination:
       knownResults[change]=1
       return 1
    elif knownResults[change] >0:
         return knownResults[change]
    else:
         maxDeno = max([ c for c in denomination if c <= change ])    
         newChange = change -maxDeno
         numCoin = 1+getChange(denomination,newChange,knownResults)
         print ' numCoin '+str(numCoin)
         knownResults[change] =numCoin
         print ' Known Results '+str(knownResults)
         return numCoin

class Test(unittest.TestCase):
      data =[([1,5,10,25],90,5)]
      
      def test_coin_change_recursion(self):
          for testDeno,testChange,expected in self.data:
              actual = getChange(testDeno,testChange)
              self.assertEqual(actual,expected)

if __name__ == "__main__":
   unittest.main()



