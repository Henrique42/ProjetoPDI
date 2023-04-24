# Open image
with open("recursos/02.pbm", "r") as file:

  # Getting the header
  header = []
  for linha in file:
    if linha.startswith("#"):
      continue
    header.append(linha.strip())
    if len(header) == 2:
      break
  # print(header)

  # Getting header informations
  format = header[0]
  width, height = map(int, header[1].split())

  # Read pixel image
  pixels = []

  # Percorro para cada linha
  for line in file:
    row = line.strip() # linha
    arr = row.split() # transformo em array
    pixels.append(arr)
    

  # Saving a new image in a new .ppm ASCII file
  with open("resultado/nova_imagem.pbm", "w") as newFile:
    # Write header
    newFile.write(format + '\n')
    newFile.write('{} {}\n'.format(width, height))

    for pixel in pixels:
      for p in pixel:
        newFile.write(f"{p}")
      newFile.write("\n")