import boto3
import urllib.request
import timeit
import datetime

MS_PER_SECOND = 1000

start = timeit.default_timer()
page = urllib.request.urlopen('https://google.com', timeout=2)
end = timeit.default_timer()

cloudwatch_client = boto3.client('cloudwatch')

cloudwatch_client.put_metric_data(
    Namespace="ConnMonitor",
    MetricData=[
        {
            'MetricName': 'Time to reach google (ms)',
            'Dimensions': [{
                'Name': 'Client',
                'Value': 'Local'
            }],
            'Timestamp': datetime.datetime.utcnow(),
            'Value': (end - start) * MS_PER_SECOND,
            'Unit': 'Milliseconds'
        }
    ]
)