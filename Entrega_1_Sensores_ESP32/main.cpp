
#include <Arduino.h>
#include "DHT.h"

#define DHTPIN 15
#define DHTTYPE DHT22

#define SENSOR_P 2
#define SENSOR_K 4
#define SENSOR_PH 34
#define RELE_PIN 5
#define LED_STATUS 18

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(115200);
  dht.begin();

  pinMode(SENSOR_P, INPUT_PULLUP);
  pinMode(SENSOR_K, INPUT_PULLUP);
  pinMode(RELE_PIN, OUTPUT);
  pinMode(LED_STATUS, OUTPUT);

  digitalWrite(RELE_PIN, LOW);
  digitalWrite(LED_STATUS, LOW);
}

void loop() {
  delay(2000);

  bool fosforo = digitalRead(SENSOR_P) == LOW;
  bool potassio = digitalRead(SENSOR_K) == LOW;
  int phAnalog = analogRead(SENSOR_PH);
  float ph = map(phAnalog, 0, 4095, 0, 14);

  float humidity = dht.readHumidity();

  Serial.print("Fósforo: ");
  Serial.print(fosforo);
  Serial.print(" | Potássio: ");
  Serial.print(potassio);
  Serial.print(" | pH: ");
  Serial.print(ph);
  Serial.print(" | Umidade: ");
  Serial.print(humidity);
  Serial.println("%");

  if (fosforo && potassio && ph >= 5.5 && ph <= 7.5 && humidity < 40.0) {
    digitalWrite(RELE_PIN, HIGH);
    digitalWrite(LED_STATUS, HIGH);
    Serial.println("Irrigação ATIVADA.");
  } else {
    digitalWrite(RELE_PIN, LOW);
    digitalWrite(LED_STATUS, LOW);
    Serial.println("Irrigação DESATIVADA.");
  }
}
