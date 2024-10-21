# codigo comunicação arduino e python

int led = 8; // definindo o pino do led

void setup () {
    pinMode(led, OUTPUT);
    Serial.begin(9600); // inicia a comunicação serial com 9600 bps
}

void loop () {
    if (Serial.available() > 0) {
        String comando = Serial.readStringUntil('\n'); // le a string enviada pelo python

        if (comando == "ligar led"){
            digitalWrite(led, HIGH); // liga o LED
        } else if (comando == "desligar led") {
            digitalWrite(led, LOW); desliga o LED
        }
    }
}