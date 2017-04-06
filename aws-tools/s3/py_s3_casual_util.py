#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'maxwu'

import boto
import boto.s3.connection


def s3_ls_bucket_contents(bucket):
    for key in bucket.list():
        print "{name}\t\t{size}\t\t{modified}".format(
            name=key.name,
            size=key.size,
            modified=key.last_modified,
        )


if __name__ == '__main__':
    conn = boto.connect_s3()
    buckets = conn.get_all_buckets()
    for bucket in buckets:
        print "--- {name}\t\t{created} ---".format(
            name=bucket.name,
            created=bucket.creation_date,
        )
        s3_ls_bucket_contents(bucket)


