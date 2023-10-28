# CPU Schecule Simulation
""" """
from rich import print
from rich.text import Text
import time

class Queue:
    def __init__(self,pcb):
        self.queue = []

    def __str__(self):
        return ",".join(self.queue)

    def addPCB(self,pcb):
        self.queue.append(pcb)
    
    def removePCB(self,pcb):
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
    
class New:
    def __init__(self,pcb):
        self.new = []

    def __str__(self):
        return ",".join(self.new)

    def addPCB(self,pcb):
        self.new.append(pcb)
    
    def removePCB(self):
        item = self.new[0]
        del self.new[0]
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

class Ready:
    def __init__(self,pcb):
        self.ready = []

    def __str__(self):
        return ",".join(self.ready)

    def addPCB(self,pcb):
        self.ready.append(pcb)
    
    def removePCB(self):
        item = self.ready[0]
        del self.ready[0]
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

class IO:
    def __init__(self,pcb):
        self.io = []

    def __str__(self):
        return ",".join(self.io)

    def addPCB(self,pcb):
        self.io.append(pcb)
    
    def removePCB(self):
        item = self.io[0]
        del self.io[0]
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

class Finished:
    def __init__(self,pcb):
        self.finished = []

    def __str__(self):
        return ",".join(self.finished)

    def addPCB(self,pcb):
        self.finished.append(pcb)
    
    def removePCB(self):
        item = self.finished[0]
        del self.finished[0]
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

class CPU:
    def __init__(self,pcb):
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
    def __init__(self,pid,at,priority,cpubursts,iobursts):
        self.pid = pid     
        self.priority = priority     
        self.arrivalTime = at
        self.cpubursts = cpubursts    
        self.iobursts=iobursts
        self.currBurstIs = 'CPU'
        self.state='New'
        self.currBurstIndex = 0
        self.currCpuBurst = cpubursts[0]
        self.currIoBurst =iobursts[0]
        self.readyTime = 0
        self.ioTime = 0
        self.cpuTime = 0
        self.ioTime =0
        self.noCpuBursts =len(cpubursts)
        self.noIoBursts =len(iobursts)

    def changeState(self, new_state):
        self.state = new_state

    def getCurrBurstType(self):
        return self.currBurstIs
    
    def getCurrBurst(self):
        if self.currBurstIs=='CPU':
            return self.cpubursts[self.currBurstIndex]
        elif self.currBurstIs =='IO':
            return self.iobursts[self.currBurstIndex]
        
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
        return f"[red]AT:[/red] {self.arrivalTime}, [green]Priority:[/green] {self.priority:2}, [yellow]CPU:[/yellow] {self.cpubursts}, [magenta]IO:[/magenta] {self.iobursts}"
    
    def processCurrBurst(self):
        pcb = self.processes['PID-1'][0]  # create a convient variable to refer to each instance of the PCB class
        if self.currBurstIs=='CPU':
            self.cpubursts[self.currBurstIndex] -=1
            if self.cpubursts[self.currBurstIndex]==0:
                self.currBurstsIndex +=1
                self.currBurstIs = 'IO'
        elif self.currBurstIs == 'IO':
            self.iobursts[self.currBurstIndex]+=1
            if self.iobursts[self.currBurstIndex]==0:
                self.currBurstsIndex +=1
                self.currBurstIs = 'CPU'                    
class SysClock:
    _shared_state = {}
    def __init__(self):
        self.__dict__ = self._shared_state
        if not 'clock' in self.__dict__: 
            self.clock = 0

    def advanceClock(self, tick=1):
        self.clock += tick
        clockTime = self.clock 
        return clockTime        
    
class Simulator:
    def __init__(self,datfile):
        self.datfile = datfile
        self.processes = {}
        self.readData()
        self.newQueue =[]
        self.readyQueue =[]
        self.CPUQueue =[]
        self.IOQueue =[]
        self.finishedQueue =[]
        self.clock = SysClock()   
        self.simLoop(self.processes)



    def __str__(self):
        s = ""
        s += "datfile: "+self.datfile +"\n"
        s += "new queue: "+",".join(self.new)  +"\n"
        s += "wait: "+",".join*(self.wait)  +"\n"
        return s

    def readData(self):
        with open(self.datfile) as f:
            self.data = f.read().split("\n")
        
        for process in self.data:
            if len(process) > 0:
                parts = process.split(' ')
                arrival = parts[0]
                pid = parts[1]
                priority = parts[2]
                bursts = parts[3:]  # gets everything else in the process list
                cpubursts=[] 
                iobursts=[]
                # parse bursts into CPU & IO
                for i in range(len(bursts)):
                    if i%2==0:
                        cpubursts.append(bursts[i])
                    else:
                        iobursts.append(bursts[i])
                
                #create dictionary of all processes with PID as key and values are PCBs        
                pcb_key=f'PID-{pid}' # use pid to be key for each PCB
                self.processes[pcb_key]=[PCB(pid,arrival,priority,cpubursts,iobursts)]
        
        for pcb_key, pcb_instances in self.processes.items():
            for pcb_instance in pcb_instances:
                print(f"[bold][blue]{pcb_key}:[/bold][/blue] {pcb_instance}")
        return self.processes    
    
    # def getPCB(self, pid, processes):    # for demonstration that PCB have been instantiated - print below       
    #     pcb_key=f'PID-{pid}'
    #     for pcb_key, pcb_instances in self.processes.items():
    #         for pcb_instance in pcb_instances:
    #             print(f"[bold][blue]{pcb_key}:[/bold][/blue] {pcb_instance}")
    #             pcb=pcb_instance
    #     return pcb
                
    # def moveToNew(self, processes):
    #     new_pcbs ={}
    #     for pid, pcbs in list(self.processes.items()):
    #           new_pcbs[pid] =[]
    #           for pcb in pcbs:
    #               if pcb.arrivalTime == time:
    #                   new_pcbs[pid].append(pcb)   # append PCB to new queue
    #                   pcbs.remove(pcb)
    #     return new_pcbs
      

    ###################
    # SIMULATION LOOP #
    ###################  
    def simLoop(self, processes): 
        newQueue =[]
        readyQueue =[]
        CPUQueue =[]
        IOQueue =[]
        finishedQueue =[]
        complete =False
        self.clock
        
      # loop to check each process and match clock time to arrival time. 
        while complete==False: #loop until all processes are in finished[] 
         # 1. add 1 to wait_time for everything in readyQueue
            if readyQueue:
                for process in readyQueue:
                    process.readyTime += 1 
            else:
                print(f'Ready queue is currently empty')
            
        #2. move anything in new to ready
            if newQueue:
               readyQueue.extend(newQueue)
               newQueue.clear()
       # 3. check for new processes which may need to go to new if pcb arrival time == time, add pcb to new
               for process in processes.values():
                    if process.arrivalTime == self.clock.clockTime:
                        newQueue.append(process)     
            else:
                print(f'new queue is currently empty')      
                
        # 4. decrement all current CPU and IO processes bursts' values by 1
            if CPUQueue:
                for process in CPUQueue:
                    process.cpuburst[0]-=1
                    remainingTime =process.cpubursrts[0]
                    print(f'PCB-{process.pid} now in CPU with {remainingTime} seconds') 
            else:    
                print(f'CPU currently empty')
            
            if IOQueue:
                for process in IOQueue:
                    process.ioburst[0]-=1
                    remainingTime =process.iobursrts[0]
                    print(f'PCB-{process.pid} now in IO with {remainingTime} seconds') 
            else:    
                print(f'IO currently empty')              

        # 5. check if CPU busy, 
            if CPUQueue: #is process in the CPU
                process=CPUQueue[0]
                if process.cpubursts[0] == 0: #is the process in CPU finished?
                    if len(process.cpubursts) == 1:  # was this the last CPU bursts of running process?
                        process.cpubursts.pop(0) # remove the finished burst from the cpue bursts list
                        finishedQueue.append(process)  # move the finished process to finished queue
                        if readyQueue: # check to see if something remains in readyqueue
                            nextProcess=readyQueue.pop(0) # pop the next process off the ready queue 
                            CPUQueue.append(nextProcess) # move the process to the CPU
                        elif not readyQueue and IOQueue: # if ready is empty, but IO still has processes
                            pass
                        else:
                            if not readyQueue and not IOQueue:
                                complete=True        
                    else: # not last CPU bursts so move to IO
                        IOQueue.append(process) # move completed process to IO
                        CPUQueue.clear() # empty CPU list
                        nextProcess=readyQueue.pop(0) # pop the next process off the ready queue 
                        CPUQueue.append(nextProcess) # move the process to the CPU
                else:  # currently running process has remaining CPU time, keep PCB in CPU,
                    remainingTime =process.cpubursrts[0]
                    print(f'PCB-{process.pid} now in CPU with {remainingTime} seconds') 
            else: #if cpu is empty add something    
                if readyQueue: # is something in the ready queue
                    nextProcess=self.readyQueue.pop(0) # pop the next process off the ready queue 
                    CPUQueue.append(nextProcess) # move the process to the CPU
                elif IOQueue and not readyQueue: # if ready is empty, but IO still has processes
                    pass
                else:
                    if not readyQueue and not IOQueue and not newQueue:
                        complete=True                   
        # 6. check to see if any PCBs' in IO have current IO burst value == 0,  
            if IOQueue:
               completeIOprocesses =[process for process in IOQueue if process.iobursrsts[0] == 0]
               for process in completeIOprocesses:
                    print(f'PCB-{process.pid} has completed its current IO burst and moved to ready') 
               IOQueue = [process for process in IOQueue if process.iobursrsts[0] != 0]
               for process in IOQueue:
                    remainingTime =process.iobursrts[0]
                    print(f'PCB-{process.pid} has {remainingTime} seconds of IO remaining') 
               readyQueue.extend(completeIOprocesses)
               completeIOprocesses.clear()
            else:
                pass
        
            time.sleep(2)
            self.clock.advanceClock(1)


if __name__=='__main__':
    sim = Simulator("datafile.dat")
   
   
    # set & print a single pcb from the processes dict
    item=sim.processes['PID-1'][0]
    print(f'{item}')
    
    #########################################
    # for a given current burst index value #
    #########################################
    #print the given burst value at an index position within the burst list of the pcb dict item. 
        
    #This all probably should be a function in a class(es)
    # ??loop over processes dict and to all this for each PCB?  
    # pass them to correct queue based on bool flags like CPU=T/F or IO=T/F
    
    # pcb_instance = sim.processes['PID-1'][0]  # create a convient variable to refer to each instance of the PCB class
    # if pcb_instance.currBurstIs=='CPU':
    #     ###########################
    #     # current CPU burst value #
    #     ###########################
    #     #check len of cpuburst list - list will eventually go to length 0,  currBurstIndex will always be [0] index
    #     if 0<=pcb_instance.currBurstIndex < pcb_instance.noCpuBursts: 
    #         currCpuBurst=pcb_instance.cpubursts[pcb_instance.currBurstIndex]
    #         if currCpuBurst ==0:  # is the current index value 0? if so pop it off the list - cpu burst is done
    #             pcb_instance.currBurstIndex.pop(0) 
    #             IO=True

    #         print(f"CPU Burst at index {pcb_instance.currBurstIndex}: {currCpuBurst}")
    #         #return currCpuBurst value so it can be operated on by CPU class methods
    #     elif 0<=pcb_instance.currBurstIndex < pcb_instance.noCpuBursts:
    #         pass 
    # else:
    #     ##########################
    #     # current IO burst value #
    #     ##########################
    #     if 0<=pcb_instance.currBurstIndex < pcb_instance.noIoBursts: 
    #         currIoBurst=pcb_instance.iobursts[pcb_instance.currBurstIndex]
    #         if currIoBurst == 0:  # is the current index value 0? if so pop it off the list - cpu burst is done
    #             pcb_instance.currBurstIndex.pop(0) 
    #             IO=False

    #         print(f"IO Burst at index {pcb_instance.currBurstIndex}: {currIoBurst}")
    #         #return currCpuBurst value so it can be operated on by CPU class methods
    #     elif 0<=pcb_instance.currBurstIndex < pcb_instance.noIoBursts:
    #         pass 
        
    # if item:
    #     for attribute in ['arrivalTime', 'pid', 'priority','cpubursts','iobursts']:
    #         print(f'{attribute.capitalize()}:  {getattr(item[0], attribute)}')
    #     for attribute in ['cpubursts']:   
    #         print(f'{attribute.capitalize()}:  {getattr(item[0], attribute)}')
    #print(f'{item}')
