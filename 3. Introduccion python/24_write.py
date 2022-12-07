with open('./text.txt','r+') as file:
  for line in file:
    print(line)
  file.write('nuevas cosas en este archivo\n')
  file.write('Otra linea\n')
  file.write('Mas linea\n')