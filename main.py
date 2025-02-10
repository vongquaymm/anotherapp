from threading import Thread
import time
from kivy.clock import Clock

class Myroot(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", spacing=20, padding=20, **kwargs)
        
        self.elapsed_time = 0.0
        self.start_time = 0.0
        self.running = False
        self.time_displayed = Label(text="0.000s", font_size=80, size_hint=(1, 0.5))

        self.BtnLayout = BoxLayout(orientation="horizontal", spacing=15, size_hint=(1, 0.3))

        self.btn_start = Button(text="Start", font_size=30, size_hint=(1, 1), on_press=self.Start_timer)
        self.btn_stop = Button(text="Stop", font_size=30, size_hint=(1, 1), on_press=self.Stop_timer)
        self.btn_reset = Button(text="Reset", font_size=30, size_hint=(1, 1), on_press=self.Reset_timer)

        self.BtnLayout.add_widget(self.btn_start)
        self.BtnLayout.add_widget(self.btn_stop)
        self.BtnLayout.add_widget(self.btn_reset)

        self.add_widget(self.time_displayed)
        self.add_widget(self.BtnLayout)

        # Tạo luồng riêng để cập nhật thời gian nhanh hơn
        self.update_thread = Thread(target=self.update_time_thread, daemon=True)
        self.update_thread.start()

        # Chạy luồng nhận tín hiệu Bluetooth
        Thread(target=self.recvsignal_thread, daemon=True).start()

    def update_time_thread(self):
        """Luồng riêng cập nhật thời gian liên tục mà không delay."""
        while True:
            if self.running:
                self.elapsed_time = time.time() - self.start_time
                Clock.schedule_once(lambda dt: self.update_ui())

    def update_ui(self):
        """Cập nhật giao diện từ luồng chính."""
        self.time_displayed.text = f"{self.elapsed_time:.3f} giây"

    def Start_timer(self, instance):
        if not self.running:
            self.running = True
            self.start_time = time.time() - self.elapsed_time
            sendsignal("1")

    def Stop_timer(self, instance):
        self.running = False
        sendsignal("0")

    def Reset_timer(self, instance):
        self.running = False
        self.elapsed_time = 0.0
        self.start_time = 0.0
        Clock.schedule_once(lambda dt: self.update_ui())
        sendsignal("0")
