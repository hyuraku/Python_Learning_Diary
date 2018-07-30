import subprocess

#run cmd by python program
subprocess.run(['ls','-al'])

# To pipe
p1 = subprocess.Popen(['ls','-al'],stdout=subprocess.PIPE)
p2 = subprocess.Popen(['grep','csv'],stdin=p1.stdout,stdout=subprocess.PIPE)
p1.stdout.close()
output = p2.communicate()[0]
print(output)
