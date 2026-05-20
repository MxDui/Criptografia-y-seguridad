#!/bin/sh
set -eu

if [ "$(id -u)" -ne 0 ]; then
    echo "Ejecuta como root, por ejemplo: su -c 'sh debian_setup_services.sh'" >&2
    exit 1
fi

apt-get update
DEBIAN_FRONTEND=noninteractive apt-get install -y apache2 vsftpd openssh-server tcpdump net-tools
systemctl enable --now apache2 vsftpd ssh
ss -tulpen | grep -E ':80|:21|:22' || true
