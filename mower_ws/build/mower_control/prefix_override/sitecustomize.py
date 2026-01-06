import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/ytrobot/Dev/neomower/mower_ws/install/mower_control'
