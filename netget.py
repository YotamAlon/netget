from subprocess import check_output as getout

print("Getting ifconfig")

ifconfig = getout(["ifconfig", "wlan0"]).decode('ascii').split()

print("Getting ip info")

ip = getout(["ip", "route", "show"]).decode('ascii').split('\n')

print("Parsing...")

addr = ''.join([item for item in ifconfig if 'addr:' in item][0]).split(':')[1]
print("addr:"+addr)

mask = ''.join([item for item in ifconfig if 'Mask:' in item]).split(':')[1]
print("mask:"+mask)

gtwy = ''.join([item for item in ''.join([item for item in ip if 'default' in item]).split() if '.' in item])
print("gtwy:"+gtwy)

print("DONE")
