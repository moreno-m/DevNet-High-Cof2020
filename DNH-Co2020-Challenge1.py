"""DevNet High - Class of 2020 - Challenge 1"""

import random
import ipaddress

# TODO: Write a print statement that displays both the type and value of 'ip'
ip = "10.1.1.200"
if type(ip).__name__ == "str":
    print("---TASK1---")
    print(f"ip value is: {ip} \nType is: string\n")
else:
    print("---TASK1---")
    print(f"ip value is: {ip} and the Type is:{type(ip).__name__}")

# TODO: Write a conditional to print out if `iosversion` is less than or greater than 14
i = random.randint(12, 17)
print("---TASK2---")
print('i is {}'.format(i))
if i < 14:
    print("IOS version is less than 14")
elif i==14:
    print("IOS version is equals to 14")
else:
    print("IOS version is greater than 14")

# TODO: Write a conditional that prints the serial number of the device
devices = ({'CAT9300':'XVNM1245ERGC'}, {'ISR4331':'VNMM8742THBX'}, {'NGFW2120':'EAQP4900RTJO'})
device = random.sample(devices, 1) [0]
device = list(device.values())[0]

print("\n---TASK3---")
print(f"The device SN is: {format(device)}")
# Function for converting CIDR notation into 32-bit netmask (nothing to do here)
def cidr_to_netmask(ip_str):
    ip = ipaddress.IPv4Network(ip_str)
    return ip.with_netmask

'''
TODO: Call the function above few times to so that the input of IP network with CIDR displays the IP network with 32-bit netmask
Example:
Input would be '10.1.1.0/24' and when printed out the output would be '10.1.1.0/255.255.255.0'
'''
print("\n---TASK4---")
i=1
while i<=3 :
    strCIDR = input('Please enter the IP/CIDR value:')
    strOutput = cidr_to_netmask(strCIDR)
    print(strOutput)
    i += 1




