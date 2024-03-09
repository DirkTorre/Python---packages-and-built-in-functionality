# Videos

- Handy [tutorial on pytest](https://www.youtube.com/watch?v=cHYq1MRoyI0) that is cool. Continue on 'Class-based Tests'.
- 

# Websites

- Handy guide on [how to structure you python code](https://docs.python-guide.org/writing/structure/).
- 

# Notes

Inside your project folder, create two folders: source and test. You can convert them to module folders by adding files in them named ```__init__.py.```. Then you can call the functions inside it from another folder.

To test the function you just run:
```bash
pytest tests/test_my_functions.py
```

In your test script, name you add the function names that you like to test, but you add the prefix test_name_of_function.py.

Note: variables, functions, classes and files must be named like this:
```python
# valid var name
this_is_a_var = 4

# valid function name
function_name(input=2)

# valid class name
ThisIsAClassName()

# valid file name
file_name.py
```