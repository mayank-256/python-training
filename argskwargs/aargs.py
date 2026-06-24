# lst = [1,2,3,4]
# dbl = list(map(lambda x: x*x, lst))
# print(dbl)

# l = []
# for i in range(3):
#     l.append(lambda: i)

# for r in l:
#     print(r())
# fal = [2,3,4,5,6]
# x = []
# for i in fal:
#     x.append(lambda i:i)

# for ele in x:
#     print(ele())
# def fun1():
#     s = 10
# def fun(fun1):
#     for i in range(10):
#         d=0
#         for j in range(5):
#             x = (lambda: j*d+fun1.s)
#             print(x(),"i= ",i,"j= ",j, "d= ",d, )

# def f():
#     s = 10

# def q(f):
#     for j in range(3):
#         d = 2
#         x = lambda: j * d + f.s
#         print(x())
# a = f()
# q(a)

# numbers = [10, 20, 30]

# it1 = iter(numbers)
# print(next(it1))  # 10
# print(next(it1))  # 20
# it2 = iter(numbers)


# print(next(it2))

# class counter:
#     """iterator for counting till limit lt"""
#     def __init__(self,lt):
#         self.num=1
#         self.lt = lt

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.num>self.lt:
#             raise StopIteration
#         current=self.num
#         self.num+=1

#         return current
    
# for n in counter(21):
#     print(n)


# a = lambda x:"q" if x ==0 else "a"

# print(a(0))

# def changecase(a):
#   print(a)
#   def myinner(x):
#     return func(x).upper()
#   return myinner

# @changecase
# def myfunction(nam):
#   return "Hello " + nam

# print(myfunction("John"))

# a = lambda i,n,ans: [ans*i for x in range(n)]
# print(a(1,5,1))
n=5
ans=1
for x in range(1,n+1):
    ans = ans * x 
    print(ans,x)
print(ans)
