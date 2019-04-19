import math
 
num = int(input())
adj = math.sqrt(num)*10
 
 
print('Original: %.2f'%(num))
print('Adjusted: %.2f'%(adj),'(+%.0f'%(adj-num),")",sep='')
