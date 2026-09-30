"""3. El programa al iniciar debe presentar un mensaje de saludo, posteriormente comenzará a 
preguntarle al usuario lo siguiente: el nombre del usuario, edad, lugar, animal, país, comida, color, 
profesión, parte del cuerpo. La información recopilada debes almacenarla en la estructura 
que consideres correcta (lista, tupla, conjunto).
La salida del programa debe ser un cuento con la siguiente estructura:

A sus edad años nombre se fue de viaje a país. Su trabajo de profesión le permitió visitar este 
lejano lugar en el que pudo comer comida. Lamentablemente terminó visitando al doctor ya que 
su parte del cuerpo se hinchó y se puso de color color por estar jugando con un/una animal que 
casualmente encontró en un lugar"""

print('Bienvenidos al cuenta cuentos :)')
nombre = input('¿Cuál es tu nombre? ')
edad = input('¿Cuál es tu edad? ')
lugar = input('¿Desde dónde te conectas con nosotros? ')
animal = input('¿Animal favorito? ')
pais = input('¿País favorito? ')
comida = input('¿Comida favorita? ')
color = input('¿En que color estas pensando ahora? ')
profesion = input('Menciona una profesión que te guste: ')
parte_del_cuerpo = input('¿Qué parte del cuerpo te duele? ')

word_box = (nombre, edad, lugar, animal, pais, comida, color, profesion, parte_del_cuerpo)

print(f'A sus {word_box[1]} años {word_box[0]} se fue de viaje a {word_box[4]}.')
print(f'Su trabajo de {word_box[7]} le permitio visitar este lejano {word_box[2]} en el que pudo comer {word_box[5]}.')
print(f'Lamentablemente termino visitando al doctor ya que su {word_box[8]} se hinchó y se puso de color {word_box[6]} por estar jugando con un/una {word_box[3]} que casualmente encontro en el lugar')