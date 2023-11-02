from microbit import *
import macqueen

mq = macqueen.Maqueen()

while True:
    if int(mq.read_distance()) < 4:
        mq.set_motor(0, 40)
        mq.set_motor(1, -40)

        sleep(1000)
        mq.motor_stop_all()

        mq.set_led(0, 0)
        mq.set_led(1, 1)

        if int(mq.read_distance()) < 4:
            mq.set_motor(0, -40)  
            mq.set_motor(1, 40)
            sleep(1000)  
            mq.motor_stop_all()

    else:
        mq.set_motor(0, 225)
        mq.set_motor(1, 225)
        mq.set_led(0, 0)
        mq.set_led(1, 0)
