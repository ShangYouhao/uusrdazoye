import copy

class Molecule():

    '''分子'''

    def __init__(self):
        self.__atoms = []
        self.__bonds = []
    
    def get_atoms(self):
        return copy.deepcopy(self.__atoms)
    
    def get_bonds(self):
        return copy.deepcopy(self.__bonds)
    
    def modify_atoms(self):
        return self.__atoms
    
    def modify_bonds(self):
        return self.__bonds
    
    def get_bond_length(self, a, b):
        pass
    
    def get_bond_angle(self, a, o, b):
        pass

    def get_dihedral_angle(self, a, b, c, d):
        pass

    def modify_bond_length(self, a, b, l):
        pass
    
    def modify_bond_angle(self, a, o, b, angle):
        pass
    
    def modify_dihedral_angle(self, a, b, c, d, angle):
        pass