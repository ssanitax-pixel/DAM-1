import zipfile

origen = "miarchivo.txt"

destino = "comprimido.zip"

archivo = zipfile.ZipFile(destino,'w')
archivo.write(origen)
