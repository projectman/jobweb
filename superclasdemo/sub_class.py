

class Person:

    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def Name(self):
        return "Person name: " + self.firstname + " " + self.lastname


class Table:

    def __init__(self, staffnum):
        self.table_num = str(staffnum)

    def tableNumber(self):
        return "Table Number is: " + self.table_num


class Employee(Table, Person):

    def __init__(self, first, last, staffnumber=1000):

        Table.__init__(self, staffnumber)
        Person.__init__(self, first, last)
        self.staffnumber = str(staffnumber)


    def GetEmployee(self):
        return "Employee:" + self.Name() + ", " +  self.staffnumber

y = Employee("Homer", "Simpson")

print(y.GetEmployee())
print(y.Name())
print(y.tableNumber())

