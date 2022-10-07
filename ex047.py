import time


print('Os números pares de 1 a 50 são esses:')
for con in range(1,51):
    if con %2 == 0:
        time.sleep(0.5)
        print(con)
print('Acabou!')