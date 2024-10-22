# codigo python mover servo

import serial # importar a biblioteca pyserial
import time

# Configura a porta serial e a velocidade (mesmos valores usados no arduino)
arduino = serial.Serial('COM5', 9600)
time.sleep(2)

# Início de um loop infinito, até que seja interrompido manualmente pelo Ctrl+C
while True:
    # Início de um bloco. Se houver erro, será tratado no bloco except
    try:
        angulo = input("Digite o ângulo para o servo (0-180): ")
        angulo = int(angulo)
        if 0 <= angulo <= 180: # checa se o valor digitado está entre 0 e 180
            arduino.write(f"{angulo}\n".encode()) # envia o ângulo para o Arduino
            print(f"Ângulo {angulo} enviado ao Arduino.")
        else:
            print("Por favor, digite um valor entre 0 e 180.")

    # parar o programa com Ctrl+c
    except KeyboardInterrupt:
        print("Encerrando programa...")
        arduino.close()