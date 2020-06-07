'''
    -----------------------------------
    @author -- Insert Author
    COVID-19 PATIENT MANAGEMENT SYSTEM
    31-05-2020
    -----------------------------------
'''



def edit_patient_status():
    count = 0
    word = []
    case_id = ""
    patient_id = ""
    f = open("positive_patients.txt", "r")
    for line in f.readlines():
        for char in line:
            if char == "\n":
                break
            if count == 2:
                word.append(char)
            if char == "-":
                count += 1
        status = "".join(word)
        del word[:]
        count = 0
        for char in line:
            if char == "-":
                break
            else:
                case_id = case_id + char
        for char in line:
            if count == 2:
                break
            else:
                if char == "-":
                    count += 1
                elif count == 1:
                    patient_id = patient_id + char
        count = 0
        print("CASE ID:", case_id, "- PATIENT ID:", patient_id, "- STATUS:", status)
        case_id = ""
        patient_id = ""
    inp = int(input("PLEASE INPUT CASE ID:"))
    case_id = inp

    f = open("positive_patients.txt", "r")
    case_id = ""
    patient_id = ""
    for line in f.readlines():
        for char in line:
            if char == "-":
                break
            else:
                case_id = case_id + char
        for char in line:
            if count == 2:
                break
            else:
                if char == "-":
                    count += 1
                elif count == 1:
                    patient_id = patient_id + char
        count = 0
        if case_id:
            print("=======================")
            print("CURRENT STATUS:", status)
            print("CASE ID:", case_id)
            print("PATIENT ID:", patient_id)
            print("=======================")
            print("[1].ACTIVE")
            print("[2].RECOVERED")
            print("[3].DECEASED")
            inp = int(input("INPUT:"))
            if inp == 1:
                new_status = "ACTIVE"
            elif inp == 2:
                new_status = "RECOVERED"
            else:
                new_status = "DECEASED"

            new_string = str(case_id) + "-" + str(patient_id) + "-" + new_status

            file = open("positive_patients.txt", "r")
            list_of_lines = file.readlines()
            for i in range(0, len(list_of_lines)):
                if int(list_of_lines[i][0]) == case_id:
                    list_of_lines[i] = new_string + "\n"

            file = open("positive_patients.txt", "w")
            file.writelines(list_of_lines)
            file.close()
            break
def test_3(code, patient_id, txt):
    test3 =  []
    test_number = 3
    test3.append(patient_id)
    txt.append(test_number)
    test3.append(test_number)
    print("============")
    print("TEST STAGE 3")
    print("[1].POSITIVE")
    print("[2].NEGATIVE")
    print("============")
    inp = int(input())

    if inp == 1:
        test_result = "POSITIVE"
        if code[patient_id] == "AEO" or code[patient_id] == "ATO" or code[patient_id] == "ACC" or code[
            patient_id] == "SID":
            action_taken = "QHNF"
        else:
            action_taken = "HQNF"

        txt.append(test_result)
        test3.append(test_result)
        txt.append(action_taken)
        test3.append(action_taken)

        if action_taken == "QHNF":
            print("========")
            print("[1].NW")
            print("[2].ICU")
            print("========")
            inp = int(input())
            if inp == 1:
                condition = "NW"
                output = "ACTION TO BE TAKEN IS TO QUARANTINE IN HOSPITAL NORMAL WARD"
            else:
                condition = "ICU"
                output = "ACTION TO BE TAKEN IS TO QUARANTINE IN HOSPITAL ICU"
            txt.append(condition)
            test3.append(condition)

        else:
            output = "ACTION TO BE TAKEN IS TO HOME QUARANTINE"

        str_positive_patient = get_positive_patient()
        int_positive_patient = []

        with open("positive_patients.txt", "r") as file:
            lines = file.read().splitlines()
            if not lines:
                case = 1
            else:
                last_line = lines[-1]
                case = int(last_line[0]) + 1

        for i in range(0, len(str_positive_patient)):
            int_positive_patient.append(int(str_positive_patient[i]))

        with open("test_result.txt", "r") as file:
            lines = file.read().splitlines()
            if lines:
                txt.insert(0,"\n")

        with open("test_result3.txt", "r") as file:
            lines = file.read().splitlines()
            if lines:
                test3.insert(0,"\n")

        if patient_id not in int_positive_patient:
            with open("positive_patients.txt", "r") as file:
                lines = file.read().splitlines()
                if lines:
                    with open("positive_patients.txt", "a") as f:
                        f.write("\n")
            with open('positive_patients.txt', 'a') as file:
                string = str(case) + "-" + str(patient_id) + "-ACTIVE"
                file.write("%s" % str(string))

        with open('test_result.txt', 'a') as file:
            for i in range(0, len(txt)):
                if i == len(txt) - 1:
                    file.write("%s" % str(txt[i]))
                elif txt[i]=="\n":
                    file.write("%s" % str(txt[i]))
                else:
                    file.write("%s-" % str(txt[i]))

        with open('test_result3.txt', 'a') as file:
            for i in range(0, len(test3)):
                if i == len(test3) - 1:
                    file.write("%s" % str(test3[i]))
                elif test3[i]=="\n":
                    file.write("%s" % str(test3[i]))
                else:
                    file.write("%s-" % str(test3[i]))

        print("TEST RESULT OF PATIENT HAS BEEN SUCCESSFULLY ADDED")
        print(output)

    else:
        test_result = "NEGATIVE"
        if code[patient_id] == "AEO" or code[patient_id] == "ATO" or code[patient_id] == "ACC" or code[
            patient_id] == "SID":
            action_taken = "RU"
            output = "ACTION TO BE TAKEN IS TO STAY AT HOME AND HAVE A FAMILY REUNION"
        else:
            action_taken = "CW"
            output = "ACTION TO BE TAKEN IS TO CONTINUE WORKING"

        txt.append(test_result)
        txt.append(action_taken)

        with open('test_result.txt', 'a') as file:
            file.write("\n")
            for i in range(0, len(txt)):
                if i == len(txt) - 1:
                    file.write("%s" % str(txt[i]))
                else:
                    file.write("%s-" % str(txt[i]))

        with open('test_result3.txt', 'a') as file:
            file.write("\n")
            for i in range(0, len(txt)):
                if i == len(txt) - 1:
                    file.write("%s" % str(txt[i]))
                else:
                    file.write("%s-" % str(txt[i]))

        print("TEST RESULT OF PATIENT HAS BEEN SUCCESSFULLY ADDED")
        print(output)

def get_patient():
    patient_tested = []
    f = open("tested_patients.txt", "r")
    for line in f.readlines():
        for char in line:
            if char:
                if char == "\n":
                    pass
                else:
                    patient_tested.append(char)
            else:
                pass
    return patient_tested

def get_positive_patient():
    positive_patient = []
    f = open("positive_patients.txt", "r")
    for line in f.readlines():
        if line[0] == "\n":
            pass
        else:
            positive_patient.append(line[2])
    return positive_patient

def test_1(code, patient_id, txt):
    int_patient_tested = []
    str_patient_tested = get_patient()

    for i in range (0,len(str_patient_tested)):
        int_patient_tested.append(int(str_patient_tested[i]))
    if patient_id not in int_patient_tested:
        with open("tested_patients.txt", "r") as file:
                lines = file.read().splitlines()
                if lines:
                    with open("tested_patients.txt", "a") as f:
                        f.write("\n")
        with open('tested_patients.txt', 'a') as file:
            file.write("%s" % str(patient_id))


    test_number = 1
    txt.append(test_number)
    print("============")
    print("TEST STAGE 1")
    print("[1].POSITIVE")
    print("[2].NEGATIVE")
    print("============")
    inp = int(input())

    if inp == 1:
        test_result = "POSITIVE"
        if code[patient_id] == "AEO" or code[patient_id] == "ATO" or code[patient_id] == "ACC" or code[
            patient_id] == "SID":
            action_taken = "QHNF"
        else:
            action_taken = "HQNF"

        txt.append(test_result)
        txt.append(action_taken)

        if action_taken == "QHNF":
            print("========")
            print("[1].NW")
            print("[2].ICU")
            print("========")
            inp = int(input())
            if inp == 1:
                condition = "NW"
                output = "ACTION TO BE TAKEN IS TO QUARANTINE IN HOSPITAL NORMAL WARD"
            else:
                condition = "ICU"
                output = "ACTION TO BE TAKEN IS TO QUARANTINE IN HOSPITAL ICU"
            txt.append(condition)

        else:
            output = "ACTION TO BE TAKEN IS TO HOME QUARANTINE"

        str_positive_patient = get_positive_patient()
        int_positive_patient = []
        for i in range(0,len(str_positive_patient)):
            int_positive_patient.append(int(str_positive_patient[i]))

        with open("positive_patients.txt", "r") as file:
            lines = file.read().splitlines()
            if not lines:
                case = 1
            else:
                last_line = lines[-1]
                case = int(last_line[0]) + 1

        if patient_id not in int_positive_patient:
            with open("positive_patients.txt", "r") as file:
                lines = file.read().splitlines()
                if lines:
                    with open('positive_patients.txt', 'a') as f:
                        f.write("\n")
            with open('positive_patients.txt', 'a') as file:
                string = str(case)+"-"+str(patient_id)+"-ACTIVE"
                print(patient_id)
                file.write("%s" % str(string))

        with open('test_result.txt', 'r') as file:
            lines = file.read().splitlines()
            if lines:
                with open('test_result.txt', 'a') as f:
                    f.write("\n")

        with open('test_result1.txt', 'r') as file:
            lines = file.read().splitlines()
            if lines:
                with open('test_result1.txt', 'a') as f:
                    f.write("\n")

        with open('test_result.txt', 'a') as file:
            for i in range(0, len(txt)):
                if i == len(txt) - 1:
                    file.write("%s" % str(txt[i]))
                else:
                    file.write("%s-" % str(txt[i]))

        with open('test_result1.txt', 'a') as file:
            for i in range(0, len(txt)):
                if i == len(txt) - 1:
                    file.write("%s" % str(txt[i]))
                else:
                    file.write("%s-" % str(txt[i]))

        print("TEST RESULT OF PATIENT HAS BEEN SUCCESSFULLY ADDED")
        print(output)

    else:
        test_result = "NEGATIVE"

        if code[patient_id]=="ATO" or code[patient_id]=="ACC" or code[patient_id]=="AEO":
            action_taken = "QDFR"
            output = "ACTION TO BE TAKEN IS TO QUARANTINE IN DESIGNATED CENTRES"
        elif code[patient_id]=="SID":
            action_taken = "HQFR"
            output = "ACTION TO BE TAKEN IS TO HOME QUARANTINE"
        else:
            action_taken = "CWFR"
            output = "ACTION TO BE TAKEN IS TO CONTINUE WORKING"

        txt.append(test_result)
        txt.append(action_taken)

        print(output)

        test_2(code, patient_id, txt)

def test_2(code, patient_id, txt):
    test2= []
    test_number = 2
    txt.append(test_number)
    test2.append(patient_id)
    test2.append(test_number)
    print("============")
    print("TEST STAGE 2")
    print("[1].POSITIVE")
    print("[2].NEGATIVE")
    print("============")
    inp = int(input())

    if inp == 1:

        test_result = "POSITIVE"
        if code[patient_id] == "AEO" or code[patient_id] == "ATO" or code[patient_id] == "ACC" or code[
            patient_id] == "SID":
            action_taken = "QHNF"
        else:
            action_taken = "HQNF"


        txt.append(test_result)
        test2.append(test_result)
        txt.append(action_taken)
        test2.append(action_taken)

        if action_taken == "QHNF":
            print("========")
            print("[1].NW")
            print("[2].ICU")
            print("========")
            inp = int(input())
            if inp == 1:
                condition = "NW"
                output = "ACTION TO BE TAKEN IS TO QUARANTINE IN HOSPITAL NORMAL WARD"
            else:
                condition = "ICU"
                output = "ACTION TO BE TAKEN IS TO QUARANTINE IN HOSPITAL ICU"
            txt.append(condition)
            test2.append(condition)

        else:
            output = "ACTION TO BE TAKEN IS TO HOME QUARANTINE"

        str_positive_patient = get_positive_patient()
        print(str_positive_patient)
        int_positive_patient = []
        with open("positive_patients.txt", "r") as file:
            lines = file.read().splitlines()
            if not lines:
                case = 1
            else:
                last_line = lines[-1]
                case = int(last_line[0]) + 1

        for i in range(0, len(str_positive_patient)):
            int_positive_patient.append(int(str_positive_patient[i]))

        if patient_id not in int_positive_patient:
            with open("positive_patients.txt", "r") as file:
                lines = file.read().splitlines()
                if lines:
                    with open("positive_patients.txt", "a") as f:
                        f.write("\n")
            with open('positive_patients.txt', 'a') as file:
                string = str(case) + "-" + str(patient_id) + "-ACTIVE"
                file.write("%s" % str(string))

        with open("test_result.txt", "r") as file:
            lines = file.read().splitlines()
            if lines:
                txt.insert(0,"\n")

        with open("test_result2.txt", "r") as file:
            lines = file.read().splitlines()
            if lines:
                test2.insert(0,"\n")

        with open('test_result.txt', 'a') as file:
            for i in range(0, len(txt)):
                if i == len(txt) - 1:
                    file.write("%s" % str(txt[i]))
                elif txt[i] == "\n":
                    file.write("%s" % str(txt[i]))
                else:
                    file.write("%s-" % str(txt[i]))

        with open('test_result2.txt', 'a') as file:
            for i in range(0, len(test2)):
                if i == len(test2) - 1:
                    file.write("%s" % str(test2[i]))
                elif test2[i] == "\n":
                    file.write("%s" % str(txt[i]))
                else:
                    file.write("%s-" % str(test2[i]))

        print("TEST RESULT OF PATIENT HAS BEEN SUCCESSFULLY ADDED")
        print(output)

    else:

        test_result = "NEGATIVE"

        if code[patient_id] == "ATO" or code[patient_id] == "ACC" or code[patient_id] == "AEO":
            action_taken = "QDFR"
            output = "ACTION TO BE TAKEN IS TO QUARANTINE IN DESIGNATED CENTRES"
        elif code[patient_id] == "SID":
            action_taken = "HQFR"
            output = "ACTION TO BE TAKEN IS TO HOME QUARANTINE"
        else:
            action_taken = "CWFR"
            output = "ACTION TO BE TAKEN IS TO CONTINUE WORKING"


        txt.append(test_result)
        txt.append(action_taken)


        print(output)

        test_3(code, patient_id, txt)

def check_recovered_cases():
    RECOVERED = 0
    f = open("positive_patients.txt", "r")
    for line in f.readlines():
        if "R" in line:
            RECOVERED += 1
    return RECOVERED

def check_active_cases():
    ACTIVE = 0
    f = open("positive_patients.txt", "r")
    for line in f.readlines():
        if "A" in line:
            ACTIVE += 1
    return ACTIVE

def patient_registration():
    patient = []

    print("Patient Name:")
    inp = list(str(input()))
    for i in range(0, len(inp)):
        if inp[i] == " ":
            inp[i] = '_'
    inp = "".join(inp)
    patient.append(inp)

    print("Contact Number")
    inp = int(input())
    patient.append(inp)

    print("Email Address")
    inp = str(input())
    patient.append(inp)

    print("Input Zone")
    print("[1].A\n[2].B\n[3].C\n[4].D")
    inp = int(input())
    if inp == 1:
        zone = "A"
    elif inp == 2:
        zone = "B"
    elif inp == 3:
        zone = "C"
    else:
        zone = "D"
    patient.append(zone)

    print("Input Group Code")
    print("[1].ATO\n[2].ACC\n[3].AEO\n[4].SID\n[5].AHS")
    inp = int(input())
    if inp == 1:
        code = "ATO"
    elif inp == 2:
        code = "ACC"
    elif inp == 3:
        code = "AEO"
    elif inp == 4:
        code = "SID"
    else:
        code = "AHS"
    patient.append(code)

    with open("patients.txt", "r") as file:
        lines = file.read().splitlines()
        if not lines:
            id = 1001
            patient.insert(0, id)
        else:
            last_line = lines[-1]
            number = ""
            for char in last_line:
                if char == "-":
                    break
                number = number + char                
            id = int(number) + 1
            patient.insert(0, id)
            patient.insert(0,"\n")

    with open('patients.txt', 'a') as file:
        for i in range(0, len(patient)):
            if i == len(patient) - 1:
                file.write("%s" % str(patient[i]))
            elif patient[i] == "\n":
                file.write("%s" % str(patient[i]))
            else:
                file.write("%s-" % str(patient[i]))

    print("PATIENT DATA HAS BEEN SUCCESSFULLY ADDED")



def get_patiend_id_and_code():
    count = 0
    txt = []
    code = []
    temp = []
    name = []
    patient = []

    f = open("patients.txt", "r")
    for line in f.readlines():
        for char in line:
            if count == 1:
                name.append(char)
            if char == "-":
                count += 1

            if count == 2:
                break

        name = name[:-1]
        final = "".join(name)
        patient.append(final)
        del name[:]
        count = 0

    for i in range(0, len(patient)):
        print("[", i, "].", patient[i])

    f = open("patients.txt", "r")
    for line in f.readlines():
        for char in line:
            if count == 5:
                temp.append(char)
            if char == "-":
                count += 1
        if temp[-1] == "\n":
            temp = temp[:-1]
        final = "".join(temp)
        code.append(final)
        del temp[:]
        count = 0

    inp = int(input())
    patient_id = inp
    txt.append(patient_id)
    return(code, patient_id, txt)

def main_menu():
    print("============================")
    print("WELCOME TO COVID-19 HOSPITAL")
    print("[1].REGISTER  NEW PATIENT")
    print("[2].TEST RESULTS AND ACTION TAKEN")
    print("[3].EDIT PATIENT STATUS")
    print("[4].EXIT")
    print("============================")

    inp = int(input("INPUT:"))
    if inp == 1:
        patient_registration()

    elif inp == 2:
        print("===============")
        print("[1].TAKE COVID-19 TEST")
        print("[2].CHECK TEST RESULT")
        print("[3].BACK TO MAIN MENU")
        print("===============")

        inp = int(input("INPUT:"))

        if inp == 1:
            code,patient_id,txt = get_patiend_id_and_code()
            test_1(code,patient_id,txt)

        if inp ==2:
            print("=========================================")
            print("[1].CHECK TOTAL NUMBER OF CONDUCTED TESTS")
            print("[2].CHECK TOTAL NUMBER OF PATIENTS TESTED")
            print("[3].CHECK TOTAL NUMBER OF POSITIVE COVID-19 PATIENTS")
            print("[4].BACK TO MAIN MENU")
            print("=========================================")

            inp = int(input("INPUT:"))
            if inp == 1:
                count = len(open("test_result.txt").readlines())
                print("THERE ARE CURRENTLY",count,"CONDUCTED TESTS")
            if inp == 2:
                count = len(open("tested_patients.txt").readlines())
                print("THERE ARE CURRENTLY",count,"PATIENTS TESTED")
            if inp == 3:
                count = len(open("positive_patients.txt").readlines())
                print("THERE ARE CURRENTLY",count,"PATIENTS TESTED POSITIVE")
            if inp ==4:
                main_menu()
        if inp == 3:
            main_menu()
    elif inp == 3:
        print("===================")
        print("[1].EDIT PATIENT STATUS")
        print("[2].CHECK TOTAL NUMBER OF RECOVERED CASES")
        print("[3].CHECK TOTAL NUMEBR OF ACTIVE CASES")
        print("[4].BACK TO MAIN MENU")
        print("===================")
        inp = int(input("INPUT:"))

        if inp == 1:
            edit_patient_status()
        if inp == 2:
            print("THERE ARE CURRENTLY",check_recovered_cases(),"RECOVERED PATIENTS")
        if inp == 3:
            print("THERE ARE CURRENTLY",check_active_cases(),"ACTIVE CASES")
        if inp == 4:
            main_menu()
    elif inp == 4:
        print("GOODBYE! SEE YOU NEXT TIME.")
        quit()


while True:
    main_menu()