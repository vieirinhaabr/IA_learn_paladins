from pynput import mouse, keyboard
import chronometer

class Control_List:
    def __init__(self):
        self.moves = []
        self.short_list = []
        self.initial_time = 0
        self.time_zone = None

    def short_list_add(self):
        pass

    def on_press(self, key):
        print('alphanumeric key {0} pressed'.format(
            key.char))

    def on_release(self, key):
        print('{0} released'.format(
            key))

    def on_move(self, x, y):
        print('Pointer moved to {0}'.format(
            (x, y)))

    def on_click(self, x, y, button, pressed):
        print('{0} at {1}'.format(
            'Pressed' if pressed else 'Released',
            (x, y, button)))

class Controller:
    Moves = Control_List()
    with mouse.Listener(
            on_move=Moves.on_move,
            on_click=Moves.on_click) as listener_mouse:

        with keyboard.Listener(
                on_press=Moves.on_press,
                on_release=Moves.on_release) as listener_keyboard:

            listener_keyboard.join()
            listener_mouse.join()
