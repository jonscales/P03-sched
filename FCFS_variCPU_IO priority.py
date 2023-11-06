# CPU Schecule Simulation
"""
This program simulates a CPU scheduler
The program can be run with different flags to simulate a FCFS or Round Robin algorithm
"""
import os
from rich import print
from rich.text import Text
import time
from prettytable import PrettyTable
import csv
import shutil
# class Queue:
#     def __init__(self,pcb):
#         self.queue = []

#     def __str__(self):
#         return ",".join(self.queue)

#     def addPCB(self,pcb):
#         self.queue.append(pcb)
    
#     def removePCB(self,pcb):
#         item = self.queue[0]
#         del self.queue[0]
#         return item

#     def decrement(self):
#         """ Iterate over the self.queue and decrement or call whatever
#             method for each of the pcb's in this queue
#         """
#         # for each process in queue
#         #    call decrementIoBurst
#         pass
    
#     def incrememnt(self,what='waittime'):
#         """ Iterate over the self.queue and decrement or call whatever
#             method for each of the pcb's in this queue
#         """
#         # for each process in queue
#         #    call incrementwaittime
#         if what =='waittime':
#             pass
#         elif what == 'runtime':
#             pass
#         pass 
    
# class CPU:
    # def __init__(self,pcb):
    #     self.busy = False
    #     self.runningPCB = None

    # def decrementCurrentProcess(self):
    #     self.runningPCB.decrementCpuBurst()
    
    # def loadProcess(self,pcb):
    #     self.runningPCB = pcb

    # def testKickOff(self):
    #     if self.runningPCB.getCurrentBurstTime() == 0:
    #         pass
    #         # kick it off the cpu

class PCB:
    """
    This class generates a process control block (PCB) from information read in from 
    a data file. The attributes are passed to PCB as the pcb is
    generated in by the readData method of the Simulator class. 
    """
    def __init__(self,pid,at,priority,cpubursts,iobursts):
        """
        Initializes a PCB instance
        """
        self.pid = pid     
        self.priority = priority     
        self.arrivalTime = int(at)
        self.cpubursts = [int(burst) for burst in cpubursts]   
        self.iobursts = [int(burst) for burst in iobursts]
        self.currBurstType = 'CPU'
        self.state='New'
        self.currBurstIndex = 0
        self.currCpuBurst = cpubursts[0]
        self.currIoBurst =iobursts[0]
        self.waitTime =0
        self.readyTime = 0
        self.initCPUTime =0
        self.initIOTime =0
        self.cpuTime = self.getTotCpuTime()
        self.ioTime = self.getTotIoTime()
        self.numCpuBursts =len(cpubursts)
        self.numIoBursts =len(iobursts)
        self.remainingCPUTime = int(cpubursts[0])
        self.remainingIOTime = int(iobursts[0])

   
    def upPriority(self):
        """
        increases the priority +1 of a process after it has remained in the ready queue 
        longer than the the sum of its CPU bursts
        """
        Simulator.getProcesses()
        for pcb in self.processes:
            if pcb.waitTime >= pcb.CPUTime:
                pcb.priority +=1

    def getPriority(self):
        """
        returns the PCB's priority
        """
        return self.priority
    
    def incrementReadyTime(self):
        """
        increments the readyTime variable.  
        readyTime is the time PCB spends in the ready queue
        this is also the wait time
        """
        self.readyTime += 1 

    def incrementWaitTime(self):
        """
        increments the readyTime variable.  
        readyTime is the time PCB spends in the ready queue
        this is also the wait time
        """
        self.waitTime += 1       
   
    def changeState(self, new_state):
        """
        changes state attribute which is the current queue location of the PCB
        """
        self.state = new_state

    def changeBurstType(self,BT):
        self.currBurstTYpe = BT
    
    def getCurrBurstType(self):
        return self.currBurstIs
    
    def getCurrBurst(self):
        if self.currBurstType =='CPU':
            return self.cpubursts[self.currBurstIndex]
        elif self.currBurstType =='IO':
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
        """
        returns the total CPU time by adding all cpu bursts
        """
        for i in range(len(self.cpubursts)):
            self.initCPUTime+=int(self.cpubursts[i])
        return self.initCPUTime
    
    def getTotIoTime(self):
        """
        returns the total IO time by adding all io bursts
        """
        for i in range(len(self.iobursts)):
            self.initIOTime+=int(self.iobursts[i])
        return self.initIOTime 
    
    def getTotalTime(self):
        """
        returns the total time the PCB spends in the system
        cpu time + io time + wait time + ready time + new time (1)
        """
        return self.cpuTime + self.ioTime + self.readyTime + self.waitTime + 1
    
    def getWaitTime(self):
        """
        returns the total time PCB spend in the wait queue
        """
        return self.waitTime  
    
    def getReadyTime(self):
        """
        returns the total time PCB spend in the ready (wait) queue
        """
        return self.readyTime  
    
    def cpu_ioRatio(self):
        """
        returns the ratio of CPU to IO times
        """
        return round((self.cpuTime/self.ioTime),2)
    
    def run_idleRatio(self):
        """
        returns the ratio of run (CPU + IO ) time to idle (wait + ready) time
        """
        return round((self.cpuTime + self.ioTime)/(self.readyTime + self.waitTime),2)

    def __str__(self):
        """
        Will print each PCB in the processes dictionary on a line as :
        PID # : process information.  Can do this as either a simple list of 
        information or an itemized list of all burst times. 
        """
       
        # simple return list
        #return f"[red]AT:[/red] {self.arrivalTime}, [blue]PID:[/blue] {self.pid}, [green]Priority:[/green] {self.priority:2}, [yellow]# CPU bursts:[/yellow] {self.noCpuBursts}, [yellow]CPU Time =[/yellow] {self.getTotCpuTime()} [magenta]# IO Bursts:[/magenta] {self.noIoBursts} [magenta]IO Time=[/magenta] {self.getTotIoTime()}"
        #burst itemized list
        return f"[red]AT:[/red] {self.arrivalTime}, [green]Priority:[/green] {self.priority:2}, [yellow]CPU:[/yellow] {self.cpubursts}, [magenta]IO:[/magenta] {self.iobursts}"
    
           
class SysClock:
    """
    This class creates a class-level variable called clock.
    The clock's value is used to drive the looping of the
    PCBs within the simulated scheduler.
    """
    _shared_state = {}
    def __init__(self):
        """
        creates the clock shared state variable
        """
        self.__dict__ = self._shared_state
        if not 'clock' in self.__dict__: 
            self.clock = 0

    def advanceClock(self, tick=1):
        """
        advances the clock +1
        """
        self.clock += tick
           
    def currentTime(self):
        """
        returns the currentTime (clock value)
        """
        return self.clock   

class Stats:
    """
    The class will display the stats associated with the movement of PCB
    through the schedular.  It will also output this information as a .csv file
    for use in other applications. 
    """    
    def __init__(self, processes,  clock, simType='None'):
        """
        Stats initialization
        """
        self.processes = processes
        self.symType =simType
        self.clock = clock
        self.statTable(clock)
        self.statFileWriter(clock, simType)
    
    def statTable(self,clock):
        """
        generates & displays a table showing the total clock time for completing all PCBs
        generates & displays a table with various stats from each PCB
        """
        #Color info
        R = "\033[0;31;40m" #RED
        G = "\033[0;32;40m" # GREEN
        Y = "\033[0;33;40m" # Yellow
        B = "\033[0;34;40m" # Blue
        P = '\033[95m' # Purple
        C = '\033[96m' #cyan
        DC= '\033[36m' # dark cyan
        BLD = '\033[1m' # bold
        U = '\033[4m' # underline
        N = "\033[0m" # Reset
        titleTable = PrettyTable()
        titleTable.field_names = ['Process Statistics Table']
        titleTable.align['Process Statistics Table'] ='c'
        titleTable.min_width['Process Statistics Table'] = 82
        titleTable.add_row([f"Total System Clock Time : {clock.currentTime()}"])
        
        statTable = PrettyTable()
        statTable.field_names = ["PID", "Total Time", "Ready Time", "CPU Time", "Wait Time", "IO Time", "CPU/IO", "Run/Idle"]
        for pid, pcb_instances in self.processes.items():
            for pcb in pcb_instances:
                statTable.add_row([pcb.pid, pcb.getTotalTime(), pcb.getReadyTime(), pcb.getTotCpuTime(), 
                                   pcb.getTotIoTime(), pcb.getReadyTime(), pcb.cpu_ioRatio(),
                                     pcb.run_idleRatio()])
        print(titleTable)
        print(statTable)
    
    def statFileWriter(self, clock, simType='none'):
        """
        """ 
        # dictionary to match output filename to simulation run type
        sim_type_to_fname = {
            'SCPU': 'SCPU_stat_data.csv',
            'SIO': 'SIO_stat_data.csv',
            'LCPU': 'LCPU_stat_data.csv',
            'LIO': 'LIO_stat_data.csv',
            'HBCt':'HBCt_stat_data.csv',
            'LBCt':'LBCt_stat_data.csv',                
            }
        if simType=='None':
            outFileName ='SimStatsData.csv'
        else:
            outFileName=sim_type_to_fname.get(self.simType, 'SimStatsData.csv')
       
        with open(outFileName, 'w', newline='') as csvfile:
            fieldnames = ["Clock Time","Process ID", "Total Time", "Ready Time", "CPU Time", "IO Time", "Wait Time","CPU/IO", "Run/Idle"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            first_row = {"Clock Time": clock.currentTime()}
            writer.writerow(first_row)
            # Write the header row to the CSV file
            writer.writeheader()

            # Write data for each PCB
            for pid, pcb_instances in self.processes.items():
                for pcb in pcb_instances:
                    data = {
                        'Process ID': pcb.pid,
                        'Total Time': pcb.getTotalTime(),
                        'Ready Time':pcb.getReadyTime(),
                        'CPU Time': pcb.cpuTime,
                        'Wait Time' : pcb.waitTime,
                        'IO Time' : pcb.ioTime,
                        'CPU/IO': pcb.cpu_ioRatio(),
                        'Run/Idle': pcb.run_idleRatio()                    
                            }
                    writer.writerow(data) 
                          
class Simulator:
    """
    This class is the main simulator operator
    methods to:
      read in the data from a file
      run the simulation loop
    """
    def __init__(self,datfile, num_cpus, num_ios):
        """
        Simulator initialization
        """
        #self.timeSlice=int(TS)
        self.datfile = datfile
        self.num_cpus =int(num_cpus)
        self.num_ios = int(num_ios)
        self.processes = {}
        self.readData()
        self.newQueue = []
        self.readyQueue =[]
        self.CPUQueue =[]
        self.IOQueue = []
        self.waitQueue = []
        self.finishedQueue =[]
        self.clock = SysClock()   
        self.simLoop(self.processes, self.num_cpus, self.num_ios)
    
    def getProcesses(self):
        """
        returns the processes dictionary to other classes' methods
        """
        return self.processes

    def readData(self):
        """
        reads in data from a datafile containing PCB process parameters
        produces a dictionary named processes using the process ID number (pid)
        in each processes parameters as the key and instantiates an instance of a
        PCB class for each process, populating that PCB with the parameters for 
        arrival time, priority, cpu bursts list & io bursts list.
        """
        with open(self.datfile) as f:
            self.data = f.read().split("\n")
        
        for process in self.data:
            if len(process) > 0:
                parts = process.split(' ')
                arrival = parts[0]
                pid = parts[1]
                priority = int(parts[2][1:])
                bursts = parts[3:]
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
        
        # for pcb_key, pcb_instances in self.processes.items():
        #     for pcb_instance in pcb_instances:
        #         print(f"[bold][blue]{pcb_key}:[/bold][/blue] {pcb_instance}")
                
        return self.processes  
         
    # def getMinCPUburst(self, pcb):
    #     try:
    #         return min(pcb.cpubursts)
    #     except ValueError:
    #         return float('inf') 

    def simLoop(self, processes, num_cpus, num_ios): 
        """ 
        SIMULATION LOOP
        This method runs the Schedular Simulation
        """
        # Create a table for displaying the queue contents
        table = PrettyTable()
        terminal_width = shutil.get_terminal_size().columns
        table.max_width = int(.9 * terminal_width)
    
        table.field_names = ["Clk", "Q", "PID, Priority , Burst"]
        table.align = 'l'
    
        complete = False
        loopIteration = 0
        
        
        while not complete: #loop until all processes are in finished[]  
        
        # 1. increment times for readyQueue & waitQueue PCBs
            if self.readyQueue:
                for process in self.readyQueue:
                    process.changeState('Ready')
                    self.readyQueue = sorted(self.readyQueue, key=lambda pcb: (pcb.priority), reverse=True)
                    process.incrementReadyTime() 
            else:
                pass
            
            if self.waitQueue:
                for process in self.waitQueue:
                    process.changeState('Wait')
                    process.incrementWaitTime() 
            else:
                pass       

        #2. move anything in new to ready
            if self.newQueue:
                self.readyQueue.extend(self.newQueue)
                for pcb in self.readyQueue:
                    pcb.changeState('Ready')
                    print(f'PID {pcb.pid} --> Ready')
                self.readyQueue = sorted(self.readyQueue, key=lambda pcb: (pcb.priority), reverse=True)
                self.newQueue.clear()
           
        # 3. check for new processes if pcb arrival time == time, add pcb to new
            for pid, PCBs in processes.items():
                for pid in PCBs: 
                    if pid.arrivalTime == self.clock.currentTime():
                        self.newQueue.append(pid)
                        pid.changeState('New')
                        print(f'PID {pid.pid} --> New')
            else:
                #print(f'new queue is currently empty')
                pass 
        
        # 4. decrement current CPU and IO processes bursts values
            if self.CPUQueue:
                for pcb in self.CPUQueue:
                    if pcb.cpubursts:
                        pcb.cpubursts[0] -= 1
                        pcb.remainingCPUTime = pcb.cpubursts[0]
                    else:
                        pass
            
            if self.IOQueue:
                for pcb in self.IOQueue:
                    if pcb.iobursts:
                        pcb.iobursts[0] -=1
                        pcb.remainingIOTime = pcb.iobursts[0] 
                    else:
                        pass
            else:    
                pass              
                    
        # 5A. sort readyQueue by priority then AT, then CPU shortest burst length  
            self.readyQueue = sorted(self.readyQueue, key=lambda pcb: (pcb.priority), reverse=True)
            # print(f'Sorted Ready Queue :')
            # for pcb in self.readyQueue:
            #     print(f'{pcb.pid}:{pcb}')
        
        # 5B check if process in CPU and if any are finished
            if self.CPUQueue:                                #is process in the CPU
                lowestCPU = min(self.CPUQueue, key=lambda pcb:pcb.priority)
                print(f'Lowest priority PCB in CPU = {lowestCPU.pid}')
                for pcb in self.CPUQueue: 
                    if pcb.cpubursts[0] == 0:                #is process in CPU finished?
                        if len(pcb.cpubursts) <= 1:          # was this last CPU bursts for process?
                            print(f'PCB {pcb.pid} DONE')
                            pcb.changeState('Finished')      # move process to finished queue
                            self.finishedQueue.append(pcb)   
                            pcb.cpubursts.pop(0)             # remove finished burst from cpu bursts list
                        else:                                   # not last CPU bursts so move to wait
                            print(f'PCB {pcb.pid} CPU burst finished, moved to Wait')
                            self.waitQueue.append(pcb)        # move completed process to wait
                            pcb.changeState('Wait')
                            if pcb.cpubursts:               
                                pcb.cpubursts.pop(0) 
                            print(f'Wait queue = ')
                            for pcb in self.waitQueue:
                                print(f'PID {pcb.pid}')
                    else:
                        pass
                self.CPUQueue = [pcb for pcb in self.CPUQueue if pcb.state == 'CPU']  # update CPU 
                self.readyQueue = sorted(self.readyQueue, key=lambda pcb: (pcb.priority), reverse=True)
                
        #5C check if any ready processes have higher priority & swap with lower CPU processes - loop till all swapped
                
             
                while loopIteration >= 3 and self.readyQueue and (self.readyQueue[0].priority > lowestCPU.priority) and self.readyQueue[0].readyTime >=1:
                    print(f'1st process in sorted ready queue: {self.readyQueue[0].pid}')
                    highestReady = self.readyQueue[0]
                    print(f'highest priority in sorted ready queue: {highestReady.pid}')
                
                    try:
                        self.CPUQueue.remove(lowestCPU)
                        print(f'PCB {lowestCPU.pid} removed from CPU')
                    except ValueError:
                        pass
                    lowestCPU.changeState('Ready')
                    self.readyQueue.append(lowestCPU)
                    
                    self.CPUQueue.append(highestReady)
                    print(f'PCB {highestReady.pid} added to CPU')
                    highestReady.changeState('CPU')
                    self.readyQueue.pop(0) 
                    print(f'Ready contains: ')
                    for pcb in self.readyQueue:
                        print(f'PCB {pcb.pid}')      
                
                self.readyQueue = [pcb for pcb in self.readyQueue if pcb.state =='Ready']  # update ready 
                self.CPUQueue = [pcb for pcb in self.CPUQueue if pcb.state =='CPU']  # update CPU 
                self.readyQueue = sorted(self.readyQueue, key=lambda pcb: (pcb.priority),reverse=True)
        #5D
                if self.readyQueue and loopIteration >= 1 and (not self.CPUQueue or len(self.CPUQueue) < self.num_cpus): # are processes in readyqueue & is CPU not full
                    num_to_assign = min(self.num_cpus - len(self.CPUQueue), len(self.readyQueue))
                    next_processes = self.readyQueue[:num_to_assign] # get # of process from ready queue needed to fill CPU
                    self.CPUQueue.extend(next_processes)  # move next processes to the CPU 
                    for pcb in next_processes:
                        pcb.changeState('CPU')
                    self.readyQueue = self.readyQueue[num_to_assign:] 
                elif self.CPUQueue and self.IOQueue and not self.readyQueue: # if ready is empty, but IO still has processes continue
                    pass
                else:
                    if loopIteration > 1 and not self.readyQueue and not self.IOQueue and not self.CPUQueue and not self.waitQueue:
                        complete=True        
                    else: # running process has remaining CPU time, keep PCB in CPU,
                        pass   
            else:                                            # if cpu is empty add something, 1st loop only    
                
                self.readyQueue = sorted(self.readyQueue, key=lambda pcb: (pcb.priority),reverse=True)
                
                if loopIteration >=2 and self.readyQueue and (not self.CPUQueue or len(self.CPUQueue) < self.num_cpus): # are processes in readyqueue & is CPU not full
                    num_to_assign =min(self.num_cpus - len(self.CPUQueue), len(self.readyQueue))
                    next_processes = self.readyQueue[:num_to_assign] # get # of process from ready queue needed to fill CPU
                    self.CPUQueue.extend(next_processes)  # move next processes to the CPU 
                    for pcb in next_processes:
                        pcb.changeState('CPU')
                    self.readyQueue = self.readyQueue[num_to_assign:] 
                elif not self.readyQueue and self.IOQueue: # if ready is empty, but IO still has processes continue
                    pass
                else:
                    if loopIteration > 1 and not self.CPUQueue and not self.readyQueue and not self.IOQueue and not self.waitQueue:
                        complete=True                      
        
        # 6. check if any PCBs' in IO have current IO burst value == 0,  
            if self.IOQueue:
                next_IOprocesses =[] #container for next processes 
                
                # make  temp list of complete processes
                completeIOprocesses = [pcb for pcb in self.IOQueue if pcb.iobursts[0] == 0]
                    
                # update IO queue with only incomplete processes
                self.IOQueue = [pcb for pcb in self.IOQueue if pcb.iobursts[0] != 0]
                for pcb in self.IOQueue: # just to print the IO burst remaining time
                    pcb.remainingTime = pcb.iobursts[0]
                
                # add the IO complete process back to ready queue
                for pcb in completeIOprocesses:
                    pcb.changeState('Ready')
                self.readyQueue.extend(completeIOprocesses)
                self.readyQueue = [pcb for pcb in self.readyQueue if pcb.state =='Ready']  # update ready
                self.readyQueue = sorted(self.readyQueue, key=lambda pcb: (pcb.priority),reverse=True) # resort ready queue
                self.IOQueue = [pcb for pcb in self.IOQueue if pcb.state =='IO']  # update IO 
                # remove the io burst from the iobursts list in PCB
                for pcb in completeIOprocesses:
                    if pcb.iobursts[0] == 0:
                       pcb.iobursts.pop(0)
                # clear the temp complete IO processes list
                completeIOprocesses.clear()  
               
                #Add processes to IO if IO already exists
                if self.waitQueue and (not self.IOQueue or len(self.IOQueue) < self.num_ios): # are processes in waitqueue & is IO not full
                    num_to_assignIO = min(self.num_ios - len(self.IOQueue), len(self.waitQueue)) # get # of process from wait queue needed to fill IO
                    potentialIOprocesses = self.waitQueue[:num_to_assignIO] 
                    for pcb in potentialIOprocesses:
                        print(f'Potential next IO processes')
                        print(f'PID {pcb.pid}')
                        if pcb.waitTime >=1:
                            next_IOprocesses.append(pcb) # move next processes to the IO if they have been in wait 1 tick
                            pcb.changeState('IO')
                    
                    if next_IOprocesses:
                        for pcb in next_IOprocesses:
                            print(f'Actual next processes are')
                            print(f'PID {pcb.pid}')
                            pcb.changeState('IO') 
                        self.IOQueue.extend(next_IOprocesses)
                        next_IOprocesses.clear()
                       
                    self.waitQueue = self.waitQueue[num_to_assignIO:] # update wait
                    self.waitQueue =[pcb for pcb in self.waitQueue if pcb.state == 'Wait']
                    potentialIOprocesses = [pcb for pcb in potentialIOprocesses if pcb.state == 'Wait'] # keep processes not moved to IO
                    self.waitQueue.extend(potentialIOprocesses) # add  processes back that had not been in wait >=1 tick  
                    self.IOQueue = [pcb for pcb in self.IOQueue if pcb.state =='IO']  # update IO 
                    potentialIOprocesses.clear()
                    next_IOprocesses.clear()                                               
                    
                    
            else: # add processes to IO if IO currently empty
                next_IOprocesses =[]
                if self.waitQueue and (not self.IOQueue or len(self.IOQueue) < self.num_ios): # are processes in waitqueue & is IO empty or not full
                    num_to_assignIO = min(self.num_ios - len(self.IOQueue), len(self.waitQueue))# get # of process from wait queue needed to fill IO
                    potentialIOprocesses = self.waitQueue[:num_to_assignIO] #get processes that could be moved to io
                    for pcb in potentialIOprocesses:
                        print(f'Potential next IO processes')
                        print(f'PID {pcb.pid}')
                        if pcb.waitTime >=1:
                            next_IOprocesses.append(pcb) # actual next processes are those that have been in ready >1 tick
                            pcb.changeState('IO') 
                    
                    if next_IOprocesses:
                        for pcb in next_IOprocesses:
                            print(f'Actual next processes are')
                            print(f'PID {pcb.pid}')
                           
                        self.IOQueue.extend(next_IOprocesses)  # move next processes to the IO 
                        next_IOprocesses.clear()
                
                    self.waitQueue = self.waitQueue[num_to_assignIO:] #update the wait queue
                    self.waitQueue =[pcb for pcb in self.waitQueue if pcb.state == 'Wait']
                    potentialIOprocesses = [pcb for pcb in potentialIOprocesses if pcb.state == 'Wait'] # keeps pcb not moved to IO
                    self.waitQueue.extend(potentialIOprocesses)
                    self.IOQueue = [pcb for pcb in self.IOQueue if pcb.state == 'IO']  # update IO   self.waitQueue.extend(potentialIOprocesses) # add those processes back that had not been in wait >=1 tick 
                    potentialIOprocesses.clear()
                    next_IOprocesses.clear()
                     
                else:
                    pass
            time.sleep(.5)
            loopIteration += 1
            self.clock.advanceClock(1)
            
            
        #    # print the processes
            # for process_key, process_value in processes.items():
            #     for pcb_instance in process_value: 
            #         print(f'{process_key} status: CPU:{pcb_instance.cpubursts}; IO:{pcb_instance.iobursts}; {pcb_instance.currBurstType} : {pcb_instance.state}')
            
            clock=self.clock.currentTime()
            # Update the table contents
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'[bold][green]Process Progress Table[/bold][/green]')
            table.clear_rows()
            table.align['PID'] = 'l'
            table.add_row(["","N", [pcb.pid for pcb in self.newQueue]])
            table.add_row(["","R", [(pcb.pid, "p:",pcb.priority, "RT:",pcb.readyTime) for pcb in self.readyQueue]])
            table.add_row([clock,"C", [(pcb.pid, "p:", pcb.priority,"CPU:", pcb.remainingCPUTime) for pcb in self.CPUQueue]])
            table.add_row(["","W",[(pcb.pid, "p:", pcb.priority,"WT:",pcb.waitTime) for pcb in self.waitQueue]])
            table.add_row(["","I", [(pcb.pid,  "p:",pcb.priority, "IO:",pcb.remainingIOTime) for pcb in self.IOQueue]])
            table.add_row(["","F", [pcb.pid for pcb in self.finishedQueue]])
            

            #Print the table
            print(table)
            # input("press enter")
            # continue

        print(f'\n[bold][red] All processes have terminated[/red][/bold]\n')
        



if __name__=='__main__':
    #For loops here to run a set of FCFS then RR, then priority based
    sim = Simulator("small.dat",'2','3')
    # the stats class will need the simulation type and the loop number to tie to the output file name
    stats=Stats(sim.getProcesses(),sim.clock)
   
   
    
