import kivy
import random

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

red = [1,0,0,1]
green = [0,1,0,1]
blue =  [0,0,1,1]
purple = [1,0,1,1]
colors = [red, green, blue, purple]

class HBoxLayoutExample(App):
    def build(self):
        layout = BoxLayout(padding=10,spacing=10)
        self.bttns = []
        for i in range(5):
            btn = Button(text=f"Button {i+1}",
                         background_color=random.choice(colors)
                         )
            self.bttns.append(btn)
            layout.add_widget(btn)
            btn.bind(on_press=self.on_click)
        return layout

    def on_click(self,instance):
        print(f'You\'ve clicked button {instance.text}')
        for btn in self.bttns:
            btn.background_color=[random.random() for i in range(4)]

if __name__ == "__main__":
    app = HBoxLayoutExample()
    app.run()