import datetime

class Task:
    def __init__(self,activity):
        self.activity=activity
        self.completed=False
        self.nexttask=None
    def mark_completed(self):
        self.completed=True
        
class LinkedList:
    def __init__(self):
        self.head=None
        
    def add_task(self,activity):
        new_task=Task(activity)
        if  self.head is None:
            self.head=new_task
        else:
            current_task=self.head
            while current_task.nexttask:
                 current_task=current_task.nexttask
            current_task.nexttask=new_task
        
    def mark_completed(self,activity):
        current_task=self.head
        while current_task:
            if current_task.activity==activity:
                current_task.completed=True
                break
            current_task=current_task.nexttask
            
    
    def remove_completed_task(self):
        while self.head and self.head.completed:
            self.head=self.head.nexttask
            
        current_task=self.head
        while current_task and current_task.nexttask:
            if current_task.nexttask.completed:
                current_task.nexttask = current_task.nexttask.nexttask
            else: current_task=current_task.nexttask
            
            
    def print_to_do(self):
        current_task=self.head
        i=0
        while current_task:
            status='[X]' if current_task.completed else "[ ]"
            print(f'task{i}:{current_task.activity +status}')
            current_task=current_task.nexttask   
            i+=1
           


if __name__ =='__main__':
    to_do_list=LinkedList()
    current_date_and_time=datetime.datetime.now()
    print("current time:",current_date_and_time.strftime("%H:%M:%S"))
    print("current time:",current_date_and_time.strftime("%Y-%m-%d"))
    to_do_list.add_task('read_bible and pray')           
    to_do_list.add_task('read spirtual man')           
    to_do_list.add_task('read power electronics')           
    to_do_list.add_task('practice python')           
    to_do_list.add_task('learn java')  
    to_do_list.add_task('start self discipline by brian  tracy')  
     
    to_do_list.mark_completed('read_bible and pray')       
    to_do_list.mark_completed('read spirtual man')       
    to_do_list.mark_completed('start self discipline by brian  tracy')  
    to_do_list.print_to_do()   
      
            