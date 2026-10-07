def find_person(**people):
    print(people.get("Antonia", "Antonia not found"))
    

find_person(Raymond = "programmer", Eduard="Teacher", Antonia="Physician")
find_person(Regina="Accountant", Michael="Lawyer")
