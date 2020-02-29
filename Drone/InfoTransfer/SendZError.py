import paramiko

s = paramiko.SSHClient()
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
conn = s.connect("169.254.231.124", username ='pi', password='Greeny25448', port=22)

z_error = 5

command = 'cd /home/pi/Desktop/Synopsys2020/ \n echo "' +str(z_error)+ '" > file.txt'

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