# Packets are sent to different ports on a computer system based on the hash of their packet ID. The value of the hash is as given below: 
# Hash = mod (packet_id, numberOfPorts) where mod is the modulus operator and takes the mod of first operand by second operand. 
# The ports are numbered from 0 to (number of ports)-1, and a packet is initially sent to the port that has theport number equal to 
# the hash of its packet ID. Each port requires t seconds to process an arriving packet. If a port is currently processing a packet, 
# any arriving is rerouted to the next port number, and so on. The list of ports is circular. If a packet arrives at the last port 
# and it is busy, it is rerouted to the first port. Given a list IDs of n packets that arrive 1 per second, find the port to which each
# packet is finally sent. The first packet is sent at time t=1.
# Example
# numberOfPorts = 3
# transmissionTime = 2
# packetIds[4,7,10,6]
# The destination ports, assuming no time conflicts are all calculated as pacetIds[i] modulo numberOfPorts, so [1,1,1,0] in this case. 
# These arrive at times 1,2,3,4. The first packet is sent to port 1 with no conflicts. Port 1 will be occupied at times 1 and 2 due to 
# the trasmission time, so the second packet has a conflict and is sent to port 1+1=2. The third packet wants to go to port 1 and arrives
# at time 3. Since port 1 is no longer transmitting packet 1, it receives the third packet. The fourth packet goes to port 0 without
# conflicts. The return array is [1,2,1,0]
# Function Description
# Complete the sentTimes function in the editor below
# sentTimes has the following parameters: 
# int numberOfPorts: the number of ports in the system 
# int transmissionTime: the time for a port to send a packet
# int packetIds[n]: the IDs of the packets in the order in which they arrive 
# Returns
# int[n]: the ports to which the packets are sent 
# Restraints 
# 1 <= numberOfPorts <= 2000
# 1 <= transmissionTime <= 100
# 1 <= n <= 2000
# 1 <= packetIds[i] <= 10^5

# Sample case
# numberOfPorts = 4
# transmissionTime = 2
# packetIds[] size n = 3
# packetIds = [0,2,6]

# Sample output
# 0
# 2
# 3

# Explanation 
# According to the hashes, packets should be sent on ports 0,2 and 2 respectively. But packet 6 arrives at time 3, at which packet 2
# is in the process of being sent. Therefore it is sent to the next port. Return the array [0,2,3]. 

# Complete the function sentTimes below

# The function is expected to return an INTEGER_ARRAY
# The function accept the following parameters
#     INTEGER numberOfPorts
#     INTEGER transmissionTime
#     INTEGER_ARRAY packetIds

def sentTimes(numberOfPorts, transmissionTime, packetIds):
    # Write your code here
    
    ports = [0] * numberOfPorts
    
    result = []
    
    for pid in packetIds: 
        next_port = pid % numberOfPorts
        
        while ports[next_port] >= transmissionTime: 
            next_port = (next_port + 1) % numberOfPorts
        result.append(next_port)
        ports[next_port] += 1 
    
        return result

if __name__ == '__main__': 
    fptr = open(osenviron['OUTPUT_PATH'], 'w')

    numberOfPorts = int(input().strip())
    transmissionTime = int(input().strip())
    packetIds_count = int(input().strip())
    packetIds = []

    for _ in range(packetIds_count):
        packetIds_item = int(input().strip())
        packetIds.append(packetIds_item)

        result = sentTimes(numberOfPorts, transmissionTime, packetIds)

        fptr.write('\n'.join(map(str,result)))
        fptr.write('\n')

        fptr.close() 

