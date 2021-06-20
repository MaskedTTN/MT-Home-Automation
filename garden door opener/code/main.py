from machine import Pin, UART, PWM
import utime

servo = PWM(Pin(2))
servo.freq(50)
servo.duty_u16(1350)#test servo
utime.sleep(2)
servo.duty_u16(8200)
running = True
led = Pin(25, machine.Pin.OUT)
led.value(0)
uart0 = UART(0, 9600)
uart0.write("Welcome to TOMT's home automation idea\r\n")
print("waiting for RX")

def get_message():
    bUart0 = b''
    prvMills = utime.ticks_ms()
    while (utime.ticks_ms()-prvMills)<3000:
        if uart0.any():
                b0 = uart0.read(1)
                bUart0 = bUart0 + b0
                #print("UART(0): " + b0.decode('utf-8')) for debugging purposes
                uart0.write(b0.upper().decode('utf-8'))
    return bUart0.decode("utf-8")
led.value(1)# to show physically the program is running
mes = get_message()
led.value(0)
print(mes)


#quick test with led to make sure concept works as using an actual servo would use too much
#power to the point the hc-05 module resets and has to wait to reconnect
#currently working on a solution to the issue by powering the raspberry pico and all other 
#components by an external battery
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
