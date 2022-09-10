import os

'''
pip3 install psutil
'''

try:
    import psutil
    print("psutil is installed")
except:
    print("psutil is not installed")
    os.system("pip3 install psutil")
    import psutil


class Monitor:
    def __init__(self) -> None:
        pass

    @staticmethod
    def get_cpu_temp():
        tempFile = open("/sys/class/thermal/thermal_zone0/temp")
        cpu_temp = tempFile.read()
        tempFile.close()
        return float(cpu_temp) / 1000


class ControlFlow:
    @staticmethod
    def show_all_info():
        print(psutil.virtual_memory().percent)
        print(psutil.disk_partitions(all=False))
        dir = '/'
        print(psutil.disk_usage(dir).percent)
        print(psutil.cpu_percent(0))
        print(psutil.cpu_percent(percpu=True))
        print(psutil.sensors_battery())
        print(psutil.sensors_fans())
        print(Monitor.get_cpu_temp())


if __name__ == '__main__':
    ControlFlow.show_all_info()
