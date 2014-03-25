'''
Created on 13 Dec 2013

@author: epot
'''

import os
import argparse

from converter import gpxhrmtotcx

def scan(folder):
    for filepath in os.listdir(folder):
        filename, fileextension = os.path.splitext(filepath)
        gpx_file = os.path.join(folder, filepath)
        if os.path.isfile(gpx_file) and fileextension == '.gpx':  
            hrm_file = os.path.join(folder, '{}.hrm'.format(filename))
            tcx_file = os.path.join(folder, '{}.tcx'.format(filename))
            if not os.path.exists(tcx_file) and os.path.exists(hrm_file):
                converter = gpxhrmtotcx.GpxHrmToTcx(gpx_file, hrm_file)
                print 'converting {} and {} to {}'.format(os.path.join(folder, filepath), hrm_file, tcx_file)
                converter.convert(tcx_file)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--folder", help="Folder to scan")
    args = parser.parse_args()
    scan(args.folder)

if __name__ == '__main__':
    main()