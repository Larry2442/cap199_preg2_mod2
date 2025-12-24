# Solucion
import pandas as pd
import requests
import zipfile
import io

def obtener_datos():
    url = "https://github.com/robintux/Datasets4StackOverFlowQuestions/blob/master/Cancer_Pulmon.zip?raw=true"
    print("Descargando archivo...")
    response = requests.get(url)

    with zipfile.ZipFile(io.BytesIO(response.content)) as z:
        nombre_archivo = z.namelist()[0]
        with z.open(nombre_archivo) as f:
            df = pd.read_csv(f)

    return df

if __name__ == "__main__":
    df = obtener_datos()
    print("Dataset cargado exitosamente.")
    print(df.head())