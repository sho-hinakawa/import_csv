#Script para convertir a TXT los enlaces CSV de TTS 
#Creditos Telegram @hinakawa

import csv
import os

def main():
    # Nombre de los archivos de entrada y salida
    input_file_csv = input("Ingrese el nombre del archivo CSV que contiene los enlaces: ").strip()

    # Verificar que el archivo tenga extensión .csv
    if not input_file_csv.lower().endswith('.csv'):
        print("Error: El archivo debe tener extensión .csv")
        return

    # Verificar si el archivo existe
    if not os.path.exists(input_file_csv):
        print(f"Error: El archivo {input_file_csv} no existe")
        return

    output_file_txt = input("Ingrese el nombre del archivo de salida (debe ser .txt ): ").strip()
    
    # Verificar que el archivo tenga extensión .txt
    if not output_file_txt.lower().endswith('.txt'):
        print("Error: El archivo debe tener extensión .txt")
        return
    


    try:
        # Leer el archivo CSV y realizar el reemplazo
        with open(input_file_csv, 'r', encoding='utf-8') as csv_file, open(output_file_txt, 'w', encoding='utf-8') as txt_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                # Verificar si la fila está vacía
                if not row:
                    continue  # Saltar filas vacías
                # Convertir la fila a texto y reemplazar el enlace
                row_text = ','.join(str(item) for item in row)  # Maneja elementos no string
                modified_text = row_text.replace('http://cloud-3.steamusercontent.com', 'https://steamusercontent-a.akamaihd.net')
                # Escribir la fila modificada en el archivo TXT
                txt_file.write(modified_text + '\n')

        print(f"Archivo procesado y guardado como {output_file_txt}")

    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo {input_file_csv}")
    except PermissionError:
        print("Error: No se tienen permisos para leer/escribir los archivos")
    except csv.Error as e:
        print(f"Error al procesar el archivo CSV: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()
