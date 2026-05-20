# Codigo de apoyo para la entrega

Esta carpeta contiene los scripts reproducibles usados para los ejercicios que
si se entregan en el reporte: 4, 5, 6 y 7.

El ejercicio 8 no se incluye porque no habia una VM Windows disponible para
realizarlo como lo pide el enunciado.

## Ejercicio 4

Ejecutar desde la raíz de la carpeta entregada:
```bash
python3 ejercicio4/solve_aes.py
```

## Ejercicio 5

Requiere `steghide` y `jp2a` instalados. Ejecutar desde la raíz de la carpeta entregada:
```bash
sh ejercicio5/extract_stego.sh
```

## Ejercicio 6

Scripts para documentar el laboratorio DoS controlado. Ejecutar desde la raíz de la carpeta entregada:
```bash
sh ejercicio6/debian_setup_services.sh
sh ejercicio6/kali_hping_capture.sh 192.168.56.10 80
```

Archivos generados/incluidos:
- `ejercicio6/ejercicio6-vm-http-syn.pcap`: Captura representativa del ataque DoS por SYN Flood en el puerto 80.

## Ejercicio 7

Scripts para configurar Telnet/SSH y capturar tráfico. Ejecutar desde la raíz de la carpeta entregada:
```bash
sh ejercicio7/debian_setup_telnet.sh
sh ejercicio7/debian_capture_telnet.sh
sh ejercicio7/debian_capture_ssh.sh
python3 ejercicio7/kali_telnet_session.py
python3 ejercicio7/kali_ssh_session.py
```

Archivos generados/incluidos:
- `ejercicio7/ejercicio7-vm-telnet.pcap`: Captura de tráfico de la sesión Telnet mostrando usuario, contraseña y comandos en texto plano.
- `ejercicio7/ejercicio7-vm-ssh-real.pcap`: Captura de tráfico de la sesión SSH mostrando la negociación y el flujo cifrado.

