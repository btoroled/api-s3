import boto3

def lambda_handler(event, context):
    # Entrada (json)
    nombre_bucket = event['body']['bucket']

    # Proceso
    s3 = boto3.client('s3')
    # us-east-1 no admite LocationConstraint
    s3.create_bucket(Bucket=nombre_bucket)

    # Salida
    return {
        'statusCode': 200,
        'mensaje': 'Bucket creado',
        'bucket': nombre_bucket
    }
