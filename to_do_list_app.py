from kivy.app import App
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import  FloatLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import to_do_list_logic as td
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label


Config.set('graphics','width','400')
Config.set('graphics','length','300')
class TODoList(App):
    def build(self):
        layout=BoxLayout(orientation= 'vertical',size=(300,300))     
        
        self.text_input=TextInput(hint_text='Enter a task...')
        
        layout.add_widget(self.text_input)
        
        add_button=Button(text='Add Task', on_press=self.add_task)
        layout.add_widget(add_button)
        
        self.task_list=td.LinkedList()
        
        self.scroll_view=ScrollView()
        layout.add_widget(self.scroll_view)
        
        self.completed_scroll_view=ScrollView()
        layout.add_widget(self.completed_scroll_view)
        
        completed_button=Button(text='Completed',on_press=self.mark_task_completed)
        
        layout.add_widget(completed_button)
        return layout
    
    
    def add_task(self,instance):
        task_text=self.text_input.text
        self.task_list.add_task(task_text)
        
        self.task_list.print_to_do()
        
        self.display_tasks()
        
        self.text_input.text=" "
        
        
        
    def display_tasks(self):
        self.scroll_view.clear_widgets()
        self.completed_scroll_view.clear_widgets()
        
        current_task=self.task_list.head
        tasks_text=" "
        completed_task_text=""
        while current_task:
            if current_task.completed:
                completed_task_text+=f"{current_task.activity}\n"
            else:
                tasks_text+=f"{current_task.activity}\n"    
            
            current_task=current_task.nexttask
            
        tasks_label=Label(text=tasks_text,font_size=20)
        completed_task_label=Label(text=completed_task_text,font_size=20)
        
        
        
        self.scroll_view.add_widget(tasks_label)
        self.completed_scroll_view.add_widget(completed_task_label)
        
    def mark_task_completed(self,instance):
        task_text=instance.text  
        current_task=self.task_list.head
        while current_task:
            if current_task.activity==task_text:
                current_task.mark_completed()
                break
            current_task=current_task.nexttask
            
        self.display_tasks()
        
        


if __name__=='__main__':
    TODoList().run()
        