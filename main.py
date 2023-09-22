import mysql.connector

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="hospital_management_system"
)

# Create tables if they don't exist
def create_tables():
    cursor = db.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS doctors (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            age INT,
            date_of_birth DATE,
            mobile_no VARCHAR(15),
            specialization VARCHAR(255),
            fees DECIMAL(10, 2),
            years_of_experience INT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS patient (
            customer_ID INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            age INT,
            gender VARCHAR(10),
            address VARCHAR(255),
            contact_no VARCHAR(15),
            date_of_birth DATE,
            consultant_name VARCHAR(255)
        )
    """)
     cursor.execute("""
        CREATE TABLE IF NOT EXISTS room (
            room_no INT AUTO_INCREMENT PRIMARY KEY,
            room_type VARCHAR(50),
            room_charges_per_day DECIMAL(10, 2),
            room_status VARCHAR(20),
            patient_name VARCHAR(255)
        )
    """)
    db.commit()


def insert_doctor():
    cursor = db.cursor()
    name = input("Enter doctor's name: ")
    age = int(input("Enter age: "))
    date_of_birth = input("Enter date of birth (YYYY-MM-DD): ")
    mobile_no = input("Enter mobile number: ")
    specialization = input("Enter specialization: ")
    fees = float(input("Enter fees: "))
    years_of_experience = int(input("Enter years of experience: "))
    query = "INSERT INTO doctors (name, age, date_of_birth, mobile_no, specialization, fees, years_of_experience) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values = (name, age, date_of_birth, mobile_no, specialization, fees, years_of_experience)
    cursor.execute(query, values)
    db.commit()
    print("Doctor record inserted.")


def update_doctor():
    cursor = db.cursor()
    doctor_id = int(input("Enter doctor's ID to update: "))
    # Check if the doctor exists
    cursor.execute("SELECT id FROM doctors WHERE id = %s", (doctor_id,))
    if not cursor.fetchone():
        print("Doctor not found.")
        return
    # Get new data
    name = input("Enter new name: ")
    age = int(input("Enter new age: "))
    date_of_birth = input("Enter new date of birth (YYYY-MM-DD): ")
    mobile_no = input("Enter new mobile number: ")
    specialization = input("Enter new specialization: ")
    fees = float(input("Enter new fees: "))
    years_of_experience = int(input("Enter new years of experience: "))
    query = "UPDATE doctors SET name=%s, age=%s, date_of_birth=%s, mobile_no=%s, specialization=%s, fees=%s, years_of_experience=%s WHERE id=%s"
    values = (name, age, date_of_birth, mobile_no, specialization, fees, years_of_experience, doctor_id)
    cursor.execute(query, values)
    db.commit()
    print("Doctor record updated.")


def delete_doctor():
    cursor = db.cursor()
    doctor_id = int(input("Enter doctor's ID to delete: "))
    cursor.execute("DELETE FROM doctors WHERE id = %s", (doctor_id,))
    db.commit()
    print("Doctor record deleted.")


def display_doctors():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM doctors")
    doctors = cursor.fetchall()
    if not doctors:
        print("No doctors found.")
        return
    for doctor in doctors:
        print(doctor)

def insert_patient():
        cursor = db.cursor()
        patient_ID = int(input("Enter id of Patient: "))
        name = input("Enter name of Patient: ")
        age = int(input("Enter age of Patient: "))
        gender = input("Enter gender of Patient: ")
        address = input("Enter address of Patient: ")
        contact_no = input("Enter contact no of Patient: ")
        date_of_birth = input("Enter date of birth of Patient: ")
        consultant_name = input("Enter consultant name of Patient: ")
        date_of_consultancy = input("Enter date of consultancy of Patient: ")
        consultancy_fees = int(input("Enter consultancy fees of Patient: "))
        query = "INSERT INTO patient( patient_ID,name,age,gender,address,contact_no,date_of_birth,consultant_name,date_of_consultancy,consultancy_fees)values(%d,'%s',%d,'%s','%s','%s','%s','%s','%s','%s',%d)"
        values = (patient_ID, name, age, gender, address, contact_no, date_of_birth, consultant_name, date_of_consultancy, consultancy_fees)
        cursor.execute(query,values)
        db.commit()

def display_patient():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM patient")
    patients = cursor.fetchall()
    if not patients:
        print("No patient found.")
        return
    for patient in patients:
        print(patient)

def update_patient():
        cursor = db.cursor()
        patient_ID = int(input("Enter patient ID to update: "))
        cursor.execute("SELECT id FROM patient WHERE id = %d", (patient_ID,))
        if not cursor.fetchone():
            print("Patient not found.")
            return
        name = input("Enter name of Patient: ")
        age = int(input("Enter age of Patient: "))
        gender = input("Enter gender of Patient: ")
        address = input("Enter address of Patient: ")
        contact_no = input("Enter contact no of Patient: ")
        date_of_birth = input("Enter date of birth of Patient: ")
        consultant_name = input("Enter consultant name of Patient: ")
        date_of_consultancy = input("Enter date of consultancy of Patient: ")
        consultancy_fees = int(input("Enter consultancy fees of Patient: "))
        query = "update patient set name='%s',age=%d ,gender='%s',address='%s',contact_no='%s',date_of_birth='%s',consultant_name='%s',date_of_consultancy='%s',department='%s',consultancy_fees=%d where patient_ID= %d"
        values = (name, age, gender, address, contact_no, date_of_birth, consultant_name, date_of_consultancy, department,
            consultancy_fees, patient_ID)
        cursor.execute(query,values)
        db.commit()

def delete_patient():
    cursor = db.cursor()
    patient_ID = int(input("Enter patient ID to delete: "))
    cursor.execute("DELETE FROM patient WHERE id = %s", (patient_ID,))
    db.commit()
    print("Patient record deleted.")

def insert_room():
        cursor = db.cursor()
        room_no = int(input("Enter Room no: "))
        room_type = input("Enter Room type: ")
        room_charges_per_day = int(input("Enter room charges per day: "))
        room_status = input("Enter room status: ")
        patient_name = input("Enter patient name: ")
        query = "insert into room_info(room_no, room_type, room_charges_per_day, room_status, patient_name )values(%d,'%s',%d,'%s','%s')"
        values = (room_no, room_type, room_charges_per_day, room_status, patient_name)
        cursor.execute(query,values)
        db.commit()

def display_room():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM room")
    rooms = cursor.fetchall()
    if not rooms:
        print("No room found.")
        return
    for room in rooms:
        print(room)


def update_room():
        cursor = db.cursor()
        room_no = int(input("Enter room no to update: "))
        cursor.execute("SELECT id FROM room WHERE id = %d", (room_no))
        if not cursor.fetchone():
            print("Room not found.")
            return
        room_no = int(input("Enter Room no: "))
        room_type = input("Enter Room type: ")
        room_charges_per_day = int(input("Enter room charges per day: "))
        room_status = input("Enter room status: ")
        patient_name = input("Enter patient name of occupied room: ")
        query = "update room_ set room_type='%s',room_charges_per_day=%d,room_status='%s',patient_name='%s'where room_no= %d"
        values = (room_type, room_charges_per_day, room_status, patient_name, room_no)
        cursor.execute(query,values)
        db.commit()


def delete_room():
    cursor = db.cursor()
    room_no = int(input("Enter room ID to delete: "))
    cursor.execute("DELETE FROM room WHERE id = %s", (room_no,))
    db.commit()
    print("room record deleted.")


# Main function
def main():
    create_tables()
    while True:
        print(
            "1.Add Record Of Doctors\n2.Update Record Of Existing Doctors\n3.Delete Record Of Doctors\n4.Access All The Records Of Doctors\n5.Add Record Of patients\n6.Update Record Of Existing patients\n7.Delete Record Of patients\n8.Access All The Records Of patients\n9.Add Record Of room info\n10.Update Record Of Existing room info\n11.Delete Record Of room info\n12.Access All The Records Of room info")
        # Repeat for other options

        a = int(input("Enter your choice (1-16): "))
        if a == '1':
            insert_doctor()

        elif a == '2':
            update_doctor()

        elif a == '3':
            display_doctors()
            delete_doctor()

        elif a == '4':
            display_doctors()

        elif a == '5':
            insert_patient()

        elif a == '6':
            update_patient()

        elif a == '7':
            display_patient()
            delete_patient()

        elif a == '8':
            display_patient()

        elif a == '9':
            insert_room()

        elif a == '10':
            update_room()

        elif a == '11':
            display_room()
            delete_room()

        elif a == '12':
            display_room()

main()
