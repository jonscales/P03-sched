timeSlice = 10
from rich import print

class Queue:
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ",".join(self.queue)

    def addPCB(self,pcb):
        self.queue.append(pcb)
    
    def removePCB(self):
        item = self.queue[0]
        del self.queue[0]
        return item

    def decrement(self):
        """ Iterate over the self.queue and decrement or call whatever
            method for each of the pcb's in this queue
        """
        # for each process in queue
        #    call decrementIoBurst
        pass
    
    def incrememnt(self,what='waittime'):
        """ Iterate over the self.queue and decrement or call whatever
            method for each of the pcb's in this queue
        """
        # for each process in queue
        #    call incrementwaittime
        if what =='waittime':
            pass
        elif what == 'runtime':
            pass
        pass

class SysClock:
    _shared_state = {}
    def __init__(self):
        self.__dict__ = self._shared_state
        if not 'clock' in self.__dict__: 
            self.clock = 0
    

class CPU:
    def __init__(self):
        self.busy = False
        self.runningPCB = None

    def decrementCurrentProcess(self):
        self.runningPCB.decrementCpuBurst()
    
    def loadProcess(self,pcb):
        self.runningPCB = pcb

    def testKickOff(self):
        if self.runningPCB.getCurrentBurstTime() == 0:
            pass
            # kick it off the cpu

class PCB:
    def __init__(self,at,pid,priority,cpubursts,iobursts):
        self.pid = pid     
        self.priority = priority     # 0
        self.arrivalTime = at
        self.cpubursts = cpubursts    # 5 3  2 2  2 3  3 3 3 2 3 3 4 2 5 2 5 3 3 3 4
        self.iobursts=iobursts
        self.currBurst = 'IO'
        self.currBurstIndex = 1
        self.cpuBurst = 5
        self.readyQueueTime = 0
        self.waitQueueTime = 0
        self.cpuTime = 0

    def decrementCpuBurst(self):
        self.bursts[self.currBurstIndex] -= 1

    def decrementIoBurst(self):
        self.bursts[self.currBurstIndex] -= 1

    def incrementBurstIndex(self):
        self.currBurstIndex += 1
    
    def getCurrentBurstTime(self):
        return self.bursts[self.currBurstIndex]
    
    def __str__(self):
        return f'AT: {self.arrivalTime}, PID: {self.pid}, Priority: {self.priority}, CPU: {self.cpubursts}, IO: {self.iobursts}'
    
class Simulator:
    def __init__(self,datfile):
        self.datfile = datfile
        self.new = Queue()
        self.wait = Queue()
        self.running = CPU()
        self.ready = Queue()
        self.terminated = Queue()
        self.readData()

    def __str__(self):
        s = ""
        s += "datfile: "+self.datfile +"\n"
        s += "new queue: "+",".join(self.new)  +"\n"
        s += "wait: "+",".join*(self.wait)  +"\n"
        return s


    def readData(self):
        with open(self.datfile) as f:
            self.data = f.read().split("\n")
        processes = {}
        pn=0
        for process in self.data:
            pn+=1
            if len(process) > 0:
               
                parts = process.split(' ')
                arrival = parts[0]
                pid = parts[1]
                priority = parts[2]
                bursts = parts[3:]  # gets everything else in the process list
                # parse bursts into CPU & IO
                cpubursts=[]
                iobursts=[]
                
                for i in range(len(bursts)):
                    if i%2==0:
                        cpubursts.append(bursts[i])
                    else:
                        iobursts.append(bursts[i])
                pcb_key=f'pcb-{pn}'
                processes[pcb_key]=[PCB(arrival,pid,priority,cpubursts,iobursts)]
                
        for pcb_key, pcb_instances in processes.items():
            for pcb_instance in pcb_instances:
                print(f"{pcb_key}: {pcb_instance}")

                #print(f"{arrival}, {pid}, {priority} {len(bursts)}{cpubursts}{iobursts}")


if __name__=='__main__':
    sim = Simulator("datafile.dat")
   # print(sim)