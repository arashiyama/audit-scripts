import boto3

# Connect to the S3 service
s3 = boto3.client('s3')

# List all of the buckets in the account
response = s3.list_buckets()
buckets = response['Buckets']

# Iterate through the buckets and check their permissions
for bucket in buckets:
  bucket_name = bucket['Name']

  # Get the bucket's ACL
  acl = s3.get_bucket_acl(Bucket=bucket_name)

  # Check if the ACL grants any excess permissions
  grants = acl['Grants']
  for grant in grants:
    permission = grant['Permission']
    if permission == 'FULL_CONTROL':
      print(f'Bucket {bucket_name} has excess permissions: {permission}')
    elif permission == 'WRITE':
      print(f'Bucket {bucket_name} has excess permissions: {permission}')
    elif permission == 'WRITE_ACP':
      print(f'Bucket {bucket_name} has excess permissions: {permission}')
    elif permission == 'READ_ACP':
      print(f'Bucket {bucket_name} has excess permissions: {permission}')

