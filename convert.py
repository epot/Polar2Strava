'''
Created on 13 Dec 2013

@author: epot
'''

import os
import argparse
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders

from converter import gpxhrmtotcx


def send_mail(send_from, send_to, subject, text, files=[], server="localhost"):
    assert type(send_to)==list
    assert type(files)==list

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach( MIMEText(text) )

    for f in files:
        part = MIMEBase('application', "octet-stream")
        part.set_payload( open(f,"rb").read() )
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f))
        msg.attach(part)

    smtp = smtplib.SMTP(server)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()

def upload_to_strava(email_from, new_tcx_files):
    if email_from and new_tcx_files:
        send_mail(email_from, ["upload@strava.com"], "Upload", "", new_tcx_files)

def scan(folder, email_from):
    new_tcx_files = []
    for filepath in os.listdir(folder):
        filename, fileextension = os.path.splitext(filepath)
        gpx_file = os.path.join(folder, filepath)
        if os.path.isfile(gpx_file) and fileextension == '.gpx':  
            hrm_file = os.path.join(folder, '{}.hrm'.format(filename))
            tcx_file = os.path.join(folder, '{}.tcx'.format(filename))
            if not os.path.exists(tcx_file) and os.path.exists(hrm_file):
                converter = gpxhrmtotcx.GpxHrmToTcx(gpx_file, hrm_file)
                print 'converting {} and {} to {}'.format(os.path.join(folder, filepath), hrm_file, tcx_file)
                try:
                    converter.convert(tcx_file)
                    new_tcx_files.append(tcx_file)
                except gpxhrmtotcx.GpxHrmToTcx.GpxHrmToTcxException as e:
                    print "Conversion failed: {}".format(e)
                
    upload_to_strava(email_from, new_tcx_files)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--folder", help="Folder to scan")
    parser.add_argument("-e", "--email", help="If this is set, then an email will be sent to Strava with new results (needs a smtp server on localhost).")
    args = parser.parse_args()
    scan(args.folder, args.email)

if __name__ == '__main__':
    main()