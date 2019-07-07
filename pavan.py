#removedup
from collections import OrderedDict
str=str(input())
k= "".join(OrderedDict.fromkeys(str))
print(k)
