import zipfile

origen = "miarchivo.txt"

destino = 'basededatos.zip'

archivo = zipfile.ZipFile(destino,'w',compression=zipfile.ZIP_DEFLATED)
archivo.write(origen)
