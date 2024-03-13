import pandas 

mydataset = {
    'cars': ["BMW", 'volvo', 'Ford'],
    'passings': [3,4,5]
}

myvar = pandas.DataFrame(mydataset)
print(myvar)


# version

import pandas as pd 
print(pd.__version__)

# series
a = [1,2,3,4,5]
myvar = pd.Series(a, index = ['one','two','three','four','five'])
print(myvar)


data = {
    'calories': [429, 380, 490],
    'duration': [40,23,49]
}

df = pd.DataFrame(data)
print(df)