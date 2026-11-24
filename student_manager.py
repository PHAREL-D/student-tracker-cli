# Import json for serializing and parsing student data, and os for checking
# whether the persistence file exists before the program starts.
import json
import os 

# Persist the in-memory student list by replacing the contents of
# "etudiants.json" with its JSON representation.
def save_list_student(list_etudiant):
    with open("etudiants.json","w") as file:
        json.dump(list_etudiant,file)
        
# Read "etudiants.json" and convert its JSON text into a Python list.
# A missing, empty, or invalid file is deliberately handled as an empty
# student list so that the rest of the program can continue safely.
def  load_list_student():
    with open("etudiants.json","r") as file:
        contenu= file.read()
        # The JSON file is valid only when it contains text to parse.
        if not contenu:
            return list()
        else:
            try:
                data = json.loads(contenu)
                return data
            # Invalid JSON can occur if the file was interrupted or edited manually.
            except json.JSONDecodeError:
                return list()


# Initialize the application's central data structure: a list of dictionaries.
# Each dictionary is expected to contain "ID", "nom", and "notes" keys.
if os.path.exists("etudiants.json"):
    list_etudiant=load_list_student()
else:
    list_etudiant = list()
    


# Interactive workflow for creating one or more student records.
# Every accepted record is immediately saved to the JSON file.
def ajouter_etudiant(list_etudiant):
    # The outer loop validates the number of students before creation begins.
    # Non-numeric input is rejected, and zero or negative values are retried.
    while True:
        try:
            n= int(input("how many students do you want to add ??:"))
            if n>0:
                break
        except ValueError:
            print("Enter a numeric value")
    
    # Each iteration collects and adds exactly one student. Decrementing n
    # ensures the loop stops after the requested number of students is reached.
    while n>0:
        # Repeatedly validate the ID until it is both positive and unused.
        while True:
            try:
                id = int(input('Enter an ID:'))
                if id>0:
                    existe= False
                    # Search all existing dictionaries for the entered ID.
                    for e in list_etudiant:
                        if e["ID"] ==id:
                            existe = True
                            break
                    if existe :
                        print('This ID already exists, please enter a different ID')
                        continue
                    else:
                        break
                print("Enter a valid ID")
            except ValueError:
                print("Enter a numeric value")
                
        nom= input('Enter a name:')
        print("Adding a student...")
        # strip() removes whitespace at the beginning and end of the name.
        nom = nom.strip()
        # Apply the minimum-name-length rule after removing outer whitespace.
        while len(nom)<3:
            print("Enter a valid name")
            nom=input("Enter a name:")
            nom=nom.strip()
        # Build the dictionary that represents one student. "notes" starts
        # empty because no grades have been entered for the new student yet.
        etudiant={
        'ID':id,
        'nom':nom,
        'notes':[], 
        }
        
        # Update both the current session and persisted JSON data.
        list_etudiant.append(etudiant)
        save_list_student(list_etudiant)
        print('Student added successfully')
        n=n-1 

# Print every stored student record, or explain that the list is empty.
def afficher_etudiant(list_etudiant):
    print("Displaying all students informations...")
    if len(list_etudiant)<1 :
        print("No student found")
    else:
        # Each loop variable refers to one student dictionary.
        for etud in list_etudiant:
            print(etud)

# Locate exactly one student by ID and display their complete stored details.
def rechercher_etudiant(list_etudiant):
    search = entre_id()
    print("Searching for a student...")
    exist =False
    # Continue scanning until a matching ID is found. The loop variable etud
    # is also reused after the loop when exist is True.
    for etud in list_etudiant:
        if etud ["ID"]==search:
            exist=True
            break
    if exist:
        print('==Student found==')
        print("ID:",etud["ID"])
        print("nom:",etud["nom"])
        print("notes:",etud["notes"])
    else:
        print('ID does not exist')



# Shared ID input helper used by search, deletion, and grade operations.
# It keeps asking until conversion succeeds and the value is greater than zero.
def entre_id():
    while True:
        try:
            idl= int(input("Enter the student ID :"))
            if idl >0:
                return idl
        except ValueError:
            print("Enter a numeric value")

# Delete the matching student dictionary from the in-memory list, then persist
# the updated list so that the deletion remains after the program restarts.
def supprimer_etudiant(list_etudiant):
    search = entre_id()
    print("Deleting a student...")
    exist =False
    # Scan the list for a matching student ID.
    for etud in list_etudiant:
        if etud ["ID"]==search:
            exist=True
            break
    if exist:
        list_etudiant.remove(etud)
        save_list_student(list_etudiant)
        print("Student deleted")
    else:
        print("ID does not exist")

# Add valid grades to a selected student. A grade must be numeric and between
# 0 and 20 inclusive; saving occurs after every accepted grade.
def ajouter_note(list_etudiant):
    add = entre_id()
    exist =False
    # Find the selected dictionary, which is needed to access its "notes" list.
    for etud in list_etudiant:
        if etud ["ID"]==add:
            exist=True
            break
    if exist:
        invalid=True
        while invalid is True:
            y = int(input("how many grades do you want to add ??:"))
            # y is a countdown. Each loop iteration accepts or rejects one grade.
            while y>0:
                try:
                    note= float(input('Enter a grade:'))
                    print("Adding a grade...")
                    # A value in [0, 20] is accepted; values outside this range
                    # leave the student unchanged and prompt for another attempt.
                    if note>=0 and note<=20:
                        etud["notes"].append(note)
                        save_list_student(list_etudiant)
                        print("Grade added successfully")
                        print('==Student found==')
                        print("ID:",etud["ID"])
                        print("nom:",etud["nom"])
                        print("Grades:",etud["notes"])
                        y=y-1
                        invalid=False
                    
                    else:
                        print("Enter numbers between 0 and 20")
                        invalid=True
                except ValueError:
                    print("Enter a numeric value ")
                    invalid=True
    else:
        print('ID does not exist')


# Retrieve a selected student and print their grades. The same student can
# safely have an empty grade list, in which case a specific message is shown.
def afficher_note(list_etudiant):
    aff = entre_id()
    print("Retrieving  student's grades...")
    exist =False
    # Scan the list for a matching student ID.
    for etud in list_etudiant:
        if etud ["ID"]==aff:
            exist=True
            break
    if exist:
        print('==Student found==')
        print("nom:",etud["nom"])
        if not etud["notes"]:
            print("this student has not yet any grades")
        else:
            print("Grades:",etud["notes"])
    else:
        print('ID does not exist')

# Calculate the arithmetic mean of a selected student's grades.
# "None" means that an average cannot be calculated because no grade exists.
def calculer_moyenne(list_etudiant):
    afe = entre_id()
    print("Calculating student's average...")
    exist =False
    # Scan the list for a matching student ID.
    for etud in list_etudiant:
        if etud["ID"]==afe:
            exist=True
            break
    if exist:
        print('==Student found==')
        print("nom:",etud["nom"])
        if not etud["notes"]:
            print("this student has not yet any grades")
            return None
        else:
            # sum() totals all grades and len() supplies the number of grades.
            moyenne = sum(etud["notes"])/len(etud["notes"])
            return moyenne
    else:
        print('ID does not exist')

# Map a numeric average to an appreciation category using ascending thresholds.
# The first condition that matches determines the returned category.
def appreciation(moyenne):
    if moyenne<10:
        return "failed"
    elif moyenne<12:
        return "satisfactory"
    elif moyenne<14:
        return "good"
    elif moyenne <16:
        return "very good"
    else:
        return"excellent"

# Calculate the overall class average across every recorded grade.
# This is a grade-weighted average: it divides the sum of all grades by the
# total number of grade entries, not by the number of students.
def moyen_classe(list_etudiant):
    # Count and print the number of student records, including students with
    # no grades.
    nbre_etudiant=len(list_etudiant)
    print("Total students =",nbre_etudiant)
    # Count the grade entries across all students. Each entry is one grade
    # rather than one student.
    total_note=0
    for etud in list_etudiant:
        total_note=total_note+len(etud["notes"])
    print("Total grades =",total_note)
    # Combine every individual grade into one total for the overall average.
    
    somme=0
    for etud in list_etudiant:
        somme=somme+sum(etud["notes"])
    # Avoid division by zero and report that no grades have been recorded.
    if total_note==0 and somme ==0:
        print("No grades have been recorded yet.")
        return None
    else:
        moyenne_classe=somme/total_note
        return moyenne_classe

# Identify the highest and lowest student averages and retain every name
# involved in a tie. Students with no grades are ignored.
def best_moyen(list_etudiant):
    # Start with an empty name list and a highest-average value of zero.
    # The first student with a positive average replaces that initial value.
    best=list()
    best_moyenne = 0
    for etud in list_etudiant:
        if not etud["notes"]:
            continue
        moyenne = sum(etud["notes"])/len(etud["notes"])
        if moyenne>best_moyenne:
            # A new strict maximum replaces all names previously collected.
            best_moyenne=moyenne
            best.clear()
            best.append(etud["nom"])
        elif moyenne==best_moyenne:
            # An equal average is added, preserving tie names.
            best.append(etud["nom"])
    print(f"The best average is: {best} with {best_moyenne} as the average")
    # Track a lowest average without assuming that a first value is known.
    # None acts as a sentinel until the first student with grades is found.

    low=list()
    lowest_moyenne= None
    for etud in list_etudiant:
        if not etud["notes"]:
            continue
        moyenne = sum(etud["notes"])/len(etud["notes"])
        if lowest_moyenne is None:
            # The first graded student establishes the initial lowest value.
            lowest_moyenne=moyenne
            low.append(etud["nom"])
        elif moyenne<lowest_moyenne:
            # A smaller average replaces the previous lowest result and its names.
            lowest_moyenne=moyenne
            low.clear()
            low.append(etud["nom"])
        elif moyenne == lowest_moyenne:
            low.append(etud["nom"])
    print(f"The lowest average is: {low} with {lowest_moyenne} as the average")

# This loop implements the main application workflow. It redisplays the menu
# after every operation until the user enters option 9.
choix=0
# The loop condition leaves the menu immediately when choix equals 9.
while choix!=9:
    print(
    "======STUDENTS MANAGEMENT====== \n"
    "1. Add a student \n"
    "2. Show students \n"
    "3. Search for a student \n"
    "4. Delete a student \n"
    "5. Add a grade \n"
    "6. Show grades \n"
    "7. Show average \n"
    "8. Class statistics \n"
    "9. Quit\n")
    
    try:
        choix=int(input('Choose an option:\n'))
    except ValueError:
        print ("Enter a valid number")
        continue

    # Dispatch to the corresponding operation according to the validated choice.
    if choix==1:
        print("Add a student")
        ajouter_etudiant(list_etudiant)
    elif choix==2:
        print("Show students")
        afficher_etudiant(list_etudiant)
    elif choix==3:
        print("Search for a student")
        rechercher_etudiant(list_etudiant)
    elif choix==4:
        print("Delete a student")
        supprimer_etudiant(list_etudiant)
    elif choix==5:
        print("Add a grade")
        ajouter_note(list_etudiant)
    elif choix==6:
        print("Show grades")
        afficher_note(list_etudiant)
    elif choix==7:
        print("Show average")
        moyenne=calculer_moyenne(list_etudiant)
        if moyenne is None:
            print("Unable to calculate the average: no grades available")
        else:
            print(moyenne)
            app=appreciation(moyenne)
            print(app)
    elif choix==8:
        print("======CLASS STATISTICS======")
        print("Analysing the class statistics...")
        moyenne_classe= moyen_classe(list_etudiant)
        if moyenne_classe is None:
            print("Unable to calculate the overall average: no grades available.")
        else:
            print("Overall class average=",moyenne_classe)
            best_moyen(list_etudiant)
    elif choix==9:
        print("Quit")
    else:
        print("Invalid choice")
