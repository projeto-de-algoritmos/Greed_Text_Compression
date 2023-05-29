import sys
from compression import HuffmanCoding

if len(sys.argv) != 2:
    print("Uso: python script.py [compress | decompress]")
    sys.exit(1)

operation = sys.argv[1]
path = "texto.txt"
##path = "algoritmohuffman.txt"

h = HuffmanCoding(path)

if operation == "compress":
    output_path = h.compress()
    print("Arquivo comprimido: " + output_path)
elif operation == "decompress":
    output_path = h.compress()
    decom_path = h.decompress(output_path)
    print("Arquivo descomprimido: " + decom_path)
else:
    print("Comando inválido. Use 'compress' ou 'decompress'.")