from time import sleep

while True:
    num = int(input('\033[33mDigite um número para ver a tabuada (0 para sair): \033[0m'))
    
    if num == 0:
        print('\033[32mEncerrando o programa...\033[0m')
        sleep(1)
        break

    print(f'\033[35mTABUADA DE {num}:\033[0m')
    
    for i in range(1, 11):
        print(f'\033[34m{num} x {i} = {num * i}\033[0m')
        sleep(0.2)

    print('\033[36m' + '-' * 30 + '\033[0m')
    sleep(0.5)
