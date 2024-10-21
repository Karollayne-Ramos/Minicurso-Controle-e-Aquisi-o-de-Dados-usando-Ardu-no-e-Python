import serial # importa a biblioteca serial. comunicação via porta serial
import time # utiliza funções relacionadas ao tempo como sleep()

# Configura a porta serial (substitua pela porta que o Arduino está usando)
arduino = serial.Serial('COM6', 9600, timeout=1)
time.sleep(2) # aguarde 2 segundos para garantir que a conexão seja estabelecida

# define a função que será responsável por controlar o LED
def controlar_led():
  while True: # cria um loop infinito que continuará executando até que seja interrompido
    comando = input("Digite 'ligar led' para ligar ou 'desligar led' para desligar' o led: ").strip()
    if comando in ['ligar led', 'desligar led']: # verifica se o comando digitado é válido 
      arduino.write((comando + '\n').encode()) # envia o comando para o Arduino
      print(f"Comando '{comando}' enviado")
    else:
        print("Comando inválido. Tente novamente.")

# finaliza o programa casa as teclas Ctrl+c seja pressionada
try:
    controlar_led()
except KeyboardInterrupt:
    print("Encerrando programa...")
finally: # garante que a conexão serial com o arduino seja fechada 
    arduino.close()