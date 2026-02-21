#args
def f1(*fruits):
    print("Your fruit"+fruits[0])
f1("apple", "banana")
#kwargs
def f2(**names):
    print("Your lastname"+names["lname"]+"Your name"+names["name"])
f2(name = "Nurali", lname = "Yessenalin")