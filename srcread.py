class SRCRead:

    def __init__(self, file):

        self.file = file

    def findPath(self, parameterType):

        with open(self.file, 'r') as src:
            linesList = src.readlines()
        
        for line in linesList:
            if line.startswith(parameterType + ': '):
                return line[line.find(' ') + 1:]
