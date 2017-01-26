#!/bin/bash

export filelist=''

# Usually bamboo is directly accessible, remove proxy settings during test.
unset http_proxy
unset https_proxy

# To fetch bamboo artifacts, the bamboo base URL and project "short name" are required.
# $YOUR_BAMBOO_SITE
# $YOUR_BAMBOO_PROJ, this var can also be fetched from RESTful API from Bamboo query. Here we set to const in test.
# The test results are expected in XUnit format and named as "xunit.xml"
# for example, nose xunit plugin to generate an XML in XUnit format, or, Maven default result format.

for i in $(seq 100 193)
do
    echo "downloading Bamboo KW Regression Result for $YOUR_BAMBOO_PROJ-$i-xunit.xml"
    wget -v http://$YOUR_BAMBOO_SITE/browse/$YOUR_BAMBOO_PROJ-$i/artifact/shared/XUnit/xunit.xml -O $YOUR_BAMBOO_PROJ-$i-xunit.xml
    if [ "$?" -eq "0" ]; then
        filelist="$filelist ./$YOUR_BAMBOO_PROJ-$i-xunit.xml"
    else
        rm -f ./$YOUR_BAMBOO_PROJ-$i-xunit.xml
    fi
done

python ./reader/xunit_reader.py $filelist


