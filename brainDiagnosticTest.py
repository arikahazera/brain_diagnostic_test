# Dataset 1: A list that consists of informations about the diagnostic tests provided
listTest = [
    {
        'name' : 'EEG',
        'type' : 'Neurophysiology',
        'function' : ['''Records the electrical activity of the brain through electrodes placed on the scalp''', 
                      'Captures brain waves', 
                      '''Provides real-time dynamic monitoring of the brain activity'''],
        'indication' : ['''To classify seizure types and localise seizure onset''', 
                        '''To differentiate epileptic seizures from other neurological or psychiatric conditions'''],
        'preparation' : ['Avoid caffeine, stimulants, and lack of sleep prior to test', 
                         'Avoid using hair products'],
        'diagnosis' : ['Epilepsy', 'Seizure', 'Brain tumors', 'Brain injury', 
                       'Encelopathy', 'Inflammation', 'Stroke', 'Sleep disorders']
    },
    {
        'name' : 'EMG',
        'type' : 'Neurophysiology',
        'function' : ['''Measures electrical activity produced by skeletal muscles to assess muscle health and nerve cells that controls them'''],
        'indication' : ['''To differentiate between muscle and nerve disorders''', 
                        '''To localise lesions affecting the peripheral nervous system'''],
        'preparation' : ['''Avoid caffeine 24 hours prior''', 
                         '''Avoid lotions, oils, or creams on the skin''', 
                         '''Wear loose-fitting clothes'''],
        'diagnosis' : ['Muscle disorders', 'Nerve disorders', 
                       'Peripheral nerve injuries', 'Neuromuscular junction disorders']
    },
    {
        'name' : 'MRI',
        'type' : 'Neuroimaging',
        'function' : ['''Creates detailed images of organs and tissues inside the body by using magnetic fields and radio waves.'''],
        'indication' : ['''When soft tissue contrast is needed to assess structural abnormalities and detect lesions invisible on CT scan'''],
        'preparation' : ['Remove all metallic items', '''Inform the doctor if patients have implanted devices in the body''', 
                         'Patients may require fasting if contrast dye is used'],
        'diagnosis' : ['Brain tumors', 'Inflammation', 'Degenerative diseases']
    },
    {
        'name' : 'CT Scan',
        'type' : 'Neuroimaging',
        'function' : ['''produces cross-sectional images of bones, blood vessels, and soft tissues by combining x-ray images taken from different angles'''],
        'indication' : ['''When rapid evaluation is needed in acute settings of stroke, head trauma, skull fractures, etc'''],
        'preparation' : ['Remove all metallic items', 
                         'Patients may require fasting if contrast dye is used'],
        'diagnosis' : ['Stroke', 'Hemorrhages', 'Fractures', 'Large brain injuries']
    },
    {
        'name' : 'PET Scan',
        'type' : 'Neuroimaging',
        'function' : ['''visualises biochemical activity and metabolic processes within tissues and organs by using a radioactive tracer'''],
        'indication' : ['To evaluate brain metabolism and function in neurodegenerative diseases', 
                        'To localise epileptic foci', 'To grade brain tumors'],
        'preparation' : ['Avoid heavy exercise 24 hours prior', 'Fast for 4 to 6 hours prior', 
                         'Avoid caffeine, alcohol, and tobacco'],
        'diagnosis' : ['Tumors', 'Dementia', 'Epilepsy', "Parkinson's disease"]
    }
]

# Function 1: This function is used to display the information about the tests before making appointments
def diagnosticTest():
    print('Offered diagnostic tests: ')
    
    for test in listTest: # "test": The items that are listed under listTest
        print(f'{test['name']} ({test['type']})')
        print('Function: ')

        # "isinstance()" function: The function is used to check the items mentioned is a list before doing looping
        # The function purpose in this case: 
        # Some of the items stored as lists with multiple elements, while others are single strings. 
        # Using isinstance() ensures that the program only loops through items that are actually lists (preventing errors).
        if isinstance(test['function'], list):
            for function in test['function']:
                print(f'- {function}')
        print()

        print('When to conduct this test? ')
        if isinstance(test['indication'], list):
            for ind in test['indication']:
                print(f'- {ind}')
        print()

        print('What to prepare before the test? ')
        if isinstance(test['preparation'], list):
            for prep in test['preparation']:
                print(f'- {prep}')
        print()
        print()

# Dataset 2: A list that consists of the information needed about the patients who wanted to place for an appointment
listAppointment = [
    {
        'Name' : 'Sagara Alam',
        'DOB' : '23/11/2001',
        'Test Appointment' : 'MRI',
        'Date & Time' : '18/10/2025 (10 AM)',
        'Test Result' : ''
    },
    {
        'Name' : 'Rachel Chu',
        'DOB' : '06/05/1998',
        'Test Appointment' : 'EMG',
        'Date & Time' : '20/10/2025 (2 PM)',
        'Test Result' : ''
    }
]

# Function 2: This function is used to view the patient appointments data
def viewAppointment():
    print('Patient Appointments Data\n')
    print('No. |     Name   \t|     DOB \t|   Test \t|  Date & Time')
    for i, appointment in enumerate(listAppointment, start=1):
        print(f'{i}   | {appointment['Name']}  \t|  {appointment['DOB']} \t|    {appointment['Test Appointment']}  \t|  {appointment['Date & Time']}')

# Function 3: This function is used to add a new appointment to the current appointments data
def addAppoint():
    patientName = input('Full name: ')
    patientBirth = input('Date of birth (dd/mm/yyyy): ')
    patientTest = input(f'Test request: ')
    date_time = input('Date and time of test (dd/mm/yyyy (XX AM/PM)): ')
    confirm = input('Submit this form? (Y/N): ')
    if confirm.capitalize() == 'Y':
        print(f'Appointment is set for {patientName} ({patientTest}).')
    else:
        print('Appointment is cancelled.')

    listAppointment.append({
            'Name': patientName,
            'DOB': patientBirth,
            'Test Appointment': patientTest,
            'Date & Time': date_time
        })
    print()

    # Loop function to display the common diagnosis outcome from the selected test in the appointment form
    if patientTest == 'EEG':
        print(f'Common diagnosis made from this test: {setDiagnosisEEG}.')
    elif patientTest == 'EMG':
        print(f'Common diagnosis made from this test: {setDiagnosisEMG}.')
    elif patientTest == 'MRI':
        print(f'Common diagnosis made from this test: {setDiagnosisMRI}.')
    elif patientTest == 'CT Scan':
        print(f'Common diagnosis made from this test: {setDiagnosisCT}.')
    else:
        print(f'Common diagnosis made from this test: {setDiagnosisPET}.')

setDiagnosisEEG = {'Epilepsy', 'Seizure', 'Brain tumors', 'Brain injury', 'Encelopathy', 'Inflammation', 'Stroke', 'Sleep disorders'}
setDiagnosisEMG = {'Muscle disorders', 'Nerve disorders', 'Peripheral nerve injuries', 'Neuromuscular junction disorders'}
setDiagnosisMRI = {'Brain tumors', 'Inflammation', 'Degenerative diseases'}
setDiagnosisCT = {'Stroke', 'Hemorrhages', 'Fractures', 'Large brain injuries'}
setDiagnosisPET = {'Brain tumors', 'Dementia', 'Epilepsy', "Parkinson's disease"}

# Function 4: This function is used to allow users to update any details in the appointment form
def updateAppoint ():
    print('Update Appointment Details: ')
    viewAppointment()
    print()
    index = int(input('Enter patient number: ')) - 1

    chooseUpdate = input('''
        1. Name
        2. Date of Birth
        3. Test Appointment
        4. Date & Time
        
        Enter the number to update: ''')
    print()
    
    if chooseUpdate == '1':
        newName = input('Full name: ')
        listAppointment[index]['Name'] = newName
    elif chooseUpdate == '2':
        newDOB = input('Date of Birth: ')
        listAppointment[index]['DOB'] = newDOB
    elif chooseUpdate == '3':
        newTest = input('Test Appointment: ')
        listAppointment[index]['Test Appointment'] = newTest
    elif chooseUpdate == '4':
        newDT = input('Date & Time: ')
        listAppointment[index]['Date & Time'] = newDT
    print()
    viewAppointment()
    
# Function 5: This function is used to delete existing appointments in the program
def deleteAppoint():
    print('Delete Appointment')
    print()
    name = input('Enter patient name: ')
    found = False

    for appointment in listAppointment:
        if appointment['Name'].lower() == name.lower(): # To allow case-insensitive
            confirm = input('Are you sure to delete this appointment? (Y/N): ')
            if confirm == 'Y':
                listAppointment.remove(appointment)
                print(f'Appointment for {name} is deleted.')
            else:
                print(f'Request is cancelled.')
            found = True
    if not found:
            print('Appointment not found!')
            

# Function 6: This function is used to update the results of the patient's test on the program based on the appointment data
def updateResults():
    viewAppointment()
    print()
    selectedPatient = int(input(f'Enter the patient Number: ')) - 1

    if 0 <= selectedPatient < len(listAppointment): # To ensure the index is correct
        patientResult = input('Enter the test result: ')
        listAppointment[selectedPatient]['Test Result'] = patientResult
        print(f'Result added for {listAppointment[selectedPatient]['Name']}.')
    else:
        print('Patient number not found!')
    print()

    print('No. |     Name   \t|     DOB \t|   Test \t|  Date & Time     \t|   Test Result')
    for i, appointment in enumerate(listAppointment, start=1):
        print(f'{i}   | {appointment['Name']}  \t|  {appointment['DOB']} \t|    {appointment['Test Appointment']}  \t|  {appointment['Date & Time']}  \t|   {appointment['Test Result']}')

# Function 7: This function is used to print exit message when the program is closed
def exit():
    print('Thank you for using this service. Stay safe and take care :)')

# To ensure the main menu keep popping up (allowing multiple actions)
role = input('Menu for admin or patient? ').lower()

while True:
    if role == 'admin':
        mainMenu = input('''
            Guide to Neurological Diagnostic Tests!
                1. List of Available Diagnostic Tests
                2. Add New Appointments
                3. Update Details
                4. Delete Appointments
                5. View All Appointments
                6. Update Test Results
                7. Exit Program

                Insert Menu Number: ''')
        if mainMenu == '1':
            diagnosticTest()
        elif mainMenu == '2':
            addAppoint()
        elif mainMenu == '3':
            updateAppoint()
        elif mainMenu == '4':
            deleteAppoint()
        elif mainMenu == '5':
            viewAppointment()
        elif mainMenu == '6':
            updateResults()
        elif mainMenu == '7':
            exit()
            break
    elif role == 'patient':
        mainMenu = input('''
            Guide to Neurological Diagnostic Tests!
            
            1. List of Available Diagnostic Tests
            2. Add New Appointments
            3. Update Details
            4. Delete Appointments
            5. Exit Program

            Insert Menu Number: ''')
        print()

        if mainMenu == '1':
            diagnosticTest()
        elif mainMenu == '2':
            addAppoint()
        elif mainMenu == '3':
            updateAppoint()
        elif mainMenu == '4':
            deleteAppoint()
        elif mainMenu == '5':
            exit()
            break
    else:
        print('Invalid role.')
        break
