#include <Servo.h>

Servo servo; // cria um objeto servo para controlar um servo motor

int servoPin = 7; // pino do servo

void setup () {
    Serial.begin(9600); // incia a comunicação serial 
    servo.attach(servoPin); // conecta o objeto servo ao pino definido, permitindo que o Arduino controle o servo conectado a esse pino
}

void loop () {
    if (Serial.available() > 0) {  // retorna o número de bytes disponíveis para leitura
        int angulo = Serial.parseInt();  //  lê os dados e convertê em um número inteiro
        if (angulo >= 0 && angulo <= 180) {  // verifica se o valor lido está entre 0 e 180 graus
            servo.write(angulo); // move o servo para o angulo recebido
            Serial.println("Servo movido para o ângulo: " + String(angulo)); // informa que o servo foi movido para o ângulo especificado
    }
  }
}