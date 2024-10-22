#include <Servo.h> // importa a biblioteca Servo, para controlar um servo motor

Servo servo;

int servoPin = 7; // pino do servo
int pot = A0;  // pino do potenciômetro
int val = 0; // armazenará os valores lidos do potenciômetro

// a função setup() é executada uma vez quando o arduino é ligado ou reiniciado
void setup () {
    Serial.begin(9600); // inicializa a comunicação serial
    servo.attach(servoPin); // define o pin do servo
}

// a função loop() é executada repetidamente enquanto o arduino está ligado
void loop () {
    val = analogRead(pot); // vai ler o valor do potenciometro
    int angulo = map(val, 0, 1023, 0, 180); // mapeia o valor para um ângulo entre 0 e 180 graus
    servo.write(angulo); // move o servo para o ângulo correspondente

  // envia o ângulo via serial para o Python
    Serial.print("Angulo: ");
    Serial.println(angulo);

    delay(100); // atraso para evitar envio muito rápido
}