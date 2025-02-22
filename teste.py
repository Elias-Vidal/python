# import pyfiglet
# texto = "SENAI"
# ascii_art = pyfiglet.figlet_format(texto, font="slant")  # Exemplo de fonte personalizada
# print(ascii_art)

beatles = []

beatles.append('John Lennon')
beatles.append('Paul McCartney')
beatles.append('George Harrison')
beatles.append('Stu Sutcliffe')
beatles.append('Pete Best')

del beatles[0:1]
beatles.insert(0,'Ringo Starr')
print(beatles)
