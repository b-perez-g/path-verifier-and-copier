# Procesamiento de Archivos de Ruta

Script en Python que verifica la existencia de archivos desde rutas indicadas en un Excel, generando un reporte en CSV con el estado y ubicación de cada coincidencia, y creando una copia de los archivos encontradosEste script permite procesar un archivo de Excel, buscar rutas de archivos en un sistema de archivos, y exportar los resultados en un archivo CSV con información sobre las coinci de cada archivo

## Requisitos

- Python 3.x
- Paquetes:
  - `pandas`
  - `openpyxl`

## Instalación

1. Clonar este repositorio o descargar los archivos.
2. Instalar los paquetes requeridos ejecutando:
   ```
   pip install -r requirements.txt
   ```

## Uso

1. Ejecutar el script `main.py`.
2. Ingresar la ruta completa del archivo Excel que contiene las rutas de archivos a procesar.
3. Ingresar la ruta del directorio base donde se buscarán los archivos.
4. El script generará un archivo `matches.csv` con los resultados del procesamiento.

## Estructura del Archivo de Excel

El archivo de Excel debe contener las siguientes columnas:

- `ruta_nueva`: La nueva ruta de archivo.
- `cbr/id`: Identificador usado para encontrar la ruta.
- `ruta_anterior`: La ruta anterior del archivo.

## Resultado

El archivo `matches.csv` incluirá:

- `estado`: Estado de la búsqueda (`ENCONTRADO` o `NO ENCONTRADO`).
- `comentario`: Descripción del estado o motivo de la falta de coincidencia.
- `coincidencia`: Ruta donde se encontró la coincidencia (si aplica).
- `guardado_en`: Ruta relativa del directorio base donde se encontró la coincidencia.

## Ejemplo de Ejecución

```shell
python main.py
```

## Notas

- El archivo CSV de salida y la copia de las coincidencias estará en el mismo directorio donde se ejecuta el script.
