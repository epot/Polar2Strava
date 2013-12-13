'''
Created on 13 Dec 2013

@author: epot
'''

import os

from converter import gpxhrmtotcx

def main():
    data_path = os.path.join(os.path.dirname(__file__), 'data')
    gna = gpxhrmtotcx.GpxHrmToTcx(
          os.path.join(data_path, '13121201.gpx'), 
          os.path.join(data_path, '13121201.hrm'))
    gna.convert(os.path.join(data_path, '13121201.tcx'))

if __name__ == '__main__':
    main()