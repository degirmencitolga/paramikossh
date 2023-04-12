import paramiko
import time

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 


commands = client.invoke_shell()  #Interactive Shell

commands.send("show vesion \n")
time.sleep(1.5)

#output = commands.recv(nbytes)
output = output.decode("utf-8")
print (output)
