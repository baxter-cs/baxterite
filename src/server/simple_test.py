import database_functions

my_student_id = 1337

database_functions.wipe_tables()

# Class Creation

oop_class_id = database_functions.new_class("Object Oriented Procrastinating", "This is a description")
oop1_standard_id = database_functions.new_standard("Meme-iness", "Proficient at making dank memes")
database_functions.new_class_standard(oop1_standard_id, oop_class_id)
oop1_instance_id = database_functions.new_instance(oop_class_id, database_functions.current_class_name_id(oop_class_id), "A", 1, 1, 2015)
oop2_instance_id = database_functions.new_instance(oop_class_id, database_functions.current_class_name_id(oop_class_id), "C", 2, 3, 2015)

mechanics_class_id = database_functions.new_class("Mechanics", "You're probably taking this because it's a required course.")
mechanics_standard1_id = database_functions.new_standard("Patience", "Proficient at saying nothing and student accepts that they'll be shusshed")
database_functions.new_class_standard(mechanics_standard1_id, mechanics_class_id)
mechanics_instance_id = database_functions.new_instance(mechanics_class_id, database_functions.current_class_name_id(mechanics_class_id), "E", 3, 3, 2015)


# Joining Classes
database_functions.new_instance_member(mechanics_instance_id, my_student_id)
database_functions.new_instance_member(oop2_instance_id, my_student_id)

# Adding grades for a class/instance

oop1_instance_standard1_id = database_functions.get_instance_standard_id(oop1_instance_id, oop1_standard_id)
mechanics_instance_standard1_id = database_functions.get_instance_standard_id(mechanics_instance_id, mechanics_standard1_id)
database_functions.new_instance_standard_grade(my_student_id, oop1_instance_standard1_id, "PR")
database_functions.new_instance_standard_grade(my_student_id, mechanics_instance_standard1_id, "EX")