import random

user_win = 0
user_health = 2
cpu_win = 0
cpu_health = 2
rounds = 1

options = ('piedra', 'papel', 'tijera')

# Función para imprimir las vidas de cada jugador
def print_lives(user_lives, cpu_lives):
    print('Vidas del jugador: ' + '❤ ' * user_lives)
    print('Vidas de la CPU:   ' + '❤ ' * cpu_lives)

# Comenzamos el juego

print('Comencemos el juego!')

while cpu_win < 2 and user_win < 2:

  print('*' * 20)
  print('ROUND ')
  print_lives(user_health, cpu_health)
  print('*' * 20)

   # La CPU elige una opción al azar
  cpu_selection = random.choice(options)

   # El usuario elige una opción
  user_selection = input('Elige piedra, papel o tijera: ').lower()

  # Validamos la selección del usuario
  while not user_selection in options:
    print('Opción inválida, por favor elige piedra, papel o tijera.')
    user_selection = input('Elige piedra, papel o tijera: ').lower()

  # Imprimimos las opciones seleccionadas
  print('La CPU eligió: ' + cpu_selection)
  
  print('Elegiste: ' + user_selection + '!!!')

  if user_selection == cpu_selection:
    print('EMPATE')

  elif (user_selection == 'piedra' and cpu_selection == 'papel') or (user_selection == 'tijera' and cpu_selection == 'piedra') or (user_selection == 'papel' and cpu_selection == 'tijera'):
    print('PERDISTE el ROUND, GANÓ LA CPU')
    cpu_win = cpu_win +1
    user_health -= 1
    rounds = rounds +1

  else:
    print('GANASTE EL ROUND')
    user_win = user_win +1
    cpu_health -= 1
    rounds = rounds + 1
    
# Alguien ganó el juego, imprimimos el resultado final
print('*' * 20)
print('Resultado final:')
print_lives(user_health, cpu_health)
print('*' * 20)

if user_win > cpu_win:
    print('¡Ganaste el juego!')
else:
    print('La CPU ganó el juego.')    

    
  