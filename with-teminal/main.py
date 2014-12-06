from initialize import * 
from function import *
import os  
def main():
    while 1:
        print '1 => upload file'
        print '2 => list of files'
        print '3 => exit'
        print '4 => clear'
        number = raw_input('Choose : ').strip()
        if number == '1':
            upload(drive_service)
        elif number == '2':
            read(drive_service)
        elif number == '3':
            exit()
        elif number == '4':
            os.system('clear')    
        else:
            print 'You should choose 1, 2, 3 or 4'

if __name__ == '__main__':
   main()