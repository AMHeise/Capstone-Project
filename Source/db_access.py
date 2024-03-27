import os
import pyodbc
import sys
from contextlib import closing

from Classes import Medication, Sibling, Referrals, Demographics, EmergencyContact, Allergy, General, \
    MedicalHistory, AppointmentTimeAndDate, Address, CarePlan, FollowUp, InjuryHistory, Labs, PhysicianNotes, \
    ProceduresPerformed, SurgicalHistory, UserLogin, Vitals, MedicalRecordAuditLog


# Call connection
from MedicalRecords.Classes import Guarantor, OfficeLocations, AppointmentStaff


def connect():
    try:
        if sys.platform == "win32":
            db = "Driver={ODBC Driver 18 for SQL Server};" \
                 "Server=tcp:capstone2023.database.windows.net,1433;" \
                 "Database=capstone2023;" \
                 "Uid=medRecordsUser;" \
                 "Pwd=Password01!;" \
                 "Encrypt=yes;" \
                 "TrustServerCertificate=no;" \
                 "Connection Timeout=30;"
        else:
            home = os.environ["HOME"]
            db = home + "Driver={ODBC Driver 18 for SQL Server};" \
                        "Server=tcp:capstone2023.database.windows.net,1433;" \
                        "Database=capstone2023;" \
                        "Uid=medRecordsUser;" \
                        "Pwd=Password01!;" \
                        "Encrypt=yes;" \
                        "TrustServerCertificate=no;" \
                        "Connection Timeout=30;"

        conn = pyodbc.connect(db)
        return conn
    except IOError as e:
        print(e)
        conn = False
        return conn


# ----------------------------------------------------------------------------------------------------------------------


def create_new_address(mrn, street_address, city, state, zip_code, apt_num):
    conn = connect()
    query = f"INSERT INTO MRAddress (MRN, StreetAddress, City, State, ZipCode, AptNum)" \
            f"VALUES ({mrn}, '{street_address}', '{city}', '{state}', '{zip_code}', '{apt_num}')"

    with closing(conn.cursor()) as c:
        c.execute(query)
        conn.commit()


def create_new_allergy(mrn, allergy_name, allergy_type, date_added):
    conn = connect()
    query = f"INSERT INTO MRAllergy (MRN, AllergyName, AllergyType, DateAdded)" \
            f"VALUES ({mrn}, '{allergy_name}', '{allergy_type}', '{date_added}')"

    with closing(conn.cursor()) as c:
        c.execute(query)
        conn.commit()


def create_new_appointment(mrn, appointment_time_and_date, status):
    conn = connect()
    query = f"INSERT INTO MRAppointment (MRN, AppointmentDateAndTime, Status)" \
            f"VALUES ({mrn}, '{appointment_time_and_date}', '{status}')"

    with closing(conn.cursor()) as c:
        c.execute(query)
        conn.commit()


def create_new_care_plan(mrn, assessment, planning, diagnosis, post_evaluation, date_added,
                         frequency, frequency_type, end_date):
    conn = connect()
    query = f"INSERT INTO MRCarePlan (MRN, Assessment, Planning, Diagnosis, PostEvaluation, DateAdded," \
            f"                        Frequency, FrequencyType, EndDate)" \
            f"VALUES ({mrn}, '{assessment}', '{planning}', '{diagnosis}', '{post_evaluation}', '{date_added}'," \
            f"       '{frequency}', '{frequency_type}', '{end_date}')"

    with closing(conn.cursor()) as c:
        c.execute(query)
        conn.commit()


def create_new_patient(mrn, first_name, last_name, gender, date_of_birth, ssn, middle_name="", suffix=""):
    conn = connect()
    query = f"INSERT INTO MRPatient (FirstName, LastName, Gender, DateOfBirth, SSN, MiddleName, Suffix)" \
            f"VALUES ('{first_name}', '{last_name}', '{gender}', '{date_of_birth}', '{ssn}', '{middle_name}', '{suffix}')"

    with closing(conn.cursor()) as c:
        c.execute(query)
        conn.commit()


def create_new_emergency_contact(mrn, first_name, last_name, gender, relationship, phone_num, email_address=""):
    conn = connect()
    query = f"INSERT INTO MREmergencyContact (MRN, FirstName, LastName, Gender, Relationship, PhoneNum, EmailAddress)" \
            f"VALUES ({mrn}, '{first_name}', '{last_name}', '{gender}', '{relationship}', '{phone_num}', '{email_address}')"

    with closing(conn.cursor()) as c:
        c.execute(query)
        conn.commit()


def create_new_follow_up(mrn, needed, follow_up_frequency, follow_up_frequency_type):
    conn = connect()
    query = f"INSERT INTO MRFollowUp (MRN, Needed, FollowUpFrequency, FollowUpFrequencyType)" \
            f"VALUES ({mrn}, {needed}, '{follow_up_frequency}', '{follow_up_frequency_type}')"

    with closing(conn.cursor()) as c:
        c.execute(query)
        conn.commit()


def create_new_general(mrn, weight, height_ft, height_in, smoking, drinking, exercise, drugs,
                       appointment_type, chief_complaint):
    conn = connect()
    query = f"INSERT INTO MRFollowUp (MRN, Weight, HeightFt, HeightIn, Smoking, Drinking, Exercise, Drugs," \
            f"                        AppointmentType, ChiefComplaint)" \
            f"VALUES ({mrn}, {weight}, {height_ft}, {height_in}, {smoking}, {drinking}, {exercise}, {drugs}," \
            f"       '{appointment_type}', '{chief_complaint}')"

    with closing(conn.cursor()) as c:
        c.execute(query)
        conn.commit()


def create_new_guarantor(mrn, first_name, last_name, gender, relationship, phone_num):
    conn = connect()
    query = f"INSERT INTO MRGuarantor (MRN, FirstName, LastName, Gender, Relationship, PhoneNum)" \
            f"VALUES ({mrn}, '{first_name}', '{last_name}', '{gender}', '{relationship}', '{phone_num}')"

    with closing(conn.cursor()) as c:
        c.execute(query)
        conn.commit()


def create_new_injury_history(mrn, description, date_occurred):
    conn = connect()
    query = f"INSERT INTO MRInjuryHistory (MRN, Description, DateOccurred)" \
            f"VALUES ({mrn}, '{description}', '{date_occurred}')"

    with closing(conn.cursor()) as c:
        c.execute(query)
        conn.commit()


def create_new_lab(mrn, lab_type, date_requested, status):
    conn = connect()
    query = f"INSERT INTO MRLabs (MRN, LabType, DateRequested, Status)" \
            f"VALUES ({mrn}, '{lab_type}', '{date_requested}', '{status}')"

    with closing(conn.cursor()) as c:
        c.execute(query)
        conn.commit()


def create_new_medical_history(mrn, diagnosis, history_type):
    conn = connect()
    query = f"INSERT INTO MRMedicalHistory (MRN, Diagnosis, HistoryType)" \
            f"VALUES ({mrn}, '{diagnosis}', '{history_type}')"

    with closing(conn.cursor()) as c:
        c.execute(query)
        conn.commit()


def create_new_medical_record_audit(mrn, field_changed, employee_id, first_name, last_name, date_changed):
    conn = connect()
    query = f"INSERT INTO MRMedicalRecordAudit (MRN, FieldChanged, EmployeeID, FirstName, LastName, DateChanged)" \
            f"VALUES ({mrn}, '{field_changed}', {employee_id}, '{first_name}', '{last_name}', '{date_changed}')"

    with closing(conn.cursor()) as c:
        c.execute(query)
        conn.commit()


def create_new_medication(mrn, medication_name, dose_amount, dose_type, frequency, frequency_type, medication_type):
    conn = connect()
    query = f"INSERT INTO MRMedications (MRN, MedicationName, Dosage, DosageType, DosageFrequency," \
            f"                          DosageFrequencyType, MedicationType)" \
            f"VALUES ({mrn}, '{medication_name}', {dose_amount}, '{dose_type}', '{frequency}', " \
            f"       '{frequency_type}', '{medication_type}')"

    with closing(conn.cursor()) as c:
        c.execute(query)
        conn.commit()


def create_new_physician_notes(mrn, notes, date_added):
    conn = connect()
    query = f"INSERT INTO MRPhysicianNotes (MRN, Notes, DateAdded)" \
            f"VALUES ({mrn}, '{notes}', '{date_added}')"

    with closing(conn.cursor()) as c:
        c.execute(query)
        conn.commit()


def create_new_procedure_performed(mrn, procedure):
    conn = connect()
    query = f"INSERT INTO MRProceduresPerformed (MRN, Notes, DateAdded)" \
            f"VALUES ({mrn}, '{procedure}')"

    with closing(conn.cursor()) as c:
        c.execute(query)
        conn.commit()


def create_new_referral(mrn, referral_num, referral_reason, status, referral_provider="", provider_npi="",
                        referral_date="", referral_expiration_date="", patient_condition=""):
    conn = connect()
    query = f"INSERT INTO MRReferral (ReferralID, ReferralReason, ReferralProvider, ProviderNPI," \
            f"                         ReferralDate, ReferralExpirationDate, PatientCondition, Status, MRN)" \
            f"VALUES ({referral_num}, '{referral_reason}', '{referral_provider}', '{provider_npi}'," \
            f"       '{referral_date}', '{referral_expiration_date}', '{patient_condition}', '{status}', {mrn})"

    with closing(conn.cursor()) as c:
        c.execute(query)
        conn.commit()


def create_new_sibling(mrn, first_name, last_name, gender):
    conn = connect()
    query = f"INSERT INTO MRSibling (MRN, FirstName, LastName, Gender)" \
            f"VALUES ({mrn}, '{first_name}', '{last_name}', '{gender}')"

    with closing(conn.cursor()) as c:
        c.execute(query)
        conn.commit()


def create_new_surgical_history(mrn, description, date_occurred):
    conn = connect()
    query = f"INSERT INTO MRSurgicalHistory (MRN, Description, DateOccurred)" \
            f"VALUES ({mrn}, '{description}', '{date_occurred}')"

    with closing(conn.cursor()) as c:
        c.execute(query)
        conn.commit()


def create_new_user_login(username, password, first_name, last_name, access_level):
    conn = connect()
    query = f"INSERT INTO MRUserLogin (Username, Password, FirstName, LastName, AccessLevel)" \
            f"VALUES ('{username}', '{password}', '{first_name}', '{last_name}', '{access_level}')"

    with closing(conn.cursor()) as c:
        c.execute(query)
        conn.commit()


def create_new_vitals(mrn, temperature, systolic_blood_pressure, diastolic_blood_pressure, respiration_rate,
                      pulse_rate, blood_oxygen_levels):
    conn = connect()
    query = f"INSERT INTO MRVitals (MRN, Temperature, SystolicBloodPressure, DiastolicBloodPressure, RespirationRate," \
            f"                      PulseRate, BloodOxygenLevels)" \
            f"VALUES ({mrn}, '{temperature}', '{systolic_blood_pressure}', '{diastolic_blood_pressure}', " \
            f"       '{respiration_rate}', '{pulse_rate}', '{blood_oxygen_levels}')"

    with closing(conn.cursor()) as c:
        c.execute(query)
        conn.commit()


# ----------------------------------------------------------------------------------------------------------------------


def search_patients(first_name="", last_name="", date_of_birth="", ssn="", mrn=""):
    conn = connect()
    query = f"SELECT FistName, LastName, DateOfBirth, SSN, MRN " \
            f"FROM MRPatient " \
            f"WHERE (FirstName = {first_name} AND " \
            f"      LastName = {last_name} AND " \
            f"      DateOfBirth = {date_of_birth} AND " \
            f"      SSN = {ssn} AND " \
            f"      MRN = {mrn})"

    with closing(conn.cursor()) as c:
        c.execute(query, )
        search_results = c.fetchall()

    return search_results


# ----------------------------------------------------------------------------------------------------------------------


def remove_allergies(mrn, allergy):
    conn = connect()
    query = f"DELETE FROM MRAllergy " \
            f"WHERE (AllergyName = {allergy.get_allergy_name()} " \
            f"       AND AllergyType = {allergy.get_allergy_type()} " \
            f"       AND MRN = {mrn})"

    with closing(conn.cursor()) as c:
        c.execute(query)
        conn.commit()


def remove_injury_history(mrn, injury_history):
    conn = connect()
    query = f"DELETE FROM MRInjuryHistory " \
            f"WHERE (Description = {injury_history.get_description()} " \
            f"       AND MRN = {mrn})"

    with closing(conn.cursor()) as c:
        c.execute(query)
        conn.commit()


def remove_medicine(mrn, medication):
    conn = connect()
    query = f"DELETE FROM MRMedications " \
            f"WHERE (MedicationName = {medication.get_medication_name()} " \
            f"       AND MedicationType = {medication.get_medication_type()} " \
            f"       AND MRN = {mrn})"

    with closing(conn.cursor()) as c:
        c.execute(query)
        conn.commit()


def remove_medical_history(mrn, medical_history):
    conn = connect()
    query = f"DELETE FROM MRMedicalHistory " \
            f"WHERE (Procedure = {medical_history.get_diagnosis()} " \
            f"       AND HistoryType = {medical_history.get_history_type()}" \
            f"       AND MRN = {mrn})"

    with closing(conn.cursor()) as c:
        c.execute(query)
        conn.commit()


def remove_procedure(mrn, procedure):
    conn = connect()
    query = f"DELETE FROM MRProceduresPerformed " \
            f"WHERE (Procedure = {procedure.get_procedure()} " \
            f"       AND MRN = {mrn})"

    with closing(conn.cursor()) as c:
        c.execute(query)
        conn.commit()


def remove_surgery_history(mrn, surgery_history):
    conn = connect()
    query = f"DELETE FROM MRSurgicalHistory " \
            f"WHERE (Procedure = {surgery_history.get_description()} " \
            f"       AND MRN = {mrn})"

    with closing(conn.cursor()) as c:
        c.execute(query)
        conn.commit()


def remove_pending_lab(mrn, labs):
    conn = connect()
    query = f"DELETE FROM MRLabs " \
            f"WHERE (Procedure = {labs.get_date_requested()} " \
            f"       AND Status = {labs.get_status()}" \
            f"       AND MRN = {mrn})"

    with closing(conn.cursor()) as c:
        c.execute(query)
        conn.commit()


# ----------------------------------------------------------------------------------------------------------------------
# Fix marked lines to update correct info


def update_address(mrn, street_address, city, state, zip_code, apt_num):
    conn = connect()
    query = f"UPDATE MRAddress " \
            f"SET StreetAddress = '{street_address}', City = '{city}', State = '{state}', " \
            f"    ZipCode = '{zip_code}', AptNum = '{apt_num}' " \
            f"WHERE MRN = {mrn}"

    with closing(conn.cursor()) as c:
        c.execute(query)
        conn.commit()


def update_allergy(allergy_id, allergy_name, allergy_type, date_added):
    conn = connect()
    query = f"UPDATE MRAllergy " \
            f"SET AllergyName = '{allergy_name}', AllergyType = '{allergy_type}', DateAdded = '{date_added}' " \
            f"WHERE AllergyID = {allergy_id}"

    with closing(conn.cursor()) as c:
        c.execute(query)
        conn.commit()


def update_appointment(appointment_id, appointment_time_and_date, status):
    conn = connect()
    query = f"UPDATE MRAppointment " \
            f"SET AppointmentTimeAndDate = '{appointment_time_and_date}', Status = '{status}' " \
            f"WHERE AppointmentID = {appointment_id}"

    with closing(conn.cursor()) as c:
        c.execute(query)
        conn.commit()


def update_care_plan(care_plan_id, assessment, planning, diagnosis, post_evaluation, date_added,
                     frequency, frequency_type, end_date):
    conn = connect()
    query = f"UPDATE MRCarePlan " \
            f"SET Assessment = '{assessment}', Planning = '{planning}', Diagnosis = '{diagnosis}', " \
            f"    PostEvaluation = '{post_evaluation}', DateAdded = '{date_added}', Frequency = '{frequency}', " \
            f"    FrequencyType = '{frequency_type}', EndDate = '{end_date}' " \
            f"WHERE CarePlanID = {care_plan_id}"

    with closing(conn.cursor()) as c:
        c.execute(query)
        conn.commit()


def update_patient(mrn, first_name, last_name, gender, date_of_birth, ssn, middle_name="", suffix=""):
    conn = connect()
    query = f"UPDATE MRPatient " \
            f"SET FirstName = '{first_name}', LastName = '{last_name}', Gender = '{gender}', " \
            f"    DateOfBirth = '{date_of_birth}', SSN = '{ssn}', MiddleName = '{middle_name}', Suffix = '{suffix}' " \
            f"WHERE MRN = {mrn}"

    with closing(conn.cursor()) as c:
        c.execute(query)
        conn.commit()


def update_emergency_contact(emergency_contact_id, first_name, last_name, gender, relationship,
                             phone_num, email_address=""):
    conn = connect()
    query = f"UPDATE MREmergencyContacts " \
            f"SET Firstname = '{first_name}', LastName = '{last_name}', Gender = '{gender}', " \
            f"    Relationship = '{relationship}', PhoneNum = '{phone_num}', EmailAddress = '{email_address}' " \
            f"WHERE EmergencyContactID = {emergency_contact_id}"

    with closing(conn.cursor()) as c:
        c.execute(query)
        conn.commit()


def update_follow_up(follow_up_id, needed, follow_up_frequency, follow_up_frequency_type):
    conn = connect()
    query = f"UPDATE MRFollowUp " \
            f"SET Needed = {needed}, FollowUpFrequency = '{follow_up_frequency}', " \
            f"    FollowUpFrequencyType = '{follow_up_frequency_type}' " \
            f"WHERE FollowUpID = {follow_up_id}"

    with closing(conn.cursor()) as c:
        c.execute(query)
        conn.commit()


def update_general(general_id, weight, height_ft, height_in, smoking, drinking, exercise, drugs,
                   appointment_type, chief_complaint):
    conn = connect()
    query = f"UPDATE MRGeneral " \
            f"SET Weight = {weight}, HeightFt = {height_ft}, HeightIn = {height_in}, Smoking = {smoking}, " \
            f"    Drinking = {drinking}, Exercise = {exercise}, Drugs = {drugs}, " \
            f"    AppointmentType = '{appointment_type}', ChiefComplaint = '{chief_complaint}'" \
            f"WHERE GeneralID = {general_id}"

    with closing(conn.cursor()) as c:
        c.execute(query)
        conn.commit()


def update_guarantor(guarantor_id, first_name, last_name, gender, relationship, phone_num):
    conn = connect()
    query = f"UPDATE MRGuarantor " \
            f"SET FirstName = '{first_name}', LastName = '{last_name}', Gender = '{gender}', " \
            f"    Relationship = '{relationship}', PhoneNum = '{phone_num}'" \
            f"WHERE GuarantorID = {guarantor_id}"

    with closing(conn.cursor()) as c:
        c.execute(query)
        conn.commit()


def update_injury_history(injury_history_id, description, date_occurred):
    conn = connect()
    query = f"UPDATE MRInjuryHistory " \
            f"SET Description = '{description}', DateOccurred = '{date_occurred}' " \
            f"WHERE InjuryHistoryID = {injury_history_id}"

    with closing(conn.cursor()) as c:
        c.execute(query)
        conn.commit()


def update_labs(lab_id, lab_type, date_requested, status):
    conn = connect()
    query = f"UPDATE MRLab " \
            f"SET LabType = '{lab_type}', DateRequested = '{date_requested}', Status = '{status}' " \
            f"WHERE LabID = {lab_id}"

    with closing(conn.cursor()) as c:
        c.execute(query)
        conn.commit()


def update_medical_history(medical_history_id, diagnosis, history_type):
    conn = connect()
    query = f"UPDATE MRMedicalHistory " \
            f"SET Diagnosis = '{diagnosis}', HistoryType = '{history_type}' " \
            f"WHERE MedicalHistoryID = {medical_history_id}"

    with closing(conn.cursor()) as c:
        c.execute(query)
        conn.commit()


def update_medication(medication_id, medication_name, dose_amount, dose_type, frequency,
                      frequency_type, medication_type):
    conn = connect()
    query = f"UPDATE MRMedications " \
            f"SET MedicationName = '{medication_name}', DoseAmount = {dose_amount}, DoseType = '{dose_type}', " \
            f"    Frequency = '{frequency}', FrequencyType = '{frequency_type}', MedicationType = '{medication_type}'" \
            f"WHERE MedicationID = {medication_id}"

    with closing(conn.cursor()) as c:
        c.execute(query)
        conn.commit()


def update_physician_notes(physician_notes_id, notes, date_added):
    conn = connect()
    query = f"UPDATE MRPhysicianNotes " \
            f"SET Notes = '{notes}', DateAdded = '{date_added}' " \
            f"WHERE PhysicianNotesID = {physician_notes_id}"

    with closing(conn.cursor()) as c:
        c.execute(query)
        conn.commit()


def update_procedure_performed(procedure_id, procedure):
    conn = connect()
    query = f"UPDATE MRProcedures_Performed " \
            f"SET Procedure = '{procedure}' " \
            f"WHERE ProcedureID = {procedure_id}"

    with closing(conn.cursor()) as c:
        c.execute(query)
        conn.commit()


def update_referral(referral_id, referral_num, referral_reason, status, referral_provider="", provider_npi="",
                    referral_date="", referral_expiration_date="", patient_condition=""):
    conn = connect()
    query = f"UPDATE MRInjuryHistory " \
            f"SET ReferralNum = {referral_num}, ReferralReason = '{referral_reason}', Status = '{status}', " \
            f"    ReferralProvider = '{referral_provider}', ProviderNPI = '{provider_npi}', " \
            f"    ReferralDate = '{referral_date}', ReferralExpirationDate = '{referral_expiration_date}'," \
            f"    PatientCondition = '{patient_condition}' " \
            f"WHERE ReferralID = {referral_id}"

    with closing(conn.cursor()) as c:
        c.execute(query)
        conn.commit()


def update_sibling(sibling_id, first_name, last_name, gender):
    conn = connect()
    query = f"UPDATE MRSibling " \
            f"SET FirstName = '{first_name}', LastName = '{last_name}', Gender = '{gender}' " \
            f"WHERE SiblingID = {sibling_id}"

    with closing(conn.cursor()) as c:
        c.execute(query)
        conn.commit()


def update_surgical_history(surgical_history_id, description, date_occurred):
    conn = connect()
    query = f"UPDATE MRSurgicalHistory " \
            f"SET Description = '{description}', DateOccurred = '{date_occurred}' " \
            f"WHERE SurgicalHistoryID = {surgical_history_id}"

    with closing(conn.cursor()) as c:
        c.execute(query)
        conn.commit()


def update_user_login(employee_id, username, password, first_name, last_name, access_level):
    conn = connect()
    query = f"UPDATE MRUserLogin " \
            f"SET Username = '{username}', Password = '{password}', FirstName = '{first_name}', Lastname = '{last_name}'," \
            f"    AccessLevel = '{access_level}' " \
            f"WHERE EmployeeID = {employee_id}"

    with closing(conn.cursor()) as c:
        c.execute(query)
        conn.commit()


def update_vitals(vitals_id, temperature, systolic_blood_pressure, diastolic_blood_pressure, respiration_rate,
                  pulse_rate, blood_oxygen_levels):
    conn = connect()
    query = f"UPDATE MRVitals " \
            f"SET Temperature = '{temperature}', SystolicBloodPressure = '{systolic_blood_pressure}', " \
            f"    DiastolicBloodPressure = '{diastolic_blood_pressure}', RespirationRate = '{respiration_rate}', " \
            f"    PulseRate = '{pulse_rate}', BloodOxygenLevels = '{blood_oxygen_levels}' " \
            f"WHERE VitalsID = {vitals_id}"

    with closing(conn.cursor()) as c:
        c.execute(query)
        conn.commit()


# ----------------------------------------------------------------------------------------------------------------------


def get_address(mrn):
    conn = connect()
    address = Address.Address
    query = f"SELECT StreetAddress, City, State, ZipCode, AptNum " \
            f"FROM MRAddress " \
            f"WHERE MRN = {mrn}"

    with closing(conn.cursor()) as c:
        c.execute(query, )
        output = c.fetchall()

    for row in output:
        address = address(row[0], row[1], row[2], row[3], row[4])

    return address


def get_allergies(mrn):
    conn = connect()
    allergies = []
    query = f"SELECT AllergyName, AllergyType, DateAdded " \
            f"FROM MRAllergy " \
            f"WHERE MRN = {mrn}"

    with closing(conn.cursor()) as c:
        c.execute(query, )
        output = c.fetchall()

    for row in output:
        allergies.append(Allergy.Allergy(row[0], row[1], row[2]))

    return allergies


def get_appointments(mrn):
    conn = connect()
    appointments = []
    query = f"SELECT AppointmentTimeAndDate, Status, AppointmentID " \
            f"FROM MRAppointment " \
            f"WHERE MRN = {mrn}"

    with closing(conn.cursor()) as c:
        c.execute(query, )
        output = c.fetchall()

    for row in output:
        appointments.append(AppointmentTimeAndDate.AppointmentTimeAndDate(row[0], row[1], row[2]))

    return appointments

def get_appointment_staff(app_id):
    conn = connect()
    appointment_staff = AppointmentStaff.AppointmentStaff
    query = f"SELECT PrimaryProvider, AppointmentProvider, AppointmentNurse, AppointmentCNA " \
            f"FROM MRAppointment " \
            f"WHERE AppointmentID = {app_id}"

    with closing(conn.cursor()) as c:
        c.execute(query, )
        output = c.fetchall()

    for row in output:
        appointment_staff = appointment_staff(row[0], row[1], row[2], row[3])

    return appointment_staff

def get_appointment_location(appointment_id):
    conn = connect()
    location = OfficeLocations.OfficeLocations
    query = f"SELECT Location " \
            f"FROM MRAppointment " \
            f"WHERE AppointmentID = {appointment_id}"

    with closing(conn.cursor()) as c:
        c.execute(query, )
        output = c.fetchall()

    for row in output:
        location = location(row[0])

    return location


def get_care_plan(mrn):
    conn = connect()
    care_plans = CarePlan.CarePlan
    query = f"SELECT Assessment, Planning, Diagnosis, PostEvaluation, DateAdded, Frequency, FrequencyType," \
            f"       EndDate " \
            f"FROM MRCarePlan " \
            f"WHERE MRN = {mrn}"

    with closing(conn.cursor()) as c:
        c.execute(query, )
        output = c.fetchall()

    for row in output:
        care_plans = care_plans(row[0], row[1], row[2], row[3],
                                            row[4], row[5], row[6], row[7])

    return care_plans


def get_emergency_contacts(mrn):
    conn = connect()
    emergency_contacts = []
    query = f"SELECT FirstName, LastName, Gender, Relationship, PhoneNum, Email " \
            f"FROM MREmergencyContacts " \
            f"WHERE MRN = {mrn}"

    with closing(conn.cursor()) as c:
        c.execute(query, )
        output = c.fetchall()

    for row in output:
        emergency_contacts.append(EmergencyContact.EmergencyContact(row[0], row[1], row[2],
                                                                    row[3], row[4], row[5]))

    return emergency_contacts


def get_follow_up(mrn):
    conn = connect()
    follow_up = FollowUp.FollowUp
    query = f"SELECT Needed, FollowUpFrequency, FollowUpFrequencyType " \
            f"FROM MRFollowUp " \
            f"WHERE MRN = {mrn}"

    with closing(conn.cursor()) as c:
        c.execute(query, )
        output = c.fetchall()

    for row in output:
        follow_up = follow_up(row[0], row[1], row[2])

    return follow_up


def get_general(mrn):
    conn = connect()
    general = General.General
    query = f"SELECT Weight, HeightFt, HeightIn, Smoking, Drinking, Exercise, Drugs, AppointmentType," \
            f"       ChiefComplaint " \
            f"FROM MRGeneral " \
            f"WHERE MRN = {mrn}"

    with closing(conn.cursor()) as c:
        c.execute(query, )
        output = c.fetchall()

    for row in output:
        general = general(row[0], row[1], row[2], row[3], row[4],
                                       row[5], row[6], row[7], row[8])

    return general


def get_guarantor(mrn):
    conn = connect()
    guarantor = Guarantor.Guarantor
    query = f"SELECT FirstName, MiddleName, LastName, Gender, Relationship, PhoneNum " \
            f"FROM MRGuarantor " \
            f"WHERE MRN = {mrn}"

    with closing(conn.cursor()) as c:
        c.execute(query, )
        output = c.fetchall()

    for row in output:
        guarantor = guarantor(row[0], row[1], row[2], row[3], row[4], row[5])

    return guarantor


def get_injury_history(mrn):
    conn = connect()
    injury_history = []
    query = f"SELECT Description, DateOccurred " \
            f"FROM MRInjuryHistory " \
            f"WHERE MRN = {mrn}"

    with closing(conn.cursor()) as c:
        c.execute(query, )
        output = c.fetchall()

    for row in output:
        injury_history.append(InjuryHistory.InjuryHistory(row[0], row[1]))

    return injury_history


def get_labs(mrn):
    conn = connect()
    labs = []
    query = f"SELECT LabType, DateRequested, Status " \
            f"FROM MRLab " \
            f"WHERE MRN = {mrn}"

    with closing(conn.cursor()) as c:
        c.execute(query, )
        output = c.fetchall()

    for row in output:
        labs.append(Labs.Labs(row[0], row[1], row[2]))

    return labs


def get_medical_history(mrn):
    conn = connect()
    medical_history = []
    query = f"SELECT Diagnosis, HistoryType " \
            f"FROM MRMedicalHistory " \
            f"WHERE MRN = {mrn}"

    with closing(conn.cursor()) as c:
        c.execute(query, )
        output = c.fetchall()

    for row in output:
        medical_history.append(MedicalHistory.MedicalHistory(row[0], row[1]))

    return medical_history


def get_medical_record_audits(mrn):
    conn = connect()
    medical_record_audits = []
    query = f"SELECT FieldChanged, EmployeeID, FirstName, LastName, DateChanged, MedicalRecordAuditID " \
            f"FROM MRMedicalRecordAudit " \
            f"WHERE MRN = {mrn}"

    with closing(conn.cursor()) as c:
        c.execute(query, )
        output = c.fetchall()

    for row in output:
        medical_record_audits.append(MedicalRecordAuditLog.MedicalRecordAuditLog(row[0], row[1],
                                                                                 row[2], row[3],
                                                                                 row[4], row[5]))

    return medical_record_audits


def get_medication_info(mrn):
    conn = connect()
    medications = []
    query = f"SELECT MedicationName, Dosage, DosageType, DosageFrequency, " \
            f"       DosageFrequencyType, MedicationType " \
            f"FROM MRMedications " \
            f"WHERE MRN = {mrn}"

    with closing(conn.cursor()) as c:
        c.execute(query, )
        output = c.fetchall()

    for row in output:
        medications.append(Medication.Medication(row[0], row[1], row[2],
                                                 row[3], row[4],
                                                 row[5]))

    return medications


def get_patient_demographics(mrn):
    conn = connect()
    demographics = Demographics.Demographics
    query = f"SELECT MRN, Firstname, LastName, Gender, DateOfBirth, SSN, PhoneNum, " \
            f"       Ethnicity, MaritalStatus, Age, MiddleName, Suffix, Email, Deceased, " \
            f"       DateOfDeath " \
            f"FROM MRPatient " \
            f"WHERE MRN = {mrn}"

    with closing(conn.cursor()) as c:
        c.execute(query, )
        output = c.fetchall()

    for row in output:
        demographics = demographics(row[0], row[1], row[2], row[3], row[4], row[5], row[6],
                                    row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14])

    return demographics


def get_physician_notes(mrn):
    conn = connect()
    physician_notes = PhysicianNotes.PhysicianNotes
    query = f"SELECT Notes, DateAdded " \
            f"FROM MRPhysicianNotes " \
            f"WHERE MRN = {mrn}"

    with closing(conn.cursor()) as c:
        c.execute(query, )
        output = c.fetchall()

    for row in output:
        physician_notes = physician_notes(row[0], row[1])

    return physician_notes


def get_procedures_performed(mrn):
    conn = connect()
    procedures_performed = []
    query = f"SELECT ProcedureInfo " \
            f"FROM MRProceduresPerformed " \
            f"WHERE MRN = {mrn}"

    with closing(conn.cursor()) as c:
        c.execute(query, )
        output = c.fetchall()

    for row in output:
        procedures_performed.append(ProceduresPerformed.ProceduresPerformed(row[0]))

    return procedures_performed


# WIP IN PROGRESS
def get_referral_info(mrn):
    conn = connect()
    referrals = []
    query = f"SELECT ReferralID, ReferralReason, ReferralProvider, ProviderNPI, ReferralDate, ReferralExpirationDate," \
            f"       PatientCondition, Status " \
            f"FROM MRReferral " \
            f"WHERE MRN = {mrn}"

    with closing(conn.cursor()) as c:
        c.execute(query, )
        output = c.fetchall()

    for row in output:
        referrals.append(Referrals.Referrals(row[0], row[1], row[2],
                                             row[3], row[4], row[5],
                                             row[6], row[7]))

    return referrals


def get_siblings(mrn):
    conn = connect()
    siblings = []
    query = f"SELECT SiblingID, FirstName, LastName, Gender " \
            f"FROM MRSibling " \
            f"WHERE MRN = {mrn}"

    with closing(conn.cursor()) as c:
        c.execute(query, )
        output = c.fetchall()

    for row in output:
        siblings.append(Sibling.Sibling(row[0], row[1], row[2], row[3]))

    return siblings


def get_surgery_history(mrn):
    conn = connect()
    surgery_history = []
    query = f"SELECT Description, DateOccurred " \
            f"FROM MRSurgeryHistory " \
            f"WHERE MRN = {mrn}"

    with closing(conn.cursor()) as c:
        c.execute(query, )
        output = c.fetchall()

    for row in output:
        surgery_history.append(SurgicalHistory.SurgeryHistory(row[0], row[1]))

    return surgery_history


def get_user_login(username, password):
    conn = connect()
    user_login = []
    query = f"SELECT Username, Password, EmployeeID, FirstName, LastName, AccessLevel " \
            f"FROM MRUserLogin " \
            f"WHERE Username = {username}" \
            f"  AND Password = {password}"

    with closing(conn.cursor()) as c:
        c.execute(query, )
        output = c.fetchone()

    for row in output:
        user_login.append(UserLogin.UserLogin(row[0], row[1], row[2], row[3],
                                              row[4], row[5]))

    return user_login


def get_vitals(mrn):
    conn = connect()
    vitals = Vitals.Vitals
    query = f"SELECT * "\
            f"FROM MRVitals " \
            f"WHERE MRN = {mrn}"

    with closing(conn.cursor()) as c:
        c.execute(query, )
        output = c.fetchall()

    for row in output:
        vitals = vitals(row[1], row[2], row[3], row[4], row[5], row[6])

    return vitals

def get_mrn():
    conn = connect()
    query = f"SELECT TOP 1 MRN "\
            f"FROM MRPatient "\
            f"ORDER BY MRN DESC"

    with closing(conn.cursor()) as c:
        c.execute(query)
        output = c.fetchone()

    mrn = output[0]
    return mrn

