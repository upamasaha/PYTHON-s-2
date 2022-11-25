##In python , we can use the <yield> keyword to convert any python function into a python generator.

def creating_gen (index):
    months=["January","March","April","May","June","July","August","September","October","November","December"]
    yield months[index]
    yield months[index+2]
next_month=creating_gen(3)
print(next(next_month),next(next_month))
