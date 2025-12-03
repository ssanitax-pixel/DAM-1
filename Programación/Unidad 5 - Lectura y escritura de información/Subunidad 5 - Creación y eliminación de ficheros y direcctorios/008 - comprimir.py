import zipfile

origen = 'miarchivo.txt'

destino = 'basededatos.zip'

archivo = zipfile.ZipFile(destino, 'w')
archivo.write(origen)
