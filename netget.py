from subprocess import check_output as getout
from pyperclip import copy

print("Getting ifconfig")

ifconfig = getout(["ifconfig", "wlan0"]).decode('ascii').split()
print("Getting ip info")
ip = getout(["ip", "route", "show"]).decode('ascii').split('\n')

print("Parsing...")

addr = ''.join([item for item in ifconfig if 'addr:' in item][0]).split(':')[1]

mask = ''.join([item for item in ifconfig if 'Mask:' in item]).split(':')[1]

gtwy = ''.join([item for item in ''.join([item for item in ip if 'default' in item]).split() if '.' in item])

print("Got three values: %s, %s, %s" %addr, mask, gtwy)
print("Copying to Clipboard")

copy(addr + ' ' + mask + ' ' + gtwy)

print("DONE")
