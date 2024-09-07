import psutil
import subprocess
import time

# 启动程序
p = subprocess.Popen(['计算器.exe'])

while True:
    # 检查程序是否在运行
    if psutil.pid_exists(p.pid):
        # 如果程序在运行，等待一段时间后再检查
        print('程序正在运行')
        time.sleep(5)
    else:
        print('程序已经停止运行')
        time.sleep(5)
