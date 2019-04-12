#!/usr/bin/python

'''

Main file for running blender binary together with a (optional) model file.

'''

import os
from subprocess import Popen

def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

import argparse
parser = argparse.ArgumentParser(description='Main file for starting up blender with a (optional) model file.')
parser.add_argument('blender_binary', type=str, help='Path to blender binary')
parser.add_argument('--model_file', type=str, default=None, help='Model file for specifying blender environment')
parser.add_argument('--windowless', type=str2bool, nargs='?',
                    const=True, default=False,
                    help="Activate nice mode.")
parser.add_argument('--dry_run', type=str2bool, nargs='?',
                    const=True, default=False,
                    help='Prints subprocess command without running')
args = parser.parse_args()

def main():
    if not os.path.isfile(args.blender_binary):
        print('Blender executable {} is not a file! Returning..'.format(args.blender_binary))
        return

    cmd = '{}'.format(args.blender_binary)
    if args.windowless:
        cmd += ' --background'
    if args.model_file is not None:
        if os.path.isfile(args.model_file):
            cmd += ' --python {}'.format(args.model_file)
        else:
            print('{} is not a valid file! Proceeding without..'.format(args.model_file))

    if args.dry_run:
        print('DRY RUN')
        print('{}'.format(cmd))
    else:
        proc = Popen(cmd, shell=True)
        proc.wait()
    print('Done!')

if __name__ == '__main__':
    main()
