#!/usr/bin/env python

import os
import re
import sys
import urllib

import numpy as np



def run_regression_test(test_1, test_2):
    pass

def fetch_regression_data(path, url):
    r"""
    Fetch the regression data from `url` storing it at path

    """
    """
    Fetch regression data from an archive on the Clawpack website: 
      http://www.clawpack.org/regression_data/TARFILE
    where TARFILE is a tarfile specific to this example (based on path within
    apps directory).

    To add new data to repository use the save_regression_data.py module.

    """
    
    # clawdir = os.environ['CLAW'] + '/'
    # thisdir = os.getcwd()
    # thisdir = thisdir.replace(clawdir,'')
    # if thisdir[0] == '/':
    #     raise Exception("This directory is not a subdirectory of clawdir = %s" \
    #              % clawdir)

    # tarfile = thisdir.replace('/','-') + '-' + target_dir + '.tar.gz'
    # regdir = target_dir + '_archived_results'

    # url = "http://www.clawpack.org/regression_data"

    # print "Trying to retrieve %s \n   from %s" % (tarfile, url)
    
    # Fetch file
    file_name = os.path.split(url)[-1]
    local_path = os.path.join(path, file_name)
    urllib.urlretrieve(url, local_path)

    # Untar the file if needed
    if os.path.splitext(file_name) == "gz" or  \
       os.path.splitext(file_name) == "tgz":

        subprocess.Popen("tar xvzf %s" % file_name, shell=True).wait()



    # try:     
    #     url = os.path.join(url, tarfile)
    #     urllib.urlretrieve(url, tarfile)
    #     if os.path.getsize(tarfile) < 500:
    #         os.system("mv %s tarfile_error.html" % tarfile)
    #         print "\n*** Error: See tarfile_error.html"
    #         raise Exception("*** Problem retrieving %s" % tarfile)
    # except:
    #     raise Exception("*** Problem retrieving %s" % tarfile)
    
    # try:
    #     os.system("tar -zxf %s" % tarfile)
    #     print "Regression data should be in ",regdir
    # except:
    #     raise Exception("*** Problem untarring %s" % tarfile)
    # return regdir, tarfile


def compare_tests(test1, test2):
    r"""Compare two tests `test1` and `test2`"""




def assert_solution_almost_equal(solution_1, solution_2, coarse=False):
    r"""Compare `solution_1` and `solution_2`

    Input
    -----
     - `solution_1` ()
     - `solution_2` ()
     - `coarse` (bool) - Only compare the coarsest level grids.  Default is 
       `False`

    Raises
    ------
    `AssertionError` (Exception) - 
    """

    raise NotImplementedError()


if __name__=="__main__":

    target_dir = sys.argv[1]

    try:
        regression_dir, tarfile = fetch_regression_data(target_dir)
    except:
        raise Exception("Error fetching regression data")
    
    print "\nDownloaded a tar file ", tarfile
    ans = raw_input("  Cleanup by removing? ")
    if ans.lower() in ['y','yes']:
        os.system("rm -rf %s" % tarfile)