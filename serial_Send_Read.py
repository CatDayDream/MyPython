import serial
import time


def port_open():
    """打开串口"""
    ser.port = "COM4"  # 设置端口号
    ser.baudrate = 9600  # 设置波特率
    ser.bytesize = 8  # 设置数据位
    ser.stopbits = 1  # 设置停止位
    ser.open()  # 打开串口,要找到对的串口号才会成功


def port_close():
    """关闭串口"""
    ser.close()


def send(send_data):
    """发送串口编码"""
    ser.write(send_data.encode('utf-8'))  # utf-8 编码发送


def current_read():
    """读取串口返回的编码"""
    port_open()
    send('<09100000000>')  # 连接
    time.sleep(0.1)
    send("<04003300000>")
    data_read = ser.read(26)
    print(data_read.decode('utf-8'))
    current_code = data_read.decode('utf-8')
    current_read = current_code[16:22]
    current = int(current_read)
    print(current)
    port_close()
    if current >= 1:
        return True
    else:
        return False


def set_voltage(voltage):
    """设定电压编码函数"""
    # -----------------------串口编码规则---------------------- #
    if 0 <= voltage < 10:
        voltage_str = "000"
    elif 10 <= voltage < 100:
        voltage_str = "0" + str(voltage)
    else:
        voltage_str = str(voltage)
    # ------------------------连接串口----------------------- #
    port_open()
    # ------------------------发送编码----------------------- #
    send('<09100000000>')  # 连接
    time.sleep(0.2)
    send('<07000000000>')  # 启动电源
    time.sleep(0.2)
    send('<01' + voltage_str + '000000>')  # 设置110V电压
    time.sleep(0.2)
    send('<09200000000>')  # 断开连接
    time.sleep(0.2)
    # -----------------------断开串口------------------------- #
    port_close()
    # -----------------------结束通信------------------------- #


if __name__ == "__main__":
    ser = serial.Serial()
    set_voltage(110)

while True:
    print(current_read())
    time.sleep(1)
