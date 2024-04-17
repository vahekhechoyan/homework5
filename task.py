class Employee:
    def __init__ (self,name,age,department):
        self.name=name
        self.age=age
        self.departament=department


def read_employee_data(file_path):
    employees=[]
    with open (file_path,'r') as file:
        for line in file:
            name,age,departament=line.strip().split(',')
            employees.append(Employee(name,int(age),departament))
    return employees

def calculate_average_age(employees):
    total_age=sum(employee.age for employee in employees)
    return total_age/len(employees)

def count_employees_by_department(employees):
    departament_count={}
    for employee in employees:
        if employee.departament in departament_count:
            departament_count[employee.departament]+=1
        else:
            departament_count[employee.departament]=1
    return departament_count

def find_oldest_and_youngest(employees):
    oldest=max(employees,key=lambda x:x.age)
    youngest=min(employees,key=lambda x:x.age)
    return oldest,youngest

def write_result_to_file(average_age,department_count,oldest,youngest,output_file):
    with open(output_file,'w') as file:
        file.write(f"Average Age of Employees:{average_age}\n")
        file.write("Number of Employees by Department:\n")
        for department,count in department_count.items():
            file.write(f"{department}:{count}\n")
        file.write("\nOldest Employee:\n")
        file.write(f"Name:{oldest.name}\n")
        file.write(f"Age:{oldest.age}\n")
        file.write(f"Department:{oldest.departament}\n")
        file.write(f"\nYoung Employee:\n")
        file.write(f"Name:{youngest.name}\n")
        file.write(f"Age:{youngest.age}\n") 
        file.write(f"Department:{youngest.departament}\n")

def main():
    file_path='persons.txt'
    output_file='persons_result.txt'

    employees=read_employee_data(file_path)
    average_age=calculate_average_age(employees)
    department_count=count_employees_by_department(employees)
    oldest,youngest=find_oldest_and_youngest(employees)
    write_result_to_file(average_age,department_count,oldest,youngest,output_file)

if __name__=="__main__":
    main()
    

