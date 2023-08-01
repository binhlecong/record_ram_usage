import psutil
import time
import matplotlib.pyplot as plt
import pandas as pd
from datetime import date


def draw_plot(usages):
    n = len(usages)
    time = list(range(n))

    plt.plot(time, usages, color='red', marker='o')
    plt.title('RAM usages', fontsize=14)
    plt.xlabel('Time (s)', fontsize=14)
    plt.ylabel('RAM (MB)', fontsize=14)
    plt.grid(True)
    plt.show()


def main(procName, duration, interval, description):
    print('> Recording RAM usage of ' + procName)
    isProcOn = True
    ramUsages = []
    while isProcOn and duration > 0:
        for proc in psutil.process_iter():
            isProcOn = False
            if proc.name() == procName:
                isProcOn = True
                vms = proc.memory_info().vms / (1024 * 1024)
                ramUsages.append(vms)
                print(vms)
                break
        time.sleep(interval)
        duration -= interval
    print('> Recording stop')

    df = pd.DataFrame(ramUsages)
    now = date.today()
    df.to_csv(description + '_' + now.strftime("%m-%d-%y-%H-%M-%S") + '.csv')
    # draw_plot(usages=ramUsages)


if __name__ == '__main__':
    main('studio64.exe', 2 * 60, 2, 'armordroid3')
