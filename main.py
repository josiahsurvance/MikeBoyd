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
from kivy.core.audio import SoundLoader
Window.clearcolor = (0.1, 0.1, 0.1, 0)

store = JsonStore('json_test_5.json')
sound1 = SoundLoader.load('Sound 1.wav')
sound2 = SoundLoader.load("Sound 2.wav")
sound3 = SoundLoader.load("Sound 3.wav")

if store.exists("main"):
    pass
else:
    store.put("main", number=1)
    store.put("choice", number=2)
    store.put("second_screen", one=1, two=1)
    store.put("third_screen", one=1, two=1, three=1)
    store.put("fourth_screen", one=1, two=1, three=1, four=1)
    store.put("fifth_screen", one=1, two=1, three=1, four=1, five=1)

count = int(store.get('choice')['number'])
z = int(store.get('main')['number'])
SecondWindow_on_off = [int(store.get("second_screen")["one"]), int(store.get("second_screen")["two"])]
ThirdWindow_on_off = [int(store.get("third_screen")["one"]), int(store.get("third_screen")["two"]), int(store.get("third_screen")["three"])]
FourthWindow_on_off = [int(store.get("fourth_screen")["one"]), int(store.get("fourth_screen")["two"]), int(store.get("fourth_screen")["three"]), int(store.get("fourth_screen")["four"])]
FifthWindow_on_off = [int(store.get("fifth_screen")["one"]), int(store.get("fifth_screen")["two"]), int(store.get("fifth_screen")["three"]), int(store.get("fifth_screen")["four"]), int(store.get("fifth_screen")["five"])]

class MainWindow(Screen):
    def update_count(self, y):
        global count
        self.ids.count.text = str(count)
        if y == 1:
            if count > 2:
                count -= 1
                self.ids.count.text = str(count)
                store.put("choice", number=count)
        elif y == 2:
            if count < 5:
                count += 1
                self.ids.count.text = str(count)
                store.put("choice", number=count)
        two.initial_on_off()
        three.initial_on_off()
        four.initial_on_off()
        five.initial_on_off()
    def next(self):
        global z
        global count
        store.put('main', number=2)
        if count == 2:
            sm.current = "two"
            three.reset()
            four.reset()
            five.reset()
        elif count == 3:
            sm.current = "three"
            two.reset()
            four.reset()
            five.reset()
        elif count == 4:
            sm.current = "four"
            two.reset()
            three.reset()
            five.reset()
        elif count == 5:
            sm.current = "five"
            two.reset()
            three.reset()
            four.reset()
        z = 2


class SecondWindow(Screen):
    def if_active(self, state, a):
        global SecondWindow_on_off
        if a == 1:
            if state:
                SecondWindow_on_off[0] = 2
                if SecondWindow_on_off[0] == 2 and SecondWindow_on_off[1] ==2:
                    sound3.play()
                else:
                    sound1.play()
            else:
                SecondWindow_on_off[0] = 1
        elif a == 2:
            if state:
                SecondWindow_on_off[1] = 2
                if SecondWindow_on_off[0] == 2 and SecondWindow_on_off[1] ==2:
                    sound3.play()
                else:
                    sound2.play()
            else:
                SecondWindow_on_off[1] = 1
        store.put("second_screen", one = SecondWindow_on_off[0], two = SecondWindow_on_off[1])
    def back(self):
        global z
        sm.current = "main"
        store.put('main', number=1)
        z = 1
    def reset(self):
        self.ids.first.active = False
        self.ids.second.active = False
    def initial_on_off(self):
        if int(store.get("second_screen")["one"]) == 2:
            self.ids.first.active = True
        if int(store.get("second_screen")["two"]) == 2:
            self.ids.second.active = True

class ThirdWindow(Screen):
    def if_active(self, state, a):
        global ThirdWindow_on_off
        if state:
            if a == 1:
                ThirdWindow_on_off[0] = 2
            elif a == 2:
                ThirdWindow_on_off[1] = 2
            elif a == 3:
                ThirdWindow_on_off[2] = 2
        else:
            if a == 1:
                ThirdWindow_on_off[0] = 1
            elif a == 2:
                ThirdWindow_on_off[1] = 1
            elif a == 3:
                ThirdWindow_on_off[2] = 1
        store.put("third_screen", one=ThirdWindow_on_off[0], two=ThirdWindow_on_off[1], three=ThirdWindow_on_off[2])
    def back(self):
        global z
        sm.current = "main"
        store.put('main', number=1)
        z = 1
    def reset(self):
        self.ids.first.active = False
        self.ids.second.active = False
        self.ids.third.active = False
    def initial_on_off(self):
        if int(store.get("third_screen")["one"]) == 2:
            self.ids.first.active = True
        if int(store.get("third_screen")["two"]) == 2:
            self.ids.second.active = True
        if int(store.get("third_screen")["three"]) == 2:
            self.ids.third.active = True

class FourthWindow(Screen):
    def if_active(self, state, a):
        global FourthWindow_on_off
        if state:
            if a == 1:
                FourthWindow_on_off[0] = 2
            elif a == 2:
                FourthWindow_on_off[1] = 2
            elif a == 3:
                FourthWindow_on_off[2] = 2
            elif a == 4:
                FourthWindow_on_off[3] = 2
        else:
            if a == 1:
                FourthWindow_on_off[0] = 1
            elif a == 2:
                FourthWindow_on_off[1] = 1
            elif a == 3:
                FourthWindow_on_off[2] = 1
            elif a == 4:
                FourthWindow_on_off[3] = 1
        store.put("fourth_screen", one=FourthWindow_on_off[0], two=FourthWindow_on_off[1], three=FourthWindow_on_off[2],
                  four=FourthWindow_on_off[3])
    def back(self):
        global z
        sm.current = "main"
        store.put('main', number=1)
        z = 1
    def reset(self):
        self.ids.first.active = False
        self.ids.second.active = False
        self.ids.third.active = False
        self.ids.fourth.active = False
    def initial_on_off(self):
        if int(store.get("fourth_screen")["one"]) == 2:
            self.ids.first.active = True
        if int(store.get("fourth_screen")["two"]) == 2:
            self.ids.second.active = True
        if int(store.get("fourth_screen")["three"]) == 2:
            self.ids.third.active = True
        if int(store.get("fourth_screen")["four"]) == 2:
            self.ids.fourth.active = True

class FifthWindow(Screen):
    def if_active(self, state, a):
        global FifthWindow_on_off
        if state:
            if a == 1:
                FifthWindow_on_off[0] = 2
            elif a == 2:
                FifthWindow_on_off[1] = 2
            elif a == 3:
                FifthWindow_on_off[2] = 2
            elif a == 4:
                FifthWindow_on_off[3] = 2
            elif a == 5:
                FifthWindow_on_off[4] = 2
        else:
            if a == 1:
                FifthWindow_on_off[0] = 1
            elif a == 2:
                FifthWindow_on_off[1] = 1
            elif a == 3:
                FifthWindow_on_off[2] = 1
            elif a == 4:
                FifthWindow_on_off[3] = 1
            elif a == 5:
                FifthWindow_on_off[4] = 1
        store.put("fifth_screen", one=FifthWindow_on_off[0], two=FifthWindow_on_off[1], three=FifthWindow_on_off[2], four=FifthWindow_on_off[3], five=FifthWindow_on_off[4])
    def back(self):
        global z
        sm.current = "main"
        store.put('main', number=1)
        z = 1
    def reset(self):
        self.ids.first.active = False
        self.ids.second.active = False
        self.ids.third.active = False
        self.ids.fourth.active = False
        self.ids.fifth.active = False
    def initial_on_off(self):
        if int(store.get("fifth_screen")["one"]) == 2:
            self.ids.first.active = True
        if int(store.get("fifth_screen")["two"]) == 2:
            self.ids.second.active = True
        if int(store.get("fifth_screen")["three"]) == 2:
            self.ids.third.active = True
        if int(store.get("fifth_screen")["four"]) == 2:
            self.ids.fourth.active = True
        if int(store.get("fifth_screen")["five"]) == 2:
            self.ids.fifth.active = True

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
                id: first
                color: 1, 1, 1, 1
                on_active: root.if_active(self.active, 1)
        GridLayout:
            cols:2               
            BackgroundLabel:
                text: 'Task #2'
                background_color: 0, 1, 1, 0.18
            CheckBox:
                id: second
                group: "check2"
                color: 1, 1, 1, 1
                on_active: root.if_active(self.active, 2)
        GridLayout:
            cols: 2          
            Button:
                text: "Back"
                background_color: 0, 1, 1, 0.25
                on_press: 
                    root.back()
            Button:
                text: "Reset"
                background_color: 0, 1, 1, 0.25
                on_press:
                    root.reset()
                
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
                id: first
                group: "check"
                color: 1, 1, 1, 1
                on_active: root.if_active(self.active, 1)
        GridLayout:
            cols:2               
            BackgroundLabel:
                text: 'Task #2'
                background_color: 0, 1, 1, 0.18
            CheckBox:
                id: second
                group: "check2"
                color: 1, 1, 1, 1
                on_active: root.if_active(self.active, 2)
        GridLayout:
            cols:2               
            BackgroundLabel:
                text: 'Task #3'
                background_color: 0, 1, 1, 0.16
            CheckBox:
                id: third
                group: "check3"
                color: 1, 1, 1, 1
                on_active: root.if_active(self.active, 3)
        GridLayout:
            cols: 2          
            Button:
                text: "Back"
                background_color: 0, 1, 1, 0.25
                on_press: 
                    root.back()
            Button:
                text: "Reset"
                background_color: 0, 1, 1, 0.25
                on_press:
                    root.reset()
                    
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
                id: first
                group: "check"
                color: 1, 1, 1, 1
                on_active: root.if_active(self.active, 1)
        GridLayout:
            cols:2               
            BackgroundLabel:
                text: 'Task #2'
                background_color: 0, 1, 1, 0.18
            CheckBox:
                id: second
                group: "check2"
                color: 1, 1, 1, 1
                on_active: root.if_active(self.active, 2)
        GridLayout:
            cols:2               
            BackgroundLabel:
                text: 'Task #3'
                background_color: 0, 1, 1, 0.16
            CheckBox:
                id: third
                group: "check3"
                color: 1, 1, 1, 1
                on_active: root.if_active(self.active, 3)
        GridLayout:
            cols:2               
            BackgroundLabel:
                text: 'Task #4'
                background_color: 0, 1, 1, 0.14
            CheckBox:
                id: fourth
                group: "check4"
                color: 1, 1, 1, 1
                on_active: root.if_active(self.active, 4)
        GridLayout:
            cols: 2          
            Button:
                text: "Back"
                background_color: 0, 1, 1, 0.25
                on_press: 
                    root.back()
            Button:
                text: "Reset"
                background_color: 0, 1, 1, 0.25
                on_press:
                    root.reset()

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
                id: first
                group: "check"
                color: 1, 1, 1, 1
                on_active: root.if_active(self.active, 1)
        GridLayout:
            cols:2               
            BackgroundLabel:
                text: 'Task #2'
                background_color: 0, 1, 1, 0.18
            CheckBox:
                id: second
                group: "check2"
                color: 1, 1, 1, 1
                on_active: root.if_active(self.active, 2)
        GridLayout:
            cols:2               
            BackgroundLabel:
                text: 'Task #3'
                background_color: 0, 1, 1, 0.16
            CheckBox:
                id: third
                group: "check3"
                color: 1, 1, 1, 1
                on_active: root.if_active(self.active, 3)
        GridLayout:
            cols:2               
            BackgroundLabel:
                text: 'Task #4'
                background_color: 0, 1, 1, 0.14
            CheckBox:
                id: fourth
                group: "check4"
                color: 1, 1, 1, 1
                on_active: root.if_active(self.active, 4)
        GridLayout:
            cols:2               
            BackgroundLabel:
                text: 'Task #5'
                background_color: 0, 1, 1, 0.12
            CheckBox:
                id: fifth
                group: "check5"
                color: 1, 1, 1, 1
                on_active: root.if_active(self.active, 5)
        GridLayout:
            cols: 2          
            Button:
                text: "Back"
                background_color: 0, 1, 1, 0.25
                on_press: 
                    root.back()
            Button:
                text: "Reset"
                background_color: 0, 1, 1, 0.25
                on_press:
                    root.reset()
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
