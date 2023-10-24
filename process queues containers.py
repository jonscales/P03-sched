# process queus containers
New=[]
Read=[]
Running=[]
Wait=[]
Exit=[]

PCB =[] # process container block
TS=5 #time slice

class SysClock:
    def __init__(self):
        # increment clock
        #loop to decrement TS-=
        #reset TS at end of TS loop & initiate moves
        
        
        pass

class Queue:
    def __init__(self)
        queue =[]
    
    def addPCB(self,pcb):
        self.append(pcb)

    def removePCB(self):
        item = queue[0]
        del queue[0]
        return item
    def decrement(self):
        # for each process in queue
        #   call decrementIoBurst
    
class CPU:
    def __init__(self):
        self.busy =False
        self.runningPID =None

    def decrementCurrentProcess(self):
        self.runningPCB.decrementCpuBurst()
        pass

    def loadProcess(self,pcb):

        self.runningPCB =pcb
    def testMoveOffCPU(self):
        #if CPU time out - move to ready
        #if CPU burst 0 - move to io
        if self.runningPCB.getCurrentBurstTime() == 0:

            pass
        # move PCB off the CPU
        if 


class PCB:
    def __init__(self, pid, bursts):
        self.bursts=bursts
        self.pid = pid 
        self.currBurst ='CPU'
        self.currBurstIndex = 0
        self.cpuBurst = 5
        self.readyQueueTime = 0
        self.waitQueueTime = 0
        self.cpuTime = 0
    
    def decrementCpuBurst(self):
        self.bursts[self.currBurstIndex] -=1
    def decrementIoBursts(self):
        self.bursts[self.currBurstIndex] -=1
    def incrementBurstIndex(self):
        self.currBurstIndex -=1

    def getCurrentBurstTime(self):

if __name__ ='__main__':
    #each processor location is an instance of the Queue class
    # running is an instance of the CPU class
    new=Queue()
    ready=Queue()
    running=CPU()
    wait=Queue()
    exit=Queue()