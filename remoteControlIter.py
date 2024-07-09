class remoteControl:
    def __init__(self):
        self.channel=['Tv9','Sports','Tv5']
        self.index=-1
    def __iter__(self):
        return self
    def __next__(self):
        self.index+=1
        if self.index==len(self.channel):
            raise StopIteration('no channels exist')
        return self.channel[self.index]
    def control(self):
        print(next(self))
r=remoteControl()
i=iter(r)
r.control()
r.control()