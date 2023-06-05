import random

count = 0
check = 0

board = [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]


def boardgame():
    print(board[0][0], "\t", board[0][1],"\t", board[0][2], "\t", board[0][3], "\n",
          board[1][0], "\t", board[1][1],"\t", board[1][2], "\t", board[1][3], "\n",
          board[2][0], "\t", board[2][1],"\t", board[2][2], "\t", board[2][3], "\n",
          board[3][0], "\t", board[3][1],"\t", board[3][2], "\t", board[3][3], "\n")


class Plant:
    def __init__(self, kind, cordx, cordy):
        self.kind = kind
        self.cordx = cordx
        self.cordy = cordy
        board[cordy][cordx] = self.kind


class Animal:
    def __init__(self, name, age, cordx, cordy):
        self.name = name
        self.age = age
        self.cordx = cordx
        self.cordy = cordy
        self.hungry = 10
        self.megadeath = random.randint(age + 15, age + 20)
        board[self.cordy][self.cordx] = self.name

    def moveup(self):
        global check
        for i in range(len(board)):
            if self.name in board[i]:
                if self.cordy == 0:
                    print(self.name + " want to relax")
                    self.hungry -= 1
                    self.age += 1
                else:
                    board[self.cordy][self.cordx] = 0
                    self.cordy -= 1
                    if board[self.cordy][self.cordx] != 0:
                        if board[self.cordy][self.cordx] == 'apple':
                            print("Apple was eaten")
                            self.hungry = 10
                            print(self.name, 'is well-fed')
                        if board[self.cordy][self.cordx] == 'lion':
                            print("Snake afraid of the lion")
                            self.cordy += 1
                            self.hungry -= 1
                        if board[self.cordy][self.cordx] == 'snake':
                            print("Lion kill the snake")
                            check = 1
                            self.hungry = 10
                            print(self.name, 'is well-fed')
                        board[self.cordy][self.cordx] = self.name
                    else:
                        self.hungry -= 1
                        board[self.cordy][self.cordx] = self.name
                    self.age += 1
                if self.age == self.megadeath:
                    self.death()
                if self.hungry == 5:
                    print(self.name, " is hungry")
                if self.hungry == 0:
                    self.death()

    def movedown(self):
        global check
        for i in range(len(board)):
            if self.name in board[i]:
                if self.cordy == 3:
                    print(self.name + " want to relax")
                    self.hungry -= 1
                    self.age += 1
                else:
                    board[self.cordy][self.cordx] = 0
                    self.cordy += 1
                    if board[self.cordy][self.cordx] != 0:
                        if board[self.cordy][self.cordx] == 'apple':
                            print("Apple was eaten")
                            self.hungry = 10
                            print(self.name, 'is well-fed')
                        if board[self.cordy][self.cordx] == 'lion':
                            print("Snake afraid of the lion")
                            self.cordy -= 1
                            self.hungry -= 1
                        if board[self.cordy][self.cordx] == 'snake':
                            print("Lion kill the snake")
                            check = 1
                            self.hungry = 10
                            print(self.name, 'is well-fed')
                        board[self.cordy][self.cordx] = self.name
                    else:
                        self.hungry -= 1
                        board[self.cordy][self.cordx] = self.name
                    self.age += 1
                if self.age == self.megadeath:
                    self.death()
                if self.hungry == 5:
                    print(self.name, " is hungry")
                if self.hungry == 0:
                    self.death()
                break

    def moveleft(self):
        global check
        for i in range(len(board)):
            if self.name in board[i]:
                if self.cordx == 0:
                    print(self.name + " want to relax")
                    self.hungry -= 1
                    self.age += 1
                else:
                    board[self.cordy][self.cordx] = 0
                    self.cordx -= 1
                    if board[self.cordy][self.cordx] != 0:
                        if board[self.cordy][self.cordx] == 'apple':
                            print("Apple was eaten")
                            self.hungry = 10
                            print(self.name, 'is well-fed')
                        if board[self.cordy][self.cordx] == 'lion':
                            print("Snake afraid of the lion")
                            self.cordx += 1
                            self.hungry -= 1
                        if board[self.cordy][self.cordx] == 'snake':
                            print("Lion kill the snake")
                            check = 1
                            self.hungry = 10
                            print(self.name, 'is well-fed')
                        board[self.cordy][self.cordx] = self.name
                    else:
                        self.hungry -= 1
                        board[self.cordy][self.cordx] = self.name
                    self.age += 1
                if self.age == self.megadeath:
                    self.death()
                if self.hungry == 5:
                    print(self.name, " is hungry")
                if self.hungry == 0:
                    self.death()

    def moveright(self):
        global check
        for i in range(len(board)):
            if self.name in board[i]:
                if self.cordx == 3:
                    print(self.name + " want to relax")
                    self.hungry -= 1
                    self.age += 1
                else:
                    board[self.cordy][self.cordx] = 0
                    self.cordx += 1
                    if board[self.cordy][self.cordx] != 0:
                        if board[self.cordy][self.cordx] == 'apple':
                            print("Apple was eaten")
                            self.hungry = 10
                            print(self.name, 'is well-fed')
                        if board[self.cordy][self.cordx] == 'lion':
                            print("Snake afraid of the lion")
                            self.cordx -= 1
                            self.hungry -= 1
                        if board[self.cordy][self.cordx] == 'snake':
                            print("Lion kill the snake")
                            check = 1
                            self.hungry = 10
                            print(self.name, 'is well-fed')
                        board[self.cordy][self.cordx] = self.name
                    else:
                        self.hungry -= 1
                        board[self.cordy][self.cordx] = self.name
                    self.age += 1
                if self.age == self.megadeath:
                    self.death()
                if self.hungry == 5:
                    print(self.name, " is hungry")
                if self.hungry == 0:
                    self.death()

    def death(self):
        if board[self.cordy][self.cordx] != 'lion':
            board[self.cordy][self.cordx] = 0
        print(self.name, " died at age ", self.age, '\n')
        del self
        global count
        global check
        count += 1
        check = 0

