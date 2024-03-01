import os
import datetime


N = 100000


outputFile = open('cpu_secp256r1_MiniPC.csv', 'w')
outputFile.write("CPU Cycles" + ';')
outputFile.write("CPU instructions" + ',' + '\n')

# Send a command to the linux terminal and return its response
def terminal(cmd):
	return os.popen(cmd).read()




for i in range(N):
	#raw = terminal('sudo perf stat -e cycles ../venv/bin/python x25519.py 2>&1 | grep "cycles"').strip().split()
	raw = terminal('sudo perf stat -e cycles,instructions ../venv/bin/python secp2561.py 2>&1 | grep -E "cycles|instructions"').strip().split()
	cycle = raw[0]
	instruct = raw[2]
	outputFile.write(str(cycle) + ';')
	outputFile.write(str(instruct) + '\n')
	print(i)
	


outputFile = open('cpu_kyber512_MiniPC.csv', 'w')
outputFile.write("CPU Cycles" + ';')
outputFile.write("CPU instructions" + ',' + '\n')






for i in range(N):
	#raw = terminal('sudo perf stat -e cycles ../venv/bin/python x25519.py 2>&1 | grep "cycles"').strip().split()
	raw = terminal('sudo perf stat -e cycles,instructions ../venv/bin/python kem.py 2>&1 | grep -E "cycles|instructions"').strip().split()
	cycle = raw[0]
	instruct = raw[2]
	outputFile.write(str(cycle) + ';')
	outputFile.write(str(instruct) + '\n')
	print(i)