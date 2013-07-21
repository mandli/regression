#!/usr/bin/env python

import os
import shutil
import tempfile

import tools

def test_fetch_regression_data(url, data_strings):
    
    # Create temporary directory for fetch data
    path = tempfile.mkdtemp()

    try:
        # Call function
        tools.fetch_regression_data(path, url)

        # Open fetched file and check for contents
        fetched_file = open(os.path.join(path,'fetch-test.data'),'r')
        for (i,line) in enumerate(fetched_file):
            # print url
            # print line
            # print data_strings[i]
            assert line == data_strings[i]
    except AssertionError as e:
        e.message = "Failed URL: %s" % url
        raise e
    finally:
        # Cleanup
        shutil.rmtree(path)

if __name__ == "__main__":
    test_urls = ["http://users.ices.utexas.edu/~kyle/fetch-test.data",
                 "http://users.ices.utexas.edu/~kyle/fetch-test.tgz",
                 "http://users.ices.utexas.edu/~kyle/fetch-test.tar.gz"]
    data_strings = ["my test data", "1.0 2.0 3.0", "pickles"]
    for url in test_urls:
        test_fetch_regression_data(url, data_strings)
