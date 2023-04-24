# Open image
with open("recursos/01.pbm", "r") as file:

  # Getting the header
  header = []
  for linha in file:
    if linha.startswith("#"):
      continue
    header.append(linha.strip())
    if len(header) == 2:
      break

  # Getting header informations
  format = header[0]
  width, height = map(int, header[1].split())

  # Read pixel image
  pixels = []

  # Percorro para cada linha
  for linha in file:
    row = linha.strip() # linha
    arr = list(row)
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