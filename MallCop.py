class MallCop:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Paul Blart', 'Paul Blart 2', 'Paul Blart 3']
 
 
    def printMembers(self):
        print('Printing members of the Mammals class')
        for member in self.members:
            print('\t%s ' % member)
