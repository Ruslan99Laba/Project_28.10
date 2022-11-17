class ITMan:
    def __init__(self, firstname, lastname, age, email, skills, people_lang, coding_lang):
        self.lastname = lastname
        self.firstname = firstname
        self.age = age
        self.email = email
        self.skills = skills
        self.people_lang = people_lang
        self.coding_lang = coding_lang

obj = ITMan('Ivasik',
            'Telesik',
            13,
            'ivasik-telesik1732@izkrnanog.ua',
            ['ходить', "говорить", "кодить"],
            ['Україньська', "Англійська"],
            ['Python', "C++", "lisp"])

print(obj.__dict__)
