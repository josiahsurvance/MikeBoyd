import json
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.storage.jsonstore import JsonStore
from kivy.core.window import Window
Window.clearcolor = (0.1, 0.1, 0.1, 0)

store = JsonStore('json_test_5.json')

print(store)
if store.exists("main"):
    pass
else:
    store.put("main", number=1)
    store.put("choice", number=2)

count = int(store.get('choice')['number'])
z = int(store.get('main')['number'])

class MainWindow(Screen):
    def update_count(self, y):
        global count
        self.ids.count.text = str(count)
        if y == 1:
            if count > 2:
                count -= 1
                self.ids.count.text = str(count)
                store.put("choice", number =count)
        elif y == 2:
            if count < 5:
                count += 1
                self.ids.count.text = str(count)
                store.put("choice", number=count)
        print(count)

    def next(self):
        global z
        global count
        store.put('main', number=2)
        print(count)
        if count == 2:
            sm.current = "two"
        elif count == 3:
            sm.current = "three"
        elif count == 4:
            sm.current = "four"
        elif count == 5:
            sm.current = "five"
        print("success")
        z = 2


class SecondWindow(Screen):
    def if_active(self, state):
        if state:
            print("True")
        else:
            print("False")
    def back(self):
        global z
        sm.current = "main"
        store.put('main', number=1)
        z = 1

class ThirdWindow(Screen):
    def if_active(self, state):
        if state:
            print("True")
        else:
            print("False")
    def back(self):
        global z
        sm.current = "main"
        store.put('main', number=1)
        z = 1

class FourthWindow(Screen):
    def if_active(self, state):
        if state:
            print("True")
        else:
            print("False")
    def back(self):
        global z
        sm.current = "main"
        store.put('main', number=1)
        z = 1

class FifthWindow(Screen):
    def if_active(self, state):
        if state:
            print("True")
        else:
            print("False")
    def back(self):
        global z
        sm.current = "main"
        store.put('main', number=1)
        z = 1

class WindowManager(ScreenManager):
    pass

Builder.load_string("""

<BackgroundColor@Widget>
    background_color: 1, 1, 1, 1
    canvas.before:
        Color:
            rgba: root.background_color
        Rectangle:
            size: self.size
            pos: self.pos

<BackgroundLabel@Label+BackgroundColor>
    background_color: 0, 0, 0, 0
    # to r 0, g 0, b 0, a 0
    
<MainWindow>:
    name: "main"

    GridLayout:
        cols: 1
        
        BackgroundLabel:
            text: 'How many checklist\\nitems would you like?'
            background_color: 0, 1, 1, 0.05
            
        GridLayout:
            cols: 3
            
            Button:
                text: '<'
                background_color: 0,1,1,0.8
                on_release:
                    root.update_count(1)
            Label:
                id: count
                text: ''
            Button:
                text: '>'
                background_color: 0,1,1,0.8
                on_release:
                    root.update_count(2)
        Button:
            text: "Next"
            background_color: 0, 1, 1, 0.1
            on_press: 
                root.next()
                
<SecondWindow>:
    name: "two"
    
    GridLayout:
        cols:1
        
        GridLayout:
            cols:2
            BackgroundLabel:
                text: 'Task #1'
                background_color: 0, 1, 1, 0.2
            CheckBox:
                group: "check"
                color: 1, 1, 1, 1
                on_active: root.if_active(self.active)
                canvas.before:
                    Color:
                        rgb: 1,1,1
                    Rectangle:
                        pos:self.center_x-8, self.center_y-8
                        size:[16,16]
                    Color:
                        rgb: 0,0,0
                    Rectangle:
                        pos:self.center_x-7, self.center_y-7
                        size:[14,14]
        GridLayout:
            cols:2               
            BackgroundLabel:
                text: 'Task #2'
                background_color: 0, 1, 1, 0.18
            CheckBox:
                group: "check2"
                color: 1, 1, 1, 1
                on_active: root.if_active(self.active)
                canvas.before:
                    Color:
                        rgb: 1,1,1
                    Rectangle:
                        pos:self.center_x-8, self.center_y-8
                        size:[16,16]
                    Color:
                        rgb: 0,0,0
                    Rectangle:
                        pos:self.center_x-7, self.center_y-7
                        size:[14,14]
        GridLayout:
            cols:1          
            Button:
                text: "Back"
                background_color: 0, 1, 1, 0.25
                on_press: 
                    root.back()
<ThirdWindow>:
    name: "three"
    
    GridLayout:
        cols:1
        
        GridLayout:
            cols:2
            BackgroundLabel:
                text: 'Task #1'
                background_color: 0, 1, 1, 0.2
            CheckBox:
                group: "check"
                color: 1, 1, 1, 1
                on_active: root.if_active(self.active)
                canvas.before:
                    Color:
                        rgb: 1,1,1
                    Rectangle:
                        pos:self.center_x-8, self.center_y-8
                        size:[16,16]
                    Color:
                        rgb: 0,0,0
                    Rectangle:
                        pos:self.center_x-7, self.center_y-7
                        size:[14,14]
        GridLayout:
            cols:2               
            BackgroundLabel:
                text: 'Task #2'
                background_color: 0, 1, 1, 0.18
            CheckBox:
                group: "check2"
                color: 1, 1, 1, 1
                on_active: root.if_active(self.active)
                canvas.before:
                    Color:
                        rgb: 1,1,1
                    Rectangle:
                        pos:self.center_x-8, self.center_y-8
                        size:[16,16]
                    Color:
                        rgb: 0,0,0
                    Rectangle:
                        pos:self.center_x-7, self.center_y-7
                        size:[14,14]
        GridLayout:
            cols:2               
            BackgroundLabel:
                text: 'Task #3'
                background_color: 0, 1, 1, 0.18
            CheckBox:
                group: "check3"
                color: 1, 1, 1, 1
                on_active: root.if_active(self.active)
                canvas.before:
                    Color:
                        rgb: 1,1,1
                    Rectangle:
                        pos:self.center_x-8, self.center_y-8
                        size:[16,16]
                    Color:
                        rgb: 0,0,0
                    Rectangle:
                        pos:self.center_x-7, self.center_y-7
                        size:[14,14]
        GridLayout:
            cols:1          
            Button:
                text: "Back"
                background_color: 0, 1, 1, 0.25
                on_press: 
                    root.back()
                    
<FourthWindow>:
    name: "four"
    
    GridLayout:
        cols:1
        
        GridLayout:
            cols:2
            BackgroundLabel:
                text: 'Task #1'
                background_color: 0, 1, 1, 0.2
            CheckBox:
                group: "check"
                color: 1, 1, 1, 1
                on_active: root.if_active(self.active)
                canvas.before:
                    Color:
                        rgb: 1,1,1
                    Rectangle:
                        pos:self.center_x-8, self.center_y-8
                        size:[16,16]
                    Color:
                        rgb: 0,0,0
                    Rectangle:
                        pos:self.center_x-7, self.center_y-7
                        size:[14,14]
        GridLayout:
            cols:2               
            BackgroundLabel:
                text: 'Task #2'
                background_color: 0, 1, 1, 0.18
            CheckBox:
                group: "check2"
                color: 1, 1, 1, 1
                on_active: root.if_active(self.active)
                canvas.before:
                    Color:
                        rgb: 1,1,1
                    Rectangle:
                        pos:self.center_x-8, self.center_y-8
                        size:[16,16]
                    Color:
                        rgb: 0,0,0
                    Rectangle:
                        pos:self.center_x-7, self.center_y-7
                        size:[14,14]
        GridLayout:
            cols:2               
            BackgroundLabel:
                text: 'Task #3'
                background_color: 0, 1, 1, 0.18
            CheckBox:
                group: "check3"
                color: 1, 1, 1, 1
                on_active: root.if_active(self.active)
                canvas.before:
                    Color:
                        rgb: 1,1,1
                    Rectangle:
                        pos:self.center_x-8, self.center_y-8
                        size:[16,16]
                    Color:
                        rgb: 0,0,0
                    Rectangle:
                        pos:self.center_x-7, self.center_y-7
                        size:[14,14]
        GridLayout:
            cols:2               
            BackgroundLabel:
                text: 'Task #4'
                background_color: 0, 1, 1, 0.18
            CheckBox:
                group: "check4"
                color: 1, 1, 1, 1
                on_active: root.if_active(self.active)
                canvas.before:
                    Color:
                        rgb: 1,1,1
                    Rectangle:
                        pos:self.center_x-8, self.center_y-8
                        size:[16,16]
                    Color:
                        rgb: 0,0,0
                    Rectangle:
                        pos:self.center_x-7, self.center_y-7
                        size:[14,14]
        GridLayout:
            cols:1          
            Button:
                text: "Back"
                background_color: 0, 1, 1, 0.25
                on_press: 
                    root.back()

<FifthWindow>:
    name: "five"
    
    GridLayout:
        cols:1
        
        GridLayout:
            cols:2
            BackgroundLabel:
                text: 'Task #1'
                background_color: 0, 1, 1, 0.2
            CheckBox:
                group: "check"
                color: 1, 1, 1, 1
                on_active: root.if_active(self.active)
                canvas.before:
                    Color:
                        rgb: 1,1,1
                    Rectangle:
                        pos:self.center_x-8, self.center_y-8
                        size:[16,16]
                    Color:
                        rgb: 0,0,0
                    Rectangle:
                        pos:self.center_x-7, self.center_y-7
                        size:[14,14]
        GridLayout:
            cols:2               
            BackgroundLabel:
                text: 'Task #2'
                background_color: 0, 1, 1, 0.18
            CheckBox:
                group: "check2"
                color: 1, 1, 1, 1
                on_active: root.if_active(self.active)
                canvas.before:
                    Color:
                        rgb: 1,1,1
                    Rectangle:
                        pos:self.center_x-8, self.center_y-8
                        size:[16,16]
                    Color:
                        rgb: 0,0,0
                    Rectangle:
                        pos:self.center_x-7, self.center_y-7
                        size:[14,14]
        GridLayout:
            cols:2               
            BackgroundLabel:
                text: 'Task #3'
                background_color: 0, 1, 1, 0.18
            CheckBox:
                group: "check3"
                color: 1, 1, 1, 1
                on_active: root.if_active(self.active)
                canvas.before:
                    Color:
                        rgb: 1,1,1
                    Rectangle:
                        pos:self.center_x-8, self.center_y-8
                        size:[16,16]
                    Color:
                        rgb: 0,0,0
                    Rectangle:
                        pos:self.center_x-7, self.center_y-7
                        size:[14,14]
        GridLayout:
            cols:2               
            BackgroundLabel:
                text: 'Task #4'
                background_color: 0, 1, 1, 0.18
            CheckBox:
                group: "check4"
                color: 1, 1, 1, 1
                on_active: root.if_active(self.active)
                canvas.before:
                    Color:
                        rgb: 1,1,1
                    Rectangle:
                        pos:self.center_x-8, self.center_y-8
                        size:[16,16]
                    Color:
                        rgb: 0,0,0
                    Rectangle:
                        pos:self.center_x-7, self.center_y-7
                        size:[14,14]
        GridLayout:
            cols:2               
            BackgroundLabel:
                text: 'Task #5'
                background_color: 0, 1, 1, 0.18
            CheckBox:
                group: "check5"
                color: 1, 1, 1, 1
                on_active: root.if_active(self.active)
                canvas.before:
                    Color:
                        rgb: 1,1,1
                    Rectangle:
                        pos:self.center_x-8, self.center_y-8
                        size:[16,16]
                    Color:
                        rgb: 0,0,0
                    Rectangle:
                        pos:self.center_x-7, self.center_y-7
                        size:[14,14]
        GridLayout:
            cols:1          
            Button:
                text: "Back"
                background_color: 0, 1, 1, 0.25
                on_press: 
                    root.back()
""")

sm = ScreenManager(transition=NoTransition())
main = MainWindow(name="main")
two = SecondWindow(name="two")
three = ThirdWindow(name="three")
four = FourthWindow(name="four")
five = FifthWindow(name="five")
sm.add_widget(main)
sm.add_widget(two)
sm.add_widget(three)
sm.add_widget(four)
sm.add_widget(five)

class MyMainApp(App):
    def build(self):
        return sm
    def on_start(self, **kwargs):
        global count
        global z
        print("count = " + str(count))
        print(type(count))
        print("z = " + str(z))
        print(type(z))
        if z == 2:
            if count == 2:
                sm.current = "two"
            elif count == 3:
                sm.current = "three"
            elif count == 4:
                sm.current = "four"
            elif count == 5:
                sm.current = "five"
        main.update_count(0)

if __name__ == "__main__":
    MyMainApp().run()
