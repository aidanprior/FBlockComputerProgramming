# func1 () -> None
def func1():
    print("Awesome")

# func2 (val) -> None
def func2( val ):
    print(val)

# func3 (val1, val2) -> None
def func3( val1, val2 ):
    print( val1 + val2 )

# func4 (val1, val2) -> Any
def func4( val1, val2 ):
    return val1 + val2


func1()
func2(5)
func3(5, 3)
f4 = func4(5, 3)
print(f4*2)