class Student():
    def __init__(self, fname, lname, major, ch, gpa, id):
        self.__fname = fname
        self.__lname = lname
        self.__major = major
        self.__ch = ch
        self.__gpa = gpa
        self.__id = id

    def get_fname(self):
        return self.__fname
    def set_fname(self, new_fname):
        self.__fname = new_fname

    def get_lname(self):
        return self.__lname
    def set_lname(self, new_lname):
        self.__lname = new_lname

    def get_major(self):
        return self.__major
    def set_major(self, new_major):
        self.__major = new_major

    def get_ch(self):
        return self.__ch
    def set_ch(self, new_ch):
        self.__ch = new_ch

    def get_gpa(self):
        return self.__gpa
    def set_gpa(self, new_gpa):
        self.__gpa = new_gpa

    def get_id(self):
        return self.__id
    
    def get_cl(self):
        credits = self.__ch
        if credits <= 30:
            cl = 'Freshmen'
        elif credits <= 60:
            cl = 'Sophmore'
        elif credits <= 90:
            cl = 'Junior'
        elif credits < 90:
            cl = 'Senior'
        return cl
    
    def update_ch(self, addition_ch):
        self.__ch =+ addition_ch

    def print_info(self):
        print(f'\n{self.__fname} {self.__lname}, ID:{self.__id}, a {self.get_cl()} with a {self.__gpa}')
        print(f'{self.__fname} {self.__lname} is in the major: {self.__major}; Credit Hours:{self.__ch}')