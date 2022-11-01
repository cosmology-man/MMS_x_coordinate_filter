# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 11:21:28 2020

@author: Asha
"""


# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 15:00:16 2020

@author: Asha
"""
import urllib.request as uq
import os
from spacepy import pycdf
import numpy as np

#Open fgm file list
##The 'r' in the f open() function is 'read mode'
#f = open('/users/asha/desktop/fgm_new.txt', 'r')
f = open('/home/aafshari/scratch/fgm_new.txt', 'r')
fgmurl = []
for i in f.readlines():
    youmst = i.rstrip('\n')
    fgmurl.append(youmst)
f.close


for i in range(0, int(len(fgmurl))):
##    i is the placeholder for where you are in fgmurl
##    fgmdownload is the path where file is temporarily downloaded
    #fgmdownload = '/users/asha/desktop/checkmate/' + fgmurl[i][74:]
    fgmdownload = '/home/aafshari/scratch/checkmate/' + fgmurl[i][74:]
    uq.urlretrieve(fgmurl[i], fgmdownload)

    #fgm file
    fgm = fgmdownload
    
    fgmfile = pycdf.CDF(fgm)
    
    fgm = fgmfile['mms1_fgm_r_gse_brst_l2'][...]
    fgm = np.array(fgm)
    fgm = np.average(fgm)
        
    if fgm > 0:
##        The 'a' in the a_file open() function is 'append mode'       
        #a_file = open('/users/asha/desktop/dates.txt', 'a')
        a_file = open('/home/aafshari/scratch/dates.txt', 'a')
        n = a_file.write(fgmurl[i][74:]+'\n')
        a_file.close()
        fgmfile.close()
        os.remove(fgmdownload)
#        print('pass')
        if os.path.isdir('/home/aafshari/scratch/logs/') is True:
             #g = open('/users/asha/desktop/logs/log_x.txt', 'a+')
             g = open('/home/aafshari/scratch/logs/log_x_coordinate_filter.txt', 'a+')
             g.write(str('\n'+str(i)+'\n'+'beginning download'+'\n'+'pass'+'\n'))
             g.close()
        else:
            #os.mkdir('/users/asha/desktop/logs/')
            #g = open('/users/asha/desktop/logs/log_x.txt', 'a+')
            os.mkdir('/home/aafshari/scratch/logs/')
            g = open('/home/aafshari/scratch/logs/log_x_coordinate_filter.txt', 'a+')
            g.write(str('\n'+str(i)+'\n'+'beginning download'+'\n'+'pass'+'\n'))
            g.close()
        
    else:
        fgmfile.close()
        os.remove(fgmdownload)
        if os.path.isdir('/home/aafshari/scratch/logs/') == True:
            #f = open('/users/asha/desktop/logs/log_x.txt', 'a+')
            f = open('/home/aafshari/scratch/logs/log_x_coordinate_filter.txt', 'a+')
            f.write('\n'+'fail'+'\n')
            f.close()
        else:
            #os.mkdir('/users/asha/desktop/logs/')
            #f = open('/users/asha/desktop/logs/log_x.txt', 'a+')
            os.mkdir('/home/aafshari/scratch/logs/')
            f = open('/home/aafshari/scratch/logs/log_x_coordinate_filter.txt', 'a+')
            f.write('\n'+'fail'+'\n')
            f.close()