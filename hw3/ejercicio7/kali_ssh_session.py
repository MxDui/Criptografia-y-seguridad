import pexpect
import sys

host = sys.argv[1] if len(sys.argv) > 1 else "192.168.56.10"
user = sys.argv[2] if len(sys.argv) > 2 else "drivera"
password = sys.argv[3] if len(sys.argv) > 3 else "Redes-2026-2"

child = pexpect.spawn(
    f"ssh -o StrictHostKeyChecking=no {user}@{host}",
    encoding="utf-8",
    timeout=12,
)
child.logfile = sys.stdout

index = child.expect(["password:", r"[$#]"])
if index == 0:
    child.sendline(password)
    child.expect(r"[$#]")

child.sendline("whoami; hostname; uname -a; pwd; ls -la | head; exit")
child.expect(pexpect.EOF)
