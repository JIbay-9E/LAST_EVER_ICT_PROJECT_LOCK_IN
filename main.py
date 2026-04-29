
class Classmate:
    def __init__(self, name, section, favorite_subject):
        self.name = name
        self.section = section
        self.favorite_subject = favorite_subject
    def introduce(self):
        return f"I am {self.name} from {self.section}. My favorite subject is {self.favorite_subject}."

names = [
    "abayon", "antes", "apostol", "banaag", "barrientos", "casal", "coeli",
    "david", "de mata", "dela cruz f", "dela cruz j", "dellejero", "fukuda", "gozum",
    "ibay", "lim", "lozano", "mamauag", "navarro", "precones", "ramos",
    "sidhu", "tiu", "villamayor", "zaragoza"
]
subjects = ["Math", "Science", "SS"]
classmates = [
    Classmate(name, "Emerald", subjects[i % len(subjects)])
    for i, name in enumerate(names)
]

def get_introductions():
    return [c.introduce() for c in classmates]

def add_classmate(name, section, subject):
    classmates.append(Classmate(name, section, subject))

try:
    from pyscript import display, document
    import numpy as np
    import logging
    import matplotlib.pyplot as plt
    logging.getLogger('matplotlib').setLevel(logging.ERROR)

    days = np.array(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
    absences = np.array([0, 0, 0, 0, 0])

    def generate_graph():
        if document.getElementById("plot") is None:
            return
        document.getElementById("plot").innerHTML = ""
        plt.figure(figsize=(6, 4))
        plt.plot(days, absences, marker='o')
        plt.title('Weekly Attendance (Absences)')
        plt.ylabel('Number of Absences')
        plt.grid(True)
        display(plt, target="plot")
        plt.close()

    def update_data(event=None):
        day_select = document.getElementById('day-select')
        absence_input = document.getElementById('absence-count')
        if day_select is None or absence_input is None:
            return
        day_idx = int(day_select.value)
        val = absence_input.value
        if val:
            absences[day_idx] = int(val)
            generate_graph()
            absence_input.value = ""

    generate_graph()
except Exception as e:
    pass
