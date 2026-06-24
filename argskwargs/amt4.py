
class custom:
    def __init__(self,limit):
        self.num = 2
        self.limit=limit

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.num>self.limit:
            raise StopIteration
        
        val = self.num+2
        self.num+=2
        # print("this next")
        return val

x = custom(10)

for n in x:
    print(n)



# def above_avg(students):
#     x = 0
#     for i in range(len(students)):
#         x+= students[i]["marks"]
    
#     ans = x/len(students)


