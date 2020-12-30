#!/bin/python3
'''
Version | Commit
0.1     | add  pulse function
0.2     | add mulit threading
'''
from threading import Thread
from DPS832 import *
from time import localtime, strftime

PSU = DP832()

def pulse(ch, volt, current, time_on, time_off, cycle=3):
    duration = 2 # 2 minutes

    counter = 0
    #total_cycle = duration * 60 // (time_off+time_on)
    total_cycle = cycle
    time_on_last = time.monotonic()
    time_off_last = time.monotonic()
    PSU.toggle_output(ch, 0)
    PSU.set_voltage(ch, volt)
    PSU.set_current(ch, current)
    state = 0 # PSU state
    while( counter < total_cycle):
        # if off time is over, begin to power off
        if (state ==0):
            if (time.monotonic() - time_off_last > time_off):
                PSU.toggle_output(ch, 1)
                #print("*", end="")
                time_on_last = time.monotonic()
                state = 1
        if ( state == 1):
            if (time.monotonic() - time_on_last > time_on):
                PSU.toggle_output(ch, 0)
                time_off_last = time.monotonic()
                counter += 1
                state = 0
    print()


def pulse_t(ch, volt, current, time_on, time_off, duration):
    # sec, sec, min
    print("Chanel", ch, "start at", strftime("%Y-%m-%d %H:%M:%S", localtime()))
    counter = 0
    total_cycle = duration * 60 // (time_off+time_on)
    time_on_last = time.monotonic()
    time_off_last = time.monotonic()
    PSU.toggle_output(ch, 0)
    PSU.set_voltage(ch, volt)
    PSU.set_current(ch, current)
    state = 0 # PSU state
    if time_off == 0:
        PSU.toggle_output(ch, 1)
        #while( time.monotonic() - time_on_last < duration)
        time.sleep(duration*60)
    else:
        while( counter < total_cycle):
            # if off time is over, begin to power off
            if (state ==0):
                if (time.monotonic() - time_off_last > time_off):
                    PSU.toggle_output(ch, 1)
                    #print("*", end="")
                    time_on_last = time.monotonic()
                    state = 1
            if ( state == 1):
                if (time.monotonic() - time_on_last > time_on):
                    PSU.toggle_output(ch, 0)
                    time_off_last = time.monotonic()
                    counter += 1
                    state = 0
    PSU.toggle_output(ch, 0)
    print("Chanel", ch, "end at", strftime("%Y-%m-%d %H:%M:%S", localtime()))


def pulse_par(ch, volt, current, time_on, time_off, duration):
    try:
        thread.start_new_thread(ch, volt, current, time_on, time_off, duration)
    except:
        print("Fail to apply new channel")

# ch1 = Thread(target=pulse_t, args=(1, 12, 0.09, 1,1,2))
# ch1.start()
# ch2 = Thread(target=pulse_t, args=(2, 12, 0.11, 1,1,2)) 
