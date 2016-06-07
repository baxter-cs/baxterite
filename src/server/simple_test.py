import database_functions

database_functions.wipe_tables()

oop_class_id = database_functions.new_class("Object Oriented Procrastinating", "This is a description")
new_standard_id = database_functions.new_standard("Meme-iness", "Proficient at making dank memes")
database_functions.new_class_standard(new_standard_id, oop_class_id)
new_instance_id = database_functions.new_instance(oop_class_id, database_functions.current_class_name_id(oop_class_id), "A", 1, 1, 2015)

mechanics_class_id = database_functions.new_class("Mechanics", "We do things you already did freshmen year")