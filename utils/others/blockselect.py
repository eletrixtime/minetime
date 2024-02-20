from ursina import *
BLOCKSELECT_NUMBER_LIST = ["1","2","3","4"]
def BLOCKSELECT_SELECT(key):
    print(f"Touch : {key} ")
    with open("cache/actualblock.txt", "r+") as f:
        value = f.read()
        f.seek(0) 
        if key == "1":
                f.write("1")
                f.close
        elif key == "2":
            f.write("2")
            f.close
        elif key == "3":
             f.write("3")
             f.close
        elif key == "4":
             f.write("4")
             f.close