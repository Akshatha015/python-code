class person:
    def __init__(self,x,y,z):
         self.nickname=x
         self.roll=y
         self.height=z
    def run(self):
         print("i can run",self.nickname,self.roll) 
harsha=person("chintu",78,6)
anjali=person("mary",98,9)
harsha.run()
anjali.run()  