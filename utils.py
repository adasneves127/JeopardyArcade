# import arcade

class Question:
    def __init__(self, value, category, question, answer, is_dd):
        self.value = value
        self.question = question
        self.answer = answer
        self.is_dd = is_dd
        self.category = category
        self.isRevealed = False


class BoardDataClass:
    def __init__(self, board_data: list[list[Question]]):
        self.board_list = board_data
        self.categories = list(set(
            [x[0].category for x in board_data]
        ))
    
    def draw(self):
        for row in self.board_data:
            for cell in row:
                cell.draw()
