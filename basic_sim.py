timeSlice = 10
from rich import print
from rich.text import Text

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
        self.priority = priority     
        self.arrivalTime = at
        self.cpubursts = cpubursts    
        self.iobursts=iobursts
        self.currBurst = 'IO'
        self.currBurstIndex = 0
        self.currCpuBurst = cpubursts[0]
        self.currIoBurst =iobursts[0]
        self.readyQueueTime = 0
        self.waitQueueTime = 0
        self.cpuTime = 0
        self.ioTime =0
        self.noCpuBursts =len(cpubursts)
        self.noIoBursts =len(iobursts)

    def decrementCpuBurst(self):
        self.bursts[self.currBurstIndex] -= 1

    def decrementIoBurst(self):
        self.bursts[self.currBurstIndex] -= 1

    def incrementBurstIndex(self):
        self.currBurstIndex += 1
    
    def getCurrentBurstTime(self):
        return self.bursts[self.currBurstIndex]
    
    def getTotCpuTime(self):
        for i in range(len(self.cpubursts)):
            self.cpuTime+=int(self.cpubursts[i])
        return self.cpuTime
    def getTotIoTime(self):
        for i in range(len(self.iobursts)):
            self.ioTime+=int(self.iobursts[i])
        return self.ioTime    
    
    def __str__(self):
       
        # simple return list
        #return f"[red]AT:[/red] {self.arrivalTime}, [blue]PID:[/blue] {self.pid}, [green]Priority:[/green] {self.priority:2}, [yellow]# CPU bursts:[/yellow] {self.noCpuBursts}, [yellow]CPU Time =[/yellow] {self.getTotCpuTime()} [magenta]# IO Bursts:[/magenta] {self.noIoBursts} [magenta]IO Time=[/magenta] {self.getTotIoTime()}"
        #burst itemized list
        return f"[red]AT:[/red] {self.arrivalTime}, [blue]PID:[/blue] {self.pid}, [green]Priority:[/green] {self.priority:2}, [yellow]CPU:[/yellow] {self.cpubursts}, [magenta]IO:[/magenta] {self.iobursts}"
        

class Simulator:
    def __init__(self,datfile):
        self.datfile = datfile
        self.new = Queue()
        self.wait = Queue()
        self.running = CPU()
        self.ready = Queue()
        self.terminated = Queue()
        self.processes = {}
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
                self.processes[pcb_key]=[PCB(arrival,pid,priority,cpubursts,iobursts)]
                
        for pcb_key, pcb_instances in self.processes.items():
            for pcb_instance in pcb_instances:
                print(f"[bold]{pcb_key}:[/bold] {pcb_instance}")
                #print(pcb_instance.to_str())

                #print(f"{arrival}, {pid}, {priority} {len(bursts)}{cpubursts}{iobursts}")
        return self.processes

if __name__=='__main__':
    sim = Simulator("datafile.dat")
   # print(sim)
    key = 'pcb-2'
    # set & print a single pcb from the processes dict
    item=sim.processes['pcb-1'][0]
    print(f'{item}')
    # for a given current burst index value
    #print the given burst value at an index position within the burst list of the pcb dict item. 
    
    #pcb_instance = sim.processes['pcb-1'][0]
    #check len of cpuburst list - list will eventually go to 0 currBurstIndex will always be 0 index
    if 0<=sim.processes['pcb-1'][0].currBurstIndex < len(sim.processes['pcb-1'][0].cpubursts): 
        currCpuBurst=sim.processes['pcb-1'][0].cpubursts[sim.processes['pcb-1'][0].currBurstIndex]
        if currCpuBurst ==0:  # is the current index value 0? if so pop it off the list - cpu burst is done
            sim.processes['pcb-1'][0].currBurstIndex.pop(0) 

        print(f"CPU Burst at index {sim.processes['pcb-1'][0].currBurstIndex}: {currCpuBurst}")
    elif 0<=sim.processes['pcb-1'][0].currBurstIndex < len(sim.processes['pcb-1'][0].cpubursts):
        
    # if item:
    #     for attribute in ['arrivalTime', 'pid', 'priority','cpubursts','iobursts']:
    #         print(f'{attribute.capitalize()}:  {getattr(item[0], attribute)}')
    #     for attribute in ['cpubursts']:   
    #         print(f'{attribute.capitalize()}:  {getattr(item[0], attribute)}')
    #print(f'{item}')
