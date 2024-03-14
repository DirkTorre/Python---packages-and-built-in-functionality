# Handy Python code snippets and info
You can quick search for subjets by ctrl-f on the following hashtags:

\#algorithms \#bins \#chaining \#collapse \#combinations \#constants \#debugging \#difference \#filtering \#intersection \#listcomprehension \#lists \#logging \#loops \#mapping \#pandas \#permutations \#plotting \#printing \#reducing \#reformatting \#removing \#sets \#sorting \#star \#strings \#structure \#subset \#symmetric_difference \#transpose \#union \#unpacking

Bash code to generate this list:

```bash
cat Python_notes.md | tr ' ' '\n' | egrep '\\#' | sort | uniq | tr '\n' ' '
```

This document is made by [Dirk van der Torre](https://github.com/DirkTorre).

This document belongs to this [GitHub repo](https://github.com/DirkTorre/Python---packages-and-built-in-functionality)

***

# Index (kinda)
1. [The structure of a Python project](#The-structure-of-a-Python-project)
2. [Pandas](#Pandas)
3. [Plain Python](#Plain-Python)
4. [Algorithms](#Algorithms)
5. [Other interesting libraries](#Other-interesting-libraries)

PS: I am dyslexic. There will be spelling mistakes and worse: the Dutch language.

***

# The structure of a Python project
\#structure

Once a project gets bigger, you will get in trouble because of redundancies and file sizes.
So the idea is create the right framework from the start to resolve this.
There is a handy document about project structure [on this website](https://docs.python-guide.org/writing/structure/)
I took it as inspiration and added some things to create a code that also fits data analysis.
Don't name files as if they are classes.

question: do the core_functions and helper_functions also need to have an ```__init__.py```??

```
project
|--data
|  |--raw
|  |  \-------------raw_download.txt
|  |
|  |--intermediate
|  |  \------------wrangled_data.txt
|  |
|  |--clean
|  |  \---ready_for_analysis.parquet
|  |
|  \--results
|     |------------------summary.csv
|     \--------------------graph.jpg
|   
|--source
|  |---------------------__init__.py
|  |--------------------constants.py
|  |
|  |--core_functions
|  |  |-----------------constants.py
|  |  |---------------core_thing1.py
|  |  \---------------core_thing2.py
|  |
|  \--helper_functions
|     |-----------------constants.py
|     \-------------------helper1.py
|
|--tests
|  |---------------------__init__.py
|  \---------------test_functions.py
|
|--notebooks
|  \------------------analysis.ipynb
|
|--docs
|  |--documentation
|  |  \-----documentation_of_code.md
|  |
|  \--notes 
|     \--notes_related_to_project.md
|
|--------------------------README.md
|-------------------requirements.txt
\----------------starter_function.py
```

# Pandas

## Drop columns
\#pandas \#removing

```python
df.drop(columns=['col1','col2'])
```

## String string in title style
\#pandas \#strings

```python
test["address"].str.title()
```

## split string on nth occurrence of char
\#pandas \#strings \#reformatting

```python
test["address"].str.split(" ", n=1)
```

## split string to new column
\#pandas \#strings \#reformatting

```python
test["address"].str.split(" ", expand=True)
```

## matrix to 2 column list to seperate variable-value pair
\#pandas \#reformatting

```python
test.melt()
```

## matrix to 2 column list to seperate variable-value pair, plus add column and rename columns
\#pandas \#reformatting

```python
test.melt(
id_vars="species",
value_vars=["Africa",'Asia'],
var_name="continent",
value_name="population")
```

## histogram plot with bins
\#pandas \#plotting \#bins

```python
dataframe.plot(kind='hist', bins=number)
```

## column of categories to multi one-hot columns:
\#pandas #one-hot #reformatting
Make sure there are no lists by first using .explode('adress')

```python
test['adress'] = test['adress'].astype('category')
pd.crosstab(test.index, test['adress'])
```

## get subset of dfa, using column values of dfz that are the same as as indices of dfa
\#pandas  \#subset

```python
dfa[dfa.index.isin(dfz['directors'])]
```

## collapse duplicate values of a column to a list, on basis of the index
\#pandas \#reformatting \#collapse

```python
directors['director'].groupby(level=0).apply(list)
```

## values of a column (with duplicate id's) as columns
\#pandas \#reformatting \#collapse

```python
pd.pivot_table(personell, values='info', index=['tconst'], columns=['category'], aggfunc=list)
```

***

# Plain Python
## make list using list comprehension with an condition
\#listcomprehension

```python
[num for num in range(10) if num % 2]
```

## get index and value in for loop 
\#loops
Enumerate makes a list of tuples from a list and ads an integer

```python
list(enumerate(["a","b","c"])) => [(0, 'a'), (1, 'b'), (2, 'c')]
for i, thing in enumerate(to_do):
  print(i, thing)
```

## making chained functions better to read
\#chaining

```python
test = (
   thing
   .groupby(alksdjalksjd)
   .min()
   .fillna()
    )
```

## chain list comprehensions
\#listcomprehension \#chaining

```python
[
    list([i,j,k]) for i in range(x+1)
    for j in range(y+1)
    for k in range(z+1)
    if i+j+k !=n
]
```

## use map() to apply function to a list
\#mapping

Its more pythonic to use list comprehensions.
map() voert een fucntie uit op alle elementen in een lijst/tupel/etc.
map is in c geschreven en erg geoptimaliseerd, dus kan sneller zijn dan een loop.
[Link to a explenation of map](https://realpython.com/python-map-function/).

```python
def fun(x):
    return x+1
map(fun, [1,2,3]) # don't call the function

# this gives a reference to an object, to circumvent this:
list(map(fun, [1,2,3]))

# if you have a function that has multiple arguments, then give 2 lists.
# list1 with all values for argument 1 and list 2 with all values for argument 2
list(map(pow, iist1, list2))
```


## filtering values that are false when put through a function
\#filtering \#lists

```python
def is_positive(num):
   return num >= 0

list(filter(is_posiitve, [-1,2,-3,4])) # [2,4]
```

##  apply a mathametical function to all elements
\#reducing
/, *, + etc.

```python
import functools
import operator

# gives the sum
functools.reduce(operator.add, [1,2,3])
```


## create a set that is constant
\#constants \#lists \#sets

```python
frozenset(your_list)
```
  
## modify a set
\#sets

```python
myset = set([1,2,3])
myset = {1,2,3}         # alternative
myset.add(2)            # add 1 element
myset.update([1,2,3,4]) # add multiple elements
myset.discard(5)        # tries to remove 5, but is oke if 5 does not excist
myset.remove(5)         # gives error if 5 is not in set
myset.pop()
```


## get union, intersection, symmetric difference
\#sets \#union \#intersection \#difference \#symmetric_difference

```python
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])
C = A.copy()
union_set = A.union(B)
intersection_set = A.intersection(B)
difference_set = A.difference(B)
symmetric_difference_set = A.symmetric_difference(B)

# Update the set by keeping only the elements found in it and an iterable/another set.
myset.intersection_update(set)
# Update the set by removing elements found in an iterable/another set.
myset.difference_update(set)
# Update the set by only keeping the elements found in either set, but not in both.
myset.symmetric_difference_update(set)
```


## get all permutations
\#permutations

```python
from itertools import permutations
thing = "ABCD" # can also be a list of elements
list( permutations(thing,2) ) # get all permutations of length 2
```


## get all combinations without duplicates
\#combinations

```python
from itertools import combinations
thing = "ABCD" # can also be a list of elements
list( combinations(thing,2) ) # get all combinations of length 2
```

## get all combinations with replacements (duplicates)
\#combinations

```python
from itertools import combinations_with_replacement
thing = "ABCD" # can also be a list of elements
list( combinations_with_replacement(thing,2) ) # get all combinations of length 2
```
    

## unpacking with star (*)
\#unpacking \#star

2e en laastste element wordt in line gestopt. [More Info](https://peps.python.org/pep-0448/).

```python
name, *line = input().split()
```

## sort list on subelement
\#sorting \#lists \#subset

```python
import operator
# with operator.itemgetter(1) you will take sub-element with index 1
sorted([[0,6],[1,2],[2,8]], key=operator.itemgetter(1))    
```


## use logging module to check code
\#debugging \#logging

```python
    works like print. can also send log to file or email etc.
```

## printing alignment
\#printing

```python
print("SATAN".ljust(10,"-"))
print("SATAN".rjust(10,"-"))
print("SATAN".center(10,"-"))
```


## wrap words of a text to a line length
\#strings

Converts string to list of strings

```python    
textwrap.fill(string, max_width)
```

***

# Algorithms

## getting the transpose of a 2d matrix without pandas or numpy
\#algorithms \#transpose

```python
def transpose(matrix):
    matrix2 = []
    for col_index in range(len(matrix)):
        new_row = []
        for row in matrix:
            new_row.append(row[col_index])
        matrix2.append(new_row)
    return matrix2
```

***

# Environments
## Conda
\#conda \#environment

More info [here](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#activating-an-environment).

Deactivating environment:

```bash
conda deactivate
```

Show environments:

```bash
conda info --envs
```

Activate environment:

```bash
conda activate name_of_env
```

# Testing
## Pytest

Make sure to name every test function test_<name of function to test>.

### Collect all tests(?):
\#testing \#command

```bash
pytest -s
```

Viewing classes in your tests:

```bash
pytest test_circle.py -s
```


***

# Other interesting libraries
    Polars: a faster pandas (4x) uses lazy loading
    tqdm: progres bar for raw code and notebook
        - from tqdm import tqdm
        - from tqdm.notebook import tqdm
        for thing in tqdm(whatever):
    - spark: voor pipelines, kan script processen/data verdelen over meerdere nodes/computers
