#!/usr/bin/python
import unittest
#Given a sequence of n real numbers A(1) ... A(n), 
#determine a contiguous subsequence A(i) ... A(j) 
#for which the sum of elements in the subsequence is maximized.

# example A = [ -2, 11, -4, 13, -5, 2 ];
# Max Sum: 20 Indices: i=1: j=3

def MaxSumofSubswquence( array):
    current_sum =0
    sum_so_far =0
    for index in range(len(array)):
        current_sum =current_sum+array[index]
        if current_sum < 0:
           current_sum =0
        if sum_so_far < current_sum :
           sum_so_far = current_sum
    return sum_so_far 

class Test(unittest.TestCase):
      data =[([ -2, 11, -4, 13, -5, 2 ],20)]
      
      def test_MaxSumofSubswquence(self):
          for array,expected in self.data:
              actual =MaxSumofSubswquence(array)
              self.assertEqual(actual,expected) 



if __name__ == "__main__":
   unittest.main()
