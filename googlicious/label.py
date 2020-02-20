#!/usr/bin/env python3
# encoding: utf-8
'''
label -- Find a document containing arbitrary text in Google Docs

googlicious.label finds documents with arbitrary text

@author:     Dimitry Dukhovny

@contact:    415-704-4547
@deffield    updated: 2020-02-12
'''

import sys
import os
import colorama
from optparse import OptionParser
import .filesearch

__all__ = []
__version__ = 0.1
__date__ = '2019-12-04'
__updated__ = '2019-12-04'


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
    #sys.stdout.write(outstring + '\n')
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
    #sys.stderr.write(outstring + '\n')
    print(colorama.Fore.RED + outstring + colorama.Style.RESET_ALL, file=sys.stderr, flush=True)


def main(argv=None):
    '''Command line options parsing.  Takes arrays and returns an integers.
    '''
    program_name = os.path.basename(sys.argv[0])
    program_version = __version__
    program_build_date = "%s" % __updated__

    program_version_string = '%%prog %s (%s)' % (program_version,
                                                 program_build_date)
    program_longdesc = '''Push host file to an AWS domain'''

    program_license = '''Copyright 2019 Dimitry Dukhovny'''

    if argv is None:
        argv = sys.argv[1:]
    try:
        # setup option parser
        parser = OptionParser(version=program_version_string,
                              epilog=program_longdesc,
                              description=program_license)
        parser.add_option("-v", "--verbose", dest="verbose",
                          action="store_true",
                          help="set verbosity level \
                          [default: %default]")
        parser.add_option("-a", "--auth", dest="auth",
                          action="store_true",
                          help="Set auth string location \
                          [default: %default]")
        parser.add_option("-s", "--searchtext", dest="searchtext",
                          action="store", type="string",
                          help="Text to search \
                          [default: %default]")
        parser.add_option("-g", "--fileglob", dest="fileglob",
                          action="store", type="string",
                          help="Limit search to these files \
                          [default: %default]")

        # set defaults
        parser.set_defaults(verbose=False)
        parser.set_defaults(auth=False)
        parser.set_defaults(searchtext='')
        parser.set_defaults(fileglob='*')

        # process options
        (opts, args) = parser.parse_args(argv)
        if args:
            more_files = args
        else:
            more_files = []

        # Handling our flags
        has_input = False
        has_domain = False
        if opts.auth:
            try:
                pass
            except:
                pass
        if opts.searchtext:
            try:
                opts.searchtext = str(opts.searchtext)
            except:
                pass
        if opts.fileglob:
            try:
                pass
            except:
                pass

    except Exception as e:
        indent = len(program_name) * " "
        sys.stderr.write(program_name + ": " + e + "\n")
        sys.stderr.write(indent + "  for help use --help\n")
        return(2)


if __name__ == '__main__':
    main(sys.argv)