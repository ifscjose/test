import serial
import time


# Configurações da porta serial
porta_serial = 'COM5'  # Altere para a porta serial correta
baud_rate = 115200  # Taxa de transmissão em bps

# Função para enviar comando AT e receber resposta
def enviar_comando_at(comando):
    ser.write((comando + '\r\n').encode())
    time.sleep(1)
    return ser.readlines()

# Inicializa a comunicação serial
ser = serial.Serial(porta_serial, baud_rate, timeout=1)

# Configuração do modem
resposta = enviar_comando_at('AT')
print(resposta)

resposta = enviar_comando_at('AT+CGNSPWR?')
print(resposta)

resposta = enviar_comando_at('AT+CGNSPWR=1')
print(resposta)

resposta = enviar_comando_at('AT+CGNSCOLD=?')
print(resposta)

resposta = enviar_comando_at('AT+CGNSXTRA=0')
print(resposta)

# Loop para receber as coordenadas a cada 1 segundo
while True:
    resposta = enviar_comando_at('AT+CGNSINF')
    print(resposta)
    time.sleep(1)

# Fechar a porta serial
ser.close()
