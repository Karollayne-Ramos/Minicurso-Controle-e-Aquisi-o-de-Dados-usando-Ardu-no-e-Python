import serial # importa a biblioteca serial. comunicação via porta serial
import time # utiliza funções relacionadas ao tempo como sleep()

# Configura a porta serial (substitua pela porta que o Arduino está usando)
arduino = serial.Serial('COM6', 9600, timeout=1) #tempo de 1 segundo para a leitura da porta serial
time.sleep(2) # aguarde 2 segundos para garantir que a conexão seja estabelecida

try:
    # inicia um loop infinito que mantém o código rodando
    while True:
        if arduino.in_waiting > 0:  # verifica se a dados para leitura
            line = arduino.readline().decode('utf-8').strip() # Lê a linha enviada pelo Arduino
            if "Angulo" in line: # verifica se a palavra "Angulo" está presente na linha lida
                print(line)
        time.sleep(0.1) # adiciona um pequeno delay para não sobrecarregar o loop
except KeyboardInterrupt: # finaliza o programa casa as teclas Ctrl+c seja pressionada
    print("\nPrograma interrompido pelo usuário.")
    arduino.close()  # fecha a conexão serial de forma segura     