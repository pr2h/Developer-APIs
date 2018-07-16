def hujambo():
    print '''
##################################################
# Tool    : nmap_to_xl_conv                      #
# Version : 1.1                                  #
# Coded with Python 2.7                          #
# Profile : https://github.com/pr2h/             #
# ######          #####   #                      #
# #    #  # ###  #     #  #                      #
# ######  ##         #    ######                 #
# #       #        #      #    #                 #
# #       #      #######  #    #                 #
##################################################
    '''
hujambo()

import time

start_time_moving_dots=time.time()
last_time=time.time()
number=1
total_number=800 # this value can be obtained from user / process
moving_dots='>'
percentage=(450000/total_number)*0.0001
round_off_to=2

while number<=total_number:
    time_left=((last_time-start_time_moving_dots)/((number*percentage)+1))*((total_number*percentage)-(number*percentage))
    time_left=round(time_left,round_off_to)

    number_of_moving_dots=int(number*percentage)
    number_of_blanks=int((total_number*percentage)-number_of_moving_dots)
    completed_percentage=round((number*percentage*100)/(total_number*percentage),round_off_to)
    
    print("\r["+(moving_dots*number_of_moving_dots)+' '*number_of_blanks+'] '+str(completed_percentage)+'%'+' , Time left: '+str(time_left)+' s '), 
    last_time=time.time()
    number+=1
    time.sleep(0.3)
