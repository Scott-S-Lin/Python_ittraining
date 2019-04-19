d1 = {'a':'alpha','o':'omega','g':'gamma'}
print(d1)


t1 = ('a','o','g')
t2 = 'alpha','omega','gamma'
d3 = dict(zip(t1,t2))
print(d3)

de = dict{zip(t1,t2)}#error
print(de)
