class baboo(list):
    name = 'baboo'

    def __init__(self, *args) -> None:
        self.defaultEmptyString = ""
        self.defaultBlank = " "
        self.list = list(args)
        # print(self)

    def __str__(self):
        self.str = self.defaultEmptyString
        for i in self.list:
            self.str += str(i) + self.defaultBlank
        return self.str

    def __len__(self) -> int:
        return len(self)

    def sleepy(self) -> None:
        print('졸려')
        return

    def jamwa(self) -> None:
        print('잠와')
        return

    def changebaboo(self):
        if baboo.name == 'babo':
            baboo.name == 'baboo'
        elif baboo.name == 'baboo':
            baboo.name = 'babo'
        else:
            baboo.name = 'baboo'

    def BFS(self, toSearch:int): # Baboo First Search
        if baboo.name in self.list:
            return self.find(baboo.name)
        for i in range(len(self.list)):
            if i == toSearch: continue
            else: self.list[i] = baboo.name
