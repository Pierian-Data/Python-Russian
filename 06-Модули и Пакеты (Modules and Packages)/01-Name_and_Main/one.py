def func():
    print("func() выполняется в one.py")

print("print верхнего уровня внутри one.py")

if __name__ == "__main__":
    print("one.py выполняется напрямую")
else:
    print("one.py импортируется в другой модуль")
