def handle_gpa(gpa):
    greetings_ = ""
    desc = ""
    if 4.5 <= gpa <= 5.0:
        greetings_ += 'Excellent Job!'
        desc += 'First Class Honors'
    elif 3.5 <= gpa < 4.5:
        greetings_ += 'Very Good Job!'
        desc += 'Second Class Upper Division'
    elif 2.5 <= gpa < 3.5:
        greetings_ += 'Good Job!'
        desc += 'Second Class Lower Division'
    elif 1.5 <= gpa < 2.5:
        greetings_ += 'Fair Job!'
        desc += 'Third Class'
    elif 1.0 <= gpa < 1.5:
        greetings_ += 'Bad Job!'
        desc += 'Pass Degree'
    elif gpa < 1.0:
        greetings_ += 'Very Bad Job!'
        desc += 'Failure!!!!'

    return greetings_, desc
  

def handle_score(score):
    grade = ""
    score_ = 0

    if 70 <= score <= 100:
        score_ += 5
        grade += "A"
    elif 60 <= score < 70:
        score_ += 4
        grade += "B"
    elif 50 <= score < 60:
        score_ += 3
        grade += "C"
    elif 45 <= score < 50:
        score_ += 2
        grade += "D"
    elif 40 <= score < 45:
        score_ += 1
        grade += "E"
    elif score < 40:
        score_ += 0
        grade += "F"

    return grade, score_


name = input("What is your name? ")
dept = input("What department are you in? ")
matric_number = input("What is your matric number? ")
print("{}\nWelcome to BlackFingers GPA Calculator\n{}".format("-" * 60, "-" * 60))
print("Enter your course code, yes/no if it's an elective or not, number of units and score.\n"
      "Enter 'q' if you no longer want to input a course info")

total_no_of_units = 0
gp_total_no_of_units = 0
all_course_tnus = 0
quit_ = ""

while quit_ == "":
    course_code = input("Enter a course code: ")
    check_elective = input("Is {} an elective? Enter 'yes' if yes and 'no' if no. => ".format(course_code))
    no_of_units = int(input("Enter the no of units for {}: ".format(course_code)))
    score = float(input("What's your score for {}? ".format(course_code)))
    grade, score_ = handle_score(score)
    if check_elective.lower() == "yes":
        total_no_of_units += no_of_units
        gp_total_no_of_units += 0
        total_point = score_ * no_of_units
        print("{}\n{} is an elective. You had a score of {} earning you a grade of {} and a total point of {}."
              " Although, this WON'T be calculated with your GP because it is an elective.\n{}".format("-" * 90,
                                                                                                       course_code,
                                                                                                       score,
                                                                                                       grade,
                                                                                                       total_point,
                                                                                                       "-" * 90))
    elif check_elective.lower() == "no":
        total_no_of_units += no_of_units
        gp_total_no_of_units += no_of_units
        total_point = score_ * no_of_units
        all_course_tnus += total_point
        print("{}\n{} is a core course. You had a score of {} earning you a grade of {} and a total point of {}."
              "\n{}".format("-" * 90,
                            course_code,
                            score,
                            grade,
                            total_point,
                            "-" * 90))

    to_quit = input("Are you done adding courses? If yes, enter 'q' to quit. Else, enter any other key to continue: ")
    if to_quit.lower() == "q":
        quit_ += "q"
        break
    else:
        pass

GPA = all_course_tnus / gp_total_no_of_units
greetings, desc = handle_gpa(GPA)

print('\n{}, at the end of this semester alone, {} with the matric number {} from {} has \n'
      'a total grade of {} and is in {}. {} again.'.format(greetings, name, matric_number, dept, GPA, desc, greetings))
