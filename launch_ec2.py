import boto3
def lauch_ec2(region, instance_id):
    for region in regions:
        
     ec2 = boto3.client( 'ec2', region_name = region)
     response=ec2.run_instance(
        ImageID = instance_id,
        MinCount = 1,
        MaxCount = 1
     )
     instance_id = response["Instance"][0]["InstanceId"]
     print(f"Instance launched in {region}: {instance_id}")
     
regions =("us-east-1","us-west-2")
image_ID= ""