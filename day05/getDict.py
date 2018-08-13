scores = { 'Korean':80, 'Math':90, 'English':80}
for k,v in scores.items():
    print(k,v)

# dictionary unpacking
# start
def my_func(Korean,Math,English, **kwargs):
    print(Korean+Math+English)
    for k, v in kwargs.items():
        print(k,v)
my_func(**scores)
my_func(1,2,3,a=3,b=4,c=5)
# end