import boto3
import argparse
from botocore.handlers import disable_signing
resource = boto3.resource('s3')
resource.meta.client.meta.events.register('choose-signer.s3.*', disable_signing)
parser = argparse.ArgumentParser()
parser.add_argument("-b", "--bucket",
                    dest="bucket",
                    help="The s3 bucket name",
                    action='store',
                    required=True)
args = parser.parse_args()
bucket_name = args.bucket
myBucket = resource.Bucket(bucket_name)
    
fileCounter = 0
with open('s3_list.txt', 'w') as f:
    for my_bucket_object in myBucket.objects.all():
        f.write(my_bucket_object.key + " " + str(my_bucket_object.size) + '\n')
        fileCounter += 1
        if fileCounter % 50 == 0:
            print(f"Filenames saved so far: {fileCounter}")
print(f"Total files saved: {fileCounter}")