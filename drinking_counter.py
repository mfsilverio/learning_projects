# Programa para contar os dias em que um usuário bebeu
# e saber a quantos dias está sem beber e gerar dados que
# possam ser analisados, tais como: dias sem beber, bebida
# mais consumida, etc.

# O programa precisa ter uma interface gráfica que informe
# o dia e pergunte quando foi a última vez que o usuério bebeu.
# Após informar a data, o programa pergunta qual foi a bebida.
# Precisa ter um botão para ver o histórico e dizer:
# quando foi a última vez que o usuário bebeu.

# antes de ter uma interface gráfica, teremos apenas no interpretador.

from datetime import date
dia_hoje = date.today()
dia_amanha = date.fromisocalendar(2020, 51, 1)
print(dia_hoje)
print(dia_amanha)
