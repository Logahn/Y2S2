#!/usr/bin env python3
print("+----------------------------------------------------------------------+")
print("Exersice 1")
print("Determine the dependence of the maximum permissible  distance between the most remote stations of a local Ethernet network.")

print("KNOWN VARIABLES:")
Vk = 10
Vc = 50000
print(f"Data transfer rate over coaxial cable =  {Vk}")
print(f"Signal propagation speed =  {Vc}")

print("UNKNOWN VARIABLE:")
En = int(input("Minimum packet (frame) length: "))
Tc_max = float((En / (Vk*(pow(10,6)))))
Smax = float(Vc * Tc_max)
Smax1 = float(0.5 * Vc * Tc_max)
print(f"Packet transmission time: {Tc_max}")
print(f"Maximum permissible distance: {Smax1}")