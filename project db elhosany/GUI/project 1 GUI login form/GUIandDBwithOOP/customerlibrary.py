class CustomerLibs():
    def __init__(self, username=None, password=None):
        self.username=username
        self.password=password

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password

    def setUsername(self, username):
        self.username=username

    def setPassword(self, password):
        self.password=password

    # def __str__(self):
    #     return ('{},{},{}'.format(self.username,self.password))