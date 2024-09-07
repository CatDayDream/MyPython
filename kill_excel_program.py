"""
<查询并关闭某个应用>
"""

import psutil  # 检查-关闭应用模块


def is_excel_running():
    for process in psutil.process_iter():
        if process.name().lower() == "excel.exe":
            return True
    return False


# 获取Excel进程ID
def get_excel_process_id():
    for process in psutil.process_iter():
        if process.name().lower() == "excel.exe":
            return process.pid
    return None


# 结束Excel进程
def kill_excel_process(pid):
    try:
        process = psutil.Process(pid)
        process.terminate()
        return True
    except psutil.NoSuchProcess:
        return False


if __name__ == "__main__":
    if is_excel_running():
        pid = get_excel_process_id()
        if pid:
            if kill_excel_process(pid):
                print("成功关闭Excel进程")
            else:
                print("关闭Excel进程失败")
        else:
            print("获取Excel进程ID失败")
    else:
        print("Excel进程未运行")
