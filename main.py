import hashlib
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window

# جعل التطبيق يملأ الشاشة بالكامل ومنع إغلاقه بسهولة (في بيئة الاختبار)
Window.fullscreen = 'auto'

class LockScreen(App):
    def build(self):
        # تشفير كلمة السر الأصلية (SHA-256) لجعلها غير واضحة في الكود
        self.correct_pass_hash = "7739507f30089e931e0840f10e4a7702f74e644917904084f72412803b984534" # رمز: 1234500@@
        
        self.layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        
        # تغيير خلفية الشاشة للأسود
        with self.layout.canvas.before:
            import kivy.graphics
            kivy.graphics.Color(0, 0, 0, 1) # أسود
            self.rect = kivy.graphics.Rectangle(size=Window.size, pos=self.layout.pos)

        self.label = Label(text="SYSTEM LOCKED\nEnter Password to Unlock", font_size=30, color=(1, 0, 0, 1))
        self.pass_input = TextInput(password=True, multiline=False, size_hint=(1, 0.2), font_size=40)
        self.unlock_btn = Button(text="UNLOCK", background_color=(0, 1, 0, 1), size_hint=(1, 0.2))
        self.unlock_btn.bind(on_press=self.check_password)

        self.layout.add_widget(self.label)
        self.layout.add_widget(self.pass_input)
        self.layout.add_widget(self.unlock_btn)
        
        return self.layout

    def check_password(self, instance):
        # تشفير القيمة المدخلة ومقارنتها بالهاش المحفوظ
        user_input = self.pass_input.text
        input_hash = hashlib.sha256(user_input.encode()).hexdigest()

        if input_hash == self.correct_pass_hash:
            self.stop() # يغلق التطبيق ويعود الهاتف لطبيعته
        else:
            self.label.text = "WRONG PASSWORD! TRY AGAIN"
            self.pass_input.text = ""

if __name__ == '__main__':
    LockScreen().run()
