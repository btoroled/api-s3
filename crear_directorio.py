import boto3

def lambda_handler(event, context):
    # Entrada (json)
    nombre_bucket = event['body']['bucket']
    directorio = event['body']['directorio'].strip('/')

    # Proceso: en S3 un "directorio" es un objeto vacío cuya key termina en "/"
    s3 = boto3.client('s3')
    s3.put_object(Bucket=nombre_bucket, Key=directorio + '/')

    # Salida
    return {
        'statusCode': 200,
        'mensaje': 'Directorio creado',
        'bucket': nombre_bucket,
        'directorio': directorio + '/'
    }
