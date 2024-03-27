import datetime

from PySide6.QtCore import QDateTime, QDate, Qt
from PySide6.QtWidgets import QMainWindow, QPushButton, QLabel, QLineEdit, QRadioButton, QComboBox, QCheckBox, \
    QListView, QListWidget
from PySide6.QtWidgets import QSpinBox, QDoubleSpinBox, QTextEdit, QTableView, QDateTimeEdit, QDateEdit, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QIcon, QAction

from Classes import Demographics, Address, Guarantor, EmergencyContact, Sibling, General, Allergy, Medication, Labs
from Classes import MedicalHistory, CarePlan, Referrals, AppointmentTimeAndDate, OfficeLocations, AppointmentStaff
from Classes import Vitals, PhysicianNotes, ProceduresPerformed, FollowUp, InjuryHistory, SurgicalHistory, \
    MedicalRecordAuditLog
from Forms import HomePage, NewPatientWindow, PatientLookup, Login
from MedicalRecords.Source import db_access


class MedicalRecord(QMainWindow):

    def __init__(self, current_user, selected_location):
        super().__init__()
        self.loader = QUiLoader()

        self.current_user = current_user
        self.selected_location = selected_location

        # Initialize Form
        self.medical_record = self.loader.load("Forms/medicalRecordWindow.ui")

        # Initialize Sub-Forms
        self.homepage = HomePage.HomePage
        self.new_patient = NewPatientWindow.NewPatient
        self.patient_lookup = PatientLookup.PatientLookup
        self.login = Login.Login

        # Set Actions
        self.actionhome = self.medical_record.findChild(QAction, "actionhome")
        self.actionhome.triggered.connect(self.on_actionhome_clicked)
        icon9 = QIcon("Images/home.png")
        self.actionhome.setIcon(icon9)
        self.actionnewPatient = self.medical_record.findChild(QAction, "actionnewPatient")
        self.actionnewPatient.triggered.connect(self.on_actionnewPatient_clicked)
        icon10 = QIcon("Images/plus-button.png")
        self.actionnewPatient.setIcon(icon10)
        self.actionpatientSearch = self.medical_record.findChild(QAction, "actionpatientSearch")
        self.actionpatientSearch.triggered.connect(self.on_actionpatientSearch_clicked)
        icon11 = QIcon("Images/magnifier.png")
        self.actionpatientSearch.setIcon(icon11)
        self.actionlogout = self.medical_record.findChild(QAction, "actionlogout")
        self.actionlogout.triggered.connect(self.on_actionlogout_clicked)
        icon12 = QIcon("Images/door-arrow.png")
        self.actionlogout.setIcon(icon12)

        # Initialize Text Fields

        # Patient information text fields (displayed on every tab) - Demographics Tab
        self.patient_photo_entry_label_demographics = self.medical_record.findChild(QLabel,
                                                                                    "patient_photo_entry_label_demographics")
        self.mrn_display_label_demographics = self.medical_record.findChild(QLabel, "mrn_display_label_demographics")
        self.first_name_display_label_demographics = self.medical_record.findChild(QLabel,
                                                                                   "first_name_display_label_demographics")
        self.middle_name_display_label_demographics = self.medical_record.findChild(QLabel,
                                                                                    "middle_name_display_label_demographics")
        self.last_name_display_label_demographics = self.medical_record.findChild(QLabel,
                                                                                  "last_name_display_label_demographics")
        self.suffix_display_label_demographics = self.medical_record.findChild(QLabel,
                                                                               "suffix_display_label_demographics")
        self.dob_display_label_demographics = self.medical_record.findChild(QLabel, "dob_display_label_demographics")
        self.age_display_label_demographics = self.medical_record.findChild(QLabel, "age_display_label_demographics")
        self.gender_display_label_demographics = self.medical_record.findChild(QLabel,
                                                                               "gender_display_label_demographics")
        self.ethnicity_display_label_demographics = self.medical_record.findChild(QLabel,
                                                                                  "ethnicity_display_label_demographics")
        self.ssn_display_label_demographics = self.medical_record.findChild(QLabel, "ssn_display_label_demographics")

        # Patient information text fields (displayed on every tab) - Emergency Contacts Tab
        self.patient_photo_entry_label_emergency_contacts = self.medical_record.findChild(QLabel,
                                                                                          "patient_photo_entry_label_emergency_contacts")
        self.mrn_display_label_emergency_contacts = self.medical_record.findChild(QLabel,
                                                                                  "mrn_display_label_emergency_contacts")
        self.first_name_display_label_emergency_contacts = self.medical_record.findChild(QLabel,
                                                                                         "first_name_display_label_emergency_contacts")
        self.middle_name_display_label_emergency_contacts = self.medical_record.findChild(QLabel,
                                                                                          "middle_name_display_label_emergency_contacts")
        self.last_name_display_label_emergency_contacts = self.medical_record.findChild(QLabel,
                                                                                        "last_name_display_label_emergency_contacts")
        self.suffix_display_label_emergency_contacts = self.medical_record.findChild(QLabel,
                                                                                     "suffix_display_label_emergency_contacts")
        self.dob_display_label_emergency_contacts = self.medical_record.findChild(QLabel,
                                                                                  "dob_display_label_emergency_contacts")
        self.age_display_label_emergency_contacts = self.medical_record.findChild(QLabel,
                                                                                  "age_display_label_emergency_contacts")
        self.gender_display_label_emergency_contacts = self.medical_record.findChild(QLabel,
                                                                                     "gender_display_label_emergency_contacts")
        self.ethnicity_display_label_emergency_contacts = self.medical_record.findChild(QLabel,
                                                                                        "ethnicity_display_label_emergency_contacts")
        self.ssn_display_label_emergency_contacts = self.medical_record.findChild(QLabel,
                                                                                  "ssn_display_label_emergency_contacts")

        # Patient information text fields (displayed on every tab) - General Tab
        self.patient_photo_entry_label_general = self.medical_record.findChild(QLabel,
                                                                               "patient_photo_entry_label_general")
        self.mrn_display_label_general = self.medical_record.findChild(QLabel, "mrn_display_label_general")
        self.first_name_display_label_general = self.medical_record.findChild(QLabel,
                                                                              "first_name_display_label_general")
        self.middle_name_display_label_general = self.medical_record.findChild(QLabel,
                                                                               "middle_name_display_label_general")
        self.last_name_display_label_general = self.medical_record.findChild(QLabel, "last_name_display_label_general")
        self.suffix_display_label_general = self.medical_record.findChild(QLabel, "suffix_display_label_general")
        self.dob_display_label_general = self.medical_record.findChild(QLabel, "dob_display_label_general")
        self.age_display_label_general = self.medical_record.findChild(QLabel, "age_display_label_general")
        self.gender_display_label_general = self.medical_record.findChild(QLabel, "gender_display_label_general")
        self.ethnicity_display_label_general = self.medical_record.findChild(QLabel, "ethnicity_display_label_general")
        self.ssn_display_label_general = self.medical_record.findChild(QLabel, "ssn_display_label_general")

        # Patient information text fields (displayed on every tab) - Allergies Tab
        self.patient_photo_entry_label_allergies = self.medical_record.findChild(QLabel,
                                                                                 "patient_photo_entry_label_allergies")
        self.mrn_display_label_allergies = self.medical_record.findChild(QLabel, "mrn_display_label_allergies")
        self.first_name_display_label_allergies = self.medical_record.findChild(QLabel,
                                                                                "first_name_display_label_allergies")
        self.middle_name_display_label_allergies = self.medical_record.findChild(QLabel,
                                                                                 "middle_name_display_label_allergies")
        self.last_name_display_label_allergies = self.medical_record.findChild(QLabel,
                                                                               "last_name_display_label_allergies")
        self.suffix_display_label_allergies = self.medical_record.findChild(QLabel, "suffix_display_label_allergies")
        self.dob_display_label_allergies = self.medical_record.findChild(QLabel, "dob_display_label_allergies")
        self.age_display_label_allergies = self.medical_record.findChild(QLabel, "age_display_label_allergies")
        self.gender_display_label_allergies = self.medical_record.findChild(QLabel, "gender_display_label_allergies")
        self.ethnicity_display_label_allergies = self.medical_record.findChild(QLabel,
                                                                               "ethnicity_display_label_allergies")
        self.ssn_display_label_allergies = self.medical_record.findChild(QLabel, "ssn_display_label_allergies")

        # Patient information text fields (displayed on every tab) - Medications Tab
        self.patient_photo_entry_label_medications = self.medical_record.findChild(QLabel,
                                                                                   "patient_photo_entry_label_medications")
        self.mrn_display_label_medications = self.medical_record.findChild(QLabel, "mrn_display_label_medications")
        self.first_name_display_label_medications = self.medical_record.findChild(QLabel,
                                                                                  "first_name_display_label_medications")
        self.middle_name_display_label_medications = self.medical_record.findChild(QLabel,
                                                                                   "middle_name_display_label_medications")
        self.last_name_display_label_medications = self.medical_record.findChild(QLabel,
                                                                                 "last_name_display_label_medications")
        self.suffix_display_label_medications = self.medical_record.findChild(QLabel,
                                                                              "suffix_display_label_medications")
        self.dob_display_label_medications = self.medical_record.findChild(QLabel, "dob_display_label_medications")
        self.age_display_label_medications = self.medical_record.findChild(QLabel, "age_display_label_medications")
        self.gender_display_label_medications = self.medical_record.findChild(QLabel,
                                                                              "gender_display_label_medications")
        self.ethnicity_display_label_medications = self.medical_record.findChild(QLabel,
                                                                                 "ethnicity_display_label_medications")
        self.ssn_display_label_medications = self.medical_record.findChild(QLabel, "ssn_display_label_medications")

        # Patient information text fields (displayed on every tab) - Exam Assessments Tab
        self.patient_photo_entry_label_exam_assessments = self.medical_record.findChild(QLabel,
                                                                                        "patient_photo_entry_label_exam_assessments")
        self.mrn_display_label_exam_assessments = self.medical_record.findChild(QLabel,
                                                                                "mrn_display_label_exam_assessments")
        self.first_name_display_label_exam_assessments = self.medical_record.findChild(QLabel,
                                                                                       "first_name_display_label_exam_assessments")
        self.middle_name_display_label_exam_assessments = self.medical_record.findChild(QLabel,
                                                                                        "middle_name_display_label_exam_assessments")
        self.last_name_display_label_exam_assessments = self.medical_record.findChild(QLabel,
                                                                                      "last_name_display_label_exam_assessments")
        self.suffix_display_label_exam_assessments = self.medical_record.findChild(QLabel,
                                                                                   "suffix_display_label_exam_assessments")
        self.dob_display_label_exam_assessments = self.medical_record.findChild(QLabel,
                                                                                "dob_display_label_exam_assessments")
        self.age_display_label_exam_assessments = self.medical_record.findChild(QLabel,
                                                                                "age_display_label_exam_assessments")
        self.gender_display_label_exam_assessments = self.medical_record.findChild(QLabel,
                                                                                   "gender_display_label_exam_assessments")
        self.ethnicity_display_label_exam_assessments = self.medical_record.findChild(QLabel,
                                                                                      "ethnicity_display_label_exam_assessments")
        self.ssn_display_label_exam_assessments = self.medical_record.findChild(QLabel,
                                                                                "ssn_display_label_exam_assessments")

        # Patient information text fields (displayed on every tab) - Medical History Tab
        self.patient_photo_entry_label_medical_history = self.medical_record.findChild(QLabel,
                                                                                       "patient_photo_entry_label_medical_history")
        self.mrn_display_label_medical_history = self.medical_record.findChild(QLabel,
                                                                               "mrn_display_label_medical_history")
        self.first_name_display_label_medical_history = self.medical_record.findChild(QLabel,
                                                                                      "first_name_display_label_medical_history")
        self.middle_name_display_label_medical_history = self.medical_record.findChild(QLabel,
                                                                                       "middle_name_display_label_medical_history")
        self.last_name_display_label_medical_history = self.medical_record.findChild(QLabel,
                                                                                     "last_name_display_label_medical_history")
        self.suffix_display_label_medical_history = self.medical_record.findChild(QLabel,
                                                                                  "suffix_display_label_medical_history")
        self.dob_display_label_medical_history = self.medical_record.findChild(QLabel,
                                                                               "dob_display_label_medical_history")
        self.age_display_label_medical_history = self.medical_record.findChild(QLabel,
                                                                               "age_display_label_medical_history")
        self.gender_display_label_medical_history = self.medical_record.findChild(QLabel,
                                                                                  "gender_display_label_medical_history")
        self.ethnicity_display_label_medical_history = self.medical_record.findChild(QLabel,
                                                                                     "ethnicity_display_label_medical_history")
        self.ssn_display_label_medical_history = self.medical_record.findChild(QLabel,
                                                                               "ssn_display_label_medical_history")

        # Patient information text fields (displayed on every tab) - Injury and Surgical History Tab
        self.patient_photo_entry_label_injury_surgery_hist = self.medical_record.findChild(QLabel,
                                                                                           "patient_photo_entry_label_injury_surgery_hist")
        self.mrn_display_label_injury_surgery_hist = self.medical_record.findChild(QLabel,
                                                                                   "mrn_display_label_injury_surgery_hist")
        self.first_name_display_label_injury_surgery_hist = self.medical_record.findChild(QLabel,
                                                                                          "first_name_display_label_injury_surgery_hist")
        self.middle_name_display_label_injury_surgery_hist = self.medical_record.findChild(QLabel,
                                                                                           "middle_name_display_label_injury_surgery_hist")
        self.last_name_display_label_injury_surgery_hist = self.medical_record.findChild(QLabel,
                                                                                         "last_name_display_label_injury_surgery_hist")
        self.suffix_display_label_injury_surgery_hist = self.medical_record.findChild(QLabel,
                                                                                      "suffix_display_label_injury_surgery_hist")
        self.dob_display_label_injury_surgery_hist = self.medical_record.findChild(QLabel,
                                                                                   "dob_display_label_injury_surgery_hist")
        self.age_display_label_injury_surgery_hist = self.medical_record.findChild(QLabel,
                                                                                   "age_display_label_injury_surgery_hist")
        self.gender_display_label_injury_surgery_hist = self.medical_record.findChild(QLabel,
                                                                                      "gender_display_label_injury_surgery_hist")
        self.ethnicity_display_label_injury_surgery_hist = self.medical_record.findChild(QLabel,
                                                                                         "ethnicity_display_label_injury_surgery_hist")
        self.ssn_display_label_injury_surgery_hist = self.medical_record.findChild(QLabel,
                                                                                   "ssn_display_label_injury_surgery_hist")

        # Patient information text fields (displayed on every tab) - Labs Tab
        self.patient_photo_entry_label_labs = self.medical_record.findChild(QLabel, "patient_photo_entry_label_labs")
        self.mrn_display_label_labs = self.medical_record.findChild(QLabel, "mrn_display_label_labs")
        self.first_name_display_label_labs = self.medical_record.findChild(QLabel, "first_name_display_label_labs")
        self.middle_name_display_label_labs = self.medical_record.findChild(QLabel, "middle_name_display_label_labs")
        self.last_name_display_label_labs = self.medical_record.findChild(QLabel, "last_name_display_label_labs")
        self.suffix_display_label_labs = self.medical_record.findChild(QLabel, "suffix_display_label_labs")
        self.dob_display_label_labs = self.medical_record.findChild(QLabel, "dob_display_label_labs")
        self.age_display_label_labs = self.medical_record.findChild(QLabel, "age_display_label_labs")
        self.gender_display_label_labs = self.medical_record.findChild(QLabel, "gender_display_label_labs")
        self.ethnicity_display_label_labs = self.medical_record.findChild(QLabel, "ethnicity_display_label_labs")
        self.ssn_display_label_labs = self.medical_record.findChild(QLabel, "ssn_display_label_labs")

        # Patient information text fields (displayed on every tab) - Care Plan Tab
        self.patient_photo_entry_label_care_plan = self.medical_record.findChild(QLabel,
                                                                                 "patient_photo_entry_label_care_plan")
        self.mrn_display_label_care_plan = self.medical_record.findChild(QLabel, "mrn_display_label_care_plan")
        self.first_name_display_label_care_plan = self.medical_record.findChild(QLabel,
                                                                                "first_name_display_label_care_plan")
        self.middle_name_display_label_care_plan = self.medical_record.findChild(QLabel,
                                                                                 "middle_name_display_label_care_plan")
        self.last_name_display_label_care_plan = self.medical_record.findChild(QLabel,
                                                                               "last_name_display_label_care_plan")
        self.suffix_display_label_care_plan = self.medical_record.findChild(QLabel, "suffix_display_label_care_plan")
        self.dob_display_label_care_plan = self.medical_record.findChild(QLabel, "dob_display_label_care_plan")
        self.age_display_label_care_plan = self.medical_record.findChild(QLabel, "age_display_label_care_plan")
        self.gender_display_label_care_plan = self.medical_record.findChild(QLabel, "gender_display_label_care_plan")
        self.ethnicity_display_label_care_plan = self.medical_record.findChild(QLabel,
                                                                               "ethnicity_display_label_care_plan")
        self.ssn_display_label_care_plan = self.medical_record.findChild(QLabel, "ssn_display_label_care_plan")

        # Patient information text fields (displayed on every tab) - Referrals Tab
        self.patient_photo_entry_label_referrals = self.medical_record.findChild(QLabel,
                                                                                 "patient_photo_entry_label_referrals")
        self.mrn_display_label_referrals = self.medical_record.findChild(QLabel, "mrn_display_label_referrals")
        self.first_name_display_label_referrals = self.medical_record.findChild(QLabel,
                                                                                "first_name_display_label_referrals")
        self.middle_name_display_label_referrals = self.medical_record.findChild(QLabel,
                                                                                 "middle_name_display_label_referrals")
        self.last_name_display_label_referrals = self.medical_record.findChild(QLabel,
                                                                               "last_name_display_label_referrals")
        self.suffix_display_label_referrals = self.medical_record.findChild(QLabel, "suffix_display_label_referrals")
        self.dob_display_label_referrals = self.medical_record.findChild(QLabel, "dob_display_label_referrals")
        self.age_display_label_referrals = self.medical_record.findChild(QLabel, "age_display_label_referrals")
        self.gender_display_label_referrals = self.medical_record.findChild(QLabel, "gender_display_label_referrals")
        self.ethnicity_display_label_referrals = self.medical_record.findChild(QLabel,
                                                                               "ethnicity_display_label_referrals")
        self.ssn_display_label_referrals = self.medical_record.findChild(QLabel, "ssn_display_label_referrals")

        # Patient information text fields (displayed on every tab) - Clinical Summary Tab
        self.patient_photo_entry_label_clinical_summary = self.medical_record.findChild(QLabel,
                                                                                        "patient_photo_entry_label_clinical_summary")
        self.mrn_display_label_clinical_summary = self.medical_record.findChild(QLabel,
                                                                                "mrn_display_label_clinical_summary")
        self.first_name_display_label_clinical_summary = self.medical_record.findChild(QLabel,
                                                                                       "first_name_display_label_clinical_summary")
        self.middle_name_display_label_clinical_summary = self.medical_record.findChild(QLabel,
                                                                                        "middle_name_display_label_clinical_summary")
        self.last_name_display_label_clinical_summary = self.medical_record.findChild(QLabel,
                                                                                      "last_name_display_label_clinical_summary")
        self.suffix_display_label_clinical_summary = self.medical_record.findChild(QLabel,
                                                                                   "suffix_display_label_clinical_summary")
        self.dob_display_label_clinical_summary = self.medical_record.findChild(QLabel,
                                                                                "dob_display_label_clinical_summary")
        self.age_display_label_clinical_summary = self.medical_record.findChild(QLabel,
                                                                                "age_display_label_clinical_summary")
        self.gender_display_label_clinical_summary = self.medical_record.findChild(QLabel,
                                                                                   "gender_display_label_clinical_summary")
        self.ethnicity_display_label_clinical_summary = self.medical_record.findChild(QLabel,
                                                                                      "ethnicity_display_label_clinical_summary")
        self.ssn_display_label_clinical_summary = self.medical_record.findChild(QLabel,
                                                                                "ssn_display_label_clinical_summary")

        # Patient information text fields (displayed on every tab) - Medical Record History Tab
        self.patient_photo_entry_label_medical_record_history = self.medical_record.findChild(QLabel,
                                                                                              "patient_photo_entry_label_medical_record_history")
        self.mrn_display_label_medical_record_history = self.medical_record.findChild(QLabel,
                                                                                      "mrn_display_label_medical_record_history")
        self.first_name_display_label_medical_record_history = self.medical_record.findChild(QLabel,
                                                                                             "first_name_display_label_medical_record_history")
        self.middle_name_display_label_medical_record_history = self.medical_record.findChild(QLabel,
                                                                                              "middle_name_display_label_medical_record_history")
        self.last_name_display_label_medical_record_history = self.medical_record.findChild(QLabel,
                                                                                            "last_name_display_label_medical_record_history")
        self.suffix_display_label_medical_record_history = self.medical_record.findChild(QLabel,
                                                                                         "suffix_display_label_medical_record_history")
        self.dob_display_label_medical_record_history = self.medical_record.findChild(QLabel,
                                                                                      "dob_display_label_medical_record_history")
        self.age_display_label_medical_record_history = self.medical_record.findChild(QLabel,
                                                                                      "age_display_label_medical_record_history")
        self.gender_display_label_medical_record_history = self.medical_record.findChild(QLabel,
                                                                                         "gender_display_label_medical_record_history")
        self.ethnicity_display_label_medical_record_history = self.medical_record.findChild(QLabel,
                                                                                            "ethnicity_display_label_medical_record_history")
        self.ssn_display_label_medical_record_history = self.medical_record.findChild(QLabel,
                                                                                      "ssn_display_label_medical_record_history")

        # -------------------------------------------------------------------------------------------------------------------

        # Initialize body of tab text fields - Demographics
        self.first_name_lineEdit = self.medical_record.findChild(QLineEdit, "first_name_lineEdit")
        self.middle_name_lineEdit = self.medical_record.findChild(QLineEdit, "middle_name_lineEdit")
        self.last_name_lineEdit = self.medical_record.findChild(QLineEdit, "last_name_lineEdit")
        self.jr_radioButton = self.medical_record.findChild(QRadioButton, "jr_radioButton")
        self.sr_radioButton = self.medical_record.findChild(QRadioButton, "sr_radioButton")
        self.I_radioButton = self.medical_record.findChild(QRadioButton, "I_radioButton")
        self.II_radioButton = self.medical_record.findChild(QRadioButton, "II_radioButton")
        self.III_radioButton = self.medical_record.findChild(QRadioButton, "III_radioButton")
        self.na_radioButton = self.medical_record.findChild(QRadioButton, "na_radioButton")
        self.dob_lineEdit = self.medical_record.findChild(QLineEdit, "dob_lineEdit")
        self.male_radioButton = self.medical_record.findChild(QRadioButton, "male_radioButton")
        self.female_radioButton = self.medical_record.findChild(QRadioButton, "female_radioButton")
        self.sex_other_radioButton = self.medical_record.findChild(QRadioButton, "sex_other_radioButton")
        self.ethnicity_comboBox = self.medical_record.findChild(QComboBox, "ethnicity_comboBox")
        self.ssn_lineEdit = self.medical_record.findChild(QLineEdit, "ssn_lineEdit")
        self.phone_number_lineEdit = self.medical_record.findChild(QLineEdit, "phone_number_lineEdit")
        self.email_address_lineEdit = self.medical_record.findChild(QLineEdit, "email_address_lineEdit")
        self.marital_status_comboBox = self.medical_record.findChild(QComboBox, "marital_status_comboBox")
        self.deceased_checkBox = self.medical_record.findChild(QCheckBox, "deceased_checkBox")
        self.date_of_death_lineEdit = self.medical_record.findChild(QLineEdit, "date_of_death_lineEdit")
        self.res_street_address_lineEdit = self.medical_record.findChild(QLineEdit, "res_street_address_lineEdit")
        self.res_apt_lineEdit = self.medical_record.findChild(QLineEdit, "res_apt_lineEdit")
        self.res_city_lineEdit = self.medical_record.findChild(QLineEdit, "res_city_lineEdit")
        self.res_state_comboBox = self.medical_record.findChild(QComboBox, "res_state_comboBox")
        self.res_zipcode_lineEdit = self.medical_record.findChild(QLineEdit, "res_zipcode_lineEdit")
        self.billing_street_address_lineEdit = self.medical_record.findChild(QLineEdit,
                                                                             "billing_street_address_lineEdit")
        self.billing_apt_lineEdit = self.medical_record.findChild(QLineEdit, "billing_apt_lineEdit")
        self.billing_city_lineEdit = self.medical_record.findChild(QLineEdit, "billing_city_lineEdit")
        self.billing_state_comboBox = self.medical_record.findChild(QComboBox, "billing_state_comboBox")
        self.billing_zipcode_lineEdit = self.medical_record.findChild(QLineEdit, "billing_zipcode_lineEdit")
        self.billing_same_as_res_address_checkBox = self.medical_record.findChild(QCheckBox,
                                                                                  "billing_same_as_res_address_checkBox")
        self.guarantor_first_name_lineEdit = self.medical_record.findChild(QLineEdit, "guarantor_first_name_lineEdit")
        self.middle_name_lineEdit_2 = self.medical_record.findChild(QLineEdit, "middle_name_lineEdit_2")
        self.guarantor_last_name_lineEdit = self.medical_record.findChild(QLineEdit, "guarantor_last_name_lineEdit")
        self.guarantor_male_radioButton = self.medical_record.findChild(QRadioButton, "guarantor_male_radioButton")
        self.guarantor_female_radioButton = self.medical_record.findChild(QRadioButton, "guarantor_female_radioButton")
        self.guarantor_sex_other_radioButton = self.medical_record.findChild(QRadioButton,
                                                                             "guarantor_sex_other_radioButton")
        self.guarantor_relationship_comboBox = self.medical_record.findChild(QComboBox,
                                                                             "guarantor_relationship_comboBox")
        self.phone_number_lineEdit_2 = self.medical_record.findChild(QLineEdit, "phone_number_lineEdit_2")
        self.guarantor_same_as_patient_address_checkBox = self.medical_record.findChild(QCheckBox,
                                                                                        "guarantor_same_as_patient_address_checkBox")
        self.guarantor_street_address_lineEdit = self.medical_record.findChild(QLineEdit,
                                                                               "guarantor_street_address_lineEdit")
        self.guarantor_apt_lineEdit = self.medical_record.findChild(QLineEdit, "guarantor_apt_lineEdit")
        self.guarantor_city_lineEdit = self.medical_record.findChild(QLineEdit, "guarantor_city_lineEdit")
        self.guarantor_state_comboBox = self.medical_record.findChild(QComboBox, "guarantor_state_comboBox")
        self.guarantor_zip_code_lineEdit = self.medical_record.findChild(QLineEdit, "guarantor_zip_code_lineEdit")
        self.sibling_at_practice_checkBox = self.medical_record.findChild(QCheckBox, "sibling_at_practice_checkBox")
        self.sibling_at_practice_checkBox.stateChanged.connect(self.on_sibling_at_practice_checkBox_state_changed)
        self.sibling_listView = self.medical_record.findChild(QListWidget, "sibling_listView")
        self.logged_in_user_display_label_demographics = self.medical_record.findChild(QLabel,
                                                                                       "logged_in_user_display_label_demographics")

        # Refresh Sibling List Button - Demographics Tab
        self.sibling_refresh_pushButton = self.medical_record.findChild(QPushButton, "sibling_refresh_pushButton")
        self.sibling_refresh_pushButton.clicked.connect(self.on_sibling_refresh_pushButton_clicked)

        # Save Changes Button - Demographics Tab
        self.save_changes_pushButton_demographics = self.medical_record.findChild(QPushButton,
                                                                                  "save_changes_pushButton_demographics")
        self.save_changes_pushButton_demographics.clicked.connect(self.on_save_changes_pushButton_demographics_clicked)

        # -------------------------------------------------------------------------------------------------------------------

        # Initialize body of tab text fields - Emergency Contacts
        self.emerg_1_first_name_lineEdit = self.medical_record.findChild(QLineEdit, "emerg_1_first_name_lineEdit")
        self.emerg_1_last_name_lineEdit = self.medical_record.findChild(QLineEdit, "emerg_1_last_name_lineEdit")
        self.emerg_1_phone_number_lineEdit = self.medical_record.findChild(QLineEdit, "emerg_1_phone_number_lineEdit")
        self.emerg_1_email_address_lineEdit = self.medical_record.findChild(QLineEdit, "emerg_1_email_address_lineEdit")
        self.emerg_1_relationship_comboBox = self.medical_record.findChild(QComboBox, "emerg_1_comboBox")
        self.emerg_1_comboBox = self.medical_record.findChild(QComboBox, "emerg_1_comboBox")
        self.emerg_2_first_name_lineEdit = self.medical_record.findChild(QLineEdit, "emerg_2_first_name_lineEdit")
        self.emerg_2_last_name_lineEdit = self.medical_record.findChild(QLineEdit, "emerg_2_last_name_lineEdit")
        self.emerg_2_phone_number_lineEdit = self.medical_record.findChild(QLineEdit, "emerg_2_phone_number_lineEdit")
        self.emerg_2_email_address_lineEdit = self.medical_record.findChild(QLineEdit, "emerg_2_email_address_lineEdit")
        self.emerg_2_relationship_comboBox = self.medical_record.findChild(QComboBox, "emerg_2_relationship_comboBox")
        # self.emerg_2_comboBox = self.medical_record.findChild(QComboBox, "emerg_2_relationship_comboBox")
        self.emerg_3_first_name_lineEdit = self.medical_record.findChild(QLineEdit, "emerg_3_first_name_lineEdit")
        self.emerg_3_last_name_lineEdit = self.medical_record.findChild(QLineEdit, "emerg_3_last_name_lineEdit")
        self.emerg_3_phone_number_lineEdit = self.medical_record.findChild(QLineEdit, "emerg_3_phone_number_lineEdit")
        self.emerg_3_email_address_lineEdit = self.medical_record.findChild(QLineEdit, "emerg_3_email_address_lineEdit")
        self.emerg_3_comboBox = self.medical_record.findChild(QComboBox, "emerg_3_relationship_comboBox")
        self.emerg_3_relationship_comboBox = self.medical_record.findChild(QComboBox, "emerg_3_relationship_comboBox")
        self.logged_in_user_display_label_emergency_contacts = self.medical_record.findChild(QLabel,
                                                                                             "logged_in_user_display_label_emergency_contacts")

        # Save Changes Button - Emergency Contacts Tab
        self.save_changes_pushButton_emergency_contacts = self.medical_record.findChild(QPushButton,
                                                                                        "save_changes_pushButton_emergency_contacts")
        self.save_changes_pushButton_emergency_contacts.clicked.connect(
            self.on_save_changes_pushButton_emergency_contacts_clicked)

        # -------------------------------------------------------------------------------------------------------------------
        # Initialize body of tab text fields - General
        self.add_weight_doubleSpinBox = self.medical_record.findChild(QDoubleSpinBox, "add_weight_doubleSpinBox")
        self.add_height_ft_spinBox = self.medical_record.findChild(QSpinBox, "add_height_ft_spinBox")
        self.add_height_inches_doubleSpinBox = self.medical_record.findChild(QDoubleSpinBox,
                                                                             "add_height_inches_doubleSpinBox")
        self.smoking_yes_radioButton = self.medical_record.findChild(QRadioButton, "smoking_yes_radioButton")
        self.smoking_no_radioButton = self.medical_record.findChild(QRadioButton, "smoking_no_radioButton")
        self.drinking_yes_radioButton = self.medical_record.findChild(QRadioButton, "drinking_yes_radioButton")
        self.drinking_no_radioButton = self.medical_record.findChild(QRadioButton, "drinking_no_radioButton")
        self.exercise_yes_radioButton = self.medical_record.findChild(QRadioButton, "exercise_yes_radioButton")
        self.exercise_no_radioButton = self.medical_record.findChild(QRadioButton, "exercise_no_radioButton")
        self.drugs_yes_radioButton = self.medical_record.findChild(QRadioButton, "drugs_yes_radioButton")
        self.drugs_no_radioButton = self.medical_record.findChild(QRadioButton, "drugs_no_radioButton")
        self.appointment_type_comboBox = self.medical_record.findChild(QComboBox, "appointment_type_comboBox")
        self.chief_complaint_textEdit = self.medical_record.findChild(QTextEdit, "chief_complaint_textEdit")
        self.logged_in_user_display_label_general = self.medical_record.findChild(QLabel,
                                                                                  "logged_in_user_display_label_general")

        # Save Changes Button - General Tab
        self.save_changes_pushButton_general = self.medical_record.findChild(QPushButton,
                                                                             "save_changes_pushButton_general")
        self.save_changes_pushButton_general.clicked.connect(self.on_save_changes_pushButton_general_clicked)

        # -------------------------------------------------------------------------------------------------------------------
        # Initialize body of tab text fields - Allergies
        self.add_allergy_lineEdit = self.medical_record.findChild(QLineEdit, "add_allergy_lineEdit")
        self.allergy_comboBox = self.medical_record.findChild(QComboBox, "allergy_comboBox")
        self.environmental_allergy_listView = self.medical_record.findChild(QListView, "environmental_allergy_listView")
        self.medication_allergy_listView = self.medical_record.findChild(QListView, "medication_allergy_listView")
        self.logged_in_user_display_label_allergies = self.medical_record.findChild(QLabel,
                                                                                    "logged_in_user_display_label_allergies")

        # Add Allergy Button - Allergies Tab
        self.add_allergy_pushButton = self.medical_record.findChild(QPushButton, "add_allergy_pushButton")
        self.add_allergy_pushButton.clicked.connect(self.on_add_allergy_pushButton_clicked)

        # Remove Environmental Allergy Button - Allergies Tab
        self.environmental_remove_pushButton = self.medical_record.findChild(QPushButton,
                                                                             "environmental_remove_pushButton")
        self.environmental_remove_pushButton.clicked.connect(self.on_environmental_remove_pushButton_clicked)

        # Remove Medication Allergy Button - Allergies Tab
        self.medication_remove_pushButton = self.medical_record.findChild(QPushButton, "medication_remove_pushButton")
        self.medication_remove_pushButton.clicked.connect(self.on_medication_remove_pushButton_clicked)

        # Save Changes Button - Allergies Tab
        self.save_changes_pushButton_allergies = self.medical_record.findChild(QPushButton,
                                                                               "save_changes_pushButton_allergies")
        self.save_changes_pushButton_allergies.clicked.connect(self.on_save_changes_pushButton_allergies_clicked)

        # -------------------------------------------------------------------------------------------------------------------
        # Initialize body of tab text fields - Medications
        self.add_medication_lineEdit = self.medical_record.findChild(QLineEdit, "add_medication_lineEdit")
        self.add_medication_dose_lineEdit = self.medical_record.findChild(QLineEdit, "add_medication_dose_lineEdit")
        self.add_medication_dose_type_comboBox = self.medical_record.findChild(QComboBox,
                                                                               "add_medication_dose_type_comboBox")
        self.add_medication_frequency_amount_doubleSpinBox = self.medical_record.findChild(QDoubleSpinBox,
                                                                                           "add_medication_frequency_amount_doubleSpinBox")
        self.add_medication_frequency_type_comboBox = self.medical_record.findChild(QComboBox,
                                                                                    "add_medication_frequency_type_comboBox")
        self.medication_type_comboBox = self.medical_record.findChild(QComboBox, "medication_type_comboBox")
        self.prescription_listView = self.medical_record.findChild(QListWidget, "prescription_listView")
        self.over_the_counter_listView = self.medical_record.findChild(QListWidget, "over_the_counter_listView")
        self.herbal_listView = self.medical_record.findChild(QListWidget, "herbal_listView")
        self.logged_in_user_display_label_medications = self.medical_record.findChild(QLabel,
                                                                                      "logged_in_user_display_label_medications")

        # Add Medication Button - Medications Tab
        self.add_medication_pushButton = self.medical_record.findChild(QPushButton, "add_medication_pushButton")
        self.add_medication_pushButton.clicked.connect(self.on_add_medication_pushButton_clicked)

        # Remove Prescription Medication Button - Medications Tab
        self.prescription_remove_pushButton = self.medical_record.findChild(QPushButton,
                                                                            "prescription_remove_pushButton")
        self.prescription_remove_pushButton.clicked.connect(self.on_prescription_remove_pushButton_clicked)

        # Remove Over the Counter Medication Button - Medications Tab
        self.over_the_counter_remove_pushButton = self.medical_record.findChild(QPushButton,
                                                                                "over_the_counter_remove_pushButton")
        self.over_the_counter_remove_pushButton.clicked.connect(self.on_over_the_counter_remove_pushButton_clicked)

        # Remove Herbal Medication Button - Medications Tab
        self.herbal_remove_pushButton = self.medical_record.findChild(QPushButton, "herbal_remove_pushButton")
        self.herbal_remove_pushButton.clicked.connect(self.on_herbal_remove_pushButton_clicked)

        # Save Changes Button - Medications Tab
        self.save_changes_pushButton_medications = self.medical_record.findChild(QPushButton,
                                                                                 "save_changes_pushButton_medications")
        self.save_changes_pushButton_medications.clicked.connect(self.on_save_changes_pushButton_medications_clicked)

        # -------------------------------------------------------------------------------------------------------------------
        # Initialize body of tab text fields - Exam Assessments
        self.appointment_dateTimeEdit = self.medical_record.findChild(QDateTimeEdit, "appointment_dateTimeEdit")
        self.office_location_comboBox = self.medical_record.findChild(QComboBox, "office_location_comboBox")
        self.primary_provider_comboBox = self.medical_record.findChild(QComboBox, "primary_provider_comboBox")
        self.appointment_provider_comboBox = self.medical_record.findChild(QComboBox, "appointment_provider_comboBox")
        self.appointment_nurse_comboBox = self.medical_record.findChild(QComboBox, "appointment_nurse_comboBox")
        self.appointment_cna_comboBox = self.medical_record.findChild(QComboBox, "appointment_cna_comboBox")
        self.exam_assessments_temperature_doubleSpinBox = self.medical_record.findChild(QDoubleSpinBox,
                                                                                        "exam_assessments_temperature_doubleSpinBox")
        self.blood_pressure_sbp_lineEdit_exam_assessment = self.medical_record.findChild(QLineEdit,
                                                                                         "blood_pressure_sbp_lineEdit_exam_assessment")
        self.blood_pressure_dbp_lineEdit_exam_assessment = self.medical_record.findChild(QLineEdit,
                                                                                         "blood_pressure_dbp_lineEdit_exam_assessment")
        self.pulse_rate_lineEdit_exam_assessment = self.medical_record.findChild(QLineEdit,
                                                                                 "pulse_rate_lineEdit_exam_assessment")
        self.respiration_rate_lineEdit_exam_assessment = self.medical_record.findChild(QLineEdit,
                                                                                       "respiration_rate_lineEdit_exam_assessment")
        self.blood_ox_levels_lineEdit_exam_assessment = self.medical_record.findChild(QLineEdit,
                                                                                      "blood_ox_levels_lineEdit_exam_assessment")
        self.physicaion_notes_textEdit_exam_assessment = self.medical_record.findChild(QTextEdit,
                                                                                       "physicaion_notes_textEdit_exam_assessment")
        self.procedures_performed_comboBox = self.medical_record.findChild(QComboBox, "procedures_performed_comboBox")
        self.procedure_other_lineEdit = self.medical_record.findChild(QLineEdit, "procedure_other_lineEdit")
        self.procedure_list_listView = self.medical_record.findChild(QListView, "procedure_list_listView")
        self.follow_up_needed_yes_radioButton = self.medical_record.findChild(QRadioButton,
                                                                              "follow_up_needed_yes_radioButton")
        self.follow_up_needed_no_radioButton = self.medical_record.findChild(QRadioButton,
                                                                             "follow_up_needed_no_radioButton")
        self.follow_up_in_frequency_spinBox = self.medical_record.findChild(QSpinBox, "follow_up_in_frequency_spinBox")
        self.follow_up_frequency_type_comboBox = self.medical_record.findChild(QComboBox,
                                                                               "follow_up_frequency_type_comboBox")
        self.logged_in_user_display_label_exam_assessments = self.medical_record.findChild(QLabel,
                                                                                           "logged_in_user_display_label_exam_assessments")

        # Add Procedure from ComboBox Button - Exam Assessments Tab
        self.add_procedure_from_comboBox_pushButton = self.medical_record.findChild(QPushButton,
                                                                                    "add_procedure_from_comboBox_pushButton")
        self.add_procedure_from_comboBox_pushButton.clicked.connect(self.on_add_procedure_from_comboBox_pushButton_clicked)

        # Add Procedure from LineEdit Button - Exam Assessments Tab
        self.add_procedure_other_pushButton = self.medical_record.findChild(QPushButton,
                                                                            "add_procedure_other_pushButton")
        self.add_procedure_other_pushButton.clicked.connect(self.on_add_procedure_other_pushButton_clicked)

        # Remove Procedure From List Button - Exam Assessments Tab
        self.remove_procedure_pushButton = self.medical_record.findChild(QPushButton, "remove_procedure_pushButton")
        self.remove_procedure_pushButton.clicked.connect(self.on_remove_procedure_pushButton_clicked)

        # Save Changes Button - Exam Assessments Tab
        self.save_changes_pushButton_exam_assessments = self.medical_record.findChild(QPushButton,
                                                                                      "save_changes_pushButton_exam_assessments")
        self.save_changes_pushButton_exam_assessments.clicked.connect(self.on_save_changes_pushbutton_exam_assessments_clicked)

        # -------------------------------------------------------------------------------------------------------------------

        # Initialize body of tab text fields - Medical History
        self.patient_history_comboBox = self.medical_record.findChild(QComboBox, "patient_history_comboBox")
        self.patient_history_other_lineEdit = self.medical_record.findChild(QLineEdit, "patient_history_other_lineEdit")
        self.patient_history_listView = self.medical_record.findChild(QListView, "patient_history_listView")
        self.patient_mothers_history_comboBox = self.medical_record.findChild(QComboBox,
                                                                              "patient_mothers_history_comboBox")
        self.patient_mothers_history_other_lineEdit = self.medical_record.findChild(QLineEdit,
                                                                                    "patient_mothers_history_other_lineEdit")
        self.patient_mothers_history_listView = self.medical_record.findChild(QListView,
                                                                              "patient_mothers_history_listView")
        self.patient_fathers_history_comboBox = self.medical_record.findChild(QComboBox,
                                                                              "patient_fathers_history_comboBox")
        self.patient_fathers_history_other_lineEdit = self.medical_record.findChild(QLineEdit,
                                                                                    "patient_fathers_history_other_lineEdit")
        self.patient_fathers_history_listView = self.medical_record.findChild(QListView,
                                                                              "patient_fathers_history_listView")
        self.logged_in_user_display_label_medical_history = self.medical_record.findChild(QLabel,
                                                                                          "logged_in_user_display_label_medical_history")

        # Add Patient History from ComboBox Button - Medical History Tab
        self.patient_history_from_comboBox_pushButton = self.medical_record.findChild(QPushButton,
                                                                                      "patient_history_from_comboBox_pushButton")
        self.patient_history_from_comboBox_pushButton.clicked.connect(self.on_patient_history_from_comboBox_pushButton_clicked)

        # Add Patient History from LineEdit Button - Medical History Tab
        self.patient_history_from_other_pushButton = self.medical_record.findChild(QPushButton,
                                                                                   "patient_history_from_other_pushButton")
        self.patient_history_from_other_pushButton.clicked.connect(self.on_patient_history_from_other_pushButton_clicked)

        # Add Remove Patient History Button - Medical History Tab
        self.remove_patient_history_pushButton = self.medical_record.findChild(QPushButton,
                                                                               "remove_patient_history_pushButton")
        self.remove_patient_history_pushButton.clicked.connect(self.on_remove_patient_history_pushButton_clicked)

        # Add Mother's History from ComboBox Button - Medical History Tab
        self.patient_mothers_history_from_comboBox_pushButton = self.medical_record.findChild(QPushButton,
                                                                                              "patient_mothers_history_from_comboBox_pushButton")
        self.patient_mothers_history_from_comboBox_pushButton.clicked.connect(self.on_patient_mothers_history_from_comboBox_pushButton_clicked)

        # Add Mother's History from LineEdit Button - Medical History Tab
        self.patient_mothers_history_from_other_pushButton = self.medical_record.findChild(QPushButton,
                                                                                           "patient_mothers_history_from_other_pushButton")
        self.patient_mothers_history_from_other_pushButton.clicked.connect(self.on_patient_mothers_history_from_other_pushButton_clicked)

        # Remove Mother's History Button - Medical History Tab
        self.remove_patient_mothers_history_pushButton = self.medical_record.findChild(QPushButton,
                                                                                       "remove_patient_mothers_history_pushButton")
        self.remove_patient_mothers_history_pushButton.clicked.connect(self.on_remove_patient_mothers_history_pushButton_clicked)

        # Add Father's History from ComboBox Button - Medical History Tab
        self.patient_fathers_history_from_comboBox_pushButton = self.medical_record.findChild(QPushButton,
                                                                                              "patient_fathers_history_from_comboBox_pushButton")
        self.patient_fathers_history_from_comboBox_pushButton.clicked.connect(self.on_patient_fathers_history_from_comboBox_pushButton_clicked)

        # Add Father's History from LineEdit Button - Medical History Tab
        self.patient_fathers_history_from_other_pushButton = self.medical_record.findChild(QPushButton,
                                                                                           "patient_fathers_history_from_other_pushButton")
        self.patient_fathers_history_from_other_pushButton.clicked.connect(self.on_patient_fathers_history_from_other_pushButton_clicked)

        # Remove Father's History Button - Medical History Tab
        self.remove_patient_fathers_history_pushButton = self.medical_record.findChild(QPushButton,
                                                                                       "remove_patient_fathers_history_pushButton")
        self.remove_patient_fathers_history_pushButton.clicked.connect(self.on_remove_patient_fathers_history_pushButton_clicked)

        # Save Changes Button - Medical History Tab
        self.save_changes_pushButton_medical_history = self.medical_record.findChild(QPushButton,
                                                                                     "save_changes_pushButton_medical_history")
        self.save_changes_pushButton_medical_history.clicked.connect(self.on_save_changes_pushbutton_medical_history_clicked)

        # -------------------------------------------------------------------------------------------------------------------

        # Initialize body of tab text fields - Injury and Surgical History
        self.add_injury_surgery_lineEdit = self.medical_record.findChild(QLineEdit, "add_injury_surgery_lineEdit")
        self.injury_surgery_date_occured_dateEdit = self.medical_record.findChild(QDateEdit,
                                                                                  "injury_surgery_date_occured_dateEdit")
        self.injury_surgery_comboBox = self.medical_record.findChild(QComboBox, "injury_surgery_comboBox")
        self.injury_history_listView = self.medical_record.findChild(QListWidget, "injury_history_listView")
        self.surgery_history_listView = self.medical_record.findChild(QListWidget, "surgery_history_listView")
        self.logged_in_user_display_label_injury_surgery_hist = self.medical_record.findChild(QLabel,
                                                                                              "logged_in_user_display_label_injury_surgery_hist")

        # Add Injury or Surgery History Button - Injury and Surgical History Tab
        self.add_injury_surgery_pushButton = self.medical_record.findChild(QPushButton, "add_injury_surgery_pushButton")
        self.add_injury_surgery_pushButton.clicked.connect(self.on_add_injury_surgery_pushButton_clicked)

        # Remove Injury History Button - Injury and Surgical History Tab
        self.injury_history_remove_pushButton = self.medical_record.findChild(QPushButton,
                                                                              "injury_history_remove_pushButton")
        self.injury_history_remove_pushButton.clicked.connect(self.on_injury_history_remove_pushButton_clicked)

        # Remove Surgery History Button - Injury and Surgical History Tab
        self.surgery_history_remove_pushButton = self.medical_record.findChild(QPushButton,
                                                                               "surgery_history_remove_pushButton")
        self.surgery_history_remove_pushButton.clicked.connect(self.on_surgery_history_remove_pushButton_clicked)

        # Save Changes Button - Injury and Surgical History Tab
        self.save_changes_pushButton_injury_surgery_hist = self.medical_record.findChild(QPushButton,
                                                                                         "save_changes_pushButton_injury_surgery_hist")
        self.save_changes_pushButton_injury_surgery_hist.clicked.connect(self.on_save_changes_pushbutton_injury_and_surgical_history_clicked)

        # -------------------------------------------------------------------------------------------------------------------

        # Initialize body of tab text fields - Labs
        self.labs_comboBox = self.medical_record.findChild(QComboBox, "labs_comboBox")
        self.pending_labs_listView = self.medical_record.findChild(QListView, "pending_labs_listView")
        self.completed_labs_listView = self.medical_record.findChild(QListWidget, "completed_labs_listView")
        self.lab_results_tableView = self.medical_record.findChild(QTableView, "lab_results_tableView")
        self.logged_in_user_display_label_labs = self.medical_record.findChild(QLabel,
                                                                               "logged_in_user_display_label_labs")

        # Request Lab Button - Labs Tab
        self.request_lab_pushButton = self.medical_record.findChild(QPushButton, "request_lab_pushButton")
        self.request_lab_pushButton.clicked.connect(self.on_request_lab_pushButton_clicked)

        # Remove Pending Labs Button - Labs Tab
        self.pending_labs_remove_pushButton = self.medical_record.findChild(QPushButton,
                                                                            "pending_labs_remove_pushButton")
        self.pending_labs_remove_pushButton.clicked.connect(self.on_pending_labs_remove_pushButton_clicked)

        # Show Completed Lab Selection Button - Labs Tab
        self.completed_labs_show_selection_pushButton = self.medical_record.findChild(QPushButton,
                                                                                      "completed_labs_show_selection_pushButton")
        self.completed_labs_show_selection_pushButton.clicked.connect(self.on_completed_labs_show_selection_pushButton_clicked)

        # Save Changes Button - Labs Tab
        self.save_changes_pushButton_labs = self.medical_record.findChild(QPushButton, "save_changes_pushButton_labs")
        self.save_changes_pushButton_labs.clicked.connect(self.on_save_changes_pushbutton_labs_clicked)

        # -------------------------------------------------------------------------------------------------------------------

        # Initialize body of tab text fields - Care Plan
        self.care_plan_assessment_textEdit = self.medical_record.findChild(QTextEdit, "care_plan_assessment_textEdit")
        self.care_plan_planning_textEdit = self.medical_record.findChild(QTextEdit, "care_plan_planning_textEdit")
        self.care_plan_diagnosis_textEdit = self.medical_record.findChild(QTextEdit, "care_plan_diagnosis_textEdit")
        self.care_plan_post_evaluation_textEdit = self.medical_record.findChild(QTextEdit,
                                                                                "care_plan_post_evaluation_textEdit")
        self.care_plan_frequency_amount_spinBox = self.medical_record.findChild(QSpinBox,
                                                                                "care_plan_frequency_amount_spinBox")
        self.care_plan_frequency_type_comboBox = self.medical_record.findChild(QComboBox,
                                                                               "care_plan_frequency_type_comboBox")
        self.care_plan_end_date_dateEdit = self.medical_record.findChild(QDateEdit, "care_plan_end_date_dateEdit")
        self.logged_in_user_display_label_care_plan = self.medical_record.findChild(QLabel,
                                                                                    "logged_in_user_display_label_care_plan")

        # Save Changes Button - Care Plan Tab
        self.save_changes_pushButton_care_plan = self.medical_record.findChild(QPushButton,
                                                                               "save_changes_pushButton_care_plan")
        self.save_changes_pushButton_care_plan.clicked.connect(self.on_save_changes_pushButton_care_plan_clicked)

        # -------------------------------------------------------------------------------------------------------------------

        # Initialize body of tab text fields - Referrals
        self.referral_number_display_label = self.medical_record.findChild(QLabel, "referral_number_display_label")
        self.referring_provider_comboBox = self.medical_record.findChild(QComboBox, "referring_provider_comboBox")
        self.referring_provider_comboBox.currentIndexChanged.connect(self.referring_provider_comboBox_on_idex_change)
        self.referring_provder_npi_display_label = self.medical_record.findChild(QLabel, "referring_provder_npi_display_label")
        self.referral_date_dateEdit = self.medical_record.findChild(QDateEdit, "referral_date_dateEdit")
        self.referral_expiration_date_dateEdit = self.medical_record.findChild(QDateEdit,
                                                                               "referral_expiration_date_dateEdit")
        self.referra_reason_comboBox = self.medical_record.findChild(QComboBox, "referra_reason_comboBox")
        self.patient_condition_textEdit = self.medical_record.findChild(QTextEdit, "patient_condition_textEdit")
        self.pending_referrals_listView = self.medical_record.findChild(QListWidget, "pending_referrals_listView")
        self.completed_referrals_listView = self.medical_record.findChild(QListWidget, "completed_referrals_listView")
        self.logged_in_user_display_label_referrals = self.medical_record.findChild(QLabel,
                                                                                    "logged_in_user_display_label_referrals")

        # Submit Referral Button - Referrals Tab
        self.submit_referral_pushButton = self.medical_record.findChild(QPushButton, "submit_referral_pushButton")
        self.submit_referral_pushButton.clicked.connect(self.on_submit_referral_pushButton_clicked)

        # Refresh Pending Referral List Button - Referrals Tab
        self.refresh_pending_referral_list_pushButton = self.medical_record.findChild(QPushButton,
                                                                                      "refresh_pending_referral_list_pushButton")
        self.refresh_pending_referral_list_pushButton.clicked.connect(self.on_refresh_pending_referral_list_pushButton_clicked)

        # Refresh Completed Referral List Button - Referrals Tab
        self.refresh_completed_referral_list_pushButton = self.medical_record.findChild(QPushButton,
                                                                                        "refresh_completed_referral_list_pushButton")
        self.refresh_completed_referral_list_pushButton.clicked.connect(self.on_refresh_completed_referral_list_pushButton_clicked)

        # Save Changes Button - Referrals Tab
        self.save_changes_pushButton_referrals = self.medical_record.findChild(QPushButton,
                                                                               "save_changes_pushButton_referrals")

        # -------------------------------------------------------------------------------------------------------------------

        # Initialize body of tab text fields - Clinical Summary
        self.clinical_summary_appt_date_and_time_dateTimeEdit = self.medical_record.findChild(QDateTimeEdit,
                                                                                              "clinical_summary_appt_date_and_time_dateTimeEdit")
        self.clinical_summary_chief_complaint_textEdit = self.medical_record.findChild(QTextEdit,
                                                                                       "clinical_summary_chief_complaint_textEdit")
        self.clinical_summary_diagnosis_textEdit = self.medical_record.findChild(QTextEdit,
                                                                                 "clinical_summary_diagnosis_textEdit")
        self.clinical_summary_physician_notes_textEdit = self.medical_record.findChild(QTextEdit,
                                                                                       "clinical_summary_physician_notes_textEdit")
        self.appointment_provider_display_label = self.medical_record.findChild(QLabel,
                                                                                "appointment_provider_display_label")
        self.appointment_nurse_display_label = self.medical_record.findChild(QLabel, "appointment_nurse_display_label")
        self.appointment_cna_display_label = self.medical_record.findChild(QLabel, "appointment_cna_display_label")
        self.clinical_summary_temperature_doubleSpinBox = self.medical_record.findChild(QDoubleSpinBox,
                                                                                        "clinical_summary_temperature_doubleSpinBox")
        self.blood_pressure_sbp_lineEdit = self.medical_record.findChild(QLineEdit, "blood_pressure_sbp_lineEdit")
        self.blood_pressure_dbp_lineEdit = self.medical_record.findChild(QLineEdit, "blood_pressure_dbp_lineEdit")
        self.pulse_rate_lineEdit = self.medical_record.findChild(QLineEdit, "pulse_rate_lineEdit")
        self.respiration_rate_lineEdit = self.medical_record.findChild(QLineEdit, "respiration_rate_lineEdit")
        self.blood_ox_levels_lineEdit = self.medical_record.findChild(QLineEdit, "blood_ox_levels_lineEdit")
        self.logged_in_user_display_label_clinical_summary = self.medical_record.findChild(QLabel,
                                                                                           "logged_in_user_display_label_clinical_summary")

        # Save Changes Button - Clinical Summary Tab
        self.save_changes_pushButton_clinical_summary = self.medical_record.findChild(QPushButton,
                                                                                      "save_changes_pushButton_clinical_summary")
        self.save_changes_pushButton_clinical_summary.clicked.connect(self.on_save_changes_pushButton_clinical_summary_clicked)

        # -------------------------------------------------------------------------------------------------------------------

        # Initialize body of tab text fields - Medical Record History
        self.medical_record_history_listView = self.medical_record.findChild(QListWidget,
                                                                             "medical_record_history_listView")
        self.logged_in_user_display_label_clinical_summary = self.medical_record.findChild(QLabel,
                                                                                           "logged_in_user_display_label_clinical_summary")

        # Save Changes Button - Clinical Summary Tab
        self.save_changes_pushButton_medical_record_history = self.medical_record.findChild(QPushButton,
                                                                                            "save_changes_pushButton_medical_record_history")

    # -------------------------------------------------------------------------------------------------------------------

    def on_actionlogout_clicked(self):
        self.login = self.login()
        self.login.initialize_login()
        self.medical_record.close()

    def on_actionpatientSearch_clicked(self):
        self.patient_lookup = self.patient_lookup(self.current_user, self.selected_location)
        self.patient_lookup.initialize_patient_lookup()
        self.medical_record.close()

    def on_actionnewPatient_clicked(self):
        self.new_patient = self.new_patient(self.current_user, self.selected_location)
        self.new_patient.initialize_new_patient_window()
        self.medical_record.close()

    def on_actionhome_clicked(self):
        self.homepage = self.homepage(self.current_user, self.selected_location)
        self.homepage.initialize_homepage()
        self.medical_record.close()

    def initialize_medical_record_window(self):
        self.medical_record.show()

    # Button On-Click
    def on_sibling_refresh_pushButton_clicked(self):
        if self.sibling_at_practice_checkBox.isChecked():
            self.sibling_listView.clear()
            mrn = str(self.mrn_display_label_demographics.text())
            sibling_info = db_access.get_siblings(mrn)
            for sibling in sibling_info:
                self.sibling_listView.addItem(f"{sibling.get_first_name()} {sibling.get_last_name()}, "
                                              f"{sibling.get_medical_record_num()}")
        else:
            pass

    def on_sibling_at_practice_checkBox_state_changed(self):
        if self.sibling_at_practice_checkBox.isChecked():
            mrn = str(self.mrn_display_label_demographics.text())
            sibling_info = db_access.get_siblings(mrn)
            for sibling in sibling_info:
                self.sibling_listView.addItem(f"{sibling.get_first_name()} {sibling.get_last_name()}, "
                                              f"{sibling.get_medical_record_num()}")
        else:
            self.sibling_listView.clear()
            print("sibling list cleared")


    def on_save_changes_pushButton_demographics_clicked(self):

        # Save Patient Info
        first_name = self.first_name_lineEdit.text()
        middle_name = self.middle_name_lineEdit.text()
        last_name = self.last_name_lineEdit.text()
        dob = self.dob_lineEdit.text()
        ssn = self.ssn_lineEdit.text()
        phone_number = self.phone_number_lineEdit.text()
        email_address = self.email_address_lineEdit.text()
        date_of_death = self.date_of_death_lineEdit.text()
        res_street_address = self.res_street_address_lineEdit.text()
        res_apt = self.res_apt_lineEdit.text()
        res_city = self.res_city_lineEdit.text()

        selectedIndex = self.res_state_comboBox.currentIndex()
        state_option = state_options.get(selectedIndex)

        res_zipcode = self.res_zipcode_lineEdit.text()
        medical_record_num = self.mrn_display_label_demographics.text()
        age = self.age_display_label_demographics.text()
        sex = self.gender_display_label_demographics.text()

        suffix = ""
        if self.jr_radioButton.isChecked():
            suffix = "Jr."
        elif self.sr_radioButton.isChecked():
            suffix = "Sr."
        elif self.I_radioButton.isChecked():
            suffix = "I"
        elif self.II_radioButton.isChecked():
            suffix = "II"
        elif self.III_radioButton.isChecked():
            suffix = "III"
        elif self.na_radioButton.isChecked():
            suffix = "na"
        else:
            print("Error, choose a suffix field")

        sex = ""
        if self.male_radioButton.isChecked():
            sex = "Male"
        elif self.female_radioButton.isChecked():
            sex = "Female"
        elif self.sex_other_radioButton.isChecked:
            sex = "Other"

        if self.billing_same_as_res_address_checkBox.isChecked():
            billing_street_address = res_street_address
            billing_apt_address = res_apt
            billing_city = res_city
            billing_state = state_option
            billing_zipcode = res_zipcode
        else:
            billing_street_address = self.billing_street_address_lineEdit.text()
            billing_apt_address = self.billing_apt_lineEdit.text()
            billing_city = self.billing_city_lineEdit.text()
            selectedIndex = self.billing_state_comboBox.currentIndex()
            billing_state = state_options.get(selectedIndex)
            billing_zipcode = self.billing_zipcode_lineEdit.text()

        marital_status = ""
        if self.marital_status_comboBox.currentIndex() == 0:
            marital_status = "Single"
        elif self.marital_status_comboBox.currentIndex() == 1:
            marital_status = "Divorced"
        elif self.marital_status_comboBox.currentIndex() == 2:
            marital_status = "Married"
        elif self.marital_status_comboBox.currentIndex() == 3:
            marital_status = "Widowed"
        else:
            print("Error, please make a selection.")

        ethnicity = ""
        if self.ethnicity_comboBox.currentIndex() == 0:
            ethnicity = "Alaska Native"
        elif self.ethnicity_comboBox.currentIndex() == 1:
            ethnicity = "American Indian"
        elif self.ethnicity_comboBox.currentIndex() == 2:
            ethnicity = "Asian"
        elif self.ethnicity_comboBox.currentIndex() == 3:
            ethnicity = "Black or African American"
        elif self.ethnicity_comboBox.currentIndex() == 4:
            ethnicity = "Native Hawaiian"
        elif self.ethnicity_comboBox.currentIndex() == 5:
            ethnicity = "Other Pacific Islander"
        elif self.ethnicity_comboBox.currentIndex() == 6:
            ethnicity = "White"
        elif self.ethnicity_comboBox.currentIndex() == 7:
            ethnicity = "Other"
        else:
            print("Error, please make a selection.")

        deceased = False
        if self.deceased_checkBox.isChecked():
            deceased = True

        sibling_at_practice = False
        if self.sibling_at_practice_checkBox.isChecked():
            sibling_at_practice = True

        current_patient = Demographics.Demographics(medical_record_num, first_name, last_name, sex, dob, ssn,
                                                    phone_number, ethnicity, marital_status, age, middle_name, suffix,
                                                    email_address, deceased, date_of_death)
        current_patient_address = Address.Address(res_street_address, res_city, state_option, res_zipcode, res_apt)
        # -------
        current_billing_address = Address.Address(billing_street_address, billing_city, billing_state, billing_zipcode,
                                                  billing_apt_address)

        # --------
        '''
        db_access.update_patient(current_patient.get_medical_record_num(), current_patient.get_first_name(),
                                 current_patient.get_last_name(), current_patient.get_gender(),
                                 current_patient.get_date_of_birth(), current_patient.get_social_security_num(),
                                 current_patient.get_middle_name(), current_patient.get_suffix())
        '''
        conn = db_access.connect()
        query = f"UPDATE MRPatient " \
                f"SET FirstName = '{current_patient.get_first_name()}', LastName = '{current_patient.get_last_name()}', " \
                f"Gender = '{current_patient.get_gender()}', DateOfBirth = '{current_patient.get_date_of_birth()}', SSN = '{current_patient.get_social_security_num()}', MiddleName = '{current_patient.get_middle_name()}', Suffix = '{current_patient.get_suffix()}' " \
                f"WHERE MRN = {current_patient.get_medical_record_num()}"

        with db_access.closing(conn.cursor()) as c:
            c.execute(query)
            conn.commit()

        # Save the additional columns
        conn = db_access.connect()
        query = f"UPDATE MRPatient " \
                f"SET PhoneNum = '{current_patient.get_phone_num()}', Ethnicity = '{current_patient.get_ethnicity()}', MaritalStatus = '{current_patient.get_marital_status()}', " \
                f"    Age = '{current_patient.get_age()}', Email = '{current_patient.get_email()}', Deceased = '{current_patient.get_deceased()}', DateOfDeath = '{current_patient.get_date_of_death()}' " \
                f"WHERE MRN = {current_patient.get_medical_record_num()}"

        with db_access.closing(conn.cursor()) as c:
            c.execute(query)
            conn.commit()

        print("Basic info saved to DB - Demographics")
        '''
        db_access.update_address(current_patient.get_medical_record_num(), current_patient_address.get_street_address(),
                                 current_patient_address.get_city(), current_patient_address.get_state(),
                                 current_patient_address.get_zip_code(), current_patient_address.get_apt_num())
        '''
        conn = db_access.connect()
        query = f"UPDATE MRAddress " \
                f"SET StreetAddress = '{current_patient_address.get_street_address()}', City = '{current_patient_address.get_city()}', State = '{current_patient_address.get_state()}', " \
                f"    ZipCode = '{current_patient_address.get_zip_code()}', AptNum = '{current_patient_address.get_apt_num()}' " \
                f"WHERE MRN = {current_patient.get_medical_record_num()}"

        with db_access.closing(conn.cursor()) as c:
            c.execute(query)
            conn.commit()

        print("Resident Address info saved to DB- Demographics")
        # --------------------------------------------------------------------------------------------------------------

        # Save Guarantor Info
        guarantor_first_name = self.guarantor_first_name_lineEdit.text()
        guarantor_middle_name = self.middle_name_lineEdit_2.text()
        guarantor_last_name = self.guarantor_last_name_lineEdit.text()
        guarantor_phone_number = self.phone_number_lineEdit_2.text()

        guarantor_sex = ""
        if self.guarantor_male_radioButton.isChecked():
            guarantor_sex = "Male"
        elif self.guarantor_female_radioButton.isChecked():
            guarantor_sex = "Female"
        elif self.guarantor_sex_other_radioButton.isChecked:
            guarantor_sex = "Other"

        guarantor_relationship = ""
        if self.guarantor_relationship_comboBox.currentIndex() == 0:
            pass
        elif self.guarantor_relationship_comboBox.currentIndex() == 1:
            pass
        elif self.guarantor_relationship_comboBox.currentIndex() == 2:
            pass
        elif self.guarantor_relationship_comboBox.currentIndex() == 3:
            pass
        elif self.guarantor_relationship_comboBox.currentIndex() == 4:
            pass
        elif self.guarantor_relationship_comboBox.currentIndex() == 5:
            pass
        else:
            print("Error, please make a selection.")

        if self.guarantor_same_as_patient_address_checkBox.isChecked():
            guarantor_street_address = res_street_address
            guarantor_apt = res_apt
            guarantor_city = res_city
            guarantor_state = state_option
            guarantor_zipcode = res_zipcode
        else:
            guarantor_street_address = self.guarantor_street_address_lineEdit.text()
            guarantor_apt = self.guarantor_apt_lineEdit.text()
            guarantor_city = self.guarantor_city_lineEdit.text()
            selectedIndex = self.guarantor_state_comboBox.currentIndex()
            guarantor_state = state_options.get(selectedIndex)
            guarantor_zipcode = self.guarantor_zip_code_lineEdit.text()

        current_guarantor = Guarantor.Guarantor(guarantor_first_name, guarantor_middle_name, guarantor_last_name,
                                                guarantor_sex,
                                                guarantor_relationship, guarantor_phone_number)
        current_guarantor_address = Address.Address(guarantor_street_address, guarantor_city, guarantor_state,
                                                    guarantor_zipcode, guarantor_apt)


        if current_guarantor.get_first_name() != "" and current_guarantor.get_last_name() != "":
            # Get GuarantorID
            guarantor_id = 1

            conn = db_access.connect()
            query = f"SELECT MAX(GuarantorID) FROM MRGuarantor"

            with db_access.closing(conn.cursor()) as c:
                c.execute(query)
                highest_guarantor_id = c.fetchone()[0]
                conn.commit()

            print("Highest GuarantorID: ", highest_guarantor_id)
            guarantor_id = highest_guarantor_id + 1

            # Get AddressID
            address_id = 1

            conn = db_access.connect()
            query = f"SELECT MAX(AddressID) FROM MRAddress"

            with db_access.closing(conn.cursor()) as c:
                c.execute(query)
                highest_address_id = c.fetchone()[0]
                conn.commit()

            print("Highest AddressID: ", highest_guarantor_id)
            guarantor_id = highest_guarantor_id + 1

            # Check to see if there is a record with the mrn already in the MRGuarantor Table
            conn = db_access.connect()
            query = f"SELECT COUNT(*) FROM MRGuarantor WHERE MRN = {current_patient.get_medical_record_num()}"

            with db_access.closing(conn.cursor()) as c:
                c.execute(query)
                result = c.fetchone()[0]
                conn.commit()

            if result == 1:
                print(f"The MRN is in the MRGuarantor Table {result} times.")
                print("The Guarantor is already in the database for a patient")

                # Update Guarantor
                conn = db_access.connect()
                query = f"UPDATE MRGuarantor " \
                        f"SET FirstName = '{current_guarantor.get_first_name()}', LastName = '{current_guarantor.get_last_name()}', " \
                        f"Gender = '{current_guarantor.get_gender()}', " \
                        f"    Relationship = '{current_guarantor.get_relationship()}', PhoneNum = '{current_guarantor.get_phone_num()}'" \
                        f"WHERE MRN = {current_patient.get_medical_record_num()}"

                with db_access.closing(conn.cursor()) as c:
                    c.execute(query)
                    conn.commit()

                # The below part doesn't work because you can't add and address to the MRAddress table without a MRN
                # and you can't use the current patient's mrn a 2nd time
                '''
                # Update Guarantor Address
                db_access.update_address(current_patient.get_medical_record_num(), current_guarantor_address.get_street_address(),
                                         current_guarantor_address.get_city(), current_guarantor_address.get_state(), current_guarantor_address.get_zip_code(),
                                         current_guarantor_address.get_apt_num(), )'''

            else:

                # Create Guarantor
                conn = db_access.connect()
                query = f"INSERT INTO MRGuarantor (MRN, FirstName, LastName, Gender, Relationship, PhoneNum, GuarantorID)" \
                        f"VALUES ({current_patient.get_medical_record_num()}, '{current_guarantor.get_first_name()}', '{current_guarantor.get_last_name()}', " \
                        f"'{current_guarantor.get_gender()}', '{current_guarantor.get_relationship()}', '{current_guarantor.get_phone_num()}', '{guarantor_id}')"

                with db_access.closing(conn.cursor()) as c:
                    c.execute(query)
                    conn.commit()

                # The below part doesn't work because you can't add and address to the MRAddress table without a MRN
                # and you can't use the current patient's mrn a 2nd time
                '''
                # Create Guarantor Address
                conn = db_access.connect()
                query2 = f"INSERT INTO MRAddress (MRN, StreetAddress, City, State, ZipCode, AptNum, AddressID)" \
                         f"VALUES ('{current_patient.get_medical_record_num()}', '{current_guarantor_address.get_street_address()}', '{current_guarantor_address.get_city()}', '{current_guarantor_address.get_state()}', '{current_guarantor_address.get_zip_code()}', '{current_guarantor_address.get_apt_num()}'," \
                         f"'{address_id}')"

                with db_access.closing(conn.cursor()) as c:
                    c.execute(query2)
                    conn.commit()'''

            print("Guarantor info saved to DB- Demographics")
        else:
            print("Guarantor first and last name left empty. Skipping Guarantor info")

        msg_box = QMessageBox()
        msg_box.setWindowTitle("Save Successful")
        msg_box.setText("Changes have been saved.")
        msg_box.exec_()

    def on_save_changes_pushButton_emergency_contacts_clicked(self):

        emerg_1_first_name = self.emerg_1_first_name_lineEdit.text()
        emerg_1_last_name = self.emerg_1_last_name_lineEdit.text()
        emerg_1_phone_number = self.emerg_1_phone_number_lineEdit.text()
        emerg_1_email_address = self.emerg_1_email_address_lineEdit.text()

        emerg_1_relationship = ""
        if self.emerg_1_comboBox.currentIndex() == 0:
            emerg_1_relationship = "None"
            e1_sex = "Other"
        elif self.emerg_1_comboBox.currentIndex() == 1:
            emerg_1_relationship = "Mother"
            e1_sex = "Female"
        elif self.emerg_1_comboBox.currentIndex() == 2:
            emerg_1_relationship = "Father"
            e1_sex = "Male"
        elif self.emerg_1_comboBox.currentIndex() == 3:
            emerg_1_relationship = "Grandmother"
            e1_sex = "Female"
        elif self.emerg_1_comboBox.currentIndex() == 4:
            emerg_1_relationship = "Grandfather"
            e1_sex = "Male"
        elif self.emerg_1_comboBox.currentIndex() == 5:
            emerg_1_relationship = "Other"
            e1_sex = "Other"
        else:
            print("Error, please fill in the required fields")

        emerg_contact_1 = EmergencyContact.EmergencyContact(emerg_1_first_name, emerg_1_last_name, e1_sex,
                                                            emerg_1_relationship, emerg_1_phone_number,
                                                            emerg_1_email_address)

        emerg_2_first_name = self.emerg_2_first_name_lineEdit.text()
        emerg_2_last_name = self.emerg_2_last_name_lineEdit.text()
        emerg_2_phone_number = self.emerg_2_phone_number_lineEdit.text()
        emerg_2_email_address = self.emerg_2_email_address_lineEdit.text()

        emerg_2_relationship = ""
        if self.emerg_2_relationship_comboBox.currentIndex() == 0:
            emerg_2_relationship = "None"
            e2_sex = "Other"
        elif self.emerg_2_relationship_comboBox.currentIndex() == 1:
            emerg_2_relationship = "Mother"
            e2_sex = "Female"
        elif self.emerg_2_relationship_comboBox.currentIndex() == 2:
            emerg_2_relationship = "Father"
            e2_sex = "Male"
        elif self.emerg_2_relationship_comboBox.currentIndex() == 3:
            emerg_2_relationship = "Grandmother"
            e2_sex = "Female"
        elif self.emerg_2_relationship_comboBox.currentIndex() == 4:
            emerg_2_relationship = "Grandfather"
            e2_sex = "Male"
        elif self.emerg_2_relationship_comboBox.currentIndex() == 5:
            emerg_2_relationship = "Other"
            e2_sex = "Other"
        else:
            print("Error, please fill in the required fields")


        emerg_contact_2 = EmergencyContact.EmergencyContact(emerg_2_first_name, emerg_2_last_name, e2_sex,
                                                            emerg_2_relationship, emerg_2_phone_number,
                                                            emerg_2_email_address)

        emerg_3_first_name = self.emerg_3_first_name_lineEdit.text()
        emerg_3_last_name = self.emerg_3_last_name_lineEdit.text()
        emerg_3_phone_number = self.emerg_3_phone_number_lineEdit.text()
        emerg_3_email_address = self.emerg_3_email_address_lineEdit.text()

        emerg_3_relationship = ""
        if self.emerg_3_comboBox.currentIndex() == 0:
            emerg_3_relationship = "None"
            e3_sex = "Other"
        elif self.emerg_3_comboBox.currentIndex() == 1:
            emerg_3_relationship = "Mother"
            e3_sex = "Female"
        elif self.emerg_3_comboBox.currentIndex() == 2:
            emerg_3_relationship = "Father"
            e3_sex = "Male"
        elif self.emerg_3_comboBox.currentIndex() == 3:
            emerg_3_relationship = "Grandmother"
            e3_sex = "Female"
        elif self.emerg_3_comboBox.currentIndex() == 4:
            emerg_3_relationship = "Grandfather"
            e3_sex = "Male"
        elif self.emerg_3_comboBox.currentIndex() == 5:
            emerg_3_relationship = "Other"
            e3_sex = "Other"
        else:
            print("Error, please fill in the required fields")

        emerg_contact_3 = EmergencyContact.EmergencyContact(emerg_3_first_name, emerg_3_last_name, e3_sex,
                                                            emerg_3_relationship, emerg_3_phone_number,
                                                            emerg_3_email_address)

        #----------------------
        medical_record_num = self.mrn_display_label_emergency_contacts.text()

        # Check to see if there is a record with the mrn already in the MREmergencyContacts Table
        conn = db_access.connect()
        query = f"SELECT COUNT(*) FROM MREmergencyContacts WHERE MRN = {medical_record_num}"

        with db_access.closing(conn.cursor()) as c:
            c.execute(query)
            result = c.fetchone()[0]
            conn.commit()

        if result == 0:
            print("Creating EContacts")

            conn = db_access.connect()
            query = f"SELECT MAX(EmergencyContactID) FROM MREmergencyContacts"

            with db_access.closing(conn.cursor()) as c:
                c.execute(query)
                highest_emerg_id = c.fetchone()[0]
                conn.commit()

            print("Highest EmergencyContactID: ", highest_emerg_id)
            emerg_id = highest_emerg_id + 1


            # Create EMContact1
            conn = db_access.connect()
            query = f"INSERT INTO MREmergencyContacts (MRN, FirstName, LastName, Gender, Relationship, PhoneNum, Email, EmergencyContactID)" \
                    f"VALUES ({medical_record_num}, '{emerg_1_first_name}', '{emerg_1_last_name}', '{e1_sex}', '{emerg_1_relationship}', " \
                    f"'{emerg_1_phone_number}', '{emerg_1_email_address}', '{emerg_id}')"

            with db_access.closing(conn.cursor()) as c:
                c.execute(query)
                conn.commit()
            emerg_id += 1

            # Create EMContact2
            conn = db_access.connect()
            query = f"INSERT INTO MREmergencyContacts (MRN, FirstName, LastName, Gender, Relationship, PhoneNum, Email, EmergencyContactID)" \
                    f"VALUES ({medical_record_num}, '{emerg_2_first_name}', '{emerg_2_last_name}', '{e2_sex}', '{emerg_2_relationship}', " \
                    f"'{emerg_2_phone_number}', '{emerg_2_email_address}', '{emerg_id}')"

            with db_access.closing(conn.cursor()) as c:
                c.execute(query)
                conn.commit()
            emerg_id += 1

            # Create EMContact3
            conn = db_access.connect()
            query = f"INSERT INTO MREmergencyContacts (MRN, FirstName, LastName, Gender, Relationship, PhoneNum, Email, EmergencyContactID)" \
                    f"VALUES ({medical_record_num}, '{emerg_3_first_name}', '{emerg_3_last_name}', '{e3_sex}', '{emerg_3_relationship}', " \
                    f"'{emerg_3_phone_number}', '{emerg_3_email_address}', '{emerg_id}')"

            with db_access.closing(conn.cursor()) as c:
                c.execute(query)
                conn.commit()

        else:
            # Update EContacts
            selected_econtact_id = 0

            # find the records in the table that have the matching mrn
            conn = db_access.connect()
            query = f"SELECT MIN(EmergencyContactID) FROM MREmergencyContacts WHERE MRN = {medical_record_num}"
            with db_access.closing(conn.cursor()) as c:
                c.execute(query, )
                selected_econtact_id = c.fetchone()
                conn.commit()

            print(int(selected_econtact_id[0]))
            selected_econtact_id = int(selected_econtact_id[0])

            # e1
            conn = db_access.connect()
            query = f"UPDATE MREmergencyContacts " \
                    f"SET Firstname = '{emerg_1_first_name}', LastName = '{emerg_1_last_name}', Gender = '{e1_sex}', " \
                    f"    Relationship = '{emerg_1_relationship}', PhoneNum = '{emerg_1_phone_number}', Email = '{emerg_1_email_address}' " \
                    f"WHERE EmergencyContactID = {selected_econtact_id}"

            with db_access.closing(conn.cursor()) as c:
                c.execute(query)
                conn.commit()
            selected_econtact_id += 1

            # e2
            conn = db_access.connect()
            query = f"UPDATE MREmergencyContacts " \
                    f"SET Firstname = '{emerg_2_first_name}', LastName = '{emerg_2_last_name}', Gender = '{e2_sex}', " \
                    f"    Relationship = '{emerg_2_relationship}', PhoneNum = '{emerg_2_phone_number}', Email = '{emerg_2_email_address}' " \
                    f"WHERE EmergencyContactID = {selected_econtact_id}"

            with db_access.closing(conn.cursor()) as c:
                c.execute(query)
                conn.commit()
            selected_econtact_id += 1

            # e3
            conn = db_access.connect()
            query = f"UPDATE MREmergencyContacts " \
                    f"SET Firstname = '{emerg_3_first_name}', LastName = '{emerg_3_last_name}', Gender = '{e3_sex}', " \
                    f"    Relationship = '{emerg_3_relationship}', PhoneNum = '{emerg_3_phone_number}', Email = '{emerg_3_email_address}' " \
                    f"WHERE EmergencyContactID = {selected_econtact_id}"

            with db_access.closing(conn.cursor()) as c:
                c.execute(query)
                conn.commit()

            print("ALL Emergency Contacts Updated")



        msg_box = QMessageBox()
        msg_box.setWindowTitle("Save Successful")
        msg_box.setText("Changes have been saved.")
        msg_box.exec_()

        #----------------------

    def on_save_changes_pushButton_general_clicked(self):
        add_weight = self.add_weight_doubleSpinBox.value()
        add_height_ft = self.add_height_ft_spinBox.value()
        add_height_inches = self.add_height_inches_doubleSpinBox.value()
        chief_complaint = self.chief_complaint_textEdit.toPlainText()

        smoking = False
        if self.smoking_yes_radioButton.isChecked():
            smoking = True

        drinking = False
        if self.drinking_yes_radioButton.isChecked():
            drinking = True

        exercise = False
        if self.exercise_yes_radioButton.isChecked():
            exercise = True

        drugs = False
        if self.drugs_yes_radioButton.isChecked():
            drugs = True

        appointment_type = ""
        if self.appointment_type_comboBox.currentIndex() == 0:
            appointment_type = "Wellness Check Up"
        elif self.appointment_type_comboBox.currentIndex() == 1:
            appointment_type = "Follow Up"
        elif self.appointment_type_comboBox.currentIndex() == 2:
            appointment_type = "Sick Visit"
        elif self.appointment_type_comboBox.currentIndex() == 3:
            appointment_type = "Injury"
        else:
            print("Error, please make a selection.")

        current_general = General.General(add_weight, add_height_ft, add_height_inches, smoking, drinking, exercise,
                                          drugs, appointment_type, chief_complaint)

        print(f"{current_general.get_weight()}, {current_general.get_height_ft()}, {current_general.get_height_in()}, {current_general.get_smoking()}, {current_general.get_drinking()}, {current_general.get_exercise()}, {current_general.get_drugs()}, {current_general.get_appointment_type()}, {current_general.get_chief_complaint()}")

        #----------------------------------------------------------------------------------
        medical_record_num = self.mrn_display_label_general.text()

        # Get available GeneralID
        conn = db_access.connect()
        query = f"SELECT MAX(GeneralID) FROM MRGeneral"

        with db_access.closing(conn.cursor()) as c:
            c.execute(query)
            highest_general_id = c.fetchone()[0]
            conn.commit()

        general_id = highest_general_id + 1


        # Check to see if there is a record with the mrn already in the MRGeneral Table
        conn = db_access.connect()
        query = f"SELECT COUNT(*) FROM MRGeneral WHERE MRN = {medical_record_num}"

        with db_access.closing(conn.cursor()) as c:
            c.execute(query)
            result = c.fetchone()[0]
            conn.commit()

        if result == 0:

            # Create new general
            conn = db_access.connect()
            query = f"INSERT INTO MRGeneral (MRN, Weight, HeightFt, HeightIn, Smoking, Drinking, Exercise, Drugs," \
                    f"                        AppointmentType, ChiefComplaint, GeneralID)" \
                    f"VALUES ('{medical_record_num}', '{int(current_general.get_weight())}', '{current_general.get_height_ft()}', " \
                    f"'{int(current_general.get_height_in())}', '{current_general.get_smoking()}', '{current_general.get_drinking()}', '{current_general.get_exercise()}', '{current_general.get_drugs()}'," \
                    f"       '{current_general.get_appointment_type()}', '{current_general.get_chief_complaint()}', '{general_id}')"

            with db_access.closing(conn.cursor()) as c:
                c.execute(query)
                conn.commit()
            print("General info added to db")

        else:
            # Update
            conn = db_access.connect()
            query = f"UPDATE MRGeneral " \
                    f"SET Weight = '{int(current_general.get_weight())}', HeightFt = '{current_general.get_height_ft()}', HeightIn = '{int(current_general.get_height_in())}', " \
                    f"    Smoking = '{current_general.get_smoking()}', Drinking = '{current_general.get_drinking()}', Exercise = '{current_general.get_exercise()}', " \
                    f"Drugs = '{current_general.get_drugs()}', AppointmentType = '{current_general.get_appointment_type()}', ChiefComplaint = '{current_general.get_chief_complaint()}'" \
                    f"WHERE MRN = {medical_record_num}"

            with db_access.closing(conn.cursor()) as c:
                c.execute(query)
                conn.commit()
            print("General info updated")

        msg_box = QMessageBox()
        msg_box.setWindowTitle("Save Successful")
        msg_box.setText("Changes have been saved.")
        msg_box.exec_()



        #----------------------------------------------------------------------------------






    def on_add_allergy_pushButton_clicked(self):
        add_allergy = self.add_allergy_lineEdit.text()
        current_date = datetime.date.today()
        add_allergy_str = f"{add_allergy}, {current_date}"
        allergy_type = ""
        if self.add_allergy_lineEdit.text() != "":
            if self.allergy_comboBox.currentIndex() == 0:
                self.medication_allergy_listView.addItem(add_allergy_str)
                allergy_type = "medication"
                self.add_allergy_lineEdit.setText("")
            else: #self.allergy_comboBox.currentIndex() == 1:
                self.environmental_allergy_listView.addItem(add_allergy_str)
                allergy_type = "environmental"
                self.add_allergy_lineEdit.setText("")
        else:
            # create a QMessageBox object
            msg_box = QMessageBox()
            # set the message box icon, title, and message text
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setWindowTitle("Error")
            msg_box.setText("Error, no allergy provided.")
            # show the message box
            msg_box.exec_()
            # print("Error, please make a selection.")

        new_allergy = Allergy.Allergy(add_allergy, allergy_type, datetime.datetime.now())

    def on_environmental_remove_pushButton_clicked(self):
        current_item = self.environmental_allergy_listView.currentItem()
        if current_item:
            self.environmental_allergy_listView.takeItem(self.environmental_allergy_listView.currentRow())
        else:
            # create a QMessageBox object
            msg_box = QMessageBox()
            # set the message box icon, title, and message text
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setWindowTitle("Error")
            msg_box.setText("Error, please make a selection.")
            # show the message box
            msg_box.exec_()
            # print("Error, please make a selection.")

    def on_medication_remove_pushButton_clicked(self):
        current_item = self.medication_allergy_listView.currentItem()
        if current_item:
            self.medication_allergy_listView.takeItem(self.medication_allergy_listView.currentRow())
        else:
            # create a QMessageBox object
            msg_box = QMessageBox()
            # set the message box icon, title, and message text
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setWindowTitle("Error")
            msg_box.setText("Error, please make a selection.")
            # show the message box
            msg_box.exec_()
            # print("Error, please make a selection.")

    def on_save_changes_pushButton_allergies_clicked(self):
        medication_allergies = []
        for row in range(self.medication_allergy_listView.model().rowCount()):
            index = self.medication_allergy_listView.model().index(row, 0)
            item_text = self.medication_allergy_listView.model().data(index, Qt.DisplayRole)
            allergy, date_added = item_text.split(", ", 2)
            medication_allergies.append(Allergy.Allergy(allergy, "medication", date_added))

            print(f"{medication_allergies[row].get_allergy_name()}, {medication_allergies[row].get_date_added()}")

        environmental_allergies = []
        for row in range(self.environmental_allergy_listView.model().rowCount()):
            index = self.environmental_allergy_listView.model().index(row, 0)
            item_text = self.environmental_allergy_listView.model().data(index, Qt.DisplayRole)
            allergy, date_added = item_text.split(", ", 2)
            environmental_allergies.append(Allergy.Allergy(allergy, "environmental", date_added))

            print(f"{environmental_allergies[row].get_allergy_name()}, {environmental_allergies[row].get_date_added()}")

        #-----------------------------------------

        medical_record_num = self.mrn_display_label_allergies.text()

        # Get available AllergyID
        allergy_id = 0
        conn = db_access.connect()
        query = f"SELECT MAX(AllergyID) FROM MRAllergy"

        with db_access.closing(conn.cursor()) as c:
            c.execute(query)
            highest_allergy_id = c.fetchone()[0]
            conn.commit()

        allergy_id = highest_allergy_id + 1
        print(allergy_id)

        # Check to see if there is a record with the mrn already in the MRAllery Table
        conn = db_access.connect()
        query = f"SELECT COUNT(*) FROM MRAllergy WHERE MRN = {medical_record_num}"

        with db_access.closing(conn.cursor()) as c:
            c.execute(query)
            result = c.fetchone()[0]
            conn.commit()

        if result == 0:

            for e_allergy in environmental_allergies:


                # Create new allergy
                conn = db_access.connect()
                query = f"INSERT INTO MRAllergy (MRN, AllergyName, AllergyType, DateAdded, AllergyID)" \
                        f"VALUES ('{medical_record_num}', '{e_allergy.get_allergy_name()}', '{e_allergy.get_allergy_type()}', " \
                        f"'{e_allergy.get_date_added()}', '{allergy_id}')"
                with db_access.closing(conn.cursor()) as c:
                    c.execute(query)
                    conn.commit()
                allergy_id += 1
            print("Environmental allergy info added to db")

            for m_allergy in medication_allergies:


                # Create new allergy
                conn = db_access.connect()
                query = f"INSERT INTO MRAllergy (MRN, AllergyName, AllergyType, DateAdded, AllergyID)" \
                        f"VALUES ('{medical_record_num}', '{m_allergy.get_allergy_name()}', '{m_allergy.get_allergy_type()}', " \
                        f"'{m_allergy.get_date_added()}', '{allergy_id}')"
                with db_access.closing(conn.cursor()) as c:
                    c.execute(query)
                    conn.commit()
                allergy_id += 1
            print("medication allergy info added to db")

        else:
            # update stuff
            # Update
            conn = db_access.connect()
            query = f"DELETE FROM MRAllergy WHERE MRN = {medical_record_num}"

            with db_access.closing(conn.cursor()) as c:
                c.execute(query)
                conn.commit()
            print("Previous Allergies deleted")

            for e_allergy in environmental_allergies:


                # Create new allergy
                conn = db_access.connect()
                query = f"INSERT INTO MRAllergy (MRN, AllergyName, AllergyType, DateAdded, AllergyID)" \
                        f"VALUES ('{medical_record_num}', '{e_allergy.get_allergy_name()}', '{e_allergy.get_allergy_type()}', " \
                        f"'{e_allergy.get_date_added()}', '{allergy_id}')"
                with db_access.closing(conn.cursor()) as c:
                    c.execute(query)
                    conn.commit()
                allergy_id += 1

            for m_allergy in medication_allergies:


                # Create new allergy
                conn = db_access.connect()
                query = f"INSERT INTO MRAllergy (MRN, AllergyName, AllergyType, DateAdded, AllergyID)" \
                        f"VALUES ('{medical_record_num}', '{m_allergy.get_allergy_name()}', '{m_allergy.get_allergy_type()}', " \
                        f"'{m_allergy.get_date_added()}', '{allergy_id}')"
                with db_access.closing(conn.cursor()) as c:
                    c.execute(query)
                    conn.commit()
                allergy_id += 1

            print("Update Done")

        msg_box = QMessageBox()
        msg_box.setWindowTitle("Save Successful")
        msg_box.setText("Changes have been saved.")
        msg_box.exec_()


    def on_add_medication_pushButton_clicked(self):
        add_medication = self.add_medication_lineEdit.text()
        add_medication_dose = self.add_medication_dose_lineEdit.text()
        frequency_amount = self.add_medication_frequency_amount_doubleSpinBox.value()

        medication_dose_type = ""
        if self.add_medication_dose_type_comboBox.currentIndex() == 0:
            medication_dose_type = "mg"
        elif self.add_medication_dose_type_comboBox.currentIndex() == 1:
            medication_dose_type = "ml"
        elif self.add_medication_dose_type_comboBox.currentIndex() == 2:
            medication_dose_type = "u"
        else:
            print("Error, please make a selection.")

        frequency_type = ""
        if self.add_medication_frequency_type_comboBox.currentIndex() == 0:
            frequency_type = "Per Hour"
        elif self.add_medication_frequency_type_comboBox.currentIndex() == 1:
            frequency_type = "Per Day"
        elif self.add_medication_frequency_type_comboBox.currentIndex() == 2:
            frequency_type = "Per Week"
        elif self.add_medication_frequency_type_comboBox.currentIndex() == 3:
            frequency_type = "Per Month"
        elif self.add_medication_frequency_type_comboBox.currentIndex() == 4:
            frequency_type = "Per Year"
        elif self.add_medication_frequency_type_comboBox.currentIndex() == 5:
            frequency_type = "Occasionally"
        else:
            print("Error, please make a selection.")

        medication_type = ""
        if self.medication_type_comboBox.currentIndex() == 0:
            medication_type = "prescription"
        elif self.medication_type_comboBox.currentIndex() == 1:
            medication_type = "over the counter"
        elif self.medication_type_comboBox.currentIndex() == 2:
            medication_type = "herbal"
        else:
            print("Error, please make a selection.")

        new_medication = Medication.Medication(add_medication, add_medication_dose, medication_dose_type,
                                               frequency_amount, frequency_type, medication_type)
        logged_in_user = ""
        #self.set_medication_tab_fields(new_medication, logged_in_user)
        if medication_type.lower() == "prescription":
            self.prescription_listView.addItem(f"{new_medication.get_medication_name()}, "
                                               f"{new_medication.get_dose_amount()} {new_medication.get_dose_type()}, "
                                               f"{new_medication.get_frequency()} {new_medication.get_frequency_type()}")
            self.add_medication_lineEdit.setText("")
        elif medication_type.lower() == "over the counter":
            self.over_the_counter_listView.addItem(f"{new_medication.get_medication_name()}, "
                                                   f"{new_medication.get_dose_amount()} {new_medication.get_dose_type()}, "
                                                   f"{new_medication.get_frequency()} {new_medication.get_frequency_type()}")
            self.add_medication_lineEdit.setText("")
        elif medication_type.lower() == "herbal":
            self.herbal_listView.addItem(f"{new_medication.get_medication_name()}, "
                                         f"{new_medication.get_dose_amount()} {new_medication.get_dose_type()}, "
                                         f"{new_medication.get_frequency()} {new_medication.get_frequency_type()}")
            self.add_medication_lineEdit.setText("")

    def on_prescription_remove_pushButton_clicked(self):
        current_item = self.prescription_listView.currentItem()
        if current_item:
            self.prescription_listView.takeItem(self.prescription_listView.currentRow())
        else:
            print("Error, please make a selection.")

    def on_over_the_counter_remove_pushButton_clicked(self):
        current_item = self.over_the_counter_listView.currentItem()
        if current_item:
            self.over_the_counter_listView.takeItem(self.over_the_counter_listView.currentRow())
        else:
            print("Error, please make a selection.")

    def on_herbal_remove_pushButton_clicked(self):
        current_item = self.herbal_listView.currentItem()
        if current_item:
            self.herbal_listView.takeItem(self.herbal_listView.currentRow())
        else:
            print("Error, please make a selection.")

    def on_save_changes_pushButton_medications_clicked(self):
        mrn = self.mrn_display_label_medications.text()
        prescription_medications = []

        conn = db_access.connect()
        query = f"DELETE FROM MRMedications WHERE MRN = {mrn}"

        with db_access.closing(conn.cursor()) as c:
            c.execute(query)
            conn.commit()

        for row in range(self.prescription_listView.model().rowCount()):
            index = self.prescription_listView.model().index(row, 0)
            item_text = self.prescription_listView.model().data(index, Qt.DisplayRole)
            medication_name, dose, frequency = item_text.split(", ", 3)
            dose_amount, dose_type = dose.split(" ", 2)
            frequency, frequency_type = frequency.split(" ", 1)

            db_access.create_new_medication(mrn, medication_name, dose_amount, dose_type, frequency, frequency_type,
                                            "prescription")


        over_the_counter_medications = []
        for row in range(self.over_the_counter_listView.model().rowCount()):
            index = self.over_the_counter_listView.model().index(row, 0)
            item_text = self.over_the_counter_listView.model().data(index, Qt.DisplayRole)
            medication_name, dose, frequency = item_text.split(", ", 3)
            dose_amount, dose_type = dose.split(" ", 2)
            frequency, frequency_type = frequency.split(" ", 1)

            db_access.create_new_medication(mrn, medication_name, dose_amount, dose_type, frequency, frequency_type,
                                            "over the counter")


        herbal_medications = []
        for row in range(self.herbal_listView.model().rowCount()):
            index = self.herbal_listView.model().index(row, 0)
            item_text = self.herbal_listView.model().data(index, Qt.DisplayRole)
            medication_name, dose, frequency = item_text.split(", ", 3)
            dose_amount, dose_type = dose.split(" ", 2)
            frequency, frequency_type = frequency.split(" ", 1)

            db_access.create_new_medication(mrn, medication_name, dose_amount, dose_type, frequency, frequency_type,
                                            "herbal")


        msg_box = QMessageBox()
        msg_box.setWindowTitle("Save Successful")
        msg_box.setText("Changes have been saved.")
        msg_box.exec_()


    def on_add_procedure_from_comboBox_pushButton_clicked(self):
        procedure_type = ""
        if self.procedures_performed_comboBox.currentIndex() == 0:
            procedure_type = "Bandaging"
            self.procedure_list_listView.addItem(procedure_type)
        elif self.procedures_performed_comboBox.currentIndex() == 1:
            procedure_type = "EKG"
            self.procedure_list_listView.addItem(procedure_type)
        elif self.procedures_performed_comboBox.currentIndex() == 2:
            procedure_type = "Labs"
            self.procedure_list_listView.addItem(procedure_type)
        elif self.procedures_performed_comboBox.currentIndex() == 3:
            procedure_type = "Stitches"
            self.procedure_list_listView.addItem(procedure_type)
        elif self.procedures_performed_comboBox.currentIndex() == 4:
            procedure_type = "X-rays"
            self.procedure_list_listView.addItem(procedure_type)
        else:
            pass

    def on_add_procedure_other_pushButton_clicked(self):
        add_procedure = self.procedure_other_lineEdit.text()
        if add_procedure != "":
            self.procedure_list_listView.addItem(add_procedure)
            self.procedure_other_lineEdit.setText("")
        else:
            # create a QMessageBox object
            msg_box = QMessageBox()
            # set the message box icon, title, and message text
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setWindowTitle("Error")
            msg_box.setText("Error, No Procedure Provided.")
            # show the message box
            msg_box.exec_()

    def on_remove_procedure_pushButton_clicked(self):
        current_item = self.procedure_list_listView.currentItem()
        if current_item:
            self.procedure_list_listView.takeItem(self.procedure_list_listView.currentRow())
        else:
            # create a QMessageBox object
            msg_box = QMessageBox()
            # set the message box icon, title, and message text
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setWindowTitle("Error")
            msg_box.setText("Error, please make a selection.")
            # show the message box
            msg_box.exec_()
            # print("Error, please make a selection.")

    def on_save_changes_pushbutton_exam_assessments_clicked(self):
        print("Save pressed")

        app_date_time = self.appointment_dateTimeEdit.text()

        office_name = ""
        index = self.office_location_comboBox.currentIndex()
        if index == 0:
            office_name = "Kernersville"
        elif index == 1:
            office_name = "Winston Salem"
        elif index == 2:
            office_name = "Mount Airy"
        else:
            pass

        primary_provider = ""
        provider_index = self.primary_provider_comboBox.currentIndex()
        if provider_index == 0:
            primary_provider = "List of Provider Names"

        app_provider = ""
        app_provider_index = self.appointment_provider_comboBox.currentIndex()
        if app_provider_index == 0:
            app_provider = "List of Provider Names"

        app_nurse = ""
        nurse_index = self.appointment_nurse_comboBox.currentIndex()
        if nurse_index == 0:
            app_nurse = "List of Nurse Names"

        app_cna = ""
        cna_index = self.appointment_cna_comboBox.currentIndex()
        if cna_index == 0:
            app_cna = "List of CNA Names"

        temperature = self.exam_assessments_temperature_doubleSpinBox.value()
        bp_sbp = self.blood_pressure_sbp_lineEdit_exam_assessment.text()
        bp_dbp = self.blood_pressure_dbp_lineEdit_exam_assessment.text()
        respiration_rate = self.respiration_rate_lineEdit_exam_assessment.text()
        pulse_rate = self.pulse_rate_lineEdit_exam_assessment.text()
        blood_ox_levels = self.blood_ox_levels_lineEdit_exam_assessment.text()

        physician_notes = self.physicaion_notes_textEdit_exam_assessment.toPlainText()
        notes_date_added = datetime.datetime.now()

        procedures = []
        for row in range(self.procedure_list_listView.model().rowCount()):
            index = self.procedure_list_listView.model().index(row, 0)
            item_text = self.procedure_list_listView.model().data(index, Qt.DisplayRole)
            procedures.append(ProceduresPerformed.ProceduresPerformed(item_text))

        needed = ""
        if self.follow_up_needed_yes_radioButton.isChecked():
            needed = "yes"
        if self.follow_up_needed_no_radioButton.isChecked():
            needed = "no"

        follow_up_frequency = self.follow_up_in_frequency_spinBox.value()

        follow_up_frequency_type = ""
        index = self.follow_up_frequency_type_comboBox.currentIndex()
        if index == 0:
            follow_up_frequency_type = "Day(s)"
        elif index == 1:
            follow_up_frequency_type = "Week(s)"
        elif index == 2:
            follow_up_frequency_type = "Month(s)"
        else:
            pass

        current_app_info = AppointmentTimeAndDate.AppointmentTimeAndDate(app_date_time)
        current_app_staff_info = AppointmentStaff.AppointmentStaff(primary_provider, app_provider, app_nurse, app_cna)
        current_office_location = OfficeLocations.OfficeLocations(office_name)
        current_vitals_info = Vitals.Vitals(temperature, bp_sbp, bp_dbp, respiration_rate, pulse_rate, blood_ox_levels)
        current_physician_notes = PhysicianNotes.PhysicianNotes(physician_notes, notes_date_added)
        current_follow_up_info = FollowUp.FollowUp(needed, follow_up_frequency, follow_up_frequency_type)

        print("Appointment Information: ")
        print(f"{current_app_info.get_appointment_time_and_date()}")
        print("Appointment Staff Information: ")
        print(f"{current_app_staff_info.get_primary_provider()}, {current_app_staff_info.get_appointment_provider()}, {current_app_staff_info.get_appointment_nurse()}, {current_app_staff_info.get_appointment_cna()}")
        print(f"{current_office_location.get_office_name()}")
        print("Vitals Information: ")
        print(f"{current_vitals_info.get_temperature()}, {current_vitals_info.get_systolic_blood_pressure()}, {current_vitals_info.get_diastolic_blood_pressure()}, {current_vitals_info.get_respiration_rate()}, {current_vitals_info.get_pulse_rate()}, {current_vitals_info.get_blood_oxygen_levels()}")
        print("Physician Notes Information: ")
        print(f"{current_physician_notes.get_notes()}, {current_physician_notes.get_date_added()}")
        print("Follow Up Information: ")
        print(f"{current_follow_up_info.get_needed()}, {current_follow_up_info.get_follow_up_frequency()}, {current_follow_up_info.get_follow_up_frequency_type()}")

        # Exam A------------------------------------------------------
        medical_record_num = self.mrn_display_label_exam_assessments.text()

        # update appointment
        conn = db_access.connect()
        query = f"UPDATE MRAppointment " \
                f"SET AppointmentTimeAndDate = '{current_app_info.get_appointment_time_and_date()}', " \
                f"Location = '{office_name}', PrimaryProvider = '{primary_provider}', AppointmentProvider = '{app_provider}', " \
                f"AppointmentNurse = '{app_nurse}', AppointmentCNA = '{app_cna}' " \
                f"WHERE MRN = {medical_record_num} and Status = 'Open'"

        with db_access.closing(conn.cursor()) as c:
            c.execute(query)
            conn.commit()

        # update vitals
        conn = db_access.connect()
        query = f"UPDATE MRVitals " \
                f"SET Temperature = '{current_vitals_info.get_temperature()}', SystolicBloodPressure = '{current_vitals_info.get_systolic_blood_pressure()}', " \
                f"    DiastolicBloodPressure = '{current_vitals_info.get_diastolic_blood_pressure()}', RespirationRate = '{current_vitals_info.get_respiration_rate()}', " \
                f"    PulseRate = '{current_vitals_info.get_pulse_rate()}', BloodOxygenLevels = '{current_vitals_info.get_blood_oxygen_levels()}' " \
                f"WHERE MRN = {medical_record_num}"

        with db_access.closing(conn.cursor()) as c:
            c.execute(query)
            conn.commit()

        # update physician notes
        conn = db_access.connect()
        query = f"UPDATE MRPhysicianNotes " \
                f"SET Notes = '{current_physician_notes.get_notes()}' " \
                f"WHERE MRN = {medical_record_num}"

        with db_access.closing(conn.cursor()) as c:
            c.execute(query)
            conn.commit()


        # Get available ProcedureID
        conn = db_access.connect()
        query = f"SELECT MAX(ProcedureID) FROM MRProceduresPerformed"

        with db_access.closing(conn.cursor()) as c:
            c.execute(query)
            highest_procedure_id = c.fetchone()[0]
            conn.commit()

        if highest_procedure_id != None:
            procedure_id = highest_procedure_id + 1
        else:
            procedure_id = 1

        # update procedures
        conn = db_access.connect()
        query = f"DELETE FROM MRProceduresPerformed WHERE MRN = {medical_record_num}"

        with db_access.closing(conn.cursor()) as c:
            c.execute(query)
            conn.commit()
        print("Previous procedures deleted")

        # Create new procedures
        for procedure in procedures:

            conn = db_access.connect()
            query = f"INSERT INTO MRProceduresPerformed (MRN, ProcedureID, ProcedureInfo)" \
                    f"VALUES ({medical_record_num}, '{procedure_id}', '{procedure.get_procedure()}')"
            print(medical_record_num)
            print(procedure_id)
            print(procedure.get_procedure())
            with db_access.closing(conn.cursor()) as c:
                c.execute(query)
                conn.commit()
            procedure_id += 1

            # update follow up
            conn = db_access.connect()
            query = f"DELETE FROM MRFollowUp WHERE MRN = {medical_record_num}"

            with db_access.closing(conn.cursor()) as c:
                c.execute(query)
                conn.commit()
            print("Previous follow deleted")

                        # Get available FollowUpID
            conn = db_access.connect()
            query = f"SELECT MAX(FollowUpID) FROM MRFollowUp"

            with db_access.closing(conn.cursor()) as c:
                c.execute(query)
                highest_follow_up_id = c.fetchone()[0]
                conn.commit()

            if highest_follow_up_id != None:
                follow_up_id = highest_follow_up_id + 1
            else:
                follow_up_id = 1

            # Create new follow up
            conn = db_access.connect()
            query = f"INSERT INTO MRFollowUp (MRN, FollowUpID, Needed, FollowUpFrequency, FollowUpFrequencyType)" \
                    f"VALUES ({medical_record_num}, '{follow_up_id}', '{current_follow_up_info.get_needed()}', " \
                    f"'{current_follow_up_info.get_follow_up_frequency()}', '{current_follow_up_info.get_follow_up_frequency_type()}')"
            with db_access.closing(conn.cursor()) as c:
                c.execute(query)
                conn.commit()
            follow_up_id += 1

        # Exam A------------------------------------------------------

        print("End\n")

        msg_box = QMessageBox()
        msg_box.setWindowTitle("Save Successful")
        msg_box.setText("Changes have been saved.")
        msg_box.exec_()

    def on_patient_history_from_comboBox_pushButton_clicked(self):
        selected_index = self.patient_history_comboBox.currentIndex()
        medical_history_option = medical_history_options.get(selected_index)
        if medical_history_option != "":
            self.patient_history_listView.addItem(medical_history_option)
        else:
            # create a QMessageBox object
            msg_box = QMessageBox()
            # set the message box icon, title, and message text
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setWindowTitle("Error")
            msg_box.setText("Error, please make a selection.")
            # show the message box
            msg_box.exec_()
            # print("Error, please make a selection.")

    def on_patient_history_from_other_pushButton_clicked(self):
        add_history = self.patient_history_other_lineEdit.text()
        if add_history != "":
            self.patient_history_listView.addItem(add_history)
            self.patient_history_other_lineEdit.setText("")
        else:
            # create a QMessageBox object
            msg_box = QMessageBox()
            # set the message box icon, title, and message text
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setWindowTitle("Error")
            msg_box.setText("Error, No History Provided.")
            # show the message box
            msg_box.exec_()

    def on_remove_patient_history_pushButton_clicked(self):
        current_item = self.patient_history_listView.currentItem()
        if current_item:
            self.patient_history_listView.takeItem(self.patient_history_listView.currentRow())
        else:
            # create a QMessageBox object
            msg_box = QMessageBox()
            # set the message box icon, title, and message text
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setWindowTitle("Error")
            msg_box.setText("Error, please make a selection.")
            # show the message box
            msg_box.exec_()

    def on_patient_mothers_history_from_comboBox_pushButton_clicked(self):
        selected_index = self.patient_mothers_history_comboBox.currentIndex()
        medical_history_option = medical_history_options.get(selected_index)
        if medical_history_option != "":
            self.patient_mothers_history_listView.addItem(medical_history_option)
        else:
            # create a QMessageBox object
            msg_box = QMessageBox()
            # set the message box icon, title, and message text
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setWindowTitle("Error")
            msg_box.setText("Error, please make a selection.")
            # show the message box
            msg_box.exec_()
            # print("Error, please make a selection.")

    def on_patient_mothers_history_from_other_pushButton_clicked(self):
        add_history = self.patient_mothers_history_other_lineEdit.text()
        if add_history != "":
            self.patient_mothers_history_listView.addItem(add_history)
            self.patient_mothers_history_other_lineEdit.setText("")
        else:
            # create a QMessageBox object
            msg_box = QMessageBox()
            # set the message box icon, title, and message text
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setWindowTitle("Error")
            msg_box.setText("Error, No History Provided.")
            # show the message box
            msg_box.exec_()

    def on_remove_patient_mothers_history_pushButton_clicked(self):
        current_item = self.patient_mothers_history_listView.currentItem()
        if current_item:
            self.patient_mothers_history_listView.takeItem(self.patient_mothers_history_listView.currentRow())
        else:
            # create a QMessageBox object
            msg_box = QMessageBox()
            # set the message box icon, title, and message text
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setWindowTitle("Error")
            msg_box.setText("Error, please make a selection.")
            # show the message box
            msg_box.exec_()

    def on_patient_fathers_history_from_comboBox_pushButton_clicked(self):
        selected_index = self.patient_fathers_history_comboBox.currentIndex()
        medical_history_option = medical_history_options.get(selected_index)
        if medical_history_option != "":
            self.patient_fathers_history_listView.addItem(medical_history_option)
        else:
            # create a QMessageBox object
            msg_box = QMessageBox()
            # set the message box icon, title, and message text
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setWindowTitle("Error")
            msg_box.setText("Error, please make a selection.")
            # show the message box
            msg_box.exec_()
            # print("Error, please make a selection.")

    def on_patient_fathers_history_from_other_pushButton_clicked(self):
        add_history = self.patient_fathers_history_other_lineEdit.text()
        if add_history != "":
            self.patient_fathers_history_listView.addItem(add_history)
            self.patient_fathers_history_other_lineEdit.setText("")
        else:
            # create a QMessageBox object
            msg_box = QMessageBox()
            # set the message box icon, title, and message text
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setWindowTitle("Error")
            msg_box.setText("Error, No History Provided.")
            # show the message box
            msg_box.exec_()

    def on_remove_patient_fathers_history_pushButton_clicked(self):
        current_item = self.patient_fathers_history_listView.currentItem()
        if current_item:
            self.patient_fathers_history_listView.takeItem(self.patient_fathers_history_listView.currentRow())
        else:
            # create a QMessageBox object
            msg_box = QMessageBox()
            # set the message box icon, title, and message text
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setWindowTitle("Error")
            msg_box.setText("Error, please make a selection.")
            # show the message box
            msg_box.exec_()

    def on_save_changes_pushbutton_medical_history_clicked(self):
        print("Save start\n")

        patient_history_list = []
        mothers_history_list = []
        fathers_history_list = []

        for row in range(self.patient_history_listView.model().rowCount()):
            index = self.patient_history_listView.model().index(row, 0)
            item_text = self.patient_history_listView.model().data(index, Qt.DisplayRole)
            patient_history_list.append(MedicalHistory.MedicalHistory(item_text, "patient"))

        print(f"Patient's History\nDiagnosis, History Type\n--------------------------------")
        for x in range(len(patient_history_list)):
            print(f"{patient_history_list[x].get_diagnosis()}, {patient_history_list[x].get_history_type()}")

        print()

        for row in range(self.patient_mothers_history_listView.model().rowCount()):
            index = self.patient_mothers_history_listView.model().index(row, 0)
            item_text = self.patient_mothers_history_listView.model().data(index, Qt.DisplayRole)
            mothers_history_list.append(MedicalHistory.MedicalHistory(item_text, "mother"))

        print(f"Mother's History\nDiagnosis, History Type\n--------------------------------")
        for x in range(len(mothers_history_list)):
            print(f"{mothers_history_list[x].get_diagnosis()}, {mothers_history_list[x].get_history_type()}")

        print()

        for row in range(self.patient_fathers_history_listView.model().rowCount()):
            index = self.patient_fathers_history_listView.model().index(row, 0)
            item_text = self.patient_fathers_history_listView.model().data(index, Qt.DisplayRole)
            fathers_history_list.append(MedicalHistory.MedicalHistory(item_text, "father"))

        print(f"Father's History\nDiagnosis, History Type\n--------------------------------")
        for x in range(len(fathers_history_list)):
            print(f"{fathers_history_list[x].get_diagnosis()}, {fathers_history_list[x].get_history_type()}")

        print("End\n")

        # ---------------------------------------
        medical_record_num = self.mrn_display_label_demographics.text()

        # delete records on the table that match the mrn
        conn = db_access.connect()
        query = f"DELETE FROM MRMedicalHistory WHERE MRN = {medical_record_num}"

        with db_access.closing(conn.cursor()) as c:
            c.execute(query)
            conn.commit()

        print("removed previous records")

        # Get available MedicalHistoryID
        med_hist_id = 0
        conn = db_access.connect()
        query = f"SELECT MAX(MedicalHistoryID) FROM MRMedicalHistory"

        with db_access.closing(conn.cursor()) as c:
            c.execute(query)
            highest_med_hist_id = c.fetchone()[0]
            conn.commit()

        if highest_med_hist_id != None:
            med_hist_id = highest_med_hist_id + 1
        else:
            med_hist_id = 1

        # add patient history records
        for med_hist in patient_history_list:
            conn = db_access.connect()
            query = f"INSERT INTO MRMedicalHistory (MRN, Diagnosis, HistoryType, MedicalHistoryID)" \
                    f"VALUES ({medical_record_num}, '{med_hist.get_diagnosis()}', '{med_hist.get_history_type()}', '{med_hist_id}')"

            with db_access.closing(conn.cursor()) as c:
                c.execute(query)
                conn.commit()
            med_hist_id += 1
            print(med_hist.get_diagnosis())
        print("added from patient history")

        # add mother history records
        for med_hist in mothers_history_list:
            conn = db_access.connect()
            query = f"INSERT INTO MRMedicalHistory (MRN, Diagnosis, HistoryType, MedicalHistoryID)" \
                    f"VALUES ({medical_record_num}, '{med_hist.get_diagnosis()}', '{med_hist.get_history_type()}', '{med_hist_id}')"

            with db_access.closing(conn.cursor()) as c:
                c.execute(query)
                conn.commit()
            med_hist_id += 1
            print(med_hist.get_diagnosis())
        print("added from mother history")

        # add father history records
        for med_hist in fathers_history_list:
            conn = db_access.connect()
            query = f"INSERT INTO MRMedicalHistory (MRN, Diagnosis, HistoryType, MedicalHistoryID)" \
                    f"VALUES ({medical_record_num}, '{med_hist.get_diagnosis()}', '{med_hist.get_history_type()}', '{med_hist_id}')"

            with db_access.closing(conn.cursor()) as c:
                c.execute(query)
                conn.commit()
            med_hist_id += 1
            print(med_hist.get_diagnosis())
        print("added from father history")
        # ---------------------------------------


        msg_box = QMessageBox()
        msg_box.setWindowTitle("Save Successful")
        msg_box.setText("Changes have been saved.")
        msg_box.exec_()

    def on_add_injury_surgery_pushButton_clicked(self):
        add_history = self.add_injury_surgery_lineEdit.text()
        date_occurred = self.injury_surgery_date_occured_dateEdit.date().toString("yyyy-MM-dd")
        selected_index = self.injury_surgery_comboBox.currentIndex()
        if self.add_injury_surgery_lineEdit != "":
            if selected_index == 0:
                self.injury_history_listView.addItem(f"{add_history}, {date_occurred}")
            else:
                self.surgery_history_listView.addItem(f"{add_history}, {date_occurred}")
            self.add_injury_surgery_lineEdit.setText("")
        else:
            # create a QMessageBox object
            msg_box = QMessageBox()
            # set the message box icon, title, and message text
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setWindowTitle("Error")
            msg_box.setText("Error, No History Provided.")
            # show the message box
            msg_box.exec_()

    def on_injury_history_remove_pushButton_clicked(self):
        current_item = self.injury_history_listView.currentItem()
        if current_item:
            self.injury_history_listView.takeItem(self.injury_history_listView.currentRow())
        else:
            # create a QMessageBox object
            msg_box = QMessageBox()
            # set the message box icon, title, and message text
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setWindowTitle("Error")
            msg_box.setText("Error, please make a selection.")
            # show the message box
            msg_box.exec_()

    def on_surgery_history_remove_pushButton_clicked(self):
        current_item = self.surgery_history_listView.currentItem()
        if current_item:
            self.surgery_history_listView.takeItem(self.surgery_history_listView.currentRow())
        else:
            # create a QMessageBox object
            msg_box = QMessageBox()
            # set the message box icon, title, and message text
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setWindowTitle("Error")
            msg_box.setText("Error, please make a selection.")
            # show the message box
            msg_box.exec_()

    def on_save_changes_pushbutton_injury_and_surgical_history_clicked(self):
        print("Save Start (Injury and Surgery)")

        injury_list = []
        surgery_list = []

        print("Injury History\n----------------------------------")
        for row in range(self.injury_history_listView.model().rowCount()):
            index = self.injury_history_listView.model().index(row, 0)
            item_text = self.injury_history_listView.model().data(index, Qt.DisplayRole)
            description, date_occurred = item_text.split(", ", 2)
            injury_list.append(InjuryHistory.InjuryHistory(description, date_occurred))

            print(f"{injury_list[row].get_description()}, {injury_list[row].get_date_occurred()}")

        print("\nSurgery History\n----------------------------------")

        for row in range(self.surgery_history_listView.model().rowCount()):
            index = self.surgery_history_listView.model().index(row, 0)
            item_text = self.surgery_history_listView.model().data(index, Qt.DisplayRole)
            description, date_occurred = item_text.split(", ", 2)
            surgery_list.append(SurgicalHistory.SurgeryHistory(description, date_occurred))

            print(f"{surgery_list[row].get_description()}, {surgery_list[row].get_date_occurred()}")

        print("End (Injury and Surgery)\n")

        # -------------------------------------------------------------------------------
        medical_record_num = self.mrn_display_label_demographics.text()

        # delete records on the both injury and surgery table that match the mrn
        conn = db_access.connect()
        query = f"DELETE FROM MRInjuryHistory WHERE MRN = {medical_record_num}"
        query2 = f"DELETE FROM MRSurgeryHistory WHERE MRN = {medical_record_num}"

        with db_access.closing(conn.cursor()) as c:
            c.execute(query)
            c.execute(query2)
            conn.commit()

        print("removed previous records")

        # Get available InjuryHistoryID
        conn = db_access.connect()
        query = f"SELECT MAX(InjuryHistoryID) FROM MRInjuryHistory"

        with db_access.closing(conn.cursor()) as c:
            c.execute(query)
            highest_injury_hist_id = c.fetchone()[0]
            conn.commit()

        # Get available SurgeryHistoryID
        conn = db_access.connect()
        query = f"SELECT MAX(SurgeryHistoryID) FROM MRSurgeryHistory"

        with db_access.closing(conn.cursor()) as c:
            c.execute(query)
            highest_surgery_hist_id = c.fetchone()[0]
            conn.commit()

        if highest_injury_hist_id != None:
            injury_hist_id = highest_injury_hist_id + 1
        else:
            injury_hist_id = 1

        if highest_surgery_hist_id != None:
            surgery_hist_id = highest_surgery_hist_id + 1
        else:
            surgery_hist_id = 1

        # add injury history records
        for injury_hist in injury_list:
            conn = db_access.connect()
            query = f"INSERT INTO MRInjuryHistory (MRN, Description, DateOccurred, InjuryHistoryID)" \
                    f"VALUES ({medical_record_num}, '{injury_hist.get_description()}', '{injury_hist.get_date_occurred()}', '{injury_hist_id}')"

            with db_access.closing(conn.cursor()) as c:
                c.execute(query)
                conn.commit()
            injury_hist_id += 1
            print(injury_hist.get_description())
        print("added from injury history")

        # add surgery history records
        for surgery_hist in surgery_list:
            conn = db_access.connect()
            query = f"INSERT INTO MRSurgeryHistory (MRN, Description, DateOccurred, SurgeryHistoryID)" \
                    f"VALUES ({medical_record_num}, '{surgery_hist.get_description()}', '{surgery_hist.get_date_occurred()}', '{surgery_hist_id}')"

            with db_access.closing(conn.cursor()) as c:
                c.execute(query)
                conn.commit()
            surgery_hist_id += 1
            print(surgery_hist.get_description())
        print("added from surgery history")


        # -------------------------------------------------------------------------------


        msg_box = QMessageBox()
        msg_box.setWindowTitle("Save Successful")
        msg_box.setText("Changes have been saved.")
        msg_box.exec_()

    def on_request_lab_pushButton_clicked(self):
        selected_index = self.labs_comboBox.currentIndex()
        order_labs_option = order_labs_options.get(selected_index)
        current_date = datetime.date.today()
        pending_labs_str = f"{order_labs_option}, {current_date}"
        if order_labs_option != "":
            self.pending_labs_listView.addItem(pending_labs_str)
        else:
            # create a QMessageBox object
            msg_box = QMessageBox()
            # set the message box icon, title, and message text
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setWindowTitle("Error")
            msg_box.setText("Error, please make a selection.")
            # show the message box
            msg_box.exec_()
            # print("Error, please make a selection.")

    def on_completed_labs_show_selection_pushButton_clicked(self):
        current_item = self.completed_labs_listView.currentItem()
        if current_item:
            # add method to call info from db for selected lab
            # placeholder to show button functionality
            self.lab_results_listView.addItem("Feature Coming Soon!")
        else:
            # create a QMessageBox object
            msg_box = QMessageBox()
            # set the message box icon, title, and message text
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setWindowTitle("Error")
            msg_box.setText("Error, please make a selection.")
            # show the message box
            msg_box.exec_()

    def on_pending_labs_remove_pushButton_clicked(self):
        current_item = self.pending_labs_listView.currentItem()
        if current_item:
            self.pending_labs_listView.takeItem(self.pending_labs_listView.currentRow())
        else:
            # create a QMessageBox object
            msg_box = QMessageBox()
            # set the message box icon, title, and message text
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setWindowTitle("Error")
            msg_box.setText("Error, please make a selection.")
            # show the message box
            msg_box.exec_()

        current_item_text = current_item.text()
        current_item_split_lab_name, current_item_split_date = current_item_text.split(", ", 2)
        print(current_item_split_lab_name)
        print(current_item_split_date)
        medical_record_num = self.mrn_display_label_labs.text()

        if current_item:
            conn = db_access.connect()
            query = f"DELETE FROM MRLab WHERE LabType = '{current_item_split_lab_name}' and DateRequested = '{current_item_split_date}' and MRN = {medical_record_num}"

            with db_access.closing(conn.cursor()) as c:
                c.execute(query)
                conn.commit()
            print("Previous Lab was deleted")
        else:
            pass


    def on_save_changes_pushbutton_labs_clicked(self):
        print("Save Start (Labs)")

        medical_record_num = self.mrn_display_label_labs.text()

        # Get available LabID
        conn = db_access.connect()
        query = f"SELECT MAX(LabID) FROM MRLab"

        with db_access.closing(conn.cursor()) as c:
            c.execute(query)
            highest_lab_id = c.fetchone()[0]
            conn.commit()

        if highest_lab_id != None:
            lab_id = highest_lab_id + 1
        else:
            lab_id = 1

        pending_labs_list = []
        for row in range(self.pending_labs_listView.model().rowCount()):
            index = self.pending_labs_listView.model().index(row, 0)
            item_text = self.pending_labs_listView.model().data(index, Qt.DisplayRole)
            lab_type, date_requested = item_text.split(", ", 2)
            pending_labs_list.append(Labs.Labs(lab_type, date_requested, "pending"))

            print(f"{pending_labs_list[row].get_lab_type()}, {pending_labs_list[row].get_date_requested()}: {pending_labs_list[row].get_status()}")


            # Labs----------------------------------------------------------

            # if lab on listview is same as lab on db table skip
            conn = db_access.connect()

            query = f"SELECT LabType, DateRequested, Status " \
                    f"FROM MRLab " \
                    f"WHERE MRN = {medical_record_num} and LabType = '{pending_labs_list[row].get_lab_type()}' and " \
                    f"DateRequested = '{pending_labs_list[row].get_date_requested()}' and Status = '{pending_labs_list[row].get_status()}'"

            with db_access.closing(conn.cursor()) as c:
                c.execute(query)
                output = c.fetchall()

            if len(output) == 1:
                # print(output[0].LabType)
                print("No record added")
            else:
                print("Record added")
                conn = db_access.connect()
                query = f"INSERT INTO MRLab (MRN, LabType, DateRequested, Status, LabID)" \
                        f"VALUES ({medical_record_num}, '{pending_labs_list[row].get_lab_type()}', '{pending_labs_list[row].get_date_requested()}', " \
                        f"'{pending_labs_list[row].get_status()}', '{lab_id}')"

                with db_access.closing(conn.cursor()) as c:
                    c.execute(query)
                    conn.commit()

                lab_id += 1

            # ----------------------------------------------------------


        print("End (Labs)\n")

        msg_box = QMessageBox()
        msg_box.setWindowTitle("Save Successful")
        msg_box.setText("Changes have been saved.")
        msg_box.exec_()

    def on_save_changes_pushButton_care_plan_clicked(self):
        assessment = self.care_plan_assessment_textEdit.toPlainText()
        planning = self.care_plan_planning_textEdit.toPlainText()
        diagnosis = self.care_plan_diagnosis_textEdit.toPlainText()
        post_evaluation = self.care_plan_post_evaluation_textEdit.toPlainText()
        date_added = datetime.datetime.now()
        frequency_amount = self.care_plan_frequency_amount_spinBox.value()

        frequency_type = ""
        if self.care_plan_frequency_type_comboBox.currentIndex() == 0:
            frequency_type = "Per Hour"
        elif self.care_plan_frequency_type_comboBox.currentIndex() == 1:
            frequency_type = "Per Day"
        elif self.care_plan_frequency_type_comboBox.currentIndex() == 2:
            frequency_type = "Per Week"
        elif self.care_plan_frequency_type_comboBox.currentIndex() == 3:
            frequency_type = "Per Month"
        elif self.care_plan_frequency_type_comboBox.currentIndex() == 4:
            frequency_type = "Per Year"
        elif self.care_plan_frequency_type_comboBox.currentIndex() == 5:
            frequency_type = "Occasionally"
        else:
            pass
        end_date = self.care_plan_end_date_dateEdit.text()

        care_plan_current_info = CarePlan.CarePlan(assessment, planning, diagnosis, post_evaluation, date_added, frequency_amount, frequency_type, end_date)

        print(f"{care_plan_current_info.get_assessment()}, {care_plan_current_info.get_planning()}, {care_plan_current_info.get_diagnosis()}, {care_plan_current_info.get_post_evaluation()}, {care_plan_current_info.get_date_added()}, {care_plan_current_info.get_frequency()}, {care_plan_current_info.get_frequency_type()}, {care_plan_current_info.get_end_date()}")

        # code for call to database
        # careplan ----------------------------------------------------
        medical_record_num = self.mrn_display_label_care_plan.text()

        # update the careplan
        conn = db_access.connect()
        query = f"UPDATE MRCarePlan " \
                f"SET Assessment = '{assessment}', Planning = '{planning}', Diagnosis = '{diagnosis}', " \
                f"    PostEvaluation = '{post_evaluation}', DateAdded = '{date_added}', Frequency = '{frequency_amount}', " \
                f"    FrequencyType = '{frequency_type}', EndDate = '{end_date}' " \
                f"WHERE MRN = {medical_record_num}"

        with db_access.closing(conn.cursor()) as c:
            c.execute(query)
            conn.commit()
        print("Care Plan updated")
        # careplan ----------------------------------------------------

        msg_box = QMessageBox()
        msg_box.setWindowTitle("Save Successful")
        msg_box.setText("Changes have been saved.")
        msg_box.exec_()

    def on_submit_referral_pushButton_clicked(self):
        mrn = int(self.mrn_display_label_referrals.text())
        referral_num = self.referral_number_display_label.text()
        updated_referral_num = int(referral_num) + 1
        self.referral_number_display_label.setText(str(updated_referral_num))
        selected_index = self.referra_reason_comboBox.currentIndex()
        referral_reason_option = referral_reason_options.get(selected_index)
        pending_referral_str = f"{referral_num}, {referral_reason_option}"
        self.pending_referrals_listView.addItem(pending_referral_str)
        selected_index = self.referring_provider_comboBox.currentIndex()
        refer_provider_option = provider_options.get(selected_index)
        refer_provider_npi = self.referring_provder_npi_display_label.text()
        refer_date = self.referral_date_dateEdit.date().toString("yyyy-MM-dd")
        refer_expiration_date = self.referral_expiration_date_dateEdit.date().toString("yyyy-MM-dd")
        selected_index = self.referra_reason_comboBox.currentIndex()
        referral_reason_option = referral_reason_options.get(selected_index)
        patient_condition = self.patient_condition_textEdit.toPlainText()
        refer_status = "pending"

        # referral = Referrals.Referrals(referral_num, referral_reason_option, refer_provider_option, refer_provider_npi,
        #                                       refer_date, refer_expiration_date, patient_condition, refer_status)
        # Add method to send referral to DB
        db_access.create_new_referral(mrn, referral_num, referral_reason_option, refer_status, refer_provider_option,
                                      refer_provider_npi, refer_date, refer_expiration_date, patient_condition)

    def on_refresh_pending_referral_list_pushButton_clicked(self):
        mrn = int(self.mrn_display_label_referrals.text())
        refresh_list = self.get_referral_info_from_db(mrn)
        self.pending_referrals_listView.clear()
        for item in refresh_list:
            if item.get_status() == "pending":
                self.pending_referrals_listView.addItem(f"{item.get_referral_num()}, {item.get_referral_reason()}")
                print("Refreshed List")
            else:
                pass

    def on_refresh_completed_referral_list_pushButton_clicked(self):
        mrn = int(self.mrn_display_label_referrals.text())
        refresh_list = self.get_referral_info_from_db(mrn)
        self.completed_referrals_listView.clear()
        for item in refresh_list:
            if item.get_status() == "completed":
                self.completed_referrals_listView.addItem(f"{item.get_referral_num()}, {item.get_referral_reason()}")
                print("Refreshed List")
            else:
                pass

    def referring_provider_comboBox_on_idex_change(self):
        selected_index = self.referring_provider_comboBox.currentIndex()
        refer_provider_option = refer_provider_options.get(selected_index)
        self.referring_provder_npi_display_label.setText(refer_provider_option)

    def on_save_changes_pushButton_clinical_summary_clicked(self):
        app_date_and_time = self.clinical_summary_appt_date_and_time_dateTimeEdit.text()

        add_weight = self.add_weight_doubleSpinBox.value()
        add_height_ft = self.add_height_ft_spinBox.value()
        add_height_inches = self.add_height_inches_doubleSpinBox.value()
        chief_complaint = self.clinical_summary_chief_complaint_textEdit.toPlainText()

        smoking = False
        if self.smoking_yes_radioButton.isChecked():
            smoking = True

        drinking = False
        if self.drinking_yes_radioButton.isChecked():
            drinking = True

        exercise = False
        if self.exercise_yes_radioButton.isChecked():
            exercise = True

        drugs = False
        if self.drugs_yes_radioButton.isChecked():
            drugs = True

        appointment_type = ""
        if self.appointment_type_comboBox.currentIndex() == 0:
            appointment_type = "wellness check up"
        elif self.appointment_type_comboBox.currentIndex() == 1:
            appointment_type = "follow up"
        elif self.appointment_type_comboBox.currentIndex() == 2:
            appointment_type = "sick visit"
        elif self.appointment_type_comboBox.currentIndex() == 3:
            appointment_type = "injury"
        else:
            print("Error, please make a selection.")

        assessment = self.care_plan_assessment_textEdit.toPlainText()
        planning = self.care_plan_planning_textEdit.toPlainText()
        diagnosis = self.clinical_summary_diagnosis_textEdit.toPlainText()
        post_evaluation = self.care_plan_post_evaluation_textEdit.toPlainText()
        diagnosis_date_added = datetime.datetime.now()
        frequency_amount = self.care_plan_frequency_amount_spinBox.value()
        end_date = self.care_plan_end_date_dateEdit.date()

        frequency_type = ""
        if self.care_plan_frequency_type_comboBox.currentIndex() == 0:
            frequency_type = "Per Hour"
        elif self.care_plan_frequency_type_comboBox.currentIndex() == 1:
            frequency_type = "Per Day"
        elif self.care_plan_frequency_type_comboBox.currentIndex() == 2:
            frequency_type = "Per Week"
        elif self.care_plan_frequency_type_comboBox.currentIndex() == 3:
            frequency_type = "Per Month"
        elif self.care_plan_frequency_type_comboBox.currentIndex() == 4:
            frequency_type = "Per Year"
        elif self.care_plan_frequency_type_comboBox.currentIndex() == 5:
            frequency_type = "Occasionally"
        else:
            pass

        physician_notes = self.clinical_summary_physician_notes_textEdit.toPlainText()
        notes_date_added = datetime.datetime.now()

        primary_provider = self.primary_provider_comboBox.currentIndex()
        appointment_provider = self.appointment_provider_display_label.text()
        appointment_nurse = self.appointment_nurse_display_label.text()
        appointment_cna = self.appointment_cna_display_label.text()

        temperature = self.clinical_summary_temperature_doubleSpinBox.value()
        blood_pressure_sbp = self.blood_pressure_sbp_lineEdit.text()
        blood_pressure_dbp = self.blood_pressure_dbp_lineEdit.text()
        pulse_rate = self.pulse_rate_lineEdit.text()
        respiration_rate = self.respiration_rate_lineEdit.text()
        blood_ox_levels = self.blood_ox_levels_lineEdit.text()

        current_app_info = AppointmentTimeAndDate.AppointmentTimeAndDate(app_date_and_time)
        current_general_info = General.General(add_weight, add_height_ft, add_height_inches, smoking, drinking, exercise, drugs, appointment_type, chief_complaint)
        current_care_plan_info = CarePlan.CarePlan(assessment, planning, diagnosis, post_evaluation, diagnosis_date_added, frequency_amount, frequency_type, end_date)
        current_physician_notes = PhysicianNotes.PhysicianNotes(physician_notes, notes_date_added)
        current_app_staff_info = AppointmentStaff.AppointmentStaff(primary_provider, appointment_provider, appointment_nurse, appointment_cna)
        current_vitals_info = Vitals.Vitals(temperature, blood_pressure_sbp, blood_pressure_dbp, pulse_rate, respiration_rate, blood_ox_levels)

        # summary -----------------------------------------------------------------
        medical_record_num = self.mrn_display_label_clinical_summary.text()
        # update appointment
        conn = db_access.connect()
        query = f"UPDATE MRAppointment " \
                f"SET AppointmentTimeAndDate = '{current_app_info.get_appointment_time_and_date()}' " \
                f"WHERE MRN = {medical_record_num}"

        with db_access.closing(conn.cursor()) as c:
            c.execute(query)
            conn.commit()

        # update cheif complaint
        conn = db_access.connect()
        query = f"UPDATE MRGeneral " \
                f"SET ChiefComplaint = '{current_general_info.get_chief_complaint()}'" \
                f"WHERE MRN = {medical_record_num}"

        with db_access.closing(conn.cursor()) as c:
            c.execute(query)
            conn.commit()

        # update diagnosis
        conn = db_access.connect()
        query = f"UPDATE MRCarePlan " \
                f"SET Diagnosis = '{current_care_plan_info.get_diagnosis()}' " \
                f"WHERE MRN = {medical_record_num}"

        with db_access.closing(conn.cursor()) as c:
            c.execute(query)
            conn.commit()

        # update physician notes
        conn = db_access.connect()
        query = f"UPDATE MRPhysicianNotes " \
                f"SET Notes = '{current_physician_notes.get_notes()}' " \
                f"WHERE MRN = {medical_record_num}"

        with db_access.closing(conn.cursor()) as c:
            c.execute(query)
            conn.commit()

        # update vitals
        conn = db_access.connect()
        query = f"UPDATE MRVitals " \
                f"SET Temperature = '{current_vitals_info.get_temperature()}', SystolicBloodPressure = '{current_vitals_info.get_systolic_blood_pressure()}', " \
                f"    DiastolicBloodPressure = '{current_vitals_info.get_diastolic_blood_pressure()}', RespirationRate = '{current_vitals_info.get_respiration_rate()}', " \
                f"    PulseRate = '{current_vitals_info.get_pulse_rate()}', BloodOxygenLevels = '{current_vitals_info.get_blood_oxygen_levels()}' " \
                f"WHERE MRN = {medical_record_num}"

        with db_access.closing(conn.cursor()) as c:
            c.execute(query)
            conn.commit()


        # ----------------------------------------------------------------------


        msg_box = QMessageBox()
        msg_box.setWindowTitle("Save Successful")
        msg_box.setText("Changes have been saved.")
        msg_box.exec_()

    # ------------------------------------------------------------------------------------------------------------------

    # Functions to get data from database
    def get_patient_demo_information_from_db(self, mrn):
        """
        # Comment out if database is active
        patient_data = {'medical_record_number': "202301", 'first_name': "John", 'middle_name': "John",
                        'last_name': "Doe",
                        'gender': "Male", 'date_of_birth': "2015-01-01", 'social_security_num': "123-45-6789",
                        'suffix': "Jr",
                        'phone_num': "000-000-0000", 'ethnicity': "Other", 'marital_status': "Single",
                        'email': "example@example.com",
                        'deceased': False, 'date_of_death': ""}

        patient_info = Demographics.Demographics(first_name=patient_data['first_name'],
                                                 last_name=patient_data['last_name'],
                                                 gender=patient_data['gender'],
                                                 medical_record_num=patient_data['medical_record_number'],
                                                 date_of_birth=patient_data['date_of_birth'],
                                                 social_security_num=patient_data['social_security_num'],
                                                 phone_num=patient_data['phone_num'],
                                                 ethnicity=patient_data['ethnicity'],
                                                 marital_status=patient_data['marital_status'],
                                                 middle_name=patient_data['middle_name'],
                                                 suffix=patient_data['suffix'],
                                                 email=patient_data['email'],
                                                 deceased=patient_data['deceased'],
                                                 date_of_death=patient_data['date_of_death'])
                                                 """
        patient_info = db_access.get_patient_demographics(mrn)
        return patient_info

    def get_patient_address_info_from_db(self, mrn):
        """
        # Comment out if database is active
        address_data = {'street_address': "123 Example Street", 'city': "Winston Salem", 'state': "North Carolina",
                        'zip_code': "27103", 'apt_num': "",
                        'billing_same_as_res': True, 'guarantor_same_as_res': True}

        patient_address_info = Address.Address(street_address=address_data['street_address'],
                                               city=address_data['city'],
                                               state=address_data['state'],
                                               zip_code=address_data['zip_code'],
                                               apt_num=address_data['apt_num'],
                                               billing_same_as_res=address_data['billing_same_as_res'],
                                               guarantor_same_as_res=address_data['guarantor_same_as_res'])
        """
        patient_address_info = db_access.get_address(mrn)
        return patient_address_info

    def get_billing_address_info_from_db(self, mrn):
        """
        # Comment out if database is active
        address_data = {'street_address': "456 Example 2 Street", 'city': "Winston Salem", 'state': "North Carolina",
                        'zip_code': "27103", 'apt_num': ""}

        billing_address_info = Address.Address(street_address=address_data['street_address'],
                                               city=address_data['city'],
                                               state=address_data['state'],
                                               zip_code=address_data['zip_code'],
                                               apt_num=address_data['apt_num'])
                                               """
        billing_address_info = db_access.get_address(mrn)
        return billing_address_info

    def get_guarantor_address_info_from_db(self, mrn):
        """
        # Comment out if database is active
        address_data = {'street_address': "789 Example 3 Street", 'city': "Winston Salem", 'state': "North Carolina",
                        'zip_code': "27103", 'apt_num': ""}

        guarantor_address_info = Address.Address(street_address=address_data['street_address'],
                                                 city=address_data['city'],
                                                 state=address_data['state'],
                                                 zip_code=address_data['zip_code'],
                                                 apt_num=address_data['apt_num'])
                                                 """
        guarantor_address_info = db_access.get_address(mrn)
        return guarantor_address_info

    def get_guarantor_info_from_db(self, mrn):
        """
        # Comment out if database is active
        guarantor_data = {'first_name': "Jane", 'middle_name': "Jane-Middle", 'last_name': "Doe", 'gender': "Female", 'relationship': "Mother",
                          'phone_num': "111-111-1111"}

        guarantor_info = Guarantor.Guarantor(first_name=guarantor_data['first_name'],
                                             middle_name=guarantor_data['middle_name'],
                                             last_name=guarantor_data['last_name'],
                                             gender=guarantor_data['gender'],
                                             relationship=guarantor_data['relationship'],
                                             phone_num=guarantor_data['phone_num'])
                                             """
        guarantor_info = db_access.get_guarantor(mrn)
        return guarantor_info

    def get_emergency_contact_info_1_from_db(self, mrn):
        """
        # Comment out if database is active
        contact_data = {'first_name': "Mickey", 'last_name': "Mouse", 'gender': "Male", 'relationship': "Grandfather",
                        'phone_num': "222-222-2222", 'email_address': "mickeym@example.com"}

        emergency_contact_info_1 = EmergencyContact.EmergencyContact(first_name=contact_data['first_name'],
                                                                     last_name=contact_data['last_name'],
                                                                     gender=contact_data['gender'],
                                                                     relationship=contact_data['relationship'],
                                                                     phone_num=contact_data['phone_num'],
                                                                     email_address=contact_data['email_address'])
                                                                     """
        emergency_contact_info = db_access.get_emergency_contacts(mrn)
        emergency_contact_info_1 = emergency_contact_info[0]
        return emergency_contact_info_1

    def get_emergency_contact_info_2_from_db(self, mrn):
        """
        # Comment out if database is active

        contact_data = {'first_name': "Minnie", 'last_name': "Mouse", 'gender': "Female", 'relationship': "Grandmother",
                        'phone_num': "222-222-2222", 'email_address': "minniem@example.com"}

        emergency_contact_info_2 = EmergencyContact.EmergencyContact(first_name=contact_data['first_name'],
                                                                     last_name=contact_data['last_name'],
                                                                     gender=contact_data['gender'],
                                                                     relationship=contact_data['relationship'],
                                                                     phone_num=contact_data['phone_num'],
                                                                     email_address=contact_data['email_address'])
                                                                     """
        emergency_contact_info = db_access.get_emergency_contacts(mrn)
        emergency_contact_info_2 = emergency_contact_info[1]
        return emergency_contact_info_2

    def get_emergency_contact_info_3_from_db(self, mrn):
        """        
        # Comment out if database is active
        contact_data = {'first_name': "Donald", 'last_name': "Duck", 'gender': "Male", 'relationship': "Other",
                        'phone_num': "333-333-3333", 'email_address': "donaldd@example.com"}

        emergency_contact_info_3 = EmergencyContact.EmergencyContact(first_name=contact_data['first_name'],
                                                                     last_name=contact_data['last_name'],
                                                                     gender=contact_data['gender'],
                                                                     relationship=contact_data['relationship'],
                                                                     phone_num=contact_data['phone_num'],
                                                                     email_address=contact_data['email_address'])
                                                                     """
        emergency_contact_info = db_access.get_emergency_contacts(mrn)
        emergency_contact_info_3 = emergency_contact_info[2]
        return emergency_contact_info_3

    def get_siblings_from_database(self, patient_info):
        mrn = patient_info.get_medical_record_num()
        """
        # Comment out if database is active
        sibling_data = {'first_name': "Goofy", 'last_name': "Doe", 'gender': "Male", 'medical_record_num': "202302"}

        sibling_info = Sibling.Sibling(first_name=sibling_data['first_name'],
                                       last_name=sibling_data['last_name'],
                                       gender=sibling_data['gender'],
                                       medical_record_num=sibling_data['medical_record_num'])
                                       """
        sibling_info = db_access.get_siblings(mrn)
        return sibling_info

    def get_general_info_from_db(self, mrn):
        """
        # Comment out if database is active
        general_data = {'weight': 70.0, 'height_ft': 4, 'height_in': 2, 'smoking': False, 'drinking': False,
                        'exercise': True, 'drugs': False, 'appointment_type': "Sick Visit",
                        'chief_complaint': "Upset stomach"}

        general_info = General.General(weight=general_data['weight'],
                                       height_ft=general_data['height_ft'],
                                       height_in=general_data['height_in'],
                                       smoking=general_data['smoking'],
                                       drinking=general_data['drinking'],
                                       exercise=general_data['exercise'],
                                       drugs=general_data['drugs'],
                                       appointment_type=general_data['appointment_type'],
                                       chief_complaint=general_data['chief_complaint'])
                                       """
        general_info = db_access.get_general(mrn)
        return general_info

    def get_allergy_info_from_db(self, mrn):
        """        
        # Comment out if database is active
        allergy_data = {'allergy_name': "Bees, ", 'allergy_type': "Environmental", 'date_added': "01/01/2022"}

        allergy_info = Allergy.Allergy(allergy_name=allergy_data['allergy_name'],
                                       allergy_type=allergy_data['allergy_type'],
                                       date_added=allergy_data['date_added'])
                                       """
        allergy_info = db_access.get_allergies(mrn)
        return allergy_info

    def get_medication_info_from_db(self, mrn):
        """
        # Comment out if database is active
        medication_data = {'medication_name': "Tylenol", 'dose_amount': "12.5", 'dose_type': "mg", 'frequency': "2.00",
                           'frequency_type': "Per Day", 'medication_type': "Over the counter"}

        medication_info = Medication.Medication(medication_name=medication_data['medication_name'],
                                                dose_amount=medication_data['dose_amount'],
                                                dose_type=medication_data['dose_type'],
                                                frequency=medication_data['frequency'],
                                                frequency_type=medication_data['frequency_type'],
                                                medication_type=medication_data['medication_type'])
                                                """
        medication_info = db_access.get_medication_info(mrn)
        return medication_info

    def get_appointment_info_from_db(self, mrn):
        """
        # Comment out if database is active
        appointment_data = {'appointment_time_and_date': "04/01/2023 08:00 AM", 'status': False}

        appointment_info = AppointmentTimeAndDate.AppointmentTimeAndDate(
            appointment_time_and_date=appointment_data['appointment_time_and_date'],
            status=appointment_data['status'])
            """
        appointment_info = db_access.get_appointments(mrn)
        return appointment_info

    def get_office_location_info_from_db(self, app_id):
        """
        # Comment out if database is active
        office_location_data = {'office_name': "Mount Airy", 'office_address': "321 Example"}

        office_location_info = OfficeLocations.OfficeLocations(office_name=office_location_data['office_name'],
                                                               office_address=office_location_data['office_address'])
                                                               """
        office_location_info = db_access.get_appointment_location(app_id)
        return office_location_info

    def get_appointment_staff_info_from_db(self, app_id):
        """
        # Comment out if database is active
        appointment_staff_data = {'primary_provider': "Example Provider", 'appointment_provider': "Example Provider",
                                  'appointment_nurse': "Example Nurse", 'appointment_cna': "Example CNA"}

        appointment_staff_info = AppointmentStaff.AppointmentStaff(
            primary_provider=appointment_staff_data['primary_provider'],
            appointment_provider=appointment_staff_data['appointment_provider'],
            appointment_nurse=appointment_staff_data['appointment_nurse'],
            appointment_cna=appointment_staff_data['appointment_cna'])
            """
        appointment_staff_info = db_access.get_appointment_staff(app_id)
        return appointment_staff_info

    def get_vitals_info_from_db(self, mrn):
        """
        # Comment out if database is active
        vitals_data = {'temperature': 100.0, 'systolic_blood_pressure': "120", 'diastolic_blood_pressure': "85",
                       'respiration_rate': "22", 'pulse_rate': "95", 'blood_oxygen_levels': "97"}

        vitals_info = Vitals.Vitals(temperature=vitals_data['temperature'],
                                    systolic_blood_pressure=vitals_data['systolic_blood_pressure'],
                                    diastolic_blood_pressure=vitals_data['diastolic_blood_pressure'],
                                    respiration_rate=vitals_data['respiration_rate'],
                                    pulse_rate=vitals_data['pulse_rate'],
                                    blood_oxygen_levels=vitals_data['blood_oxygen_levels'])
                                    """
        vitals_info = db_access.get_vitals(mrn)
        return vitals_info

    def get_physician_notes_info_from_db(self, mrn):
        """
        # Comment out if database is active
        physician_notes_data = {'notes': "Test Notes", 'date_added': "04/01/2023"}

        physician_notes_info = PhysicianNotes.PhysicianNotes(notes=physician_notes_data['notes'],
                                                             date_added=physician_notes_data['date_added'])
                                                             """
        physician_notes_info = db_access.get_physician_notes(mrn)
        return physician_notes_info

    def get_procedures_performed_info_from_db(self, mrn):
        """
        # Comment out if database is active
        procedures_performed_data = {'procedure': "EKG"}

        procedures_performed_info = ProceduresPerformed.ProceduresPerformed(
            procedure=procedures_performed_data['procedure'])
            """
        procedures_performed_info = db_access.get_procedures_performed(mrn)
        return procedures_performed_info

    def get_follow_up_info_from_db(self, mrn):
        """
        # Comment out if database is active
        follow_up_data = {'needed': "True", 'follow_up_frequency': "1", 'follow_up_frequency_type': "Week(s)"}

        follow_up_info = FollowUp.FollowUp(needed=follow_up_data['needed'],
                                           follow_up_frequency=follow_up_data['follow_up_frequency'],
                                           follow_up_frequency_type=follow_up_data['follow_up_frequency_type'])
                                           """
        follow_up_info = db_access.get_follow_up(mrn)
        return follow_up_info

    def get_medical_history_info_from_db(self, mrn):
        """
        # Comment out if database is active
        medical_history_data = {'diagnosis': "Anemia", 'history_type': "patient"}

        medical_history_info = MedicalHistory.MedicalHistory(diagnosis=medical_history_data['diagnosis'],
                                                             history_type=medical_history_data['history_type'])
                                                             """
        medical_history_info = db_access.get_medical_history(mrn)
        return medical_history_info

    def get_injury_history_info_from_db(self, mrn):
        """
        # Comment out if database is active
        injury_history_data = {'description': "Broken Arm", 'date_occurred': "01/01/2020"}

        injury_history_info = InjuryHistory.InjuryHistory(description=injury_history_data['description'],
                                                          date_occurred=injury_history_data['date_occurred'])
                                                          """
        injury_history_info = db_access.get_injury_history(mrn)
        return injury_history_info

    def get_surgery_history_info_from_db(self, mrn):
        """
        # Comment out if database is active
        surgery_history_data = {'description': "Fix broken arm", 'date_occurred': "01/05/2020"}

        surgery_history_info = SurgicalHistory.SurgeryHistory(description=surgery_history_data['description'],
                                                              date_occurred=surgery_history_data['date_occurred'])
                                                              """
        surgery_history_info = db_access.get_surgery_history(mrn)
        return surgery_history_info

    def get_lab_info_from_db(self, mrn):
        """
        # Comment out if database is active
        lab_data = {'lab_type': "Basic Metabolic Panel (BMP0),", 'date_requested': "04/01/2023", 'status': "pending"}

        lab_info = Labs.Labs(lab_type=lab_data['lab_type'],
                             date_requested=lab_data['date_requested'],
                             status=lab_data['status'])
                             """
        lab_info = db_access.get_labs(mrn)
        return lab_info

    def get_care_plan_info_from_db(self, mrn):
        """
        # Comment out if database is active
        care_plan_data = {'assessment': "Test assessment", 'planning': "Test planning", 'diagnosis': "Test diagnosis",

                          'post_evaluation': "Test post evaluation", 'date_added': "04/01/2023",
                          'frequency': 1, 'frequency_type': "Per Month", 'end_date': "01/01/2024"}

        care_plan_info = CarePlan.CarePlan(assessment=care_plan_data['assessment'],
                                           planning=care_plan_data['planning'],
                                           diagnosis=care_plan_data['diagnosis'],
                                           post_evaluation=care_plan_data['post_evaluation'],
                                           date_added=care_plan_data['date_added'],
                                           frequency=care_plan_data['frequency'],
                                           frequency_type=care_plan_data['frequency_type'],
                                           end_date=care_plan_data['end_date'])
                                           """
        care_plan_info = db_access.get_care_plan(mrn)
        return care_plan_info

    def get_referral_info_from_db(self, mrn):
        """        
        # Comment out if database is active

        referral_data = {'referral_num': "111111", 'referral_reason': "Second Opinion",
                         'referral_provider': "Example Provider",
                         'provider_npi': "123456789", 'referral_date': "04/01/2023",
                         'referral_expiration_date': "05/01/2023", 'patient_condition': "Stable", 'status': "pending"}

        referral_info = Referrals.Referrals(referral_num=referral_data['referral_num'],
                                            referral_reason=referral_data['referral_reason'],
                                            referral_provider=referral_data['referral_provider'],
                                            provider_npi=referral_data['provider_npi'],
                                            referral_date=referral_data['referral_date'],
                                            referral_expiration_date=referral_data['referral_expiration_date'],
                                            patient_condition=referral_data['patient_condition'],
                                            status=referral_data['status'])
                                            """
        referral_info = db_access.get_referral_info(mrn)
        return referral_info

    def get_medical_record_audit_info_from_db(self, mrn):
        """
        # Comment out if database is active

        medical_record_audit_data = {'field_changed': "Physician Notes", 'employee_id': "987654",
                                     'first_name': "Gandalf",
                                     'last_name': "The Grey", 'date_changed': "02/01/2023"}

        medical_record_audit_info = MedicalRecordAuditLog.MedicalRecordAuditLog(
            field_changed=medical_record_audit_data['field_changed'],
            employee_id=medical_record_audit_data['employee_id'],
            first_name=medical_record_audit_data['first_name'],
            last_name=medical_record_audit_data['last_name'],
            date_changed=medical_record_audit_data['date_changed'])
            """

        medical_record_audit_info = db_access.get_medical_record_audits(mrn)
        return medical_record_audit_info

    # -------------------------------------------------------------------------------------------------------------------

    def calculate_age(self, date_of_birth):
        today = datetime.date.today()
        if isinstance(date_of_birth, str):
            date_of_birth = datetime.datetime.strptime(date_of_birth, '%Y-%m-%d').date()
        age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
        return str(age)

    # -------------------------------------------------------------------------------------------------------------------

    # set Patient Information fields before window is initialized (displays on every tab)
    def set_patient_info_to_display(self, patient_info):
        self.map_patient_info_on_demographics_tab(patient_info)
        self.map_patient_info_on_emergency_contacts_tab(patient_info)
        self.map_patient_info_on_general_tab(patient_info)
        self.map_patient_info_on_allergies_tab(patient_info)
        self.map_patient_info_on_medications_tab(patient_info)
        self.map_patient_info_on_exam_assessments_tab(patient_info)
        self.map_patient_info_on_medical_history_tab(patient_info)
        self.map_patient_info_on_injury_and_surgery_history_tab(patient_info)
        self.map_patient_info_on_labs_tab(patient_info)
        self.map_patient_info_on_care_plan_tab(patient_info)
        self.map_patient_info_on_referrals_tab(patient_info)
        self.map_patient_info_on_clinical_summary_tab(patient_info)
        self.map_patient_info_on_medical_record_history_tab(patient_info)

    def map_patient_info_on_demographics_tab(self, patient_info):
        # self.patient_photo_entry_label_demographics =
        self.mrn_display_label_demographics.setText(str(patient_info.get_medical_record_num()))
        self.first_name_display_label_demographics.setText(patient_info.get_first_name())
        self.middle_name_display_label_demographics.setText(str(patient_info.get_middle_name()))
        self.last_name_display_label_demographics.setText(patient_info.get_last_name())
        self.suffix_display_label_demographics.setText(patient_info.get_suffix())
        self.dob_display_label_demographics.setText(str(patient_info.get_date_of_birth()))
        self.age_display_label_demographics.setText(str(self.calculate_age(patient_info.get_date_of_birth())))
        self.gender_display_label_demographics.setText(patient_info.get_gender())
        self.ethnicity_display_label_demographics.setText(patient_info.get_ethnicity())
        self.ssn_display_label_demographics.setText(patient_info.get_social_security_num())

    def map_patient_info_on_emergency_contacts_tab(self, patient_info):
        # self.patient_photo_entry_label_emergency_contacts
        self.mrn_display_label_emergency_contacts.setText(str(patient_info.get_medical_record_num()))
        self.first_name_display_label_emergency_contacts.setText(patient_info.get_first_name())
        self.middle_name_display_label_emergency_contacts.setText(str(patient_info.get_middle_name()))
        self.last_name_display_label_emergency_contacts.setText(patient_info.get_last_name())
        self.suffix_display_label_emergency_contacts.setText(patient_info.get_suffix())
        self.dob_display_label_emergency_contacts.setText(str(patient_info.get_date_of_birth()))
        self.age_display_label_emergency_contacts.setText(str(self.calculate_age(patient_info.get_date_of_birth())))
        self.gender_display_label_emergency_contacts.setText(patient_info.get_gender())
        self.ethnicity_display_label_emergency_contacts.setText(patient_info.get_ethnicity())
        self.ssn_display_label_emergency_contacts.setText(patient_info.get_social_security_num())

    def map_patient_info_on_general_tab(self, patient_info):
        # self.patient_photo_entry_label_general
        self.mrn_display_label_general.setText(str(patient_info.get_medical_record_num()))
        self.first_name_display_label_general.setText(patient_info.get_first_name())
        self.middle_name_display_label_general.setText(str(patient_info.get_middle_name()))
        self.last_name_display_label_general.setText(patient_info.get_last_name())
        self.suffix_display_label_general.setText(patient_info.get_suffix())
        self.dob_display_label_general.setText(str(patient_info.get_date_of_birth()))
        self.age_display_label_general.setText(str(self.calculate_age(patient_info.get_date_of_birth())))
        self.gender_display_label_general.setText(patient_info.get_gender())
        self.ethnicity_display_label_general.setText(patient_info.get_ethnicity())
        self.ssn_display_label_general.setText(patient_info.get_social_security_num())

    def map_patient_info_on_allergies_tab(self, patient_info):
        # self.patient_photo_entry_label_allergies
        self.mrn_display_label_allergies.setText(str(patient_info.get_medical_record_num()))
        self.first_name_display_label_allergies.setText(patient_info.get_first_name())
        self.middle_name_display_label_allergies.setText(str(patient_info.get_middle_name()))
        self.last_name_display_label_allergies.setText(patient_info.get_last_name())
        self.suffix_display_label_allergies.setText(patient_info.get_suffix())
        self.dob_display_label_allergies.setText(str(patient_info.get_date_of_birth()))
        self.age_display_label_allergies.setText(str(self.calculate_age(patient_info.get_date_of_birth())))
        self.gender_display_label_allergies.setText(patient_info.get_gender())
        self.ethnicity_display_label_allergies.setText(patient_info.get_ethnicity())
        self.ssn_display_label_allergies.setText(patient_info.get_social_security_num())

    def map_patient_info_on_medications_tab(self, patient_info):
        # self.patient_photo_entry_label_medications
        self.mrn_display_label_medications.setText(str(patient_info.get_medical_record_num()))
        self.first_name_display_label_medications.setText(patient_info.get_first_name())
        self.middle_name_display_label_medications.setText(patient_info.get_middle_name())
        self.last_name_display_label_medications.setText(patient_info.get_last_name())
        self.suffix_display_label_medications.setText(patient_info.get_suffix())
        self.dob_display_label_medications.setText(str(patient_info.get_date_of_birth()))
        self.age_display_label_medications.setText(str(self.calculate_age(patient_info.get_date_of_birth())))
        self.gender_display_label_medications.setText(patient_info.get_gender())
        self.ethnicity_display_label_medications.setText(patient_info.get_ethnicity())
        self.ssn_display_label_medications.setText(patient_info.get_social_security_num())

    def map_patient_info_on_exam_assessments_tab(self, patient_info):
        # self.patient_photo_entry_label_exam_assessments
        self.mrn_display_label_exam_assessments.setText(str(patient_info.get_medical_record_num()))
        self.first_name_display_label_exam_assessments.setText(patient_info.get_first_name())
        self.middle_name_display_label_exam_assessments.setText(patient_info.get_middle_name())
        self.last_name_display_label_exam_assessments.setText(patient_info.get_last_name())
        self.suffix_display_label_exam_assessments.setText(patient_info.get_suffix())
        self.dob_display_label_exam_assessments.setText(str(patient_info.get_date_of_birth()))
        self.age_display_label_exam_assessments.setText(str(self.calculate_age(patient_info.get_date_of_birth())))
        self.gender_display_label_exam_assessments.setText(patient_info.get_gender())
        self.ethnicity_display_label_exam_assessments.setText(patient_info.get_ethnicity())
        self.ssn_display_label_exam_assessments.setText(patient_info.get_social_security_num())

    def map_patient_info_on_medical_history_tab(self, patient_info):
        # self.patient_photo_entry_label_medical_history
        self.mrn_display_label_medical_history.setText(str(patient_info.get_medical_record_num()))
        self.first_name_display_label_medical_history.setText(patient_info.get_first_name())
        self.middle_name_display_label_medical_history.setText(patient_info.get_middle_name())
        self.last_name_display_label_medical_history.setText(patient_info.get_last_name())
        self.suffix_display_label_medical_history.setText(patient_info.get_suffix())
        self.dob_display_label_medical_history.setText(str(patient_info.get_date_of_birth()))
        self.age_display_label_medical_history.setText(str(self.calculate_age(patient_info.get_date_of_birth())))
        self.gender_display_label_medical_history.setText(patient_info.get_gender())
        self.ethnicity_display_label_medical_history.setText(patient_info.get_ethnicity())
        self.ssn_display_label_medical_history.setText(patient_info.get_social_security_num())

    def map_patient_info_on_injury_and_surgery_history_tab(self, patient_info):
        # self.patient_photo_entry_label_injury_surgery_hist
        self.mrn_display_label_injury_surgery_hist.setText(str(patient_info.get_medical_record_num()))
        self.first_name_display_label_injury_surgery_hist.setText(patient_info.get_first_name())
        self.middle_name_display_label_injury_surgery_hist.setText(patient_info.get_middle_name())
        self.last_name_display_label_injury_surgery_hist.setText(patient_info.get_last_name())
        self.suffix_display_label_injury_surgery_hist.setText(patient_info.get_suffix())
        self.dob_display_label_injury_surgery_hist.setText(str(patient_info.get_date_of_birth()))
        self.age_display_label_injury_surgery_hist.setText(str(self.calculate_age(patient_info.get_date_of_birth())))
        self.gender_display_label_injury_surgery_hist.setText(patient_info.get_gender())
        self.ethnicity_display_label_injury_surgery_hist.setText(patient_info.get_ethnicity())
        self.ssn_display_label_injury_surgery_hist.setText(patient_info.get_social_security_num())

    def map_patient_info_on_labs_tab(self, patient_info):
        # self.patient_photo_entry_label_labs
        self.mrn_display_label_labs.setText(str(patient_info.get_medical_record_num()))
        self.first_name_display_label_labs.setText(patient_info.get_first_name())
        self.middle_name_display_label_labs.setText(patient_info.get_middle_name())
        self.last_name_display_label_labs.setText(patient_info.get_last_name())
        self.suffix_display_label_labs.setText(patient_info.get_suffix())
        self.dob_display_label_labs.setText(str(patient_info.get_date_of_birth()))
        self.age_display_label_labs.setText(str(self.calculate_age(patient_info.get_date_of_birth())))
        self.gender_display_label_labs.setText(patient_info.get_gender())
        self.ethnicity_display_label_labs.setText(patient_info.get_ethnicity())
        self.ssn_display_label_labs.setText(patient_info.get_social_security_num())

    def map_patient_info_on_care_plan_tab(self, patient_info):
        # self.patient_photo_entry_label_care_plan
        self.mrn_display_label_care_plan.setText(str(patient_info.get_medical_record_num()))
        self.first_name_display_label_care_plan.setText(patient_info.get_first_name())
        self.middle_name_display_label_care_plan.setText(patient_info.get_middle_name())
        self.last_name_display_label_care_plan.setText(patient_info.get_last_name())
        self.suffix_display_label_care_plan.setText(patient_info.get_suffix())
        self.dob_display_label_care_plan.setText(str(patient_info.get_date_of_birth()))
        self.age_display_label_care_plan.setText(str(self.calculate_age(patient_info.get_date_of_birth())))
        self.gender_display_label_care_plan.setText(patient_info.get_gender())
        self.ethnicity_display_label_care_plan.setText(patient_info.get_ethnicity())
        self.ssn_display_label_care_plan.setText(patient_info.get_social_security_num())

    def map_patient_info_on_referrals_tab(self, patient_info):
        # self.patient_photo_entry_label_referrals
        self.mrn_display_label_referrals.setText(str(patient_info.get_medical_record_num()))
        self.first_name_display_label_referrals.setText(patient_info.get_first_name())
        self.middle_name_display_label_referrals.setText(patient_info.get_middle_name())
        self.last_name_display_label_referrals.setText(patient_info.get_last_name())
        self.suffix_display_label_referrals.setText(patient_info.get_suffix())
        self.dob_display_label_referrals.setText(str(patient_info.get_date_of_birth()))
        self.age_display_label_referrals.setText(str(self.calculate_age(patient_info.get_date_of_birth())))
        self.gender_display_label_referrals.setText(patient_info.get_gender())
        self.ethnicity_display_label_referrals.setText(patient_info.get_ethnicity())
        self.ssn_display_label_referrals.setText(patient_info.get_social_security_num())

    def map_patient_info_on_clinical_summary_tab(self, patient_info):
        # self.patient_photo_entry_label_clinical_summary
        self.mrn_display_label_clinical_summary.setText(str(patient_info.get_medical_record_num()))
        self.first_name_display_label_clinical_summary.setText(patient_info.get_first_name())
        self.middle_name_display_label_clinical_summary.setText(patient_info.get_middle_name())
        self.last_name_display_label_clinical_summary.setText(patient_info.get_last_name())
        self.suffix_display_label_clinical_summary.setText(patient_info.get_suffix())
        self.dob_display_label_clinical_summary.setText(str(patient_info.get_date_of_birth()))
        self.age_display_label_clinical_summary.setText(str(self.calculate_age(patient_info.get_date_of_birth())))
        self.gender_display_label_clinical_summary.setText(patient_info.get_gender())
        self.ethnicity_display_label_clinical_summary.setText(patient_info.get_ethnicity())
        self.ssn_display_label_clinical_summary.setText(patient_info.get_social_security_num())

    def map_patient_info_on_medical_record_history_tab(self, patient_info):
        # self.patient_photo_entry_label_medical_record_history
        self.mrn_display_label_medical_record_history.setText(str(patient_info.get_medical_record_num()))
        self.first_name_display_label_medical_record_history.setText(patient_info.get_first_name())
        self.middle_name_display_label_medical_record_history.setText(patient_info.get_middle_name())
        self.last_name_display_label_medical_record_history.setText(patient_info.get_last_name())
        self.suffix_display_label_medical_record_history.setText(patient_info.get_suffix())
        self.dob_display_label_medical_record_history.setText(str(patient_info.get_date_of_birth()))
        self.age_display_label_medical_record_history.setText(str(self.calculate_age(patient_info.get_date_of_birth())))
        self.gender_display_label_medical_record_history.setText(patient_info.get_gender())
        self.ethnicity_display_label_medical_record_history.setText(patient_info.get_ethnicity())
        self.ssn_display_label_medical_record_history.setText(patient_info.get_social_security_num())

    # -------------------------------------------------------------------------------------------------------------------

    # Set Demographics tab fields before window is initialized
    def set_demographics_tab_fields(self, patient_info, patient_address_info, billing_address_info,
                                    guarantor_address_info,
                                    guarantor_info, logged_in_user):
        self.first_name_lineEdit.setText(patient_info.get_first_name())
        self.middle_name_lineEdit.setText(patient_info.get_middle_name())
        self.last_name_lineEdit.setText(patient_info.get_last_name())
        self.set_suffix_radio_buttons(patient_info)
        self.dob_lineEdit.setText(str(patient_info.get_date_of_birth()))
        self.set_gender_radio_buttons(patient_info)
        self.ethnicity_comboBox.setCurrentText(patient_info.get_ethnicity())
        self.ssn_lineEdit.setText(patient_info.get_social_security_num())
        self.phone_number_lineEdit.setText(patient_info.get_phone_num())
        self.email_address_lineEdit.setText(patient_info.get_email())
        self.marital_status_comboBox.setCurrentText(patient_info.get_marital_status())
        if patient_info.get_deceased():
            self.deceased_checkBox.select()
            self.date_of_death_lineEdit.get_date_of_death()
        self.res_street_address_lineEdit.setText(patient_address_info.get_street_address())
        self.res_apt_lineEdit.setText(patient_address_info.get_apt_num())
        self.res_city_lineEdit.setText(patient_address_info.get_city())
        self.res_state_comboBox.setCurrentText(patient_address_info.get_state())
        self.res_zipcode_lineEdit.setText(patient_address_info.get_zip_code())

        if patient_address_info.get_billing_same_as_res():
            self.billing_street_address_lineEdit.setText(patient_address_info.get_street_address())
            self.billing_apt_lineEdit.setText(patient_address_info.get_apt_num())
            self.billing_city_lineEdit.setText(patient_address_info.get_city())
            self.billing_state_comboBox.setCurrentText(patient_address_info.get_state())
            self.billing_zipcode_lineEdit.setText(patient_address_info.get_zip_code())
            self.billing_same_as_res_address_checkBox.setChecked(True)
        else:
            self.billing_street_address_lineEdit.setText(billing_address_info.get_street_address())
            self.billing_apt_lineEdit.setText(billing_address_info.get_apt_num())
            self.billing_city_lineEdit.setText(billing_address_info.get_city())
            self.billing_state_comboBox.setCurrentText(billing_address_info.get_state())
            self.billing_zipcode_lineEdit.setText(billing_address_info.get_zip_code())
        self.guarantor_first_name_lineEdit.setText(guarantor_info.get_first_name())
        self.middle_name_lineEdit_2.setText(guarantor_info.get_middle_name())
        self.guarantor_last_name_lineEdit.setText(guarantor_info.get_last_name())
        self.set_guarantor_gender_radio_buttons(guarantor_info)
        self.guarantor_relationship_comboBox.setCurrentText(guarantor_info.get_relationship())
        self.phone_number_lineEdit_2.setText(guarantor_info.get_phone_num())
        if patient_address_info.get_guarantor_same_as_res():
            self.guarantor_same_as_patient_address_checkBox.setChecked(True)
            self.guarantor_street_address_lineEdit.setText(patient_address_info.get_street_address())
            self.guarantor_apt_lineEdit.setText(patient_address_info.get_apt_num())
            self.guarantor_city_lineEdit.setText(patient_address_info.get_city())
            self.guarantor_state_comboBox.setCurrentText(patient_address_info.get_state())
            self.guarantor_zip_code_lineEdit.setText(patient_address_info.get_zip_code())
        else:
            self.guarantor_street_address_lineEdit.setText(guarantor_address_info.get_street_address())
            self.guarantor_apt_lineEdit.setText(guarantor_address_info.get_apt_num())
            self.guarantor_city_lineEdit.setText(guarantor_address_info.get_city())
            self.guarantor_state_comboBox.setCurrentText(guarantor_address_info.get_state())
            self.guarantor_zip_code_lineEdit.setText(guarantor_address_info.get_zip_code())
            if self.sibling_at_practice_checkBox.isChecked():
                mrn = str(self.mrn_display_label_demographics.text())
                sibling_info = db_access.get_siblings(mrn)
                for sibling in sibling_info:
                    self.sibling_listView.addItem(f"{sibling.get_first_name()} {sibling.get_last_name()}, "
                                                f"{sibling.get_medical_record_num()}")
            else:
                pass

        # user object created from login window
        self.logged_in_user_display_label_demographics.setText(self.current_user)

    # -------------------------------------------------------------------------------------------------------------------

    # Set Emergency Contacts tab fields before window is initialized
    def set_emergency_contacts_tab_fields(self, emergency_contact_info_1, emergency_contact_info_2,
                                          emergency_contact_info_3, logged_in_user):
        self.emerg_1_first_name_lineEdit.setText(emergency_contact_info_1.get_first_name())
        self.emerg_1_last_name_lineEdit.setText(emergency_contact_info_1.get_last_name())
        self.emerg_1_phone_number_lineEdit.setText(emergency_contact_info_1.get_phone_num())
        self.emerg_1_email_address_lineEdit.setText(emergency_contact_info_1.get_email_address())
        self.emerg_1_relationship_comboBox.setCurrentText(emergency_contact_info_1.get_relationship())
        self.emerg_2_first_name_lineEdit.setText(emergency_contact_info_2.get_first_name())
        self.emerg_2_last_name_lineEdit.setText(emergency_contact_info_2.get_last_name())
        self.emerg_2_phone_number_lineEdit.setText(emergency_contact_info_2.get_phone_num())
        self.emerg_2_email_address_lineEdit.setText(emergency_contact_info_2.get_email_address())
        self.emerg_2_relationship_comboBox.setCurrentText(emergency_contact_info_2.get_relationship())
        self.emerg_3_first_name_lineEdit.setText(emergency_contact_info_3.get_first_name())
        self.emerg_3_last_name_lineEdit.setText(emergency_contact_info_3.get_last_name())
        self.emerg_3_phone_number_lineEdit.setText(emergency_contact_info_3.get_phone_num())
        self.emerg_3_email_address_lineEdit.setText(emergency_contact_info_3.get_email_address())
        self.emerg_3_relationship_comboBox.setCurrentText(emergency_contact_info_3.get_relationship())
        self.logged_in_user_display_label_emergency_contacts.setText(self.current_user)

    # -------------------------------------------------------------------------------------------------------------------

    # Set General tab fields before window is initialized
    def set_general_tab_fields(self, general_info, logged_in_user):
        self.add_weight_doubleSpinBox.setValue(general_info.get_weight())
        self.add_height_ft_spinBox.setValue(general_info.get_height_ft())
        self.add_height_inches_doubleSpinBox.setValue(general_info.get_height_in())

        if general_info.get_smoking():
            self.smoking_yes_radioButton.setChecked(True)
        else:
            self.smoking_no_radioButton.setChecked(True)

        if general_info.get_drinking():
            self.drinking_yes_radioButton.setChecked(True)
        else:
            self.drinking_no_radioButton.setChecked(True)

        if general_info.get_exercise():
            self.exercise_yes_radioButton.setChecked(True)
        else:
            self.exercise_no_radioButton.setChecked(True)

        if general_info.get_drugs():
            self.drugs_yes_radioButton.setChecked(True)
        else:
            self.drugs_no_radioButton.setChecked(True)

        self.appointment_type_comboBox.setCurrentText(general_info.get_appointment_type())
        self.chief_complaint_textEdit.setText(general_info.get_chief_complaint())
        self.logged_in_user_display_label_general.setText(self.current_user)

    # -------------------------------------------------------------------------------------------------------------------

    # Set Allergies tab fields before window is initialized
    def set_allergy_tab_fields(self, allergy_info, logged_in_user):
        for allergy in allergy_info:
            if allergy.get_allergy_type() == "environmental":
                self.environmental_allergy_listView.addItem(f"{allergy.get_allergy_name()}, "
                                                            f"{allergy.get_date_added()}")
            else:
                self.medication_allergy_listView.addItem(f"{allergy.get_allergy_name()}, "
                                                        f"{allergy.get_date_added()}")
        self.logged_in_user_display_label_allergies.setText(self.current_user)

    # -------------------------------------------------------------------------------------------------------------------

    # Set Medications tab fields before window is initialized

    def set_medication_tab_fields(self, medication_info, logged_in_user):
        for medication in medication_info:
            if medication.get_medication_type().lower() == "prescription":
                self.prescription_listView.addItem(f"{medication.get_medication_name()}, "
                                                   f"{medication.get_dose_amount()} {medication.get_dose_type()}, "
                                                   f"{medication.get_frequency()} {medication.get_frequency_type()}")
                self.add_medication_lineEdit.setText("")
            elif medication.get_medication_type().lower() == "over the counter":
                self.over_the_counter_listView.addItem(f"{medication.get_medication_name()}, "
                                                       f"{medication.get_dose_amount()} {medication.get_dose_type()}, "
                                                       f"{medication.get_frequency()} {medication.get_frequency_type()}")
                self.add_medication_lineEdit.setText("")
            elif medication.get_medication_type().lower() == "herbal":
                self.herbal_listView.addItem(f"{medication.get_medication_name()}, "
                                             f"{medication.get_dose_amount()} {medication.get_dose_type()}, "
                                             f"{medication.get_frequency()} {medication.get_frequency_type()}")
                self.add_medication_lineEdit.setText("")
        self.logged_in_user_display_label_medications.setText(self.current_user)

    # -------------------------------------------------------------------------------------------------------------------

    # Set Exam Assessments tab fields before window is initialized

    def set_exam_assessments_tab_fields(self, appointment_info, office_location_info, appointment_staff_info,
                                        vitals_info, physician_notes_info, procedures_performed_info,
                                        follow_up_info, logged_in_user):
        appt_time_str = appointment_info.get_appointment_time_and_date()
        appt_format = "MM/dd/yyyy hh:mm AP"
        appt_time = QDateTime.fromString(appt_time_str, appt_format)
        # appt_time = QDateTime.currentDateTime()
        self.appointment_dateTimeEdit.setDateTime(appt_time)

        appointment_info.set_status(True)
        self.office_location_comboBox.setCurrentText(office_location_info.get_office_name())
        self.primary_provider_comboBox.setCurrentText(appointment_staff_info.get_primary_provider())
        self.appointment_provider_comboBox.setCurrentText(appointment_staff_info.get_appointment_provider())
        self.appointment_nurse_comboBox.setCurrentText(appointment_staff_info.get_appointment_nurse())
        self.appointment_cna_comboBox.setCurrentText(appointment_staff_info.get_appointment_cna())
        self.exam_assessments_temperature_doubleSpinBox.setValue(float(vitals_info.get_temperature()))
        self.blood_pressure_sbp_lineEdit_exam_assessment.setText(vitals_info.get_systolic_blood_pressure())
        self.blood_pressure_dbp_lineEdit_exam_assessment.setText(vitals_info.get_diastolic_blood_pressure())
        self.pulse_rate_lineEdit_exam_assessment.setText(vitals_info.get_pulse_rate())
        self.respiration_rate_lineEdit_exam_assessment.setText(vitals_info.get_respiration_rate())
        self.blood_ox_levels_lineEdit_exam_assessment.setText(vitals_info.get_blood_oxygen_levels())
        self.physicaion_notes_textEdit_exam_assessment.setText(physician_notes_info.get_notes())

        for procedure in procedures_performed_info:
            self.procedure_list_listView.addItem(procedure.get_procedure())

        if follow_up_info.get_needed() == "yes":
            self.follow_up_needed_yes_radioButton.setChecked(True)
            self.follow_up_in_frequency_spinBox.setValue(int(follow_up_info.get_follow_up_frequency()))
            self.follow_up_frequency_type_comboBox.setCurrentText(follow_up_info.get_follow_up_frequency_type())
        else:
            self.follow_up_needed_no_radioButton.setChecked(True)
        self.logged_in_user_display_label_exam_assessments.setText(self.current_user)
    # -------------------------------------------------------------------------------------------------------------------
    def set_office_location_for_create_new_appointment(self, selected_location):
        self.office_location_comboBox.setCurrentText(selected_location)

    # -------------------------------------------------------------------------------------------------------------------
    def set_office_location_for_create_new_appointment(self, selected_location):
        self.office_location_comboBox.setCurrentText(selected_location)

    # Set Medical History tab fields before window is initialized
    def set_medical_history_tab_fields(self, medical_history_info, logged_in_user):
        for history in medical_history_info:
            if history.get_history_type() == "patient":
                self.patient_history_listView.addItem(history.get_diagnosis())
            elif history.get_history_type() == "mother":
                self.patient_mothers_history_listView.addItem(history.get_diagnosis())
            else:
                self.patient_fathers_history_listView.addItem(history.get_diagnosis())
        self.logged_in_user_display_label_medical_history.setText(self.current_user)

    # -------------------------------------------------------------------------------------------------------------------

    # Set Injury and Surgical History tab fields before window is initialized
    def set_injury_and_surgical_history_tab_fields(self, injury_history_info, surgery_history_info, logged_in_user):
        for injury in injury_history_info:
            self.injury_history_listView.addItem(f"{injury.get_description()}, "
                                                 f"{injury.get_date_occurred()}")
        for surgery in surgery_history_info:
            self.surgery_history_listView.addItem(f"{surgery.get_description()}, "
                                                  f"{surgery.get_date_occurred()}")
        self.logged_in_user_display_label_injury_surgery_hist.setText(self.current_user)

    # -------------------------------------------------------------------------------------------------------------------

    # Set Labs tab fields before window is initialized
    def set_labs_tab_fields(self, lab_info, logged_in_user):
        for lab in lab_info:
            if lab.get_status() == "pending":
                self.pending_labs_listView.addItem(f"{lab.get_lab_type()}, {lab.get_date_requested()}")
            else:
                lab.get_status() == "completed"
                self.completed_labs_listView.addItem(f"{lab.get_lab_type()}, {lab.get_date_requested()}")
        self.logged_in_user_display_label_labs.setText(self.current_user)

    # -------------------------------------------------------------------------------------------------------------------

    # Set Care Plan tab fields before window is initialized
    def set_care_plan_tab_fields(self, care_plan_info, logged_in_user):
        self.care_plan_assessment_textEdit.setText(care_plan_info.get_assessment())
        self.care_plan_planning_textEdit.setText(care_plan_info.get_planning())
        self.care_plan_diagnosis_textEdit.setText(care_plan_info.get_diagnosis())
        self.care_plan_post_evaluation_textEdit.setText(care_plan_info.get_post_evaluation())
        self.care_plan_frequency_amount_spinBox.setValue(int(care_plan_info.get_frequency()))
        self.care_plan_frequency_type_comboBox.setCurrentText(care_plan_info.get_frequency_type())
        care_plan_end_date_str = care_plan_info.get_end_date()
        care_plan_end_date = QDate.fromString(care_plan_end_date_str, "M/d/yyyy")
        self.care_plan_end_date_dateEdit.setDate(care_plan_end_date)
        self.logged_in_user_display_label_care_plan.setText(self.current_user)

    # -------------------------------------------------------------------------------------------------------------------

    # Set Referrals tab fields before window is initialized
    def set_referrals_tab_fields(self, referral_info, logged_in_user):
        selected_index = self.referring_provider_comboBox.currentIndex()
        refer_provider_option = refer_provider_options.get(selected_index)
        self.referring_provder_npi_display_label.setText(refer_provider_option)
        counter = 0
        for referral in referral_info:
            if counter == 0:
                referral_num = referral.get_referral_num() + 1
                self.referral_number_display_label.setText(str(referral_num))
            if referral.get_status() == "pending":
                self.pending_referrals_listView.addItem(f"{referral.get_referral_num()}, "
                                                        f"{referral.get_referral_reason()}")
            else:
                self.completed_referrals_listView.addItem(f"{referral.get_referral_num()}, "
                                                          f"{referral.get_referral_reason()}")
        self.logged_in_user_display_label_referrals.setText(self.current_user)

    # -------------------------------------------------------------------------------------------------------------------

    # Set Clinical Summary tab fields before window is initialized

    def set_clinical_summary_tab_fields(self, appointment_info, general_info, care_plan_info, physician_notes_info,
                                        appointment_staff_info, vitals_info, logged_in_user):
        clinical_summary_appt_date_and_time_str = appointment_info.get_appointment_time_and_date()
        appt_format = "MM/dd/yyyy hh:mm AP"
        clinical_summary_appt_date_and_time = QDateTime.fromString(clinical_summary_appt_date_and_time_str, appt_format)
        self.clinical_summary_appt_date_and_time_dateTimeEdit.setDateTime(clinical_summary_appt_date_and_time)


        self.clinical_summary_chief_complaint_textEdit.setText(general_info.get_chief_complaint())
        self.clinical_summary_diagnosis_textEdit.setText(care_plan_info.get_diagnosis())
        self.clinical_summary_physician_notes_textEdit.setText(physician_notes_info.get_notes())
        self.appointment_provider_display_label.setText(appointment_staff_info.get_appointment_provider())
        self.appointment_nurse_display_label.setText(appointment_staff_info.get_appointment_nurse())
        self.appointment_cna_display_label.setText(appointment_staff_info.get_appointment_cna())
        self.clinical_summary_temperature_doubleSpinBox.setValue(float(vitals_info.get_temperature()))
        self.blood_pressure_sbp_lineEdit.setText(vitals_info.get_systolic_blood_pressure())
        self.blood_pressure_dbp_lineEdit.setText(vitals_info.get_diastolic_blood_pressure())
        self.pulse_rate_lineEdit.setText(vitals_info.get_pulse_rate())
        self.respiration_rate_lineEdit.setText(vitals_info.get_respiration_rate())
        self.blood_ox_levels_lineEdit.setText(vitals_info.get_blood_oxygen_levels())
        self.logged_in_user_display_label_clinical_summary.setText(self.current_user)

    # -------------------------------------------------------------------------------------------------------------------

    # Set Medical Record History tab fields before window is initialized
    def set_medical_record_history_tab_fields(self, medical_record_audit_info, logged_in_user):
        for medical_record_audit in medical_record_audit_info:
            self.medical_record_history_listView.addItem(f"{medical_record_audit.get_field_changed()}, "
                                                         f"{medical_record_audit.get_date_changed()}, "
                                                         f"{medical_record_audit.get_first_name()} "
                                                         f"{medical_record_audit.get_last_name()},"
                                                         f"{medical_record_audit.get_employee_id()}")
        self.logged_in_user_display_label_clinical_summary.setText(self.current_user)

    # -------------------------------------------------------------------------------------------------------------------
    # Set logged in user for each tab - these are for when the create new appointment button is clicked from Open Patient Menu
    def set_logged_in_user_for_create_new_appointment(self, logged_in_user):
        print("In set_logged_in_user_for_create_new_appointment")
        self.logged_in_user_display_label_general.setText(self.current_user)
        self.logged_in_user_display_label_allergies.setText(self.current_user)
        self.logged_in_user_display_label_medications.setText(self.current_user)
        self.logged_in_user_display_label_exam_assessments.setText(self.current_user)
        self.logged_in_user_display_label_medical_history.setText(self.current_user)
        self.logged_in_user_display_label_injury_surgery_hist.setText(self.current_user)
        self.logged_in_user_display_label_labs.setText(self.current_user)
        self.logged_in_user_display_label_care_plan.setText(self.current_user)
        self.logged_in_user_display_label_referrals.setText(self.current_user)
        self.logged_in_user_display_label_clinical_summary.setText(self.current_user)
        # self.logged_in_user_display_label_medical_record_history.setText(self.current_user)

    # -------------------------------------------------------------------------------------------------------------------

    # set Demographics tab radio buttons
    def set_suffix_radio_buttons(self, patient_info):
        match patient_info.get_suffix():
            case "Jr":
                self.jr_radioButton.setChecked(True)
                return
            case "Sr":
                self.sr_radioButton.setChecked(True)
                return
            case "I":
                self.I_radioButton.setChecked(True)
                return
            case "II":
                self.II_radioButton.setChecked(True)
                return
            case "III":
                self.III_radioButton.setChecked(True)
                return
            case "na":
                self.na_radioButton.setChecked(True)

    def set_gender_radio_buttons(self, patient_info):
        match patient_info.get_gender():
            case "Male":
                self.male_radioButton.setChecked(True)
                return
            case "Female":
                self.female_radioButton.setChecked(True)
                return
            case "Other":
                self.sex_other_radioButton.setChecked(True)

    def set_guarantor_gender_radio_buttons(self, guarantor_info):
        match guarantor_info.get_gender():
            case "Male":
                self.guarantor_male_radioButton.setChecked(True)
                return
            case "Female":
                self.guarantor_female_radioButton.setChecked(True)
                return
            case "Other":
                self.guarantor_sex_other_radioButton.setChecked(True)


# Medical History Tab Dictionary for Combo Boxes

medical_history_options = {
    0: 'Abnormal Pap smear',
    1: 'Anemia',
    2: 'Angina',
    3: 'Anxiety',
    4: 'Asthma',
    5: 'Black stools',
    6: 'Bleeding between periods',
    7: 'Blood clots',
    8: 'Blood in stools',
    9: 'Blood in urine',
    10: 'Cancer - Bladder',
    11: 'Cancer - Breast',
    12: 'Cancer - Bronchus',
    13: 'Cancer - Colon',
    14: 'Cancer - Endometrial',
    15: 'Cancer - Kidney',
    16: 'Cancer - Leukemia',
    17: 'Cancer - Liver',
    18: 'Cancer - Lung',
    19: 'Cancer - Melanoma of the skin',
    20: 'Cancer - Non-Hodgkin lymphoma',
    21: 'Cancer - Pancreatic',
    22: 'Cancer - Prostate',
    23: 'Cancer - Rectum',
    24: 'Cancer - Renal pelvis',
    25: 'Cancer - Thyroid',
    26: 'Cataracts',
    27: 'Chest pain',
    28: 'Colitis',
    29: 'Color changes of hands or feet',
    30: 'Constipation',
    31: 'Cough',
    32: 'Crohn’s disease',
    33: 'Depression',
    34: 'Diabetes',
    35: 'Difficulties with sexual arousal',
    36: 'Difficulty falling asleep',
    37: 'Difficulty staying asleep',
    38: 'Difficulty swallowing',
    39: 'Double or blurred vision',
    40: 'Emphysema',
    41: 'Epilepsy (seizures)',
    42: 'Excessive worries',
    43: 'Eye dryness',
    44: 'Eye pain',
    45: 'Eye redness',
    46: 'Fainting or loss of consciousness',
    47: 'Fatigue',
    48: 'Fever',
    49: 'Food cravings',
    50: 'Frequent crying',
    51: 'Frequent or painful urination',
    52: 'Frequent sore throats',
    53: 'Goiter',
    54: 'Guilty thoughts',
    55: 'Hair loss',
    56: 'Hallucinations',
    57: 'Headaches',
    58: 'Heart murmur',
    59: 'Heart palpitations',
    60: 'Heart problems',
    61: 'Heartburn',
    62: 'Hepatitis',
    63: 'High blood pressure',
    64: 'High cholesterol',
    65: 'HIV/AIDS',
    66: 'Hoarseness',
    67: 'Hypothyroidism',
    68: 'Irregular periods',
    69: 'Irritability',
    70: 'Jaundice',
    71: 'Joint pain',
    72: 'Joint swelling',
    73: 'Kidney disease',
    74: 'Kidney stones',
    75: 'Leukemia',
    76: 'Loss of hearing',
    77: 'Loss of vision',
    78: 'Memory loss',
    79: 'Mood swings',
    80: 'Muscle weakness',
    81: 'Nausea',
    82: 'Night sweats',
    83: 'Nodules/bumps',
    84: 'Numbness or tingling',
    85: 'Pain in jaw',
    86: 'Paranoia',
    87: 'Persistent diarrhea',
    88: 'PMS',
    89: 'Pneumonia',
    90: 'Poor appetite',
    91: 'Poor concentration',
    92: 'Psoriasis',
    93: 'Pulmonary embolism',
    94: 'Racing thoughts',
    95: 'Rapid speech',
    96: 'Rash',
    97: 'Rheumatic fever',
    98: 'Ringing in ears',
    99: 'Risky behavior',
    100: 'Sensitivity',
    101: 'Shortness of breath',
    102: 'Skin redness',
    103: 'Stomach or peptic ulcer',
    104: 'Stomach pain',
    105: 'Stress',
    106: 'Stroke',
    107: 'Swollen legs or feet',
    108: 'Thoughts of suicide / attempts',
    109: 'Tuberculosis',
    110: 'Vomiting',
    111: 'Weakness'}

order_labs_options = {
    0: 'Activated Partial Thromboplastin Time (PTT)',
    1: 'Basic Metabolic Panel (BMP)',
    2: 'Blood Urea Nitrogen (BUN)',
    3: 'Complete Blood Count (CBC)',
    4: 'Comprehensive Metabolic Panel (CMP)',
    5: 'Creatinine',
    6: 'Lipid Profile',
    7: 'Prothrombin Time (PT) with INR',
    8: 'Thyroid Test',
    9: 'Urinalysis (UA)',
    10: 'White Blood Cell (WBC) Differential'}

referral_reason_options = {
    0: 'Allergy and Immunology',
    1: 'Anesthesiology',
    2: 'Dermatology',
    3: 'Diagnostic Radiology',
    4: 'Higher level of care',
    5: 'Internal Medicine',
    6: 'Medical Genetics',
    7: 'Neurology',
    8: 'Nuclear Medicine',
    9: 'Obstetrics/Gynecology',
    10: 'Ophthalmology',
    11: 'Physical Medicine/Rehabilitation',
    12: 'Pathology',
    13: 'Psychiatry',
    14: 'Radiation Oncology',
    15: 'Second Opinion',
    16: 'Surgery',
    17: 'Urology'}

refer_provider_options = {
    0: 'List of Provider Names'
}

state_options = {
    0: 'Alabama',
    1: 'Alaska',
    2: 'Arizona',
    3: 'Arkansas',
    4: 'California',
    5: 'Colorado',
    6: 'Connecticut',
    7: 'Delaware',
    8: 'Florida',
    9: 'Georgia',
    10: 'Hawaii',
    11: 'Idaho',
    12: 'Illinois',
    13: 'Indiana',
    14: 'Iowa',
    15: 'Kansas',
    16: 'Kentucky',
    17: 'Louisiana',
    18: 'Maine',
    19: 'Maryland',
    20: 'Massachusetts',
    21: 'Michigan',
    22: 'Minnesota',
    23: 'Mississippi',
    24: 'Missouri',
    25: 'Montana',
    26: 'Nebraska',
    27: 'Nevada',
    28: 'New Hampshire',
    29: 'New Jersey',
    30: 'New Mexico',
    31: 'New York',
    32: 'North Carolina',
    33: 'North Dakota',
    34: 'Ohio',
    35: 'Oklahoma',
    36: 'Oregon',
    37: 'Pennsylvania',
    38: 'Rhode Island',
    39: 'South Carolina',
    40: 'South Dakota',
    41: 'Tennessee',
    42: 'Texas',
    43: 'Utah',
    44: 'Vermont',
    45: 'Virginia',
    46: 'Washington',
    47: 'West Virginia',
    48: 'Wisconsin',
    49: 'Wyoming'
}

provider_options = {
    0: 'Alexis Chole',
    1: 'Barnie Sanders',
    2: 'Blanchett Cate',
    3: 'Bryson Walker',
    4: 'Butch Cassidy',
    5: 'Christopher Jenkins',
    6: 'Cole Brown',
    7: 'Ferb Jackson',
    8: 'Jake Cooper',
    9: 'Justin Rose',
    10: 'Kaitlan Collins',
    11: 'Kate Baldwin',
    12: 'Kelly Rowland',
    13: 'Morpheus Mattix',
    14: 'Olivia Benson',
    15: 'Pamela James',
    16: 'Patrick Cantalay',
    17: 'Robert Kelly',
    18: 'Tamar Braxton',
    19: 'Taylor Swift',
    20: 'Terry Maholmes',
    21: 'Tommy Strong',
    22: 'Travis Scott',
    23: 'Usher Raymond',
    24: 'Xander Chole'
}

refer_provider_options = {
    0: '3915460047',
    1: '8213891451',
    2: '6073522871',
    3: '9571198122',
    4: '5135212156',
    5: '6906696513',
    6: '3737024315',
    7: '9954404707',
    8: '6503742895',
    9: '8847029643',
    10: '7261846482',
    11: '2407955101',
    12: '7315916832',
    13: '9349251529',
    14: '1288732654',
    15: '8935617944',
    16: '9332986135',
    17: '7153929085',
    18: '2049599214',
    19: '8079542081',
    20: '9679086709',
    21: '7475405665',
    22: '4552088206',
    23: '8331932125',
    24: '5417829756',
}
