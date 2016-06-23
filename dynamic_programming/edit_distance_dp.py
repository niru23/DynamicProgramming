#!/usr/bin/python
import unittest

def editDistance(s1,s2,m,n):
    table =[[0]*(n+1)for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            # when s1 is empty
            if i ==0:
               table[i][j] =j
    
            # when s2 is empty 
            if j==0:
               table[i][j] =i
            
            elif s1[i-1] == s2[j-1]:
                 table[i][j] =table[i-1][j-1]
            else:
                table[i][j] =1+ min(table[i-1][j],table[i][j-1],table[i-1][j-1])
    return table[m][n]
            
 
class Test(unittest.TestCase):
      data =[('sunday','saturday',3),
             ('cat','cut',1),
             ('geek','gesek',1)
            ]

      def test_editDistance(self):
          for s1,s2,expected in self.data:
              actual =editDistance(s1,s2,len(s1),len(s2))
              self.assertEqual(actual,expected)


if __name__ == "__main__":

    unittest.main()
 
    

