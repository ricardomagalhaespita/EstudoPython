# Desafio Operadores Lógicos

# Os Trabalhos
trabalho_terca = True
trabalho_quinta = False

# - Confirmado os 2 trabalho: TV 50' + Sorvete
# - Confirmado apenas 1 trabalho: TV 32' + Sorvete
# - Nenhum confirmado: Fica em Casa

tv_50 = trabalho_terca and trabalho_quinta
sorvete = trabalho_terca or trabalho_quinta
tv_32 = trabalho_terca != trabalho_quinta
mais_saudavel = not sorvete

print("Tv50={} Tv32={} Sorvete={} Saudavel={}"
      .format(tv_50, tv_32, sorvete, mais_saudavel))
