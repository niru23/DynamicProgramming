#!/usr/bin/python

import unittest
# 3 main operations insert,delete,replace would be perfomed in the first string
def editDistance( s1,s2,l1,l2):
    # string1 is null then chars from string2 need to be inserted into string one
    if l1 is 0:
       return l2
    # string2 is null then chars from string1 need to be deleted
    if l2 is 0:
      return l1
    # if the characters match do nothing check the next character
    if s1[l1-1] ==s2[l2-1]: 
       return editDistance(s1,s2,l1-1,l2-1)

    return 1 + min(editDistance(s1,s2,l1,l2-1),# insert
                   editDistance(s1,s2,l1-1,l2),  #delete
                   editDistance(s1,s2,l1-1,l2-1) # replace
                  )


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







