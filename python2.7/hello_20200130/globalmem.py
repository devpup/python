g_x = 1000

def change_x():
    #global g_x
    g_x = 300
    print("local_gx : " + str(g_x))

change_x()
print("global_gx: " + str(g_x))