import boto3, json

session = boto3.Session(profile_name='development')
east = 'us-east-1'
west = 'us-west-2'

ec2East = session.client('ec2', region_name = east)


response = ec2East.describe_security_groups(
    Filters=[
        {
            'Name': 'ip-permission.cidr',
            'Values': [
                '0.0.0.0/0',
            ]
        },
        
        
    ],
)

sgs = response['SecurityGroups']
sgsWithOpenPorts = []

for i in sgs:
    
    sgsWithOpenPorts.append(i['GroupId'])

print(sgsWithOpenPorts)

# revoke 0.0.0.0/0 on port 443 for the given SGs in the list 
for i in sgsWithOpenPorts:
    ports = [80, 22, 443]
    for j in ports:

        response = ec2East.revoke_security_group_ingress(
            CidrIp='0.0.0.0/0',
            FromPort=j,
            GroupId= i,
            IpProtocol='tcp',
            ToPort=j,
    )