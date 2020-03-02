import paramiko
import random
s = paramiko.SSHClient()
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
conn = s.connect("169.254.248.74", username ='pi', password='raspberry', port=22)
while True:
    z_error = random.randint(0, 5)

    command = 'cd /home/pi/Desktop/Synopsys2020/Drone \n echo "' +str(z_error)+ '" > file.txt'

    s.exec_command(command)

"""
Code to read error
F = open("file.txt","r")
        try:
           z_error = int(F.read())
        except:
           if F.read() == "done":
             
              sys.exit()
           z_error = 0
       
        print(z_error)
        F.close()
"""