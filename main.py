from kivy.app import App
from kivy.lang import Builder

kv = Builder.load_string(
"""
BoxLayout:
    spacing : 10
    orientation: "vertical"
    ActionBar:
        
        size_hint: (1, None)
        size: (root.width, 50)
        ActionView:
            ActionPrevious:
                title: "APP TEST"
                with_previous: True
            ActionButton:
                text : "Button 1"


    ScrollView:
        size_hint: (1, 0.2)
        do_scroll_x: True
        do_scroll_y: False
        GridLayout:
            padding: 10
            rows: 1
            size_hint_x: None
            width: self.minimum_width

            spacing : 20
            BoxLayout:
                size_hint: (None, None)
                size: (300, 150)
                canvas.before:
                    Color:
                        rgba: (1, 0, 0, 1)
                    RoundedRectangle:
                        size: self.size
                        pos: self.pos
                        radius: [20]
                Label:
                    text : "Text"
            BoxLayout:
                size_hint: (None, None)
                size: (300, 150)
                canvas.before:
                    Color:
                        rgba: (1, 0, 0, 1)
                    RoundedRectangle:
                        size: self.size
                        pos: self.pos
                        radius: [20]
                Label:
                    text : "Text"
            BoxLayout:
                size_hint: (None, None)
                size: (300, 150)
                canvas.before:
                    Color:
                        rgba: (1, 0, 0, 1)
                    RoundedRectangle:
                        size: self.size
                        pos: self.pos
                        radius: [20]
                Label:
                    text : "Text"
            BoxLayout:
                size_hint: (None, None)
                size: (300, 150)
                canvas.before:
                    Color:
                        rgba: (1, 0, 0, 1)
                    RoundedRectangle:
                        size: self.size
                        pos: self.pos
                        radius: [20]
                Label:
                    text : "Text"
            BoxLayout:
                size_hint: (None, None)
                size: (300, 150)
                canvas.before:
                    Color:
                        rgba: (1, 0, 0, 1)
                    RoundedRectangle:
                        size: self.size
                        pos: self.pos
                        radius: [20]
                Label:
                    text : "Text"
            BoxLayout:
                size_hint: (None, None)
                size: (300, 150)
                canvas.before:
                    Color:
                        rgba: (1, 0, 0, 1)
                    RoundedRectangle:
                        size: self.size
                        pos: self.pos
                        radius: [20]
                Label:
                    text : "Text"
            BoxLayout:
                size_hint: (None, None)
                size: (300, 150)
                canvas.before:
                    Color:
                        rgba: (1, 0, 0, 1)
                    RoundedRectangle:
                        size: self.size
                        pos: self.pos
                        radius: [20]
                Label:
                    text : "Text"
            BoxLayout:
                size_hint: (None, None)
                size: (300, 150)
                canvas.before:
                    Color:
                        rgba: (1, 0, 0, 1)
                    RoundedRectangle:
                        size: self.size
                        pos: self.pos
                        radius: [20]
                Label:
                    text : "Text"
            BoxLayout:
                size_hint: (None, None)
                size: (300, 150)
                canvas.before:
                    Color:
                        rgba: (1, 0, 0, 1)
                    RoundedRectangle:
                        size: self.size
                        pos: self.pos
                        radius: [20]
                Label:
                    text : "Text"
            BoxLayout:
                size_hint: (None, None)
                size: (300, 150)
                canvas.before:
                    Color:
                        rgba: (1, 0, 0, 1)
                    RoundedRectangle:
                        size: self.size
                        pos: self.pos
                        radius: [20]
                Label:
                    text : "Text"
            BoxLayout:
                size_hint: (None, None)
                size: (300, 150)
                canvas.before:
                    Color:
                        rgba: (1, 0, 0, 1)
                    RoundedRectangle:
                        size: self.size
                        pos: self.pos
                        radius: [20]
                Label:
                    text : "Text"
            BoxLayout:
                size_hint: (None, None)
                size: (300, 150)
                canvas.before:
                    Color:
                        rgba: (1, 0, 0, 1)
                    RoundedRectangle:
                        size: self.size
                        pos: self.pos
                        radius: [20]
                Label:
                    text : "Text"
            BoxLayout:
                size_hint: (None, None)
                size: (300, 150)
                canvas.before:
                    Color:
                        rgba: (1, 0, 0, 1)
                    RoundedRectangle:
                        size: self.size
                        pos: self.pos
                        radius: [20]
                Label:
                    text : "Text"
            BoxLayout:
                size_hint: (None, None)
                size: (300, 150)
                canvas.before:
                    Color:
                        rgba: (1, 0, 0, 1)
                    RoundedRectangle:
                        size: self.size
                        pos: self.pos
                        radius: [20]
                Label:
                    text : "Text"
            BoxLayout:
                size_hint: (None, None)
                size: (300, 150)
                canvas.before:
                    Color:
                        rgba: (1, 0, 0, 1)
                    RoundedRectangle:
                        size: self.size
                        pos: self.pos
                        radius: [20]
                Label:
                    text : "Text"
                    
                    
    ScrollView:
        
        size_hint_x:1
        size_hint_y: 0.5
        GridLayout:
            padding: 20
            cols:2
            spacing: 20
            size_hint_y: None
            height: self.minimum_height
            BoxLayout:
                size_hint_y: None
                height: 300
                canvas.before:
                    Color:
                        rgba: (1,0,0,1)
                    RoundedRectangle:
                        pos:self.pos
                        size: self.size

            BoxLayout:
                size_hint_y: None
                height: 300
                canvas.before:
                    Color:
                        rgba: (1,0,0,1)
                    RoundedRectangle:
                        pos:self.pos
                        size: self.size
            BoxLayout:
                size_hint_y: None
                height: 300
                canvas.before:
                    Color:
                        rgba: (1,0,0,1)
                    RoundedRectangle:
                        pos:self.pos
                        size: self.size

            BoxLayout:
                size_hint_y: None
                height: 300
                canvas.before:
                    Color:
                        rgba: (1,0,0,1)
                    RoundedRectangle:
                        pos:self.pos
                        size: self.size
            BoxLayout:
                size_hint_y: None
                height: 300
                canvas.before:
                    Color:
                        rgba: (1,0,0,1)
                    RoundedRectangle:
                        pos:self.pos
                        size: self.size

            BoxLayout:
                size_hint_y: None
                height: 300
                canvas.before:
                    Color:
                        rgba: (1,0,0,1)
                    RoundedRectangle:
                        pos:self.pos
                        size: self.size
            BoxLayout:
                size_hint_y: None
                height: 300
                canvas.before:
                    Color:
                        rgba: (1,0,0,1)
                    RoundedRectangle:
                        pos:self.pos
                        size: self.size

            BoxLayout:
                size_hint_y: None
                height: 300
                canvas.before:
                    Color:
                        rgba: (1,0,0,1)
                    RoundedRectangle:
                        pos:self.pos
                        size: self.size
            BoxLayout:
                size_hint_y: None
                height: 300
                canvas.before:
                    Color:
                        rgba: (1,0,0,1)
                    RoundedRectangle:
                        pos:self.pos
                        size: self.size

            BoxLayout:
                size_hint_y: None
                height: 300
                canvas.before:
                    Color:
                        rgba: (1,0,0,1)
                    RoundedRectangle:
                        pos:self.pos
                        size: self.size
            BoxLayout:
                size_hint_y: None
                height: 300
                canvas.before:
                    Color:
                        rgba: (1,0,0,1)
                    RoundedRectangle:
                        pos:self.pos
                        size: self.size

            BoxLayout:
                size_hint_y: None
                height: 300
                canvas.before:
                    Color:
                        rgba: (1,0,0,1)
                    RoundedRectangle:
                        pos:self.pos
                        size: self.size
            BoxLayout:
                size_hint_y: None
                height: 300
                canvas.before:
                    Color:
                        rgba: (1,0,0,1)
                    RoundedRectangle:
                        pos:self.pos
                        size: self.size

            BoxLayout:
                size_hint_y: None
                height: 300
                canvas.before:
                    Color:
                        rgba: (1,0,0,1)
                    RoundedRectangle:
                        pos:self.pos
                        size: self.size
            BoxLayout:
                size_hint_y: None
                height: 300
                canvas.before:
                    Color:
                        rgba: (1,0,0,1)
                    RoundedRectangle:
                        pos:self.pos
                        size: self.size

            BoxLayout:
                size_hint_y: None
                height: 300
                canvas.before:
                    Color:
                        rgba: (1,0,0,1)
                    RoundedRectangle:
                        pos:self.pos
                        size: self.size
"""
)

class main(App):
    def build(self):
        return kv

main().run()
