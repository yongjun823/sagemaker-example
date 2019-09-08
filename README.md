# Sagemaker Training & Hyper parameter tuning

1. Tensorflow Keras (CIFAR 10 dataset)
2. AWS Lambda & API Gateway

## test
URL: https://ovtuhal0e9.execute-api.us-west-2.amazonaws.com/stage1/predictsage  
METHOD: POST  
Headers:  
    content-type: application/json  
BODY:  
{
   "data": {(n, 32, 32, 1) shape numpy list}
}

## python code test
``` python
import requests
import json 
import numpy as np

data = np.random.randn(1, 32, 32, 3)
payload = {'data': data.tolist()}

URL = 'https://ovtuhal0e9.execute-api.us-west-2.amazonaws.com/stage1/predictsage'
headers = {'Content-Type': 'application/json; charset=utf-8'} 
res = requests.post(URL, headers=headers, data=json.dumps(payload))

result = res.json()

print(result)

```

## ARC test
https://drive.google.com/open?id=1Yud54L57qBW3PdFXwtaom-AsiOk7hxyJ

## slide
https://docs.google.com/presentation/d/1scP2qZRXUuaNUXUulHOK_rhnnaaSbAeoqka8hr-GgkA/edit#slide=id.g627cd6fe37_0_6

## reference
https://github.com/awslabs/amazon-sagemaker-examples/tree/master/sagemaker-python-sdk/tensorflow_keras_cifar10
https://github.com/awslabs/amazon-sagemaker-examples/blob/master/hyperparameter_tuning/tensorflow_mnist/
https://docs.aws.amazon.com/ko_kr/sagemaker/latest/dg/automatic-model-tuning-monitor.html
