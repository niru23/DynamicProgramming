#!/usr/bin/python
import unittest


def lcs(s1,s2):
    table =[[0]*(len(s2)+1)for i in range(len(s1)+1)]
    longest =0
    current_s1_index =0
    for m in range(len(s1)+1):
        for n in range(len(s2)+1):
            if s1[m-1] ==s2[n-1]:
               table[m][n] =table[m-1][n-1]+1
               if table[m][n] >longest:
                  longest = table[m][n]
                  current_s1_index =m
            else:
                table[m][n]=0
    return s1[current_s1_index-longest:current_s1_index]

class Test(unittest.TestCase):
      data =[('OldSite:GeeksforGeeks.org','NewSite:GeeksQuiz.com','Site:Geeks')]

      def test_lcs(self):
          for s1,s2,expected in self.data :
              actual = lcs(s1,s2)
              self.assertEqual(actual,expected) 
            

if __name__ =="__main__":
   
    unittest.main()     






