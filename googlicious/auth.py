#!/usr/bin/env python3
# encoding: utf-8
'''
auth -- Authenticate with Google using Oauth.

googlicious.auth provides an authenticator class and scriptable auth

@author:     Dimitry Dukhovny

@contact:    415-704-4547
@deffield    updated: 2020-02-13
'''

import sys
import os
import colorama
import pprint
from optparse import OptionParser
from pydrive.auth import GoogleAuth
from pydrive.settings import InvalidConfigError

__all__ = []
__version__ = 0.1
__date__ = '2020-02-13'
__updated__ = '2020-02-13'


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


class gauth:
    def __init__(self, verbose=0):
        self.gauth = None
        self.doauth()
        if verbose:
            self.report()

    def doauth(self):
        self.gauth = GoogleAuth()
        self.gauth.LocalWebserverAuth()

    def report(self):
        pprint.pprint(self.gauth.attr)


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
    program_longdesc = '''Authenticate against Google using Oauth.'''

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

        # set defaults
        parser.set_defaults(verbose=False)

        # process options
        (opts, args) = parser.parse_args(argv)
        if args[1:]:
            searchstring = ' '.join(args[1:])
        else:
            searchstring = []

        if opts.verbose:
            global verbose
            verbose = True

    except Exception as e:
        indent = len(program_name) * " "
        sys.stderr.write(program_name + ": " + e + "\n")
        sys.stderr.write(indent + "  for help use --help\n")
        halt(2, "Options error.")

    if opts.verbose:
        OUTERR('Started with opts %s and args %s' % (str(opts), str(searchstring)))
    try:
        g = gauth(verbose=opts.verbose)
    except InvalidConfigError:
        OUTERR('Probably failed to find client_secrets.json')
        OUTPUT('Visit:\n\thttps://console.cloud.google.com/apis/credentials?')
        OUTPUT('Create a project, authorize API access,\n and save the JSON file as client_secrets.json')
        halt(1, "Failed login in %s with options:  %s" % (str(os.getcwd()), str(opts.__dict__)))
    return(g)


if __name__ == '__main__':
    main(sys.argv)
