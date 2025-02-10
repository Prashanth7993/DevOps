try:
    #print(10+'50')
    print(50/0)
    #print("50"+10)
except TypeError:
    print("This is Type Error")

except ValueError:
    print("this is Value Error")

except ZeroDivisionError:
    print("this is Zero Division Error")

finally:
    print("this block wil always print")


