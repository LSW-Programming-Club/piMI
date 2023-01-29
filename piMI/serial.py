# This code is inspired by jdts' code from December 2019 on the Micropython forms here: https://forum.micropython.org/viewtopic.php?t=7325

# For reading from the serial bus
from sys import stdin
from uselect import poll, POLLIN
# For async sleep so GPIO is non-blocking
from uasyncio import sleep

# Serial read requirements
spoll=poll()
spoll.register(stdin,POLLIN)

async def listen():
    # Create a variable to hold until buffer read
    data = ""
    while True:
        # If serial data is ready to be read
        if (spoll.poll(0)):
            # Read one byte at a time and append it to data
            byte = stdin.read(1)
            data += byte
        # If no serial data ready to read
        else:
            # If there is data in buffer
            if (data != ""):
                # Send it to websocket
                print(data)
                # Clear buffer
                data = ""
            # Async wait half a second to allow other processes to run
            await sleep(0.5)