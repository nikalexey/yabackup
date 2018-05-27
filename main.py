#!/usr/bin/env python
# coding: utf-8

import argparse
import os.path
import sys
from yadisk import YaDisk


def main():
    parser = argparse.ArgumentParser(description='Yandex Disk folder backup')
    parser.add_argument('-u', '--username', metavar='username', required=True, type=str, help='Yandex Disk user name')
    parser.add_argument('-p', '--password', metavar='password', required=True, type=str, help='Yandex Disk password')
    parser.add_argument('-y', '--ydfolder', metavar='ydfolder', required=False, type=str, help='Yandex Disk folder')
    parser.add_argument('folder', metavar='folder', type=str, help='Folder to backup')
    args = parser.parse_args()
    # check input
    if not os.path.isdir(args.folder):
        print('Error: folder \'{0}\' not found'.format(args.folder))
        sys.exit(-1)
    print('Folder for backup: {0}'.format(args.folder))
    files = [f for f in os.listdir(args.folder) if os.path.isfile(os.path.join(args.folder, f))]
    if args.ydfolder is None:
        args.ydfolder = ''
    else:
        args.ydfolder = args.ydfolder.strip('/')
    # Upload files
    disk = YaDisk(args.username, args.password)
    disk.mkdirs(args.ydfolder)
    for file in files:
        print('Upload file {0}...'.format(file), end='')
        sys.stdout.flush()
        if not disk.exist(args.ydfolder + '/' + file):
            disk.upload(os.path.join(args.folder, file), args.ydfolder + '/' + file)
            print('ok')
        else:
            print('skip, file exist')
        sys.stdout.flush()

if __name__ == '__main__':
    main()
