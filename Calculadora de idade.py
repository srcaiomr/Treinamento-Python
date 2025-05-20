import datetime
ano_nascimento = int(input("Qual sua data de nascimento?:"))
mes_nascimento = int(input("Qual seu mês de aniversario?:"))
dia_nascimento = int(input("Qual o dia do seu aniversario?:"))

ano_atual = datetime.datetime.now().year
data_atual = datetime.datetime.now()

if ano_nascimento > ano_atual:
    print("ANO INVALIDO")
else:
    idade = ano_atual - ano_nascimento
    print(f"Você tem {idade} anos.")

if idade >= 60:
    print("Você é idoso")
elif idade >= 18:
    print("Você é adulto")
elif idade >= 12:
    print("Você é adoslecente")
else:
    print("Você é criança")

data_nascimento = datetime.datetime(ano_nascimento, mes_nascimento, dia_nascimento)
dia_de_vida = (data_atual - data_nascimento).days

print(f"Você tem aproximadamente {dia_de_vida} dias de vida: ")

hoje = datetime.date.today()
ano_atual = hoje.year

try:
    proximo_aniversario = datetime.date(ano_atual, mes_nascimento, dia_nascimento)
except ValueError:
    print("Data inválida pro próximo aniversário")
else:
    if proximo_aniversario < hoje:
        proximo_aniversario = datetime.date(ano_atual + 1, mes_nascimento, dia_nascimento)

    dias_para_aniversario = (proximo_aniversario - hoje).days
    print(f"Faltam {dias_para_aniversario} dias pro seu próximo aniversário!")