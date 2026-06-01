from enum import Enum

class AllureEpic(str, Enum):
    LMS = "LMS system"
    STUDENT = "Student system"
    ADMINISTRATIONS = "Administration system"