import arcade
from typing import List
import question
# from threading import Thread


class Board(arcade.Window):
    def __init__(self, board_data: dict):
        width, height = arcade.get_display_size()
        super().__init__(width, height, resizable=True,
                         title="Jeopardy!")
        self.board_data = board_data
        self.padding = 0
        self.is_single = True
        self.round_data = self.board_data.get("single", [])
        self.blue = arcade.color_from_hex_string("060CE9")
        self.game_state: List[List[bool]] = \
            [[True for x in range(5)] for y in range(6)]

    def draw_categories(self):
        for idx, category in enumerate(self.round_data.get("categories")):

            arcade.Text(category.get("name", ""),
                        idx * self.scl_x + self.scl_x/2,
                        self.window_size[1] - self.scl_y / 2,
                        width=self.scl_x,
                        anchor_x="center",
                        anchor_y="center",
                        font_name=("Korinna",),
                        font_size=40,
                        align="center",
                        multiline=True
                        ).draw()

    def draw_questions(self):
        for idx, category in enumerate(self.round_data.get("categories")):
            for i in range(5):
                if self.game_state[idx][i]:
                    #print(self.game_state)
                    value = (i + 1) * 200
                else:
                    value = "---"
                if not self.is_single:
                    value *= 2
                arcade.Text('$' + str(value),
                            idx * self.scl_x + self.scl_x/2,
                            self.window_size[1] - (i + 1) *
                            self.scl_y - self.scl_y // 2,
                            width=self.scl_x,
                            anchor_x="center",
                            anchor_y="center",
                            font_name=("Korinna",),
                            font_size=50,
                            align="center",
                            multiline=True,
                            color=arcade.color.YELLOW
                            ).draw()

    def draw_grid(self):
        for x in range(6):
            arcade.draw_line(
                x * self.scl_x - 1.5,
                0,
                x * self.scl_x - 1.5,
                self.window_size[1],
                arcade.color.BLACK,
                4
                )

        for y in range(6):
            arcade.draw_line(0,
                             y * self.scl_y - 1.5,
                             self.window_size[0],
                             y * self.scl_y - 1.5,
                             arcade.color.BLACK,
                             4
                             )

    # Colors:
    # Background: #060CE9
    # Foreground: yellow
    def on_draw(self):
        self.window_size = self.get_size()
        self.scl_x = self.window_size[0] / 6
        self.scl_y = self.window_size[1] / 6
        arcade.start_render()
        arcade.set_background_color(self.blue)
        self.draw_grid()
        self.draw_categories()
        self.draw_questions()
        arcade.finish_render()

    def on_mouse_press(self, x, y, button, modifiers):
        b_x, b_y = (int(x // self.scl_x),
                    int((self.window_size[1] - y) // self.scl_y - 1))
        print(b_x, b_y)
        if b_x < 0 or b_y < 0:
            return
        self.game_state[b_x][b_y] = False
        question.Question_Screen(
            "Test Question", "Answer", 400, "TESTING"
        )
