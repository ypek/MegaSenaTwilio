# Importe as bibliotecas necessárias
import random
from twilio.rest import Client

# Etapa 1: Receber as 6 dezenas do jogador
def receber_dezenas():
    dezenas = []
    while len(dezenas) < 6:
        dezena = int(input("Digite uma dezena entre 1 e 60: "))
        if 1 <= dezena <= 60 and dezena not in dezenas:
            dezenas.append(dezena)
    dezenas.sort()
    return dezenas

# Etapa 2: Executar os sorteios em um looping
def sortear_dezenas():
    contador = 0
    dezenas_sorteio = []
    while len(dezenas_sorteio) < 6:
        dezena = random.randint(1, 60)
        if dezena not in dezenas_sorteio:
            dezenas_sorteio.append(dezena)
            contador += 1
            print(f"Sorteio {contador}: {dezenas_sorteio}")
            if dezenas_sorteio == dezenas_jogador:
                gerar_log(contador, dezenas_jogador)
                enviar_sms(contador, dezenas_jogador)

# Etapa 3: Gerar o log
def gerar_log(contador, dezenas_jogador):
    with open("log.txt", "a") as arquivo:
        arquivo.write(f"Total de sorteios: {contador}\n")
        arquivo.write(f"Dezenas apostadas: {dezenas_jogador}\n")

# Etapa 4: Enviar um SMS para o celular do integrante
def enviar_sms(contador, dezenas_jogador):
    account_sid = 'AC4178ca1094a96f26c17099ca9e3a0b2c'
    auth_token = 'ae574bcdda7373623461d308ad843b46'
    client = Client(account_sid, auth_token)
    dezenas_sorteio = sortear_dezenas()
    message = client.messages.create(
        body=f"Você ganhou na Mega Sena! Total de sorteios: {contador}. Dezenas apostadas: {dezenas_jogador}. Dezenas sorteadas: {dezenas_sorteio}",
        from_='14302372837',
        to='5554999213874'
    )
    print(f"Mensagem enviada: {message.sid}")

# Método para verificar se o envio de SMS está funcionando
def verificar_envio_sms():
    account_sid = 'AC4178ca1094a96f26c17099ca9e3a0b2c'
    auth_token = 'ae574bcdda7373623461d308ad843b46'
    client = Client(account_sid, auth_token)
    try:
        message = client.messages.create(
            body="Sua conta ITAU FOI HACKEADA!!!! FDP",
            from_='14302372837',
            to='5554999213874'
        )
        print("SMS enviado com sucesso!")
        print(f"Mensagem SID: {message.sid}")
    except Exception as e:
        print(f"Erro ao enviar SMS: {str(e)}")

# Etapa 1: Receber as dezenas do jogador
dezenas_jogador = receber_dezenas()

# Etapa 2: Sortear as dezenas em um looping
sortear_dezenas()

# Verificar o envio de SMS
verificar_envio_sms()
