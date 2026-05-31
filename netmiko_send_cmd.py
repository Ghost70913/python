from netmiko import ConnectHandler

dispositivo = {
    "device_type": "cisco_ios",
    "host": "10.30.0.24",
    "username": "admin",
    "password": "password",
    "port": 22,
}

connessione = ConnectHandler(**dispositivo)
print("Connesso!")

output = connessione.send_command("ping 8.8.8.8","show ip route") 
#output1 = connessione.send_command("show ip route")
print(output)
#print(output1)

connessione.disconnect()
print("Disconnesso.")
