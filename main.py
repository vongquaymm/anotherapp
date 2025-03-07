from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.screen import MDScreen
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.label import MDLabel

gui = '''

ScreenManager:
    HomeScreen:
    ClientScreen:
<HomeScreen@MDScreen>
    name: "home_page"
    md_bg_color: 1,1,1,1
    MDBoxLayout:
        size_hint: None, None
        adaptive_size: True
        spacing: "15dp"
        orientation: "vertical"
        pos_hint: {"center_x":.5, "center_y":.6}
        Image:
            source: "asset/mcclogo.png"
            size_hint: None, None
            size: "150dp","150dp"
            pos_hint: {"center_x": .5}
        MDLabel:
            text: "MCC LOADER"
            bold: True
            halign: "center"
            font_size: "20dp"
            pos_hint: {"center_x":.5}
        MDLabel:
            text: "A free all-in-one clients downloader for Minecraft Cheater"
            halign: "center"
            font_style: "Caption"
            adaptive_height: True
        MDRoundFlatButton:
            md_bg_color: 0,0,0,1
            pos_hint: {"center_x": .5}
            text: "[b]GET STARTED[/b]"
            font_size: "20dp"
            markup: True
            line_color: 0,0,0,1
            text_color: 1,1,1,1   
            on_press: app.root.current = "client_page"
<ClientScreen@Screen>:
    name: "client_page"
    MDBoxLayout:
        orientation: "vertical"
        MDTopAppBar:
            md_bg_color: 0,0,0,1
            left_action_items: [["home", lambda x: app.switch_to_home()]]
            right_action_items: [["youtube", lambda x: app.callback()], ["forum", lambda x: app.callback()],]
            title: "MCC Loader"
        MDBottomNavigation:
            type: "large"
            MDBottomNavigationItem:
                name: "Home"
                icon: "home"
                text: "Home"
                MDScreen:
                    ScrollView:
                        bar_width: 0
                        MDBoxLayout:
                            orientation: "vertical"
                            padding: "15dp"
                            adaptive_height: True
                            spacing: "15dp"
                            MDLabel:
                                text: "HOT CLIENTS"
                                font_style: "Subtitle2"
                            ScrollView:
                                bar_width: 0
                                size_hint_y: None
                                height: "150dp"
                                MDBoxLayout:
                                    spacing: "15dp"
                                    adaptive_width: True
                                    Image:
                                        source: "asset/vape.png"
                                        size_hint: None, None
                                        size: "150dp", "150dp"
                                    Image:
                                        source: "asset/rise.png"
                                        size_hint: None, None
                                        size: "150dp", "150dp"
                                    Image:
                                        source: "asset/raven.png"
                                        size_hint: None, None
                                        size: "150dp", "150dp"
                                    Image:
                                        source: "asset/slinky.png"
                                        size_hint: None, None
                                        size: "150dp", "150dp"
                                    Image:
                                        source: "asset/liquidbounce.png"
                                        size_hint: None, None
                                        size: "150dp", "150dp"
                                    Image:
                                        source: "asset/fdp.png"
                                        size_hint: None, None
                                        size: "150dp", "150dp"
                                    Image:
                                        source: "asset/breeze.png"
                                        size_hint: None, None
                                        size: "150dp", "150dp"
                                    
                            MDLabel:
                                text: "CLIENT CREDITS"
                                font_style: "Subtitle2"

                            MDGridLayout:
                                spacing: "15dp"
                                cols : 1
                                adaptive_height: True
                                CreditCard:
                                    avatar: "asset/lusvy.webp"
                                    credit_name: "luvsy's crib"

                                CreditCard:
                                    avatar: "asset/vape.jpg"
                                    credit_name: "fled."

                                CreditCard:
                                    avatar: "asset/vape.jpg"
                                    credit_name: "Ghost"

                                CreditCard:
                                    avatar: "asset/vape.jpg"
                                    credit_name: "WonderLand Library"
                                CreditCard:
                                
                                    avatar: "asset/vape.jpg"
                                    credit_name: "CookieAC"

                                CreditCard:
                                    avatar: "asset/googlechrome.png"
                                    credit_name: "MimHax"

                                CreditCard:
                                    avatar: "asset/vape.jpg"
                                    credit_name: "Trillium INC."

                                CreditCard:
                                    avatar: "asset/vape.jpg"
                                    credit_name: "Splash Software"

                                CreditCard:
                                    avatar: "asset/themilkarchive.webp"
                                    credit_name: "The Milk Archive"
            MDBottomNavigationItem:
                name: "Ghost"
                icon: "ghost"
                text: "Ghost"
                MDScreen:
                    MDBoxLayout:
                        orientation: "vertical"
                        padding: "15dp"
                        spacing: "10dp"
                        ScrollView:
                            bar_width: 0
                            MDGridLayout:
                                cols: 4
                                spacing: "10dp"
                                adaptive_height: True
                                id: ghost_menu

                

            MDBottomNavigationItem:
                name: "Blatant"
                icon: "home"
                text: "Blatant"
                MDScreen:
                    MDBoxLayout:
                        orientation: "vertical"
                        padding: "15dp"
                        spacing: "10dp"
                        ScrollView:
                            bar_width: 0
                            MDGridLayout:
                                cols: 4
                                spacing: "10dp"
                                adaptive_height: True
                                id: blatant_menu


            
            MDBottomNavigationItem:
                name: "Search"
                icon: "magnify"
                text: "Search"
                MDScreen:
                    bar_width: 0
                    MDBoxLayout: 
                        adaptive_height: True
                        padding: "15dp"
                        spacing: "15dp"
                        orientation: "vertical"
                        MDBoxLayout:
                            adaptive_height: True
                            MDTextField:
                                id: client_search
                                hint_text: "Search.."
                                multiline: False
                                mode: "rectangle"
                        ScrollView:
                            bar_width: 0
                            MDGridLayout:
                                cols: 4
                                spacing: "10dp"
                                adaptive_height: True
                                id: search_menu



<CreditCard@MDCard>:

    orientation: "horizontal"
    spacing: "15dp"
    padding: "10dp"
    size_hint_y: None
    height: "100dp"
    credit_name: ''
    radius: 25
    

    Image:
        source: "asset/discord.png"
        size_hint: None, None
        size: "80dp", "80dp"


    MDBoxLayout:
        orientation: "vertical"
        MDLabel:
            text: root.credit_name
            font_size: "20dp"
            bold: True
<ClientCard@MDCard>:
    ripple_behavior: True
    size_hint_y: None
    height: "100dp"
    orientation: "vertical"
    client_image: ""
    client_name: ""
    spacing: "5dp"
    MDBoxLayout:
        orientation: "vertical"
        padding: "5dp"
        spacing: "10dp"
        Image:
            source: root.client_image
            size_hint: None, None
            size: "50dp", "50dp"
            pos_hint: {"center_x":.5}
        MDLabel:
            text: root.client_name
            adaptive_height: True
            halign: "center"
        MDRaisedButton:
            elevation: 0
            text: "DOWNLOAD"
            adaptive_size: True
            pos_hint:{"center_x": .5}





'''

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(gui)
    def on_start(self):
        pass
    def switch_to_home(self):
        self.root.current = "home_page"
    def callback(self):
        print("ok")
MainApp().run()
