import database_functions

database_functions.wipe_tables()
oop_class_id = database_functions.new_class("Object Oriented Procrastinating", "This is a description")
database_functions.new_instance(oop_class_id, database_functions.current_class_name_id(oop_class_id), "A", 1, 1, 2015)
