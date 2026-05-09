from netmiko import ConnectHandler

dispositivo = {
    "device_type": "linux",
    "host": "",
    "username": "",
    "password": "",
    "port": 22,
}

connessione = ConnectHandler(**dispositivo)
print("Connesso!")

output = connessione.send_command("dh -f")
print(output)

connessione.disconnect()
print("Disconnesso.")
