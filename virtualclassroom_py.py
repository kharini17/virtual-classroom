import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class VirtualClassroomManager:
    def __init__(self):
        self.classrooms = {}
        self.assignments = {}
        self.submissions = {}
        
    def add_classroom(self, class_name):
        if class_name in self.classrooms:
            logging.info(f"Classroom {class_name} already exists.")
            return
        self.classrooms[class_name] = []
        self.assignments[class_name] = []
        logging.info(f"Classroom {class_name} has been created.")
    
    def add_student(self, student_id, class_name):
        if class_name not in self.classrooms:
            logging.error(f"Classroom {class_name} does not exist.")
            return
        if student_id in self.classrooms[class_name]:
            logging.info(f"Student {student_id} is already enrolled in {class_name}.")
            return
        self.classrooms[class_name].append(student_id)
        logging.info(f"Student {student_id} has been enrolled in {class_name}.")
    
    def schedule_assignment(self, class_name, assignment_details):
        if class_name not in self.classrooms:
            logging.error(f"Classroom {class_name} does not exist.")
            return
        self.assignments[class_name].append(assignment_details)
        logging.info(f"Assignment for {class_name} has been scheduled.")
    
    def submit_assignment(self, student_id, class_name, assignment_details):
        if class_name not in self.classrooms:
            logging.error(f"Classroom {class_name} does not exist.")
            return
        if student_id not in self.classrooms[class_name]:
            logging.error(f"Student {student_id} is not enrolled in {class_name}.")
            return
        if (student_id, class_name) not in self.submissions:
            self.submissions[(student_id, class_name)] = []
        self.submissions[(student_id, class_name)].append(assignment_details)
        logging.info(f"Assignment submitted by Student {student_id} in {class_name}.")
    
    def list_classrooms(self):
        if not self.classrooms:
            logging.info("No classrooms available.")
            return
        for class_name in self.classrooms:
            print(class_name)
    
    def list_students(self, class_name):
        if class_name not in self.classrooms:
            logging.error(f"Classroom {class_name} does not exist.")
            return
        students = self.classrooms[class_name]
        if not students:
            logging.info(f"No students enrolled in {class_name}.")
            return
        for student in students:
            print(student)

def main():
    manager = VirtualClassroomManager()
    
    while True:
        user_input = input("Enter command: ")
        parts = user_input.split(' ', 2)
        command = parts[0].strip()
        
        try:
            if command == "add_classroom":
                manager.add_classroom(parts[1].strip())
            elif command == "add_student":
                student_id, class_name = parts[1].split(' ', 1)
                manager.add_student(student_id.strip(), class_name.strip())
            elif command == "schedule_assignment":
                class_name, details = parts[1].split(' ', 1)
                manager.schedule_assignment(class_name.strip(), details.strip())
            elif command == "submit_assignment":
                student_id, rest = parts[1].split(' ', 1)
                class_name, details = rest.split(' ', 1)
                manager.submit_assignment(student_id.strip(), class_name.strip(), details.strip())
            elif command == "list_classrooms":
                manager.list_classrooms()
            elif command == "list_students":
                class_name = parts[1].strip()
                manager.list_students(class_name)
            else:
                print("Unknown command.")
        except Exception as e:
            logging.error(f"Error processing command: {e}")

if __name__ == "__main__":
    main()
