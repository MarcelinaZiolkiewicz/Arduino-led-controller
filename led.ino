#include <Adafruit_NeoPixel.h> 

#define LED_PIN 10
#define LED_COUNT 40

Adafruit_NeoPixel strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, NEO_GRB + NEO_KHZ800);

int r,g,b, color;
String dane, rS, gS,bS;


void setup() {
    Serial.begin(9600);
    Serial.print("Device ready!");

    strip.begin();
    strip.show();

}

void loop() {
    readStr();
}

void readStr() {

    while (Serial.available() > 0)
    {      
   
        dane = Serial.readString();
        Serial.println(dane);

        rS = dane.substring(0,3);
        gS = dane.substring(3,6);
        bS = dane.substring(6,9);

        r = rS.toInt();
        g = gS.toInt();
        b = bS.toInt();

        Serial.println("Color loading");

        for(int i = 0; i <= LED_COUNT; i++){
            strip.setPixelColor(i, r, b, g); 
            //value rbg because my led strip have wrong coding
            strip.show();
            delay(80);
        }            
    }       
}


void modes() {
   //tutaj bedzie sie wybieralo jaki tryb bedziemy aktualnie uzywali

}