# def varargs(*args):
#     return args

# print(varargs(1,2,3,4,5))

# def keyword_args(**kwargs):
#     return kwargs
# print(keyword_args(big="foot", book="Rich Dad and Poor Dad", sport= "Football"))

def all_the_args(*args, **kwargs):
    print(args)
    print(kwargs)
    return True

print(all_the_args(1.,2, a=1))


def all_args(*ar, **kwar):
    print(f"Args: {ar}")
    print(f"Kwargs: {kwar}")

all_args(1,2,3,4,5,6,"cow", "rat", sport="football", book="Rich Dad and Poor Dad")