import json
import sagemaker
import base64
from sagemaker.serializers import IdentitySerializer

# Fill this in with the name of your deployed model
ENDPOINT = "image-classification-2023-10-15-09-28-38-338"## TODO: fill in


def lambda_handler(event, context):
    # Decode the image data
    image = base64.b64decode(event['image_data'])

    # Instantiate a Predictor
    predictor = sagemaker.predictor.Predictor(ENDPOINT)## TODO: fill in

    # For this model the IdentitySerializer needs to be "image/png"
    predictor.serializer = IdentitySerializer("image/png")
    
    # Make a prediction:
    inferences = predictor.predict(image)## TODO: fill in
    
    # We return the data back to the Step Function    
    event["inferences"] = inferences.decode('utf-8')
    return {
  "image_data": event['image_data'],
  "s3_bucket": "final-project-04",
  "s3_key": "test/bicycle_s_000513.png",
  "inferences": event["inferences"]
}
    
