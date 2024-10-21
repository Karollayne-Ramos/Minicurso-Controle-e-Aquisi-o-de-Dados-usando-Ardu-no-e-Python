// Acende LED

int led = 8;  // definindo o pino do led

void setup () {
    pinMode(led, OUTPUT);
    Serial.begin(9600);  // inicia a comunicação serial com 9600 bps
}

void loop () {
    if (Serial.available() > 0) {  // verifica se há dados disponíveis para leitura na porta serial
        String comando = Serial.readStringUntil('\n');  // le a string enviada pelo python

        if (comando == "ligar led"){   // verifica se a string lida é igual a "ligar led"
            digitalWrite(led, HIGH);  // liga o LED
        } else if (comando == "desligar led") {
            digitalWrite(led, LOW); desliga o LED  // desliga o LED
        }
    }
}