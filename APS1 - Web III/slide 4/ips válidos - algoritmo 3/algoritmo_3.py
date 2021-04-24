def ip_ok(ip):
    ip = ip.split('.')
    for byte in ip:
        if int(byte) > 255:
            return False
    return True
arq = open('IPS.txt')
validos = open('valido.txt', 'w')
invalidos = open('invalidos.txt', 'w')
for linha in arq.redlines():
    if ip_ok(linha):
        validos.write(linha)
    else:
        invalidos.write(linha)
arq.close()
validos.close()
invalidos.close()