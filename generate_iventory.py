import os

target_ip = os.getenv("TARGET_IP")
if not target_ip:
    raise ValueError("TARGET_IP environment variable is not set!")

with open("ansible/inventory.ini", "w") as f:
    f.write(f"[target]\n{target_ip} ansible_user=ubuntu ansible_ssh_private_key_file=~/.ssh/id_rsa\n")

