#!/usr/bin/python
import unittest
def getChange(denomination,change):
    # check the base condition
    print ' Denominations '+str(denomination)
    print ' Change '+str(change)
    if change in denomination:
       return 1
    else:
         maxDeno = max([ c for c in denomination if c <= change ])    
         newChange = change -maxDeno
         numCoin = 1+getChange(denomination,newChange)
         print ' numCoin '+str(numCoin)
         return numCoin

class Test(unittest.TestCase):
      data =[([1,5,10,25],90,5)]
      
      def test_coin_change_recursion(self):
          for testDeno,testChange,expected in self.data:
              actual = getChange(testDeno,testChange)
              self.assertEqual(actual,expected)

if __name__ == "__main__":
   unittest.main()



