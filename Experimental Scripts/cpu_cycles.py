import os
import datetime


N = 100


outputFile = open('cpu_secp256r1_RPi.csv', 'w')
outputFile.write("CPU Cycles" + ';')
outputFile.write("CPU instructions" + ',' + '\n')

# Send a command to the linux terminal and return its response
def terminal(cmd):
	return os.popen(cmd).read()




for i in range(N):
	print(i)
	raw = terminal('sudo perf stat -e cycles,instructions ~/PQC/venv/bin/python secp2561.py 2>&1 | grep -E "cycles|instructions"').strip().split()
	cycle = raw[0]
	instruct = raw[2]
	outputFile.write(str(cycle) + ';')
	outputFile.write(str(instruct) + '\n')
	
	


outputFile = open('cpu_kyber512_Rpi.csv', 'w')
outputFile.write("CPU Cycles" + ';')
outputFile.write("CPU instructions" + ',' + '\n')


for i in range(N):
	print(i)
	raw = terminal('sudo perf stat -e cycles,instructions ~/PQC/venv/bin/python kem.py 2>&1 | grep -E "cycles|instructions"').strip().split()
	cycle = raw[0]
	instruct = raw[2]
	outputFile.write(str(cycle) + ';')
	outputFile.write(str(instruct) + '\n')
	
	
	
outputFile = open('cpu_x25519_Rpi.csv', 'w')
outputFile.write("CPU Cycles" + ';')
outputFile.write("CPU instructions" + ',' + '\n')


for i in range(N):
	print(i)
	raw = terminal('sudo perf stat -e cycles,instructions ~/PQC/venv/bin/python x25519.py 2>&1 | grep -E "cycles|instructions"').strip().split()
	cycle = raw[0]
	instruct = raw[2]
	outputFile.write(str(cycle) + ';')
	outputFile.write(str(instruct) + '\n')
	
