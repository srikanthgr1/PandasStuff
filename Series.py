#CREATE A SERIES
import pandas as pd
srs = pd.Series([10, 7, 1, 22],
index = ['1968', '1969', '1970', '1970'],
name = 'srs')

#Print the series
In: srs
Out[4]: 
1968    10
1969     7
1970     1
1970    22
Name: srs, dtype: int64

#Search values in a series
In: srs['1970']
Out[6]: 
1970     1
1970    22
Name: srs, dtype: int64

#Iterate through a series
In: for item in srs:
        print (item)
Out:    
10
7
1
22

#See if a value exists in a series
In: 22 in set(srs)
Out[9]: True

In: 22 in srs.values
Out: True
        
#See membership (over the index)
In: '1970' in srs
Out: True

#Iterate over tuples (index + value)
for item in srs.iteritems():
        print item
Out:
('1968', 10)
('1969', 7)
('1970', 1)
('1970', 22)

#UPDATE A SERIES
#if you insert the same index, it will overwrite the previous value; 
#if two indexes have different values in the original series, both will be updated)
In: srs['1900'] = 11
Out: 
1968    10
1969     7
1970     1
1970    22
1900    11
Name: srs, dtype: int64
                
#To update a value according to its position in the series use ILOC
srs = pd.Series([10, 7, 1, 22],
index = ['1968', '1969', '1970', '1970'],
name = 'srs')

In: srs.iloc[3] = 30

Out: 
1968    10
1969     7
1970     1
1970    30

#To append another series use .append
In: srs.append(pd.Series({'1980':9}))
Out: 
1968    10
1969     7
1970     1
1970    30
1980     9
dtype: int64
        
#to add a new item and return the series use .set_value (attention, it will be deprecated and replaced by .at[] or .iat[])
srs.set_value('1990', 9)
Out[7]: 
1968    10
1969     7
1970     1
1970    30
1990     9
Name: srs, dtype: int64
                

