import one

print("print верхнего уровня в two.py")

one.func()

if __name__ == "__main__":
    print("two.py выполняется напрямую")
else:
    print("two.py импортируется в другой модуль")
