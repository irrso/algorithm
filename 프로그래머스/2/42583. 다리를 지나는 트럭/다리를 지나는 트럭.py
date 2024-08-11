from collections import deque

def solution(bridge_length, weight, truck_weights):
    wait = deque(truck_weights)
    bridge = deque([0]*bridge_length)
    bridge_weight = 0

    ans = 0
    while(True):
    	if not wait and not bridge_weight:
    		break

    	bridge_weight -= bridge.popleft()

    	if wait and bridge_weight+wait[0] <= weight:
    		truck = wait.popleft()
    		bridge.append(truck)
    		bridge_weight += truck
    	else:
    		bridge.append(0)

    	ans +=1 

    return ans