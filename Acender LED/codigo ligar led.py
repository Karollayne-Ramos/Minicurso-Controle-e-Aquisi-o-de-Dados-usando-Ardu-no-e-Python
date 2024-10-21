import serial # importa a biblioteca serial. comunicação via porta serial
import time # utiliza funções relacionadas ao tempo como sleep()

# Configura a porta serial (substitua pela porta que o Arduino está usando)
arduino = serial.Serial('COM6', 9600, timeout=1)
time.sleep(2) # aguarde 2 segundos para garantir que a conexão seja estabelecida

def controlar_led():
  while True: # cria um loop infinito que continuará executando até que seja interrompido
    comando = input("Digite 'ligar led' para ligar ou 'desligar led' para desligar' o led: ").strip()
    if comando in ['ligar led', 'desligar led']: # erifica se o comando digitado é válido 
      arduino.write((comando + '\n').encode())
      print(f"Comando '{comando}' enviado")
    else:
        print("Comando inválido. Tente novamente.")

try:
    controlar_led()
except KeyboardInterrupt:
    print("Encerrando programa...")
finally:
    arduino.close()