import arcade


class Question_Screen(arcade.Window):
    def __init__(self, question_text: str,
                 question_answer: str,
                 question_value: int,
                 question_category: str):
        width, height = arcade.get_display_size()
        super().__init__(width, height, resizable=True,
                         title=f"{question_category} for {question_value}", fullscreen=True)
        self.text = question_text
        self.answ = question_answer
        self.val = question_value
        self.cat = question_category
        self.is_revealed = False

    def on_draw(self):
        self.window_size = self.get_size()
        arcade.start_render()
        arcade.set_background_color(arcade.color_from_hex_string("060CE9"))
        arcade.Text(self.text, self.window_size[0] / 2,
                    self.window_size[1] - 100,
                    align="center",
                    anchor_x="center",
                    anchor_y="center",
                    font_size=40,
                    width=self.window_size[0]).draw()        
        arcade.finish_render()
        
    def on_mouse_press(self, x, y, button, modifiers):
        pass
