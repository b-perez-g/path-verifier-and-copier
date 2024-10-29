import os
import pandas as pd
import csv

def write_csv(file_path, data):
    if not data:
        return
    
    headers = data[0].keys()
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers, delimiter=";")
        writer.writeheader()
        writer.writerows(data)

def join_path(*paths):
    return os.path.join(*paths)

def search_directory(base_dir, folder_name):
    path = join_path(base_dir, folder_name)
    return path if os.path.exists(path) else None

def get_folder_to_search(base_dir, delivery_num, cbr):
    folder_map = {
        "1": "A_GRUPO 1",
        "2": "A_GRUPO 2",
        "3": "A_GRUPO 3",
        "4": "restante",
        "5": "TEMPORAL_NO_TOCAR"
    }
    folder_name = folder_map.get(delivery_num)
    return join_path(base_dir, folder_name, cbr) if folder_name else None

def process_row(row, base_dir):
    new_path = str(row.get('ruta_nueva', ''))
    
    if "_" not in new_path:
        row.update({"estado": "NO ENCONTRADO", "comentario": "RUTA NUEVA NO VALIDA", 
                    "coincidencia": "N/A", "guardado_en": "N/A"})
        return row

    delivery_num = new_path.split("_")[0]
    if not (delivery_num.isdigit() and 1 <= int(delivery_num) <= 5):
        row.update({"estado": "NO ENCONTRADO", "comentario": "NUMERO DE ENTREGA NO VALIDO EN RUTA NUEVA", 
                    "coincidencia": "N/A", "guardado_en": "N/A"})
        return row

    folder_to_search = get_folder_to_search(base_dir, delivery_num, row['cbr/id'].split("/")[0])
    
    if not folder_to_search:
        row.update({"estado": "NO ENCONTRADO", "comentario": "RUTA ANTERIOR EXISTE", 
                    "coincidencia": "N/A", "guardado_en": "N/A"})
    elif not os.path.exists(folder_to_search):
        row.update({"estado": "NO ENCONTRADO", "comentario": "SIN COINCIDENCIAS", 
                    "coincidencia": "N/A", "guardado_en": "N/A"})
    else:
        previous_path = search_directory(folder_to_search, str(row['ruta_anterior']))
        if previous_path:
            row.update({"estado": "ENCONTRADO", "comentario": "ENCONTRADO", 
                        "coincidencia": previous_path, 
                        "guardado_en": "matches\\" + os.path.relpath(previous_path, base_dir)})
        else:
            row.update({"estado": "NO ENCONTRADO", "comentario": "SIN COINCIDENCIAS", 
                        "coincidencia": "N/A", "guardado_en": "N/A"})
    return row

if __name__ == "__main__":
    file_path = input("Ingrese la ruta completa del archivo Excel: ")
    while not os.path.exists(file_path):
        file_path = input("Ingrese la ruta completa del archivo Excel: ")
        
    base_dir = input("Ingrese la ruta del directorio donde se buscarán los directorios:")
    while not os.path.exists(base_dir):
        base_dir = input("Ingrese la ruta del directorio donde se buscarán los directorios:")
    
    df = pd.read_excel(file_path, sheet_name=0)
    rows = df.to_dict(orient='records')
    
    processed_rows = [process_row(row, base_dir) for row in rows]
    
    write_csv("matches.csv", processed_rows)
    
    input("Proceso Finalizado con éxito\nPRESIONE ENTER PARA SALIR")

