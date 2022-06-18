try:
    print(x + "macarons")

except NameError:
    print("PLease Define your variable.")
except IndentationError:
    print("PLease be careful when indenting your code.")

except:
    print("Something else went wrong. We need to figure it out.")

#finally block
try:
    print(h)

except:
    print("There's something wrong with our program.")
finally:
    print("Let's run our program anyway")