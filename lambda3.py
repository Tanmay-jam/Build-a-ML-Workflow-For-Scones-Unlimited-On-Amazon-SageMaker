import json
import ast

THRESHOLD = .8

def lambda_handler(event, context):
    # Grab the inferences from the event
    inferences = ast.literal_eval(event["inferences"])## TODO: fill in
    
    # Check if any values in our inferences are above THRESHOLD
    meets_threshold = ((inferences[0]>=THRESHOLD) or (inferences[1]>=THRESHOLD))## TODO: fill in
    
    # If our threshold is met, pass our data back out of the
    # Step Function, else, end the Step Function with an error
    if meets_threshold:
        pass
    else:
        raise("THRESHOLD_CONFIDENCE_NOT_MET")

    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }