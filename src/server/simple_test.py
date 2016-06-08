import database_functions

database_functions.wipe_tables()

my_student_id = 1337

oop_class_id = database_functions.new_class("Object Oriented Procrastinating", "This is a description")
new_standard_id = database_functions.new_standard("Meme-iness", "Proficient at making dank memes")
database_functions.new_class_standard(new_standard_id, oop_class_id)
new_instance_id = database_functions.new_instance(oop_class_id, database_functions.current_class_name_id(oop_class_id), "A", 1, 1, 2015)
oop2_instance_id = database_functions.new_instance(oop_class_id, database_functions.current_class_name_id(oop_class_id), "C", 2, 3, 2015)

database_functions.new_instance_member(oop2_instance_id, my_student_id)

mechanics_class_id = database_functions.new_class("Mechanics", "You're probably taking this because it's a required course.")
mechanics_instance_id = database_functions.new_instance(mechanics_class_id, database_functions.current_class_name_id(mechanics_class_id), "E", 3, 3, 2015)
database_functions.new_instance_member(mechanics_instance_id, my_student_id)