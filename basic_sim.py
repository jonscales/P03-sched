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
    """
    """
    def __init__(self,pid,at,priority,cpubursts,iobursts):
        self.pid = pid     
        self.priority = priority     
        self.arrivalTime = int(at)
        self.cpubursts = [int(burst) for burst in cpubursts]   
        self.iobursts = [int(burst) for burst in iobursts]
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
   
    def incrementReadyTime(self):
        self.readyTime += 1    
   
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
    
           
class SysClock:
    """
    """
    _shared_state = {}
    def __init__(self):
        self.__dict__ = self._shared_state
        if not 'clock' in self.__dict__: 
            self.clock = 0

    def advanceClock(self, tick=1):
        self.clock += tick
           
    def currentTime(self):
        return self.clock   
    
class Simulator:
    """
    """
    def __init__(self,datfile):
        self.datfile = datfile
        self.processes = {}
        self.readData()
        self.newQueue = []
        self.readyQueue =[]
        self.CPUQueue =[]
        self.IOQueue = []
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
        """
        """
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
                self.processes[pcb_key] = [PCB(pid, arrival, priority, cpubursts, iobursts)]
        
        for pcb_key, pcb_instances in self.processes.items():
            for pcb_instance in pcb_instances:
                print(f"[bold][blue]{pcb_key}:[/bold][/blue] {pcb_instance}")
                
        return self.processes       

    ###################
    # SIMULATION LOOP #
    ###################  
    def simLoop(self, processes): 
        """ 
        
        
        """
        complete = False
        loopIteration = 0
       # loop to check each process and match clock time to arrival time.
        while not complete: #loop until all processes are in finished[] 
            print(f'The clock is {self.clock.currentTime()}')
         # 1. add 1 to wait_time for everything in readyQueue
            if self.readyQueue:
                for process in self.readyQueue:
                    process.incrementReadyTime() 
            else:
                print(f'Ready queue is currently empty')
            
        #2. move anything in new to ready
            if self.newQueue:
               self.readyQueue.extend(self.newQueue)
               self.newQueue.clear()
           
       # 3. check for new processes which may need to go to new if pcb arrival time == time, add pcb to new
            for process_key, process_value in processes.items():
                for pcb_instance in process_value: 
                    #print(f'PCB instance is : {pcb_instance}')
                    if pcb_instance.arrivalTime == self.clock.currentTime():
                        self.newQueue.append(pcb_instance)
                        print(f'{pcb_instance} has been added to newQueue')
            else:
                print(f'new queue is currently empty') 
            if self.newQueue:
                processes_in_new = [pcb.pid for pcb in self.newQueue]
                print(f'The processes currently in new are: {processes_in_new}')    
        
        # 4. decrement all current CPU and IO processes bursts' values by 1
            if self.CPUQueue:
                for process in self.CPUQueue:
                    if process.cpubursts:
                       process.cpubursts[0] -= 1
                       remainingTime = process.cpubursts[0]
                       print(f'PCB-{process.pid} now in CPU with {remainingTime} seconds') 
                    else:
                        pass
            else:    
                print(f'CPU currently empty')
            
            if self.IOQueue:
                for process in self.IOQueue:
                    process.iobursts[0] -=1
                    remainingTime = process.iobursts[0]
                    print(f'PCB-{process.pid} now in IO with {remainingTime} seconds') 
            else:    
                print(f'IO currently empty')              

        # 5. check if process in CPU , 
            if self.CPUQueue:                                #is process in the CPU
                process=self.CPUQueue[0]
                
                if process.cpubursts[0] == 0:                #is the process in CPU finished?
                    if len(process.cpubursts) <= 1:          # was this the last CPU bursts of running process?
                        self.finishedQueue.append(process)  # move the finished process to finished queue
                        print(f'process {process} has terminated')
                        process.cpubursts.pop(0)             # remove the finished burst from the cpue bursts list
                        self.CPUQueue.clear()
                        if self.readyQueue: # check to see if something remains in readyqueue
                            nextProcess=self.readyQueue.pop(0) # pop the next process off the ready queue 
                            self.CPUQueue.append(nextProcess) # move the process to the CPU
                        elif not self.readyQueue and self.IOQueue: # if ready is empty, but IO still has processes
                            pass
                        else:
                            if loopIteration > 1 and not self.readyQueue and not self.IOQueue:
                                complete=True        
                    else:                                   # not last CPU bursts so move to IO
                        self.IOQueue.append(process)        # move completed process to IO
                        if process.cpubursts:               
                            process.cpubursts.pop(0) 
                            self.CPUQueue.clear()           # empty CPU list
                            if self.readyQueue:
                                nextProcess=self.readyQueue.pop(0) # pop the next process off the ready queue 
                                self.CPUQueue.append(nextProcess) # move the process to the CPU
                            else:
                                pass    
                else:  # currently running process has remaining CPU time, keep PCB in CPU,
                    remainingTime = process.cpubursts[0]
                    print(f'PCB-{process.pid} now in CPU with {remainingTime} seconds') 
            else: #if cpu is empty add something    
                if self.readyQueue: # is something in the ready queue
                    nextProcess=self.readyQueue.pop(0) # pop the next process off the ready queue 
                    self.CPUQueue.append(nextProcess) # move the process to the CPU
                elif self.IOQueue and not self.readyQueue: # if ready is empty, but IO still has processes
                    pass
                else:
                    if loopIteration > 1 and not self.readyQueue and not self.IOQueue and not self.newQueue:
                        complete=True                   
        # 6. check to see if any PCBs' in IO have current IO burst value == 0,  
            if self.IOQueue:
                completeIOprocesses =[process for process in self.IOQueue if process.iobursts[0] == 0]
                for process in completeIOprocesses:
                    print(f'PCB-{process.pid} has completed its current IO burst and moved to ready')
                     
                self.IOQueue = [process for process in self.IOQueue if process.iobursts[0] != 0]
                for process in self.IOQueue:
                    remainingTime = process.iobursts[0]
                    print(f'PCB-{process.pid} has {remainingTime} seconds of IO remaining') 
                self.readyQueue.extend(completeIOprocesses)
                for process in completeIOprocesses:
                    if process.iobursts[0]==0:
                       process.iobursts.pop(0)
                completeIOprocesses.clear()
            else:
                pass
                
            time.sleep(.1)
            loopIteration += 1
            self.clock.advanceClock(1)
            for process_key, process_value in processes.items():
                for pcb_instance in process_value: 
                    print(f'{process_key} status: CPU:{pcb_instance.cpubursts}; IO:{pcb_instance.iobursts}; {pcb_instance.currBurstIs} : {pcb_instance.state}')
        print(f'\n\n All processes have terminated\n\n')

if __name__=='__main__':
    sim = Simulator("datafile.dat")
   
   
    
