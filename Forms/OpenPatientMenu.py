from PySide6.QtWidgets import QMainWindow, QPushButton, QListView, QListWidgetItem, QListWidget, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QIcon, QAction
from Source import db_access

from Forms import MedicalRecordWindow, HomePage, PatientLookup, Login, NewPatientWindow
# from Classes import AppointmentTimeAndDate, Patient, General
from MedicalRecords.Classes import AppointmentTimeAndDate


class OpenPatientMenu(QMainWindow):
    def __init__(self, current_user, selected_location, mrn):
        super().__init__()
        self.loader = QUiLoader()

        self.current_user = current_user
        self.selected_location = selected_location
        self.mrn = mrn
        print("In open patient menu " + mrn)

        # Initialize Form
        self.open_patient_menu = self.loader.load("Forms/openPatientMenu.ui")

        # Initialize Sub-Forms
        self.medical_records_window = MedicalRecordWindow.MedicalRecord
        self.new_patient = NewPatientWindow.NewPatient
        self.homepage = HomePage.HomePage
        self.patient_lookup = PatientLookup.PatientLookup
        self.login = Login.Login

        # ------ Remove if database is active ----- #
        # self.mrn = "202301"
        # self.current_user = "Test"

        # Set Actions
        self.actionhome = self.open_patient_menu.findChild(QAction, "actionhome")
        self.actionhome.triggered.connect(self.on_actionhome_clicked)
        icon9 = QIcon("Images/home.png")
        self.actionhome.setIcon(icon9)
        self.actionnewPatient = self.open_patient_menu.findChild(QAction, "actionnewPatient")
        self.actionnewPatient.triggered.connect(self.on_actionnewPatient_clicked)
        icon10 = QIcon("Images/plus-button.png")
        self.actionnewPatient.setIcon(icon10)
        self.actionpatientSearch = self.open_patient_menu.findChild(QAction, "actionpatientSearch")
        self.actionpatientSearch.triggered.connect(self.on_actionpatientSearch_clicked)
        icon11 = QIcon("Images/magnifier.png")
        self.actionpatientSearch.setIcon(icon11)
        self.actionlogout = self.open_patient_menu.findChild(QAction, "actionlogout")
        self.actionlogout.triggered.connect(self.on_actionlogout_clicked)
        icon12 = QIcon("Images/door-arrow.png")
        self.actionlogout.setIcon(icon12)

        # Initialize Select Appointment Button
        self.select_appointment_pushButton = self.open_patient_menu.findChild(QPushButton, "select_appointment_pushButton")
        self.select_appointment_pushButton.clicked.connect(self.on_select_appointment_pushButton_clicked)

        # Initialize Create New Appointment Button
        self.create_new_appointment_pushButton = self.open_patient_menu.findChild(QPushButton, "create_new_appointment_pushButton")
        self.create_new_appointment_pushButton.clicked.connect(self.on_create_new_appointment_pushButton_clicked)

        # Initialize Text Fields
        self.appointment_history_listView = self.open_patient_menu.findChild(QListWidget, "appointment_history_listView")

    def on_actionlogout_clicked(self):
        self.login = self.login()
        self.login.initialize_login()
        self.open_patient_menu.close()

    def on_actionpatientSearch_clicked(self):
        self.patient_lookup = self.patient_lookup(self.current_user, self.selected_location)
        self.patient_lookup.initialize_patient_lookup()
        self.open_patient_menu.close()

    def on_actionnewPatient_clicked(self):
        self.new_patient = self.new_patient(self.current_user, self.selected_location)
        self.new_patient.initialize_new_patient_window()
        self.open_patient_menu.close()

    def on_actionhome_clicked(self):
        self.homepage = self.homepage(self.current_user, self.selected_location)
        self.homepage.initialize_homepage()
        self.open_patient_menu.close()

    def initialize_open_patient_menu_window(self):
        self.get_patient_app_info(self.mrn)
        self.open_patient_menu.show()

    def on_select_appointment_pushButton_clicked(self):
        list_item = self.appointment_history_listView.currentItem()
        if list_item:
            self.medical_records_window = self.medical_records_window(self.current_user, self.selected_location)
            self.login = self.login()
            self.appointment_info_str = list_item.text()
            app_date_time, app_status, app_id = self.appointment_info_str.split(",", 3)
            self.appointment_info = AppointmentTimeAndDate.AppointmentTimeAndDate(app_date_time, app_status, app_id)
            self.initialize_fields_for_select_appointment_button_clicked(self.current_user, self.appointment_info, app_id)
            self.medical_records_window.initialize_medical_record_window()
            self.open_patient_menu.close()
        else:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setWindowTitle("Error")
            msg_box.setText("Error, please make a selection.")
            msg_box.exec_()

    def on_create_new_appointment_pushButton_clicked(self):
        self.medical_records_window = self.medical_records_window(self.current_user, self.selected_location)
        self.initialize_fields_for_create_appointment_button_clicked(self.current_user, self.selected_location)
        self.medical_records_window.initialize_medical_record_window()
        self.open_patient_menu.close()

    def get_patient_app_info(self, mrn):
        appointments = db_access.get_appointments(mrn)

        for appointment in appointments:
            item = f"{appointment.get_appointment_time_and_date()}, {appointment.get_status()}, {appointment.get_appointment_id()}"
            self.appointment_history_listView.addItem(item)

    """
    # comment out if database active

    def get_patient_app_info(self, patient_info, app_info, general_info):
        test_app = AppointmentTimeAndDate.AppointmentTimeAndDate(appointment_time_and_date=app_info['app_time_and_date'],
                                                                          status=app_info['status'])

        test_patient = Patient.Patient(first_name=patient_info['first_name'],
                                            last_name=patient_info['last_name'],
                                            gender=patient_info['gender'],
                                            medical_record_num=patient_info['MRN'],
                                            date_of_birth=patient_info['DOB'],
                                            social_security_num=patient_info['ssn'])
    
        general_patient_info = General.General(weight=general_info['weight'],
                                           height_ft=general_info['height_ft'],
                                           height_in=general_info['height_in'],
                                           smoking=general_info['smoking'],
                                           drinking=general_info['drinking'],
                                           exercise=general_info['exercise'],
                                           drugs=general_info['drugs'],
                                           appointment_type=general_info['app_type'],
                                           chief_complaint=general_info['chief_complaint'])

        patient_app_info = str(test_patient.get_first_name() + " " + test_patient.get_last_name()) + str(test_app.get_appointment_time_and_date()) + str(general_patient_info.get_appointment_type())
        self.appointment_history_listView.addItem(patient_app_info)
    """

    # Get data from database and initialize fields of the Medical Records Window
    def initialize_fields_for_select_appointment_button_clicked(self, logged_in_user, appointment_info, app_id):
        patient_info = self.medical_records_window.get_patient_demo_information_from_db(self.mrn)
        patient_address_info = self.medical_records_window.get_patient_address_info_from_db(self.mrn)
        billing_address_info = self.medical_records_window.get_billing_address_info_from_db(self.mrn)
        guarantor_address_info = self.medical_records_window.get_guarantor_address_info_from_db(self.mrn)
        guarantor_info = self.medical_records_window.get_guarantor_info_from_db(self.mrn)
        emergency_contact_info_1 = self.medical_records_window.get_emergency_contact_info_1_from_db(self.mrn)
        emergency_contact_info_2 = self.medical_records_window.get_emergency_contact_info_2_from_db(self.mrn)
        emergency_contact_info_3 = self.medical_records_window.get_emergency_contact_info_3_from_db(self.mrn)
        general_info = self.medical_records_window.get_general_info_from_db(self.mrn)
        allergy_info = self.medical_records_window.get_allergy_info_from_db(self.mrn)
        medication_info = self.medical_records_window.get_medication_info_from_db(self.mrn)
        medical_history_info = self.medical_records_window.get_medical_history_info_from_db(self.mrn)
        injury_history_info = self.medical_records_window.get_injury_history_info_from_db(self.mrn)
        surgery_history_info = self.medical_records_window.get_surgery_history_info_from_db(self.mrn)
        lab_info = self.medical_records_window.get_lab_info_from_db(self.mrn)
        care_plan_info = self.medical_records_window.get_care_plan_info_from_db(self.mrn)
        referral_info = self.medical_records_window.get_referral_info_from_db(self.mrn)
        # appointment_info = self.medical_records_window.get_appointment_info_from_db(self.mrn)
        office_location_info = self.medical_records_window.get_office_location_info_from_db(app_id)
        appointment_staff_info = self.medical_records_window.get_appointment_staff_info_from_db(app_id)
        vitals_info = self.medical_records_window.get_vitals_info_from_db(self.mrn)
        physician_notes_info = self.medical_records_window.get_physician_notes_info_from_db(self.mrn)
        procedures_performed_info = self.medical_records_window.get_procedures_performed_info_from_db(self.mrn)
        follow_up_info = self.medical_records_window.get_follow_up_info_from_db(self.mrn)
        medical_record_audit_info = self.medical_records_window.get_medical_record_audit_info_from_db(self.mrn)
        self.set_data_from_database_to_initialize_fields(patient_info, patient_address_info, billing_address_info,
                                                         guarantor_address_info, guarantor_info, emergency_contact_info_1,
                                                         emergency_contact_info_2, emergency_contact_info_3, general_info,
                                                         allergy_info, medication_info, medical_history_info,
                                                         injury_history_info, surgery_history_info, lab_info, care_plan_info,
                                                         referral_info, appointment_info, office_location_info,
                                                         appointment_staff_info, vitals_info, physician_notes_info,
                                                         procedures_performed_info, follow_up_info, medical_record_audit_info,
                                                         logged_in_user)

    def set_data_from_database_to_initialize_fields(self, patient_info, patient_address_info, billing_address_info,
                                                    guarantor_address_info, guarantor_info, emergency_contact_info_1,
                                                    emergency_contact_info_2, emergency_contact_info_3, general_info,
                                                    allergy_info, medication_info, medical_history_info,
                                                    injury_history_info, surgery_history_info, lab_info, care_plan_info,
                                                    referral_info, appointment_info, office_location_info,
                                                    appointment_staff_info, vitals_info, physician_notes_info,
                                                    procedures_performed_info, follow_up_info, medical_record_audit_info,
                                                    logged_in_user):
        self.medical_records_window.set_patient_info_to_display(patient_info)
        self.medical_records_window.set_demographics_tab_fields(patient_info, patient_address_info,
                                                                billing_address_info, guarantor_address_info,
                                                                guarantor_info, logged_in_user)
        self.medical_records_window.set_emergency_contacts_tab_fields(emergency_contact_info_1,
                                                                      emergency_contact_info_2, emergency_contact_info_3,
                                                                      logged_in_user)
        self.medical_records_window.set_general_tab_fields(general_info, logged_in_user)
        self.medical_records_window.set_allergy_tab_fields(allergy_info, logged_in_user)
        self.medical_records_window.set_medication_tab_fields(medication_info, logged_in_user)
        self.medical_records_window.set_exam_assessments_tab_fields(appointment_info, office_location_info, appointment_staff_info,
                                                                    vitals_info, physician_notes_info, procedures_performed_info,
                                                                    follow_up_info, logged_in_user)
        self.medical_records_window.set_medical_history_tab_fields(medical_history_info, logged_in_user)
        self.medical_records_window.set_injury_and_surgical_history_tab_fields(injury_history_info, surgery_history_info,
                                                                               logged_in_user)
        self.medical_records_window.set_labs_tab_fields(lab_info, logged_in_user)
        self.medical_records_window.set_care_plan_tab_fields(care_plan_info, logged_in_user)
        self.medical_records_window.set_referrals_tab_fields(referral_info, logged_in_user)
        self.medical_records_window.set_clinical_summary_tab_fields(appointment_info, general_info, care_plan_info, physician_notes_info,
                                                                    appointment_staff_info, vitals_info, logged_in_user)
        self.medical_records_window.set_medical_record_history_tab_fields(medical_record_audit_info, logged_in_user)

    def initialize_fields_for_create_appointment_button_clicked(self, logged_in_user, selected_location):
        patient_info = self.medical_records_window.get_patient_demo_information_from_db(self.mrn)
        patient_address_info = self.medical_records_window.get_patient_address_info_from_db(self.mrn)
        billing_address_info = self.medical_records_window.get_billing_address_info_from_db(self.mrn)
        guarantor_address_info = self.medical_records_window.get_guarantor_address_info_from_db(self.mrn)
        guarantor_info = self.medical_records_window.get_guarantor_info_from_db(self.mrn)
        emergency_contact_info_1 = self.medical_records_window.get_emergency_contact_info_1_from_db(self.mrn)
        emergency_contact_info_2 = self.medical_records_window.get_emergency_contact_info_2_from_db(self.mrn)
        emergency_contact_info_3 = self.medical_records_window.get_emergency_contact_info_3_from_db(self.mrn)
        self.set_data_from_database_to_initialize_fields_create_new_appointment_clicked(patient_info, patient_address_info,
                                                                                   billing_address_info, guarantor_address_info,
                                                                                   guarantor_info, emergency_contact_info_1,
                                                                                   emergency_contact_info_2, emergency_contact_info_3,
                                                                                   logged_in_user, selected_location)
    def set_data_from_database_to_initialize_fields_create_new_appointment_clicked(self, patient_info, patient_address_info,
                                                                                   billing_address_info, guarantor_address_info,
                                                                                   guarantor_info, emergency_contact_info_1,
                                                                                   emergency_contact_info_2, emergency_contact_info_3,
                                                                                   logged_in_user, selected_location):
        self.medical_records_window.set_patient_info_to_display(patient_info)
        self.medical_records_window.set_demographics_tab_fields(patient_info, patient_address_info,
                                                                billing_address_info, guarantor_address_info,
                                                                guarantor_info, logged_in_user)
        self.medical_records_window.set_emergency_contacts_tab_fields(emergency_contact_info_1,
                                                                      emergency_contact_info_2,
                                                                      emergency_contact_info_3,
                                                                      logged_in_user)
        self.medical_records_window.set_logged_in_user_for_create_new_appointment(logged_in_user)
        self.medical_records_window.set_office_location_for_create_new_appointment(selected_location)
