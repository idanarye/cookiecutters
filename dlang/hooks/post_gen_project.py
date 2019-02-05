#!/usr/bin/python3

import json

from plumbum import local

local['dub']['init']['-n']()

with open('dub.json') as f:
    dub_json = json.load(f)

dub_json['name'] = 'app'
dub_json['versions'] = ['notrace', 'dlang_version_2_066']
dub_json['buildRequirements'] = ['silenceDeprecations']
dub_json['excludedSourceFiles'] = ['source/weka/lib/stats/tools/raw_stats_file_tool.d',
                                   'source/weka/core_collector/core_collector.d',
                                   'source/weka/core_collector/collector_test.d',
                                   'source/weka/core_collector/collector_server.d']

with open('dub.json', 'w') as f:
    json.dump(dub_json, f, indent=4)

local['dfmt']['--inplace']('source/app.d')
