from datetime import datetime
import os
import sys
import time

# There are a lot of datadog python libraries.
# This one is https://github.com/DataDog/datadogpy
import datadog
import datadog_api_client
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.metrics_api import MetricsApi
from datadog_api_client.v2.model.metric_intake_type import MetricIntakeType
from datadog_api_client.v2.model.metric_payload import MetricPayload
from datadog_api_client.v2.model.metric_point import MetricPoint
from datadog_api_client.v2.model.metric_resource import MetricResource
from datadog_api_client.v2.model.metric_series import MetricSeries

def main():
    if len(sys.argv) < 4:
        sys.exit(os.EX_USAGE)

    binary_sizes_file = sys.argv[1]     
    api_key = sys.argv[2]
    app_key = sys.argv[3]
    print(api_key)
    print(app_key)

    print("Initializing datadog")
    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = api_key
    configuration.api_key["appKeyAuth"] = app_key
    
    body = MetricPayload(
        series=[
            MetricSeries(
                metric="example.gauge.1",
                type=MetricIntakeType.UNSPECIFIED,
                points=[ [ int(time.time()), 17] ],
                # tags=["env:debug"],
                resources=[
                  MetricResource(
                        name="dummyhost",
                        type="host",
                    ),
                ],
            )
        ]
    )

    print("Sending metrics to datadog")
    with ApiClient(configuration) as api_client:
        api_instance = MetricsApi(api_client)
        response = api_instance.submit_metrics(body=body)
        print(response)

main()