int acceloratorPin = 8;
int hopperPin = 13;

void setup()
{
     pinMode(acceloratorPin, OUTPUT);
     pinMode(hopperPin, OUTPUT);
     Serial.begin(9600);
}

void loop()
{
    if (Serial.available() > 0) {
      String data = Serial.readStringUntil('\n');
      if(data.equals("FIRE")){
        fire();
      }
      if(data.equals("FAKE")){
        fake();
      }
    }
}

void fire(){
     digitalWrite(acceloratorPin, HIGH);
     delay(750);
     digitalWrite(hopperPin, HIGH);
     delay(500);
     digitalWrite(acceloratorPin, LOW);
     digitalWrite(hopperPin, LOW);
}

void fake() {
     digitalWrite(acceloratorPin, HIGH);
     delay(750);
     digitalWrite(acceloratorPin, LOW);
}
