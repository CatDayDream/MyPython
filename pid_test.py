import psutil

pl = psutil.pids()
print(pl)
for pid in pl:
    print(psutil.Process(pid).name())
    if psutil.Process(pid).name() == "PyCharm":
        com_flag = True
        print(233)

