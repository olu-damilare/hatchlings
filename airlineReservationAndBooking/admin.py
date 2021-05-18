class Admin(object):

    def __init__(self, full_name, phone_number, email_address, staff_ID):
        self.__full_name = full_name
        self.__phone_number = phone_number
        self.__email_address = email_address
        self.__staff_ID = staff_ID

    def __str__(self):
        return "Full Name = {}\nPhone number = {}\nEmail address = {}\nStaff ID = {}".format(self.__full_name, self.__phone_number, self.__email_address, self.__staff_ID)
