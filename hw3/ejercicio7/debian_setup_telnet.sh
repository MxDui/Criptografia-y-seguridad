#!/bin/sh
set -eu

if [ "$(id -u)" -ne 0 ]; then
    echo "Ejecuta como root, por ejemplo: su -c 'sh debian_setup_telnet.sh'" >&2
    exit 1
fi

apt-get update
DEBIAN_FRONTEND=noninteractive apt-get install -y xinetd telnetd telnet openssh-server tcpdump

cat > /etc/xinetd.d/telnet <<'TELNETEOF'
service telnet
{
    disable = no
    flags = REUSE
    socket_type = stream
    wait = no
    user = root
    server = /usr/sbin/telnetd
    log_on_failure += USERID
}
TELNETEOF

systemctl restart xinetd.service
systemctl enable --now ssh
ss -tulpen | grep -E ':23|:22' || true
