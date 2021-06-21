from machine import Pin, UART, PWM
import utime
import json

#right now attempting ways of making the hub know which devices are available
device_data = {
    "Name" : "Garden Gate",
    "Version" : "Alpha0.1",
    "Owner" : "MaskedTitan",
    "Passcode" : 1234
    }

servo = PWM(Pin(2))
servo.freq(50)
servo.duty_u16(1350)
utime.sleep(2)
servo.duty_u16(8200)
running = True
led = Pin(25, machine.Pin.OUT)
led.value(0)
uart0 = UART(0, 9600)
uart0.write(json.dumps(device_data)+'>')
print("waiting for RX")

def get_message():
    bUart0 = b''
    prvMills = utime.ticks_ms()
    while (utime.ticks_ms()-prvMills)<3000:
        if uart0.any():
                b0 = uart0.read(1)
                bUart0 = bUart0 + b0
                #print("UART(0): " + b0.decode('utf-8'))
                uart0.write(b0.upper().decode('utf-8'))
    return bUart0.decode("utf-8")
led.value(1)
mes = get_message()#.decode("utf-8")
led.value(0)
print(mes)



while running:
    cmd = get_message()
    if "led" in cmd and "on" in cmd:
        print("turning on LED")
        led.value(1)
    elif "led" in cmd and "off" in cmd:
        print("turning off LED")
        led.value(0)
    else:
        print("no known cmd")
#bUart0 = b''
#prvMills = utime.ticks_ms()
#while (utime.ticks_ms()-prvMills)<3000:
#    if uart0.any():
#            b0 = uart0.read(1)
#            bUart0 = bUart0 + b0
#            print("UART(0): " + b0.decode('utf-8'))
#            uart0.write(b0.upper().decode('utf-8'))

#f_data = ""
#while True:
#    #if uart0.any() > 0:
#    if uart0.any():
#        #data = uart0.read(1)
#        data = uart0.readline()
#        print(data.decode("utf-8"))
#        #if data == b"\n"
#        if data != "\n":
#            f_data = f_data + data.decode("utf-8")
#        if data == "\n":
#            print(f_data)
