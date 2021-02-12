# This script will copy snapshot with matching tags from "us-east-1" to "eu - central -1".

import boto3, json

session = boto3.Session(profile_name = 'development')

east1 = 'us-east-1'
central1 = 'eu-central-1'

ec2East = session.client('ec2', region_name = east1)
ec2Central = session.client('ec2', region_name = central1)
 
tag_match = ec2East.describe_snapshots ( Filters = [ {'Name': 'tag:Copy', 'Values': ['True'] } ] )
SnapshotIDs = []
snap = tag_match['Snapshots']
for i in snap:
    SnapshotIDs.append(i['SnapshotId'])
print('Target Snapshot ID: ', SnapshotIDs)

for j in SnapshotIDs:
    response = ec2Central.copy_snapshot(
        Description='This is my copied snapshot.',
        DestinationRegion = central1,
        SourceRegion = east1,
        SourceSnapshotId = j,
    )
print(response)