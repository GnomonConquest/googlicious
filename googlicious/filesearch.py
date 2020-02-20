#!/usr/bin/env python3
# encoding: utf-8
'''
filesearch -- Find a document containing arbitrary text in Google Docs

googlicious.filesearch finds documents with arbitrary text

@author:     Dimitry Dukhovny

@contact:    415-704-4547
@deffield    updated: 2020-02-12
'''

import sys
import os
import colorama
from optparse import OptionParser
#from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from .auth import gauth


__all__ = []
__version__ = 0.1
__date__ = '2020-02-12'
__updated__ = '2020-02-12'


def OUTPUT(outstring=''):
    '''
    Simple output printer.
    Will halt the program if it fails to write to stdout.

    Args:
        outstring: a string or anything that can become one
    Returns:
        None
    '''
    try:
        outstring = str(outstring)
    except:
        outstring = ''
    print(colorama.Fore.GREEN + outstring + colorama.Style.RESET_ALL, file=sys.stdout, flush=True)


def OUTERR(outstring=''):
    '''
    Simple error printer.
    Will halt the program if it fails to write to stderr.

    Args:
        outstring: a string or anything that can become one
    Returns:
        None
    '''
    try:
        outstring = str(outstring)
    except:
        outstring = ''
    print(colorama.Fore.RED + outstring + colorama.Style.RESET_ALL, file=sys.stderr, flush=True)


class googler(gauth):
    def __init__(self, alldrives=0):
        if 'verbose' in globals():
            try:
                self.verbose = verbose
            except:
                self.verbose = True
        else:
            self.verbose = False
        self.gauth = None
        self.gdrive = None
        self.doauth()
        self.getdrive()
        self.driveId = ''
        if alldrives:
            self.alldrives = "true"
            self.corpora = "allDrives"
        else:
            self.alldrives = "false"
            self.corpora = "default"

#    def doauth(self):
#        try:
#            self.gauth = GoogleAuth()
#            self.gauth.LocalWebserverAuth()
#
#        except:
#            self.gauth = None
#        try:
#            self.drive = GoogleDrive(self.gauth)
#        except:
#            self.drive = None

    def getdrive(self):
        try:
            self.drive = GoogleDrive(self.gauth)
        except:
            self.drive = None

    def listall(self):
        '''
        List all Google Drive content.
        '''
        querydict = {
            "q": "",
            "corpora": self.corpora,
            "includeItemsFromAllDrives": self.alldrives,
            "supportsAllDrives": self.alldrives
        }
        if self.verbose:
            OUTERR("Google Drive Query:  %s" % (str(querydict)))
        filelist = self.drive.ListFile(querydict).GetList()
        googlefiles(filelist)

    def ls(self, titlestring="", searchstring=""):
        '''
        List Google Drive content by name or body text.
        '''
        querystring = "title contains '%s'" % (titlestring)
        if searchstring:
            querystring += " and fullText contains '%s'" % (str(searchstring))
        querydict = {
                "q": querystring,
                "corpora": self.corpora,
                "includeItemsFromAllDrives": self.alldrives,
                "supportsAllDrives": self.alldrives
        }
        if self.verbose:
            OUTERR("Google Drive Query:  %s" % (str(querydict)))
        filelist = self.drive.ListFile(querydict).GetList()
        googlefiles(filelist)


def googlefiles(gfilelist=[]):
    for file in gfilelist:
        print('title: {}, id: {}'.format(file['title'], file['id']))
    if 'verbose' in globals():
        if verbose:
            OUTERR("Found %d matching files." % (len(gfilelist)))


def halt(exitcode=0, finalthoughts=''):
    if finalthoughts:
        if exitcode:
            OUTERR('FATAL: %s' % (finalthoughts))
        else:
            OUTPUT(finalthoughts)
    sys.exit(exitcode)


def main(argv=None):
    '''Command line options parsing.  Takes arrays and returns an integers.
    '''
    program_name = os.path.basename(sys.argv[0])
    program_version = __version__
    program_build_date = "%s" % __updated__

    program_version_string = '%%prog %s (%s)' % (program_version,
                                                 program_build_date)
    program_longdesc = '''Search Google Drive for matching file names or body text.'''

    program_license = '''See LICENSE'''

    if argv is None:
        argv = sys.argv[1:]
    try:
        parser = OptionParser(version=program_version_string,
                              epilog=program_longdesc,
                              description=program_license)
        parser.add_option("-v", "--verbose", dest="verbose",
                          action="store_true",
                          help="set verbosity level \
                          [default: %default]")
        parser.add_option("-g", "--global", dest="alldrives",
                          action="store_true",
                          help="Search all shared drives or not \
                          [default: %default]")
        parser.add_option("-f", "--filename", dest="filename",
                          action="store", type="string",
                          help="Limit search to these files \
                          [default: %default]")

        # set defaults
        parser.set_defaults(verbose=False)
        parser.set_defaults(alldrives=False)
        parser.set_defaults(filename='')

        # process options
        (opts, args) = parser.parse_args(argv)
        if args[1:]:
            searchstring = ' '.join(args[1:])
        else:
            searchstring = []

        if opts.verbose:
            global verbose
            verbose = True
        if opts.filename:
            try:
                opts.filename = str(opts.filename)
            except:
                OUTERR('Could not stringify your file filter.')
                halt(255)

    except Exception as e:
        indent = len(program_name) * " "
        sys.stderr.write(program_name + ": " + e + "\n")
        sys.stderr.write(indent + "  for help use --help\n")
        halt(2, "Options error.")

    if opts.verbose:
        OUTERR('Started with opts %s and args %s' % (str(opts), str(searchstring)))
    try:
        g = googler(opts.alldrives)
        g.ls(titlestring=opts.filename, searchstring=searchstring)
    except:
        halt(1, "Failed query with options:  %s" % (str(opts.__dict__)))
    return(g)


if __name__ == '__main__':
    main(sys.argv)
