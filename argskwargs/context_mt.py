# f = open('readme.txt', 'r')
# context = f.read()
# print(context)
# f.close()

# class ContextManager:
#     def __enter__(self):
#         print("Entered file")
#         return "Show Resource"
    
#     def __exit__(self, exc_type, exc, tb):
#         print("Exiting file")

# with ContextManager() as cm:
#     print(f"using {cm}")


# with open('readme.txt','r') as f:
#     context = f.read()

# print(f.closed)
# print(context)


# def add_item(item, items=[]):
#     items.append(item)
#     return items

# print(add_item(1))
# print(add_item(2))
# print(add_item(2,[1,3]))

# print("untuned".strip("un"))
# print("untuned".removeprefix("un"))