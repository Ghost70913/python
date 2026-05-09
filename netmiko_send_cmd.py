from netmiko import ConnectHandler

dispositivo = {
    "device_type": "",
    "host": "",
    "username": "",
    "password": "",
    "port": ,
}

connessione = ConnectHandler(**dispositivo)
print("Connesso!")

output = connessione.send_command("")
print(output)

connessione.disconnect()
print("Disconnesso.")
