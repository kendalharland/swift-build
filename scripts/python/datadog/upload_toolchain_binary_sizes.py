import datadog
import os
import sys

dogstatsd_options = {
    'statsd_host':'127.0.0.1',
    'statsd_port':8125
}

def main():
    if len(sys.argv) < 1:
        print("missing input filename")
        sys.exit(os.EX_USAGE)
        
    print("Initializing datadog")
    datadog.initialize(**dogstatsd_options)

    binary_sizes_file = sys.argv[1:]
    print(f"Got binary sizes file {binary_sizes_file}")
