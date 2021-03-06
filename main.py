
import ISP_Helper as isp
import Host_Names as hn
import os
import platform

use_windows = 0
if platform.system()=="Windows":
    use_windows = 1
host = hn.get_hosts()
num_tries = 30

if not os.path.exists('Data'):
    os.makedirs('Data')

now = isp.get_date_and_time()
fid = open('Data/'+str(now.year)+'_'+str(now.month)+'_'+str(now.day)+'_'
          +str(now.hour)+'_'+str(now.minute)+".txt","w")
fid.write(str(now)+'\n')
fid.write("Website,min_time,ave_time,max_time,std_time ms\n")

for k in range(len(host)):
    if use_windows == 0:
        out,error = isp.ping_address(host[k],num_tries)
    else:
        out,error = isp.ping_address_windows(host[k],num_tries)
    msg = isp.parse_msg(out)
    if use_windows == 0:
        min_val, ave_val, max_val, std_val = isp.get_vals(msg)
    else:
        min_val, ave_val, max_val, std_val = isp.get_vals_windows(msg)
    line = (host[k] +','+ str(min_val) +','+ str(ave_val) +','
           + str(max_val) +','+ str(std_val) + '\n')
    fid.write(line)
    print line
fid.close()

