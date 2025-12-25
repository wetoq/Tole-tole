from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.core.image import Image as CoreImage

class GameWidget(Widget):
    def init(self, **kwargs):
        super().init(**kwargs)
        # Загружаем фон и игрока (те же файлы, что были в Pygame)
        self.background = CoreImage("background.png").texture
        self.player_texture = CoreImage("player.png").texture
        
        self.player_pos = [100, 100]
        
        # Запуск игрового цикла (60 кадров в секунду)
        Clock.schedule_interval(self.update, 1.0 / 60.0)

    def update(self, dt):
        # Очищаем и рисуем всё заново
        self.canvas.clear()
        with self.canvas:
            # Рисуем фон на весь экран
            Rectangle(texture=self.background, pos=(0, 0), size=Window.size)
            
            # Рисуем игрока
            Rectangle(texture=self.player_texture, pos=self.player_pos, size=(100, 100))

    def on_touch_move(self, touch):
        # Движение игрока пальцем по экрану
        self.player_pos = [touch.x - 50, touch.y - 50]

class ToleToleApp(App):
    def build(self):
        return GameWidget()

if name == 'main':
    ToleToleApp().run()
