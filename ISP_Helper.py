import subprocess
import datetime

def ping_address(host,n):
    ping = subprocess.Popen(
       ["ping","-c",str(n),host],
       stdout = subprocess.PIPE,
       stderr = subprocess.PIPE)
    out,error = ping.communicate()
    return out,error

def parse_msg(msg):
    line = msg.split('\n')
    N = len(line)-2
    line = line[N]
    return line

def get_vals(msg):
    rhs = msg.split('=')
    try:
        nums = rhs[1].split('/')
        min_num = float(nums[0])
        ave_num = float(nums[1])
        max_num = float(nums[2])
        std_num = nums[3].split(' ')
        std_num = float(std_num[0])
    except:
        print("Could not Ping Website...")
        min_num = float('nan')
        ave_num = float('nan')
        max_num = float('nan')
        std_num = float('nan')
    return min_num, ave_num, max_num, std_num

def get_date_and_time():
    return datetime.datetime.now()
