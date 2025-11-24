# countdown timer
# recebe um valor em segundos e realiza uma contagem regressiva formatada (HH:MM:SS)

import time

my_time = int(input("Enter the time in seconds: "))

# loop regressivo formatando horas, minutos e segundos
for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Time's Up!")
