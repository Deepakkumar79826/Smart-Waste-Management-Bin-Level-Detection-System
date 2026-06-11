# Wiring Diagram Reference

This project is implemented as a Python virtual simulation.

If upgraded to hardware, use the following connections.

---

## ESP32 + HC-SR04

HC-SR04 VCC → ESP32 5V

HC-SR04 GND → ESP32 GND

HC-SR04 TRIG → GPIO 5

HC-SR04 ECHO → GPIO 18

---

## Buzzer

Positive → GPIO 23

Negative → GND

---

## LEDs

Green → GPIO 25

Yellow → GPIO 26

Red → GPIO 27

---

## OLED Display

SDA → GPIO 21

SCL → GPIO 22

VCC → 3.3V

GND → GND

---

## Future Hardware Upgrade

* ESP32
* HC-SR04
* OLED Display
* MQTT
* Node-RED
* Blynk
* ThingSpeak

The software architecture is already compatible with future hardware integration.
