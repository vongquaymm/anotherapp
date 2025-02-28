from kivy.lang import Builder
from kivymd.app import MDApp

gui = """
MDScreen:
    md_bg_color: 1,1,1,1
    MDBoxLayout:
        orientation: "vertical"
        adaptive_height: True
        spacing: "20dp"
        pos_hint: {"center_x":.5,"center_y":.6}

        Image:
            pos_hint: {"center_x":.5}
            source: "asset/mcclogo.png"
            size_hint_y:None
            size_hint_x:None
            height:'160dp'
            width:'160dp'
        MDLabel:
            text: "Welcome to MCC LOADER"
            halign: 'center'
            font_size: '20dp'
            bold: True
        MDLabel:
            text: "All in one loader for minecraft cheaters"
            halign: 'center'
            font_size: '15dp'
  
        MDRoundFlatButton:
            md_bg_color: 0,0,0,1
            pos_hint:{"center_x":.5}
            text: "[b]GET STARTED[/b]"
            text_color: 1, 1, 1, 1
            font_size: "20dp"
            markup : True
"""


class MainApp(MDApp):
    def build(self):
        return Builder.load_file(gui)
MainApp().run()
