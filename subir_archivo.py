import base64
import boto3

def lambda_handler(event, context):
    # Entrada (json)
    nombre_bucket = event['body']['bucket']
    directorio = event['body']['directorio'].strip('/')
    nombre_archivo = event['body']['nombre_archivo']
    contenido_b64 = event['body']['contenido_base64']

    # Proceso: el archivo llega codificado en base64 dentro del JSON
    contenido = base64.b64decode(contenido_b64)
    key = f"{directorio}/{nombre_archivo}" if directorio else nombre_archivo

    s3 = boto3.client('s3')
    s3.put_object(Bucket=nombre_bucket, Key=key, Body=contenido)

    # Salida
    return {
        'statusCode': 200,
        'mensaje': 'Archivo subido',
        'bucket': nombre_bucket,
        'key': key,
        'bytes': len(contenido)
    }
