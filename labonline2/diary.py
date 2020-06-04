import json

def to_file(diary, filename):
    f = open(filename, "w")
    json.dump(diary, f, indent = 4)
    f.close()

def from_file(filename):
    f = open(filename, "r")
    diary = json.load(f)
    f.close()

    return diary

def create_diary():
    diary = {
        "students": [],
        "courses": [],
        "marks": []
    }
    return diary

def create_id(diary, list):
    if len(diary[list]) == 0:
        return 0
    else:
        current_id = max(diary[list], key = lambda a: a["id"])
        return current_id["id"] + 1

def get_at_id(diary, list, id):
    for obj in diary[list]:
        if obj["id"] == id:
            return obj
    return None

def add_student(diary, name, surname):
    new_student = {
        "id" : create_id(diary, "students"),
        "name" : name,
        "surname" : surname
    }
    diary["students"].append(new_student)

def add_course(diary, name):
    new_course = {
        "id" : create_id(diary, "courses"),
        "name" : name
    }
    diary["courses"].append(new_course)

def add_mark(diary, mark, student_id, course_id):
    if get_at_id(diary, "students", student_id) != None: 
        if get_at_id(diary, "courses", course_id) != None:
            new_mark = {
                "id" : create_id(diary, "marks"),
                "mark" : mark,
                "student_id" : student_id,
                "course_id" : course_id
            }
    diary["marks"].append(new_mark)

def mark_mean(matched):
    if len(matched) == 0:
        return 0
    else:
        sum = 0
        for match in matched:
            sum += match["mark"]
        sum = sum / len(matched)

        return sum 
    

def is_the_student_or_course(mark, student_id = None, course_id = None):
    if mark["student_id"] == student_id or student_id == None:
        if mark["course_id"] == course_id or course_id == None:
            return True
    return False

def mean_for_student(diary, student_id):
    find_a_match = lambda a: is_the_student_or_course(a, student_id = student_id)
    matches = list(filter(find_a_match, diary["marks"]))

    return mark_mean(matches)

def mean_for_course(diary, course_id):
    find_a_match = lambda a: is_the_student_or_course(a, course_id = course_id)
    matches = list(filter(find_a_match, diary["marks"]))

    return mark_mean(matches)

def mean_for_student_in_course(diary, student_id, course_id):
    find_a_match = lambda a: is_the_student_or_course(a, student_id = student_id, course_id = course_id)
    matches = list(filter(find_a_match, diary["marks"]))

    return mark_mean(matches)

def the_absolute_mean(diary):
    return mark_mean(diary["marks"])
