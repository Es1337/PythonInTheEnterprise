import diary as lib
import sys
import json


if __name__ == "__main__":

    def give_student_info(diary, student_id):
        student = lib.get_at_id(diary, 'students', student_id)

        print(f"Information on Student ID: {student_id}")
        print(f"Full Name: {student['name']} {student['surname']}")
        print(f"Mean of marks: {lib.mean_for_student(diary, student_id)}")

        for course in diary["courses"]:
            id = course["id"]
            name = course["name"]
            print(f"Mean of marks in: {name} = {lib.mean_for_student_in_course(diary, student_id, id)}")

    def give_course_info(diary, course_id):
        course = lib.get_at_id(diary, "courses", course_id)

        print(f"Information on Course ID: {course_id}")
        print(f"Name: {course['name']}")
        print(f"Mean of mark in the course = {lib.mean_for_course(diary, course_id)}")

    def print_absolute_mean(diary):
        print(f"Absolute mean of everything = {lib.the_absolute_mean(diary)}")

    if len(sys.argv) < 2:
        diary = lib.create_diary()

        lib.add_student(diary, "Aaron", "Sorkin")
        lib.add_student(diary, "Ethan", "Coen")
        lib.add_student(diary, "Joel", "Coen")
        lib.add_student(diary, "Quentin", "Tarantino")

        lib.add_course(diary, "Screenwriting Masterclass")
        lib.add_course(diary, "How to make pierogi")

        lib.add_mark(diary, 5.0, 0, 0)
        lib.add_mark(diary, 2.0, 0, 1)

        lib.add_mark(diary, 5.0, 1, 0)
        lib.add_mark(diary, 3.0, 1, 1)

        lib.add_mark(diary, 5.0, 2, 0)
        lib.add_mark(diary, 3.5, 2, 1)

        lib.add_mark(diary, 5.0, 3, 0)
        lib.add_mark(diary, 5.0, 3, 1)

        filename = "diary.json"
        lib.to_file(diary, filename)

        print(f"Created {filename}")
        print("You can open a diary by typing in its filename as argument in command prompt")
        print("e. g. task.py diary.json")

    if len(sys.argv) == 2:
        try:
            diary = lib.from_file(sys.argv[1])
            print(json.dumps(diary, indent = 4))
            print(">" * 80)
            give_student_info(diary, 0)
            print(">" * 80)
            give_course_info(diary, 0)
            print(">" * 80)
            print_absolute_mean(diary)

        except FileNotFoundError:
            print("Enter correct filename")
    





