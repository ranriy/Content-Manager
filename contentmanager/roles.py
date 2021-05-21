from rolepermissions.roles import AbstractUserRole

class Instructor(AbstractUserRole):
    available_permissions = {
        'upload_webinar_video': True,
        'retrieve_most_views':True,
        'modify_courses_subjects_tags':True,
    }

class Student(AbstractUserRole): 
    available_permissions = {
        'view_content': True,
    }
