from kivy import utils
from kivy.app import App
from kivy.graphics.context_instructions import Color
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup


class MainApp(App):
    def build(self):
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = None
        self.last_button = None
        main_layout = BoxLayout(orientation="vertical", spacing=6)
        self.solution = TextInput(multiline=False, readonly=True, halign="right", font_size=55, background_color=[216/255,216/255,216/255,1])
        main_layout.add_widget(self.solution)
        buttons = [["7", "8", "9", "/"], ["4", "5", "6", "*"], ["1", "2", "3", "-"], [".", "0", "C", "+"]]
        self.buttons = {}
        for row in buttons:
            h_layout = BoxLayout(spacing=6)
            for label in row:
                button = Button(text=label, pos_hint={"center_x": 0.5, "center_y": 0.5},background_color = utils.get_color_from_hex('#ff8c4e'), background_normal='', color=[0,0,0,1], font_size=30)
                self.buttons[label] = button
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        for i in range(10):
            self.buttons[str(i)].background_color= utils.get_color_from_hex('#ffbb4e')
        equals_button = Button(text="=", pos_hint={"center_x": 0.5, "center_y": 0.5},background_color = utils.get_color_from_hex('#ff634e'), color=[0,0,0,1],font_size=30)
        equals_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equals_button)
        return main_layout

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text
        if button_text == "C":
            # Clear the solution widget
            self.solution.text = ""
        else:
            if current and (
                    self.last_was_operator and button_text in self.operators):
                # Don't add two operators right after each other
                return
            elif current == "" and button_text in self.operators:
                # First character cannot be an operator
                return
            else:
                new_text = current + button_text
                self.solution.text = new_text
        self.last_button = button_text

        self.last_was_operator = self.last_button in self.operators
    def on_solution(self, instance):
        try:
            text = self.solution.text
            if text:
                solution = str(eval(self.solution.text))
                self.solution.text = solution
        except:
            content = Button(text="Close")
            pop_up = Popup(title="Something went wrong", content=content, size_hint=(.25,.25))
            content.bind(on_press=pop_up.dismiss)
            pop_up.open()
            self.solution.text = ""

if __name__ == "__main__":
    app = MainApp()
    app.run()