'''
Created on 13 Dec 2013

This modules allows you to merge the content of a gpx and its associated hrm in a single tcx file.

It is highly inspired from http://colby.id.au/combining-gpx-and-hrm-files, but written in Python.

It could be done in a much nicer/modular way if time allowed.

@author: epot
'''

from thirdparty import hrmparser

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
        self.__gpx_file_path = gpx_file_path
        self.__hrm_file_path = hrm_file_path
    
    def convert(self, tcx_file_path):
        try:
            with open(self.__gpx_file_path, 'r') as gpx_file, \
                open(tcx_file_path, 'w') as tcx_file:
                polarClass = hrmparser.PolarClass()
                polarClass.LoadFromFile(self.__hrm_file_path)
                self.__convert(gpx_file, polarClass, tcx_file)
                
        except IOError as e:
            raise self.GpxHrmToTcxException("IOError: {}".format(e))
        
    def __convert(self, gpx_file, polarClass, tcx_file):
        tcx_file.write("<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\" ?>\n\
<TrainingCenterDatabase xmlns=\"http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2\"\
 xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\
 xsi:schemaLocation=\"http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2\
 http://www.garmin.com/xmlschemas/TrainingCenterDatabasev2.xsd\">\n")
        tcx_file.write("\n  <Activities>\n")
        sport = "Running"
        tcx_file.write("    <Activity Sport=\"{}\">\n".format(sport))
        
        