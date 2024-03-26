"""
Checking out the dataclass library.
Used this video: # https://www.youtube.com/watch?v=vBH6GRJ1REM

There is also a 'attr' library.
It does the same, but hase a bit more functions.
"""


from dataclasses import dataclass, astuple, asdict, replace, field
import inspect

@dataclass(frozen=True, order=True)
class Comment:
    """
    - 'frozen=True' makes the values immutable.
    - 'order=True'  adds comparison logic to the objects
    """
    id: int
    text: str = "default value"
    # This is needed to create a list
    replies: list[int] = field(default_factory=list)
    # you can also add more options
    # repr=False silences variables that are not used
    areplies: list[int] = field(default_factory=list, compare=False, hash=False, repr=True)


def main():
    comment = Comment(1, "I just subscribed")
    print(comment)

    # convert to tuple (you need to import astuple from dataclasses)
    print(astuple(comment))
    
    # convert to dict (you need to import asdict from dataclasses)
    print(asdict(comment))
    
    # check the methods in the class (you need to import inspect)
    print(inspect.getmembers(Comment, inspect.isfunction))

    # If you want to change a value of an immutable dataclass,
    # You can still do that with this:
    print("old:",comment)
    print("new", replace(comment, id=3))

    # comment.id = 3


if __name__ == '__main__':
    main()