'''
Created on 13 Dec 2013

This modules allows you to merge the content of a gpx and its associated hrm in a single tcx file.

It is highly relies on http://colby.id.au/combining-gpx-and-hrm-files.

It could be done in a much nicer/modular way (with xsl transformation) if time allows.

@author: epot
'''

import subprocess
import shlex
import os

class GpxHrmToTcx(object):
    '''
    classdocs
    '''
    class GpxHrmToTcxException(Exception):
        '''
        Exception raised if the conversion went wrong.
        '''
        pass

    def __init__(self, gpx_file_path, hrm_file_path):
        '''
        Constructor
        @param gpx_file_path: path of the gpx file
        @param hrm_file_path: path of the hrm file
        '''
        self.__gpx_file_path = os.path.abspath(gpx_file_path)
        self.__hrm_file_path = os.path.abspath(hrm_file_path)
    
    def convert(self, tcx_file_path):
        try:
            awk_file = os.path.join(os.path.dirname(__file__), 'thirdparty', 'gpx2tcx.awk')
            cmd = 'awk -f {} -v HRMFILE={} {} > {}'.format(
                    awk_file, self.__hrm_file_path,self.__gpx_file_path, os.path.abspath(tcx_file_path))
            print "slip"
            print cmd
            print "slip"
            subprocess.check_call(cmd, shell=True)
                
        except (subprocess.CalledProcessError, OSError) as e:
            raise self.GpxHrmToTcxException("CalledProcessError: {}".format(e))
        
        