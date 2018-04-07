import _thread
import hashlib
import time
import sys

NACL = 'yhbG'
HASH = 'f2b31b3a7a7c41093321d0c98c37f5ad' #This is test hash
FINAL = 'No good'

def computehash( string, cont ):
    if HASH == hashlib.md5(str(string+NACL).encode()).hexdigest():
        print('Success!\n'+string+'\n')
        FINAL = string
        cont[0] = False
    print('Done')


#Compute file name from arg.  If invalid number of args, use 'infile.txt' as file name
argList = sys.argv
if len(argList) == 2:
    print( 'Need fewer arguments next time.')
    infileName = argList[1]
else:
    infileName = 'input.txt'
print('Input file name:', infileName)
time.sleep(1.5)




#Open file and turn into array
f = open(infileName, 'r')
print('Converting file to array...')
f = f.read().split('\n')





#MEAT of the script
cont = [True]
for i in range(0, len(f)):
    if cont[0]:
        print('Spinning', i)
        _thread.start_new_thread( computehash, (f[i], cont )) #Starts the reminder thread
    else:
        break

print('Now waiting...')
minutes = 0
while cont[0]:
    time.sleep(60)
    minutes += 1
    print('Minutes passed:', minutes)

print(FINAL)
