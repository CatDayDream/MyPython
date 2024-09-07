import time
import serial
import serial.tools.list_ports

com_port = "COM4"
while 1:
    # 获取串口列表
    ports_list = list(serial.tools.list_ports.comports())
    print(ports_list)
    print(ports_list[0])
    print(ports_list[1])

    # 判断串口是否打开
    com_flag = False
    for comport in ports_list:
        if comport[0] == com_port:
            print(comport[0])
            com_flag = True
    print(com_flag)
    time.sleep(3)

