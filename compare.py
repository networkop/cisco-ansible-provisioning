#!/usr/bin/python
#coding: utf-8 -*-

import os.path

DEVICES = ['BR-1-AS01', 'BR-1-AS02', 'BR-1-AS03', 'BR-1-CORE', 'BR-1-WAN-1', 'BR-1-WAN-2', 'DC-CORE', 'DC-TOR', 'DC-WAN-1', 'DC-WAN-2']
EXTENSIONS = ['conf', 'mgmt', 'wan-qos', 'accces-ports', 'vlan']
ORIGINAL_EXT = 'original'
DIRECTORY = './files/'
IGNORE_LINES = ('!', '#', 'username', 'Building configuration', 'Current configuration', 'version')

def merge(device_name):
    result = ''
    for ext in EXTENSIONS:
        result += read_file_text(device_name, ext)
    return result

def compare(merged, original, direction):
    found_error = False
    for line in merged.splitlines():
        if not line.strip().startswith(IGNORE_LINES):
            if line.strip() not in original:
                print "ORIGNAL " + direction + " MERGED : " + line
                found_error = True
    if not found_error:
        print "NO INCONSISTENCIES FOUND BETWEEN ORIGINAL " + direction + " MERGED "

def read_file_text(device_name, extension):
    file_name = DIRECTORY + device_name + "." + extension
    if os.path.isfile(file_name):
        file_object = open(file_name, 'r')
        return file_object.read()
    return ''

def main():
    for device_name in DEVICES:
        print "COMPARING " + device_name
        merged_config = merge(device_name)
        print "##################"
        original_config = read_file_text(device_name, ORIGINAL_EXT)
        compare(merged_config, original_config, "<-")
        print "----------------"
        compare(original_config, merged_config, "->")
        print "##################"



if __name__ == "__main__":
  main()

