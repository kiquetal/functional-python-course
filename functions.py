from typing import List, Tuple


def call_in_something():
    print("I am called in something")


def f(x: int) -> List[int]:
    my_list: List[int] = [x, 2]
    if x % 2 == 0:
        my_list.append(3)
    else:
        my_list.append(4)
    return my_list


def tuples():
    t1: Tuple = ()
    t2: Tuple = ("1", "2")
    t3: Tuple[int, str, bool] = (1, "2", True)
    t4: Tuple[int, ...] = (1, 2, 3, 4, 5)

    print(t3)
    print(t4)


if __name__ == "__main__":
    print("I am called in main")
    call_in_something()
    print(f(4))
    tuples()
