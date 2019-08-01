def Solution(value):
    answers = []
    def find(current, history):
        print(current, history)
        if current == value:
            answers.append(history)
            return history
        if current+5 <= value:
            find(current + 5, '(' + history + ' + 5)')
        if current*3 <= value:
            find(current * 3, '(' + history + ' * 3)')

    find(1, '1')
    return answers

print(Solution(24))