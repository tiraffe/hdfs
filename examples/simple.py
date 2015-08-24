#!/usr/bin/env python
# encoding: utf-8

"""Simple HdfsCLI example.

In this example, we show how to we can transfer some JSON-serialized data to
and from HDFS.

"""

from hdfs import Config
from json import dumps, loads


# Get the default alias' client.
client = Config().get_client()

# Some sample data.
weights = {
  'first_feature': 48,
  'second_feature': 12,
  # ...
}

# The path on HDFS where we will store the file.
path = 'static/weights.json'

# Store as JSON on HDFS.
data = dumps(weights)
client.write(path, data=data, overwrite=True)

# The file's HDFS status, we can use it to verify that all the data is there.
status = client.status(path)
assert status['length'] == len(data)

# Download the file back and check that the deserialized contents match.
with client.read(path) as reader:
  contents = reader.read().decode('utf-8')
  assert loads(contents) == weights
