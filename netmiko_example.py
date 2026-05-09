from netmiko import ConnectHandler

dispositivo = {
    "device_type": "linux",
    "host": "100.108.119.72",
    "username": "ghostadmin",
    "password": "Bbbabyface1987|!",
    "port": 22,
}

connessione = ConnectHandler(**dispositivo)
print("Connesso!")

output = connessione.send_command("dh -f")
print(output)

connessione.disconnect()
print("Disconnesso.")
