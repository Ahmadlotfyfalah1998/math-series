import pytest

from series.series import fibonacci
from series.series import lucas
from series.series import sum_series
def test_one_fibonacci ():
     actual=fibonacci(1)
     excepted =1
     assert actual== excepted
     
     
     
     
def test_two_fibonacci ():
     actual=fibonacci(8)
     excepted =21
     assert actual== excepted
     
def test_three_fibonacci ():
     actual=fibonacci(7)
     excepted =13
     assert actual== excepted
     
    
def test_four_lucas ():
     actual=lucas(1)
     excepted =1
     assert actual== excepted 
     
def test_five_lucas ():
     actual=lucas(0)
     excepted =2
     assert actual== excepted 
     
     
     
def test_six_lucas ():
     actual=lucas(6)
     excepted =18
     assert actual== excepted 
     
     
def test_one_sum_series ():
     actual=sum_series(0,0,1)
     excepted =0
     assert actual== excepted 
     
     
def test_two_sum_series():
     actual=sum_series(1,0,1)
     excepted =1
     assert actual== excepted      
     
     
def test_three_sum_series  ():
     actual=sum_series(6,2,1)
     excepted =18
     assert actual== excepted          
     
     
def test_four_sum_series  ():
     actual=sum_series(4,4,5)
     excepted =23
     assert actual== excepted      
     '4,5,9,14,23'
     
     
def test_five_sum_series  ():
     actual=sum_series(6)
     excepted =8
     assert actual== excepted    
     

def test_six_sum_series  ():
     actual=sum_series("str")
     excepted ='please enter a number'
     assert actual== excepted    
     
