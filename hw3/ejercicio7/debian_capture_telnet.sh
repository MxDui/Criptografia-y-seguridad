#!/bin/sh
set -eu

PCAP="${1:-ejercicio7-vm-telnet.pcap}"
echo "Capturando Telnet en $PCAP"
exec tcpdump -ni enp0s3 -s0 -w "$PCAP" tcp port 23
