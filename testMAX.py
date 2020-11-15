import uuid

mac = hex(uuid.getnode())[2:]
mac = '-'.join(mac[i:i + 2] for i in range(0, len(mac), 2))
print(mac)