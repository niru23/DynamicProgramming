#!/usr/bin/python
import unittest
#Given a sequence of n real numbers A(1) ... A(n),
#determine a contiguous subsequence A(i) ... A(j)
#for which the sum of elements in the subsequence is maximized.
# This method is a slight imporvization which can handle all negative

# example A = [ -2, 11, -4, 13, -5, 2 ];
# Max Sum: 20 Indices: i=1: j=3


def MaxSumsSubsequence(array):
    curr_sum =0
    sum_so_far =0
    for index in range(len(array)):
        curr_sum = max(array[index],(curr_sum+array[index]))
        sum_so_far =max(sum_so_far,curr_sum)
    return sum_so_far

# handling all negative values
def MaxSumsSubsequence(array):
    if not [ i for i in array if i >0]:
       curr_sum = min(array)
       sum_so_far =min(array)
    else:
       curr_sum =0
       sum_so_far =0    
    for index in range(len(array)):
        curr_sum = max(array[index],(curr_sum+array[index]))
        sum_so_far =max(sum_so_far,curr_sum)
    return sum_so_far 
# print out the sequence of elements

def MaxSumsSubsequence(array):
       curr_sum =0
       sum_so_far =0
       result =[]
       for index in range(len(array)):
          curr_sum = curr_sum+array[index]
          if curr_sum <0:
             curr_sum =0
          else:
              r =(index,array[index])
              result.append(r)
          if sum_so_far< curr_sum:
              sum_so_far =curr_sum
       return (sum_so_far,result)

def MaxProductSubsequence(array):
    curr_product =1
    product_so_far =1
    subarray =[]
    final_subarray=[]
    for index in range(len(array)):
        print 'current product '+str(curr_product)
        print 'product so far '+str(product_so_far)
        print 'array value '+ str(array[index])
        if array[index]==0:
           curr_product =1
           subarray =[]
        else:
           curr_product =curr_product*array[index]
           subarray.append(array[index])
        if  product_so_far < curr_product:
            product_so_far =curr_product
            final_subarray =subarray[:]
        print final_subarray
    return  product_so_far



