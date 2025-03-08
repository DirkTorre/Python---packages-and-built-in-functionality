# Videos

- Handy [tutorial on pytest](https://www.youtube.com/watch?v=cHYq1MRoyI0) that is cool. Continue on 'Mocking'.

# Websites

- Handy guide on [how to structure you python code](https://docs.python-guide.org/writing/structure/).
- Guide on [how to use unit tests on Pandas DataFrames](https://machinelearningtutorials.org/pandas-testing-tutorial-with-examples/)

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

You can add tags to tests like this:

```python
@pytest.mark.sometagthatyoucanputhere
def test_very_slow():
    pass
```

You can execute the functions with the same tag like this:

```bash
pytest -m sometagthatyoucanputhere
```

There are built-in marks, like this one:
You can else skip test, in case a feature is broken because you worked on it.

```python
@pytest.mark.skip(reason="This feature is currently broken")
```

If you want to test for multiple input scenario's yo can use the build in function: @pytest.mark.parametrize().

```python
@pytest.mark.parametrize("side_length, expected_area", [(5, 25), (4, 16), (9, 81)])
def test_multiple_square_areas(side_length, expected_area):
    """
    Using decorator @pytest.mark.parametrize() to test multiple parameters.
    tuple[0] = value for first variable stated in string.
    """
    assert shapes.Square(side_length).area() == expected_area
```