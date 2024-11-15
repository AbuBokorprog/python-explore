class Employee:
    name= 'Abu';
    language= 'Bengali';
    salary= 12000;

    def greet(self):
        print(f'Good Morning! {self.name}');


abu = Employee()
abu.greet()
# print(abu.name, abu.language, abu.salary)