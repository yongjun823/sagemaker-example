import os
import io
import boto3
import json
import numpy as np

# grab environment variables
ENDPOINT_NAME = os.environ['ENDPOINT_NAME']
runtime= boto3.client('runtime.sagemaker')

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    
    data = json.loads(json.dumps(event))
    data = data['data']
    data = np.array(data, dtype=np.float32)
    
    payload = json.dumps({'inputs_input': data.tolist()})
    
    response = runtime.invoke_endpoint(EndpointName=ENDPOINT_NAME,
                                       ContentType='application/json',
                                       Body=payload)
    
    result = json.loads(response['Body'].read().decode())
    result = result['outputs']['activation_5']['floatVal']
    
    return result
    
