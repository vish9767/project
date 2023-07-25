from django.db import models
from django_enumfield import enum
from rest_framework import status
from datetime import date

from django.utils import timezone
import datetime
from django.contrib.auth.models import(
	BaseUserManager,AbstractBaseUser
)
# Create your models here.

class enquiry_from_enum(enum.Enum):
	website = 1
	application = 2
	consultant = 3
	__default__ = website

class active_inactive_enum(enum.Enum):
    Active=1
    Inactive=2

class Treatmet_Type_enum(enum.Enum):
	Sergery = 1
	Medicine = 2
	__default__ = Sergery

class status_enum(enum.Enum):
	Active = 1
	Inactive = 2
	Delete = 3

class level(enum.Enum):
    Primary = 0
    Secondary = 1
	
class yes_no_enum(enum.Enum):
	yes = 1
	no = 2

class last_modified_by_enum(enum.Enum):
	System = 1
	App = 2

class Session_status_enum(enum.Enum):
	Pending = 1
	Completed = 2
	Upcoming =3
	No_show_by_Patient = 4
	No_show_by_Professional = 5
	Closed = 6
	Enroute = 7
	Started_Session = 8
	Completed_Session = 9

class Reason_for_no_serivce_enum(enum.Enum):
	Session_added = 1
	Patient_Hospitalized = 2
	Patient_Death =3
	Other = 4

class enquiry_status_enum(enum.Enum):
	Enquiry_received = 1
	Called_back = 2
	Confirm =3
	Cancel = 4

class discount_type_enum(enum.Enum):
	In_Percentage = 1
	In_amount = 2
	No_discount = 3
	__default__ = No_discount

   
class estimate_cost_enum(enum.Enum):
	not_set = 1
	No = 2
	Yes =3

class Payment_type_enum(enum.Enum):
	Offline = 1
	Online = 2

class types_enum(enum.Enum):
	Family_doctors = 1
	Consultant = 2

class reporting_by_enum(enum.Enum):
	SMS = 1
	Email = 2
	PhoneCall =3

class Role_id_enum(enum.Enum):
	Professional = 1
	Admin = 2

class cl_status_enum(enum.Enum):
	Incoming = 1
	Disconnect = 2

class srv_status_enum(enum.Enum):
	Confirmed = 1
	Enquiry = 2

class professional_type_enum(enum.Enum):
	Professional = 1
	Vender = 2

class flag_enum(enum.Enum):
	HD_systems = 1
	Mobile_App = 2
	__default__ = HD_systems

class Tf_enum(enum.Enum):
	HD_systems = 1
	Mobile_App = 2
	__default__ = HD_systems

class package_status_enum(enum.Enum):
	Servcie = 1
	Package = 2

class pt_gender_enum(enum.Enum):
	Male = 1
	Female = 2
	Trans_gender = 3

class reg_status_enum(enum.Enum):
	registration = 1
	Reject = 2
	Accept = 3

class reference_type_enum(enum.Enum):
	Professional = 1
	Vender = 2

class set_location_enum(enum.Enum):
	home_locatoin = 1
	work_location = 2

class document_status_enum(enum.Enum):
	Verified = 1
	need_more_details = 2
	Rejected = 3
	In_Progress = 4

class reg_source_enum(enum.Enum):
	System = 1
	App = 2

class skin_perfusion_enum(enum.Enum):
	NA = 1
	Normal = 2
	Abnormal = 3

class airway_enum(enum.Enum):
	NA = 1
	Open = 2
	Closed = 3

class breathing_enum(enum.Enum):
	NA = 1
	Present = 2
	Compromised = 3
	Absent = 4

class circulation_enum(enum.Enum):
	NA = 1
	Radial = 2
	Present = 3
	Absent = 4

class baseline_enum(enum.Enum):
	NA = 1
	A = 2
	V = 3
	P = 4
	U = 5

class consumption_type_enum(enum.Enum):
	unitmedicine = 1
	nonunitmedicine = 2
	unitconsumable = 3
	nonunitconsumble = 4

class user_type_enum(enum.Enum):
	dcm = 1
	hd = 2
	caller = 3

class option_type_enum(enum.Enum):
	Text = 1
	Radio = 2
	Checkbox = 3
	Rating = 4

class professional_types_enum(enum.Enum):
	Professional = 1
	Patient = 2

class acceptance_status_enum(enum.Enum):
	Pending = 1
	Accepted = 2
	Rejected = 3

class user_types_enum(enum.Enum):
	Professional = 1
	HD_User = 2

class payment_status_enum(enum.Enum):
	Amount_With_Profesional = 1
	Amount_paid_to_spero = 2

class Payment_mode_enum(enum.Enum):
	Offline = 1
	Online = 2

class Payment_type_enum(enum.Enum):
	Cash = 1
	Cheque = 2

class OTP_verifivation_enum(enum.Enum):
	Verified = 1
	Not_Verified = 2


class caller_status_enum(enum.Enum):
	mobile=1
	website=2
	walking=3
	calling=4

class service_status_enum(enum.Enum):
	Pending = 1
	Ongoing = 2
	Completed = 3
	terminated = 4

class agg_hhc_callers(models.Model):#113 this table is used for app register user as well as for web caller register
	caller_id=models.AutoField(primary_key=True)
	phone=models.BigIntegerField(null=True)#this will used to store otp
	otp=models.IntegerField(null=True)
	otp_expire_time=models.DateTimeField(null=True)
	fname=models.CharField(max_length=50,null=True)
	lname=models.CharField(max_length=50,null=True)
	caller_rel_id=models.ForeignKey('agg_hhc_caller_relation',on_delete=models.CASCADE,null=True)
	age=models.IntegerField(null=True)
	gender=models.CharField(max_length=20,null=True)
	email=models.EmailField(null=True)
	contact_no=models.BigIntegerField(null=True)
	alter_contact=models.BigIntegerField(null=True)
	Address=models.CharField(max_length=50,null=True)
	save_this_add=models.CharField(max_length=50,null=True)
	added_date=models.DateField(null=True,auto_now=True)
	emp_id=models.BigIntegerField(null=True)
	last_modified_by=models.BigIntegerField(null=True)
	last_modified_date=models.DateField(null=True)
	profile_pic=models.ImageField(null=True)# profile picture
	status=enum.EnumField(active_inactive_enum,null=True)
	caller_status=enum.EnumField(caller_status_enum,null=True)

	def __str__(self):
		return f"{self.caller_id}"
	
	
"""
class agg_hhc_callers(models.Model):#20
	caller_id = models.AutoField(primary_key = True)
	fullname = models.CharField(max_length=255,null=True)
	relation = models.CharField(max_length=255,null=True)
	phone_no = models.CharField(max_length=20,null=True)
	# srv_prof_id = models.BigIntegerField(null=True)
	# doc_cons_presc_id = models.BigIntegerField(null=True)
	status = enum.EnumField(status_enum,null=True)
	emp_id = models.BigIntegerField(null=True)
	added_date = models.DateField(null=True)
	last_modified_by = models.BigIntegerField(null=True)
	last_modified_date = models.DateField(null=True)"""

class agg_hhc_patinet_list_enquiry(models.Model):#1
	pt_id = models.AutoField(primary_key = True)
	consultat_id = models.BigIntegerField(null=True)
	consultat_fname = models.CharField(max_length=50,null=True)
	name = models.CharField(max_length=50,null=True)
	contact = models.CharField(max_length=20,null=True)
	call_type=models.CharField(max_length=50,null=True)
	relation = models.CharField(max_length=20,null=True)
	patient_fname = models.CharField(max_length=50,null=True)
	patient_age = models.CharField(max_length=2,null=True)
	patient_date_of_birth=models.DateField(null=True)
	patient_gender = models.CharField(max_length=20,null=True)
	suffered_from=models.CharField(max_length=200,null=True)
	hospital_name=models.CharField(max_length=150,null=True)
	patient_add = models.CharField(max_length=200,null=True)
	patient_Locality=models.CharField(max_length=250,null=True)
	google_location = models.CharField(max_length=200,null=True)
	patient_contact = models.CharField(max_length=10,null=True)
	patient_email=models.EmailField(null=True)
	# mainService = models.CharField(max_length=11,null=True)
	# sub_service = models.CharField(max_length=11,null=True)
	# Start_Date_and_Time=models.DateTimeField(null=True)
	# End_Date_and_Time=models.DateTimeField(null=True)
	# Professional_Preferred=models.CharField(max_length=100,null=True)
	# note = models.CharField(max_length=50,null=True)
	status = models.CharField(max_length=2,null=True)
	added_date = models.DateField(default=timezone.now,null=True)
	enquiry_from = enum.EnumField(enquiry_from_enum,null=True)
	
class agg_hhc_assessment_patient(models.Model):#2
	ass_pt_id = models.AutoField(primary_key = True)
	ass_pt_li_id = models.BigIntegerField(null=True)
	haemodynamics_day1ass = models.CharField(max_length=2,null=True)
	haemodynamics_day2ass = models.CharField(max_length=2,null=True)
	haemodynamics_day3ass = models.CharField(max_length=2,null=True)
	haemodynamics_day4ass = models.CharField(max_length=2,null=True)
	haemodynamics_remark = models.CharField(max_length=50,null=True)
	BP_Day1 = models.CharField(max_length=1,null=True)
	BP_Day2 = models.CharField(max_length=1,null=True)
	BP_Day3 = models.CharField(max_length=1,null=True)
	BP_Day4 = models.CharField(max_length=1,null=True)
	PULSE_Day1 = models.CharField(max_length=1,null=True)
	PULSE_Day2 = models.CharField(max_length=1,null=True)
	PULSE_Day3 = models.CharField(max_length=1,null=True)
	PULSE_Day4 = models.CharField(max_length=1,null=True)
	SPO2_Day1 = models.IntegerField(null=True)
	SPO2_Day2 = models.CharField(max_length=1,null=True)
	SPO2_Day3 = models.CharField(max_length=1,null=True)
	SPO2_Day4 = models.CharField(max_length=1,null=True)
	UO_Day1 = models.CharField(max_length=1,null=True)
	UO_Day2 = models.CharField(max_length=1,null=True)
	UO_Day3 = models.CharField(max_length=1,null=True)
	UO_Day4 = models.CharField(max_length=1,null=True)
	Temp_Day1 = models.CharField(max_length=1,null=True)
	Temp_Day2 = models.CharField(max_length=1,null=True)
	Temp_Day3 = models.CharField(max_length=1,null=True)
	Temp_Day4 = models.CharField(max_length=1,null=True)
	BSL_Day1 = models.CharField(max_length=1,null=True)
	BSL_Day2 = models.CharField(max_length=1,null=True)
	BSL_Day3 = models.CharField(max_length=1,null=True)
	BSL_Day4 = models.CharField(max_length=1,null=True)
	Total_Day1 = models.CharField(max_length=1,null=True)
	Total_Day2 = models.CharField(max_length=1,null=True)
	Total_Day3 = models.CharField(max_length=1,null=True)
	Total_Day4 = models.CharField(max_length=1,null=True)
	necessary_Invest_before_initiating_HHC = models.CharField(max_length=50,null=True)
	milestone_before_initiating_HHC = models.CharField(max_length=50,null=True)
	discharge_homecare = models.CharField(max_length=5,null=True)
	# TreatmentType = enum.EnumField(TreatmentType_enum,null=True)
	hosp_id = models.CharField(max_length=1,null=True)
	emp_id = models.CharField(max_length=1,null=True)
	# status = enum.EnumField(status_enum,null=True)
	added_date = models.DateField(default=timezone.now,null=True)
	modify_date = models.DateField(null=True)
	

class agg_hhc_assessment_patient_details(models.Model):#3
	agg_sp_ass_pt_dt_id = models.AutoField(primary_key = True)
	ass_pt_li_id = models.BigIntegerField(null=True)
	ass_pt_id = models.BigIntegerField(null=True)
	mental_day1ass = models.CharField(max_length=3,null=True)
	mental_day2ass = models.CharField(max_length=3,null=True)
	mental_day3ass = models.CharField(max_length=3,null=True)
	mental_day4ass = models.CharField(max_length=3,null=True)
	altered_consciousness_comatose_day1 = models.CharField(max_length=3,null=True)
	altered_consciousness_comatose_day2 = models.CharField(max_length=3,null=True)
	altered_consciousness_comatose_day3 = models.CharField(max_length=3,null=True)
	altered_consciousness_comatose_day4 = models.CharField(max_length=3,null=True)
	altered_consciousness_comatose_remark = models.CharField(max_length=20,null=True)
	Conscious_day1 = models.CharField(max_length=3,null=True)
	Conscious_day2 = models.CharField(max_length=3,null=True)
	Conscious_day3 = models.CharField(max_length=3,null=True)
	Conscious_day4 = models.CharField(max_length=3,null=True)
	Conscious_remark = models.CharField(max_length=20,null=True)
	ventilator_day1 = models.CharField(max_length=3,null=True)
	ventilator_day2 = models.CharField(max_length=3,null=True)
	ventilator_day3 = models.CharField(max_length=3,null=True)
	ventilator_day4 = models.CharField(max_length=3,null=True)
	ventilator_remark = models.CharField(max_length=30,null=True)
	O2_day1 = models.CharField(max_length=3,null=True)
	O2_day2 = models.CharField(max_length=3,null=True)
	O2_day3 = models.CharField(max_length=3,null=True)
	O2_day4 = models.CharField(max_length=3,null=True)
	O2_remark = models.CharField(max_length=30,null=True)
	RT_day1 = models.CharField(max_length=3,null=True)
	RT_day2 = models.CharField(max_length=3,null=True)
	RT_day3 = models.CharField(max_length=3,null=True)
	RT_day4 = models.CharField(max_length=3,null=True)
	RT_remark = models.CharField(max_length=30,null=True)
	Drain_day1 = models.CharField(max_length=3,null=True)
	Drain_day2 = models.CharField(max_length=3,null=True)
	Drain_day3 = models.CharField(max_length=3,null=True)
	Drain_day4 = models.CharField(max_length=3,null=True)
	Drain_remark = models.CharField(max_length=30,null=True)
	ICD_day1 = models.CharField(max_length=3,null=True)
	ICD_day2 = models.CharField(max_length=3,null=True)
	ICD_day3 = models.CharField(max_length=3,null=True)
	ICD_day4 = models.CharField(max_length=3,null=True)
	ICD_remark = models.CharField(max_length=30,null=True)
	Colostomy_Enterostomy_day1 = models.CharField(max_length=3,null=True)
	Colostomy_Enterostomy_day2 = models.CharField(max_length=3,null=True)
	Colostomy_Enterostomy_day3 = models.CharField(max_length=3,null=True)
	Colostomy_Enterostomy_day4 = models.CharField(max_length=3,null=True)
	Colostomy_Enterostomy_remark = models.CharField(max_length=30,null=True)
	PEG_day1 = models.CharField(max_length=3,null=True)
	PEG_day2 = models.CharField(max_length=3,null=True)
	PEG_day3 = models.CharField(max_length=3,null=True)
	PEG_day4 = models.CharField(max_length=3,null=True)
	PEG_remark = models.CharField(max_length=30,null=True)
	Dressing_day1 = models.CharField(max_length=3,null=True)
	Dressing_day2 = models.CharField(max_length=3,null=True)
	Dressing_day3 = models.CharField(max_length=3,null=True)
	Dressing_day4 = models.CharField(max_length=3,null=True)
	Dressing_remark = models.CharField(max_length=30,null=True)
	Dressing_large_day1 = models.CharField(max_length=3,null=True)
	Dressing_large_day2 = models.CharField(max_length=3,null=True)
	Dressing_large_day3 = models.CharField(max_length=3,null=True)
	Dressing_large_day4 = models.CharField(max_length=3,null=True)
	Dressing_medium_day1 = models.CharField(max_length=3,null=True)
	Dressing_medium_day2 = models.CharField(max_length=3,null=True)
	Dressing_medium_day3 = models.CharField(max_length=3,null=True)
	Dressing_medium_day4 = models.CharField(max_length=3,null=True)
	Dressing_small_day1 = models.CharField(max_length=3,null=True)
	Dressing_small_day2 = models.CharField(max_length=3,null=True)
	Dressing_small_day3 = models.CharField(max_length=3,null=True)
	Dressing_small_day4 = models.CharField(max_length=3,null=True)
	Bedsorecare_day1 = models.CharField(max_length=3,null=True)
	Bedsorecare_day2 = models.CharField(max_length=3,null=True)
	Bedsorecare_day3 = models.CharField(max_length=3,null=True)
	Bedsorecare_day4 = models.CharField(max_length=3,null=True)
	Bedsorecare_remark = models.CharField(max_length=30,null=True)
	BedsorecareLarge_day1 = models.CharField(max_length=3,null=True)
	BedsorecareLarge_day2 = models.CharField(max_length=3,null=True)
	BedsorecareLarge_day3 = models.CharField(max_length=3,null=True)
	BedsorecareLarge_day4 = models.CharField(max_length=3,null=True)
	BedsorecareMedium_day1 = models.CharField(max_length=3,null=True)
	BedsorecareMedium_day2 = models.CharField(max_length=3,null=True)
	BedsorecareMedium_day3 = models.CharField(max_length=3,null=True)
	BedsorecareMedium_day4 = models.CharField(max_length=3,null=True)
	Bedsorecaresmall_day1 = models.CharField(max_length=3,null=True)
	Bedsorecaresmall_day2 = models.CharField(max_length=3,null=True)
	Bedsorecaresmall_day3 = models.CharField(max_length=3,null=True)
	Bedsorecaresmall_day4 = models.CharField(max_length=3,null=True)
	Sutures_day1 = models.CharField(max_length=3,null=True)
	Sutures_day2 = models.CharField(max_length=3,null=True)
	Sutures_day3 = models.CharField(max_length=3,null=True)
	Sutures_day4 = models.CharField(max_length=3,null=True)
	Sutures_remark = models.CharField(max_length=30,null=True)
	Catheter_day1 = models.CharField(max_length=3,null=True)
	Catheter_day2 = models.CharField(max_length=3,null=True)
	Catheter_day3 = models.CharField(max_length=3,null=True)
	Catheter_day4 = models.CharField(max_length=3,null=True)
	Catheter_remark = models.CharField(max_length=30,null=True)
	Enema_day1 = models.CharField(max_length=3,null=True)
	Enema_day2 = models.CharField(max_length=3,null=True)
	Enema_day3 = models.CharField(max_length=3,null=True)
	Enema_day4 = models.CharField(max_length=3,null=True)
	Enema_remark = models.CharField(max_length=30,null=True)
	IV_Injections_day1 = models.CharField(max_length=3,null=True)
	IV_Injections_day2 = models.CharField(max_length=3,null=True)
	IV_Injections_day3 = models.CharField(max_length=3,null=True)
	IV_Injections_day4 = models.CharField(max_length=3,null=True)
	IV_Injections_remark = models.CharField(max_length=30,null=True)
	IM_Injections_day1 = models.CharField(max_length=3,null=True)
	IM_Injections_day2 = models.CharField(max_length=3,null=True)
	IM_Injections_day3 = models.CharField(max_length=3,null=True)
	IM_Injections_day4 = models.CharField(max_length=3,null=True)
	IM_Injections_remark = models.CharField(max_length=30,null=True)
	SC_Injections_day1 = models.CharField(max_length=3,null=True)
	SC_Injections_day2 = models.CharField(max_length=3,null=True)
	SC_Injections_day3 = models.CharField(max_length=3,null=True)
	SC_Injections_day4 = models.CharField(max_length=3,null=True)
	SC_Injections_remark = models.CharField(max_length=30,null=True)
	Intracath_day1 = models.CharField(max_length=3,null=True)
	Intracath_day2 = models.IntegerField(null=True)
	Intracath_day3 = models.IntegerField(null=True)
	Intracath_day4 = models.IntegerField(null=True)
	Intracath_remark = models.BigIntegerField(null=True)
	Tracheostomy_caresuction_day1 = models.IntegerField(null=True)
	Tracheostomy_caresuction_day2 = models.IntegerField(null=True)
	Tracheostomy_caresuction_day3 = models.IntegerField(null=True)
	Tracheostomy_caresuction_day4 = models.IntegerField(null=True)
	Tracheostomy_caresuction_remark = models.BigIntegerField(null=True)
	Nebulization_day1 = models.IntegerField(null=True)
	Nebulization_day2 = models.IntegerField(null=True)
	Nebulization_day3 = models.IntegerField(null=True)
	Nebulization_day4 = models.IntegerField(null=True)
	Nebulization_remark = models.BigIntegerField(null=True)
	Investigations_day1 = models.CharField(max_length=3,null=True)
	Investigations_day2 = models.CharField(max_length=3,null=True)
	Investigations_day3 = models.CharField(max_length=3,null=True)
	Investigations_day4 = models.CharField(max_length=3,null=True)
	InvestigationsEcg_day1 = models.CharField(max_length=3,null=True)
	InvestigationsEcg_day2 = models.CharField(max_length=3,null=True)
	InvestigationsEcg_day3 = models.CharField(max_length=3,null=True)
	InvestigationsEcg_day4 = models.CharField(max_length=3,null=True)
	InvestigationsEcg_remark = models.CharField(max_length=3,null=True)
	InvestigationsChestXray_day1 = models.CharField(max_length=3,null=True)
	InvestigationsChestXray_day2 = models.CharField(max_length=3,null=True)
	InvestigationsChestXray_day3 = models.CharField(max_length=3,null=True)
	InvestigationsChestXray_day4 = models.CharField(max_length=3,null=True)
	InvestigationsChestXray_remark = models.CharField(max_length=3,null=True)
	InvestigationsUsg_day1 = models.CharField(max_length=3,null=True)
	InvestigationsUsg_day2 = models.CharField(max_length=3,null=True)
	InvestigationsUsg_day3 = models.CharField(max_length=3,null=True)
	InvestigationsUsg_day4 = models.CharField(max_length=3,null=True)
	InvestigationsUsg_remark = models.CharField(max_length=3,null=True)
	# TreatmentType = enum.EnumField(TreatmentType_enum,null=True)
	hosp_id = models.BigIntegerField(null=True)
	emp_id = models.BigIntegerField(null=True)
	# status = enum.EnumField(status_enum,null=True)
	added_date = models.DateField(default=timezone.now,null=True)
	
class agg_hhc_assessment_patient_list(models.Model):#4
	agg_sp_ass_pt_li_id = models.AutoField(primary_key = True)
	MRD_NO = models.CharField(max_length=30,null=True)
	name = models.CharField(max_length=20,null=True)
	first_name = models.CharField(max_length=15,null=True)
	middle_name = models.CharField(max_length=15,null=True)
	relation = models.CharField(max_length=10,null=True)
	phone_no = models.CharField(max_length=10,null=True)
	patient_name = models.CharField(max_length=15,null=True)
	patient_first_name = models.CharField(max_length=15,null=True)
	patient_middle_name = models.CharField(max_length=15,null=True)
	age = models.CharField(max_length=2,null=True)
	gender = models.CharField(max_length=7,null=True)
	residential_address = models.CharField(max_length=200,null=True)
	google_location = models.CharField(max_length=200,null=True)
	patient_mobile_no = models.CharField(max_length=10,null=True)
	patient_email_id = models.CharField(max_length=20,null=True)
	hosp_id = models.CharField(max_length=11,null=True)
	srv_id = models.CharField(max_length=11,null=True)
	sub_srv_id = models.CharField(max_length=11,null=True)
	reg_no = models.CharField(max_length=20,null=True)
	admission_date = models.DateField(null=True)
	consultant_name = models.CharField(max_length=20,null=True)
	hosp_id = models.BigIntegerField(null=True)
	dept_id = models.BigIntegerField(null=True)
	Treatmet_Type = enum.EnumField(Treatmet_Type_enum,null=True)
	notes = models.CharField(max_length=50,null=True)
	CaseID = models.CharField(max_length=100,null=True)
	OPIPNo = models.CharField(max_length=100,null=True)
	country = models.CharField(max_length=50,null=True)
	State = models.CharField(max_length=50,null=True)
	city = models.CharField(max_length=50,null=True)
	area = models.CharField(max_length=100,null=True)
	pin = models.IntegerField(null=True)
	VisitAdmitTime = models.CharField(max_length=50,null=True)
	VisitType = models.CharField(max_length=50,null=True)
	DoctorLoginName = models.CharField(max_length=50,null=True)
	Discharge_Date = models.CharField(max_length=50,null=True)
	TimeofDischarge = models.CharField(max_length=50,null=True)
	DateofDeath = models.CharField(max_length=50,null=True)
	status = models.CharField(max_length=2,null=True)
	added_date = models.DateField(default=timezone.now,null=True)

class agg_hhc_patients(models.Model):#6
	agg_sp_pt_id = models.AutoField(primary_key = True)
	#app_user_id=models.ForeignKey(agg_hhc_app_caller_register,on_delete=models.CASCADE,null=True)
	caller_id=models.ForeignKey(agg_hhc_callers,on_delete=models.CASCADE,null=True)
	hhc_code = models.CharField(max_length=50,null=True, blank=True)
	membership_id = models.CharField(max_length=50,null=True)
	name = models.CharField(max_length=255,null=True)
	# first_name = models.CharField(max_length=50,null=True)
	# middle_name = models.CharField(max_length=50,null=True)
	pincode=models.PositiveIntegerField(null=True)
	Age = models.BigIntegerField(null=True)
	Gender = models.CharField(max_length=10,null=True)
	email_id = models.EmailField(null=True)
	address_type=models.CharField(max_length=100,null=True)
	residential_address = models.CharField(max_length=500,null=True)
	permanant_address = models.CharField(max_length=500,null=True)
	state=models.CharField(max_length=150,null=True)
	city_id = models.BigIntegerField(null=True)
	sub_location = models.CharField(max_length=50,null=True)
	zone_id = models.ForeignKey('agg_hhc_professional_zone',on_delete=models.CASCADE,null=True)
	otp=models.IntegerField(null=True)
	otp_expire_time=models.DateTimeField(null=True)
	google_location = models.CharField(max_length=240,null=True)
	Suffered_from=models.CharField(max_length=240,null=True)
	hospital_name=models.CharField(max_length=240,null=True)
	preferred_hosp_id=models.ForeignKey('agg_hhc_hospitals',on_delete=models.CASCADE,null=True)# updated
	phone_no = models.CharField(max_length=20,null=True)
	mobile_no = models.CharField(max_length=20,null=True)
	dob = models.DateField(null=True)
	patient_ref_name = models.CharField(max_length=50,null=True)
	status = enum.EnumField(status_enum,null=True)
	isDelStatus = models.BigIntegerField(null=True)
	isVIP = enum.EnumField(yes_no_enum,null=True)
	added_by = models.BigIntegerField(null=True)
	added_date = models.DateField(default=timezone.now,null=True)
	last_modified_by = models.BigIntegerField(null=True)
	last_modified_date = models.DateField(null=True)
	lattitude = models.FloatField(null=True)
	langitude = models.FloatField(null=True)
	Profile_pic = models.CharField(max_length=200,null=True)

	def save(self, *args, **kwargs):
		if not self.agg_sp_pt_id:
			last_pt = agg_hhc_patients.objects.order_by('-agg_sp_pt_id').first()
			prefix = self.hosp_id.hospital_short_code if self.hosp_id else None
			if not prefix:
				raise status.HTTP_404_NOT_FOUND
			last_sequence = int(last_pt.hhc_code[-4:]) + 1 if last_pt else 1
			self.hhc_code = f"{prefix}HC{last_sequence:05d}"
		return super().save(*args, **kwargs)

# class agg_hhc_webinar_patient_table(models.Model):#7
# 	agg_sp_web_pt_li_id = models.AutoField(primary_key = True)
# 	HHC_no = models.CharField(max_length=20,null=True)
# 	patient_name = models.CharField(max_length=100,null=True)
# 	Email = models.CharField(max_length=50,null=True)
# 	mob = models.CharField(max_length=15,null=True)
# 	address = models.CharField(max_length=200,null=True)
# 	date = models.DateField(null=True)
# 	status = enum.EnumField(status_enum,null=True)

class agg_hhc_detailed_event_plan_of_care(models.Model):#8
	agg_sp_dt_eve_poc_id = models.AutoField(primary_key = True)
	agg_sp_pt_id= models.ForeignKey(agg_hhc_patinet_list_enquiry, on_delete=models.CASCADE, null=True)
	eve_id = models.BigIntegerField(null=True)
	eve_req_id = models.BigIntegerField(null=True)
	index_of_Session = models.BigIntegerField(null=True)
	srv_prof_id = models.ForeignKey('agg_hhc_service_professionals', related_name='relation_id',on_delete=models.CASCADE, null=True, blank=True, default=None)
	ext_srv_id = models.CharField(max_length=11,null=True)
	service_date = models.DateField(null=True)
	service_date_to = models.DateField(null=True)
	Actual_Service_date = models.DateField(null=True)
	start_date = models.DateField(null=True)
	end_date = models.DateField(null=True)
	actual_StartDate_Time = models.DateField(null=True)
	actual_EndDate_Time = models.DateField(null=True)
	service_cost = models.FloatField(null=True)
	amount_received = models.CharField(max_length=11,null=True)
	status = enum.EnumField(status_enum,null=True)
	added_by = models.BigIntegerField(null=True)
	added_date = models.DateField(default=timezone.now,null=True)
	emp_id = models.BigIntegerField(null=True)
	last_modified_by = enum.EnumField(last_modified_by_enum,null=True)
	last_modified_date = models.DateField(null=True)
	Session_status = enum.EnumField(Session_status_enum,null=True)
	session_note = models.CharField(max_length=200,null=True)
	Reason_for_no_serivce = enum.EnumField(Reason_for_no_serivce_enum,null=True)
	Comment_for_no_serivce = models.CharField(max_length=100,null=True)
	OTP = models.CharField(max_length=4,null=True)
	OTP_count = models.BigIntegerField(null=True)
	otp_expire_time = models.DateField(null=True)
	Reschedule_count = models.BigIntegerField(null=True)
	service_status = enum.EnumField(service_status_enum, null=True)

class agg_hhc_events(models.Model):#9
	eve_id = models.AutoField(primary_key = True)
	event_code = models.CharField(max_length=640,null=True,blank=True)
	caller_id = models.ForeignKey('agg_hhc_callers',on_delete=models.CASCADE,null=True)
	# relation = models.CharField(max_length=64,null=True)
	agg_sp_pt_id= models.ForeignKey(agg_hhc_patients,on_delete=models.CASCADE, null=True)
	purp_call_id = models.BigIntegerField(null=True)
	bill_no_ref_no = models.BigIntegerField(null=True)
	event_date = models.DateTimeField(auto_now_add=True,null=True)
	note = models.CharField(max_length=500,null=True)
	service_date_of_Enquiry = models.DateField(null=True)
	enquiry_added_date = models.DateField(default=timezone.now,null=True)
	enquiry_status = enum.EnumField(enquiry_status_enum,null=True)
	enquiry_cancel_from = models.BigIntegerField(null=True)
	enquiry_cancellation_reason = models.CharField(max_length=500,null=True)
	enquiry_cancel_date = models.DateField(null=True)
	description = models.CharField(max_length=500,null=True)
	finalcost = models.CharField(max_length=240,null=True)
	discount_type = enum.EnumField(discount_type_enum,null=True)
	discount_value = models.FloatField(null=True)
	discount_amount = models.FloatField(null=True)
	status = enum.EnumField(status_enum,null=True)
	# inc_call_id = models.CharField(max_length=100,null=True)
	# event_status = enum.EnumField(event_status_enum,null=True)
	# estimate_cost = enum.EnumField(estimate_cost_enum,null=True)
	isArchive = enum.EnumField(yes_no_enum,null=True)
	isConvertedService = enum.EnumField(yes_no_enum,null=True)
	isDelStatus = models.BigIntegerField(null=True)
	added_by = models.BigIntegerField(null=True)
	# Added_through = enum.EnumField(Added_through_enum,null=True)
	Invoice_narration = models.CharField(max_length=100,null=True)
	invoice_narration_desc = models.CharField(max_length=500,null=True)
	added_date = models.DateField(default=timezone.now,null=True)
	last_modified_by = models.BigIntegerField(null=True)
	last_modified_date = models.DateField(null=True)
	# purpose_event_id = models.BigIntegerField(null=True)
	branch_code = models.CharField(max_length=50,null=True)
	hosp_id = models.BigIntegerField(null=True)
	suffer_from = models.CharField(max_length=200,null=True)
	hosp_id = models.CharField(max_length=30,null=True)
	ref_hos_nm = models.CharField(max_length=50,null=True)
	# Tally_Remark = models.BigIntegerField(null=True)
	# Payment_type = enum.EnumField(Payment_type_enum,null=True)
	OTP = models.CharField(max_length=11,null=True)
	OTP_count = models.IntegerField(null=True)
	otp_expire_time = models.DateField(null=True)
	sor_of_enq_id = models.BigIntegerField(null=True)

	def save(self, *args, **kwargs):
		if not self.eve_id:
			last_pt = agg_hhc_events.objects.order_by('-eve_id').first()
			prefix=str(date.today()).replace('-','')
			if last_pt and last_pt.event_code[:-4]==prefix:
				last_sequence = int(last_pt.event_code[-4:]) + 1  
			else:last_sequence= 1
			self.event_code = f"{prefix}{last_sequence:04d}"
			return super().save(*args, **kwargs)
	# def save(self, *args, **kwargs):
	# 	if not self.eve_id:
	# 		last_pt = agg_hhc_events.objects.order_by('-eve_id').first()
	# 		prefix = str(date.today()).replace('-', '')
	# 		if last_pt and last_pt.event_code[:-4] == prefix:
	# 			last_sequence = int(last_pt.event_code[-4:]) + 1
	# 		else:
	# 			last_sequence = 1
	# 			self.event_code = f"{prefix}{last_sequence:04d}"

    #     # Format the datetime to "yyyy-mm-dd hh:min"
	# 	if self.event_date:
	# 		formatted_date = self.event_date.strftime('%Y-%m-%d %H:%M')
	# 		self.event_date = formatted_date
	# 	return super(agg_hhc_events, self).save(*args, **kwargs)




class agg_hhc_event_consultant_call(models.Model):#10
	eve_cons_call_id = models.AutoField(primary_key = True)
	eve_id = models.BigIntegerField(null=True)
	consultant_event_id = models.BigIntegerField(null=True)
	consultant_caller_id = models.BigIntegerField(null=True)
	added_by = models.BigIntegerField(null=True)
	added_date = models.DateField(default=timezone.now,null=True)

class agg_hhc_event_doctor_mapping(models.Model):#11
	eve_doct_map_id = models.AutoField(primary_key = True)
	eve_id = models.BigIntegerField(null=True)
	pt_id = models.BigIntegerField(null=True)
	doct_cons_id = models.BigIntegerField(null=True)
	types = enum.EnumField(types_enum,null=True)
	status = enum.EnumField(status_enum,null=True)
	added_by = models.BigIntegerField(null=True)
	added_date = models.DateField(default=timezone.now,null=True)
	last_modified_by = models.BigIntegerField(null=True)
	last_modified_date = models.DateField(null=True)

class agg_hhc_event_follow_up(models.Model):#12
	eve_follow_up_id = models.AutoField(primary_key = True)
	eve_id = models.BigIntegerField(null=True)
	enq_follow_up_id = models.BigIntegerField(null=True)
	enq_follow_up_id = models.BigIntegerField(null=True)
	date = models.DateField(null=True)
	added_by = models.BigIntegerField(null=True)
	added_date = models.DateField(default=timezone.now,null=True)

class agg_hhc_event_job_summary(models.Model):#13
	eve_job_summ_id = models.AutoField(primary_key = True)
	eve_id = models.BigIntegerField(null=True)
	srv_id = models.BigIntegerField(null=True)
	eve_prof_id = models.BigIntegerField(null=True)
	srv_prof_id = models.BigIntegerField(null=True)
	reporting_instruction = models.CharField(max_length=500,null=True)
	types = enum.EnumField(types_enum,null=True)
	report_status = enum.EnumField(reporting_by_enum,null=True)
	status = enum.EnumField(status_enum,null=True)
	isDelStatus = models.BigIntegerField(null=True)
	added_by = models.BigIntegerField(null=True)
	added_date = models.DateField(default=timezone.now,null=True)
	modified_by = models.BigIntegerField(null=True)
	last_modified_date = models.DateField(null=True)

class agg_hhc_event_other_call(models.Model):#14
	eve_o_call_id = models.AutoField(primary_key = True)
	eve_id = models.BigIntegerField(null=True)
	purp_call_id = models.BigIntegerField(null=True)
	description = models.CharField(max_length=500,null=True)
	status = enum.EnumField(status_enum,null=True)
	added_by = models.BigIntegerField(null=True)
	added_date = models.DateField(default=timezone.now,null=True)
	modified_by = models.BigIntegerField(null=True)
	last_modified_date = models.DateField(null=True)

class agg_hhc_event_plan_of_care(models.Model):#15
	eve_poc_id = models.AutoField(primary_key = True)
	eve_id = models.ForeignKey(agg_hhc_events,on_delete=models.CASCADE,null=True)# new added
	srv_id = models.ForeignKey('agg_hhc_services',on_delete=models.CASCADE,null=True)# new added
	sub_srv_id = models.ForeignKey('agg_hhc_sub_services', on_delete=models.CASCADE,null=True)
	hosp_id = models.ForeignKey('agg_hhc_hospitals',on_delete=models.CASCADE,null=True)# new added
	doct_cons_id = models.ForeignKey('agg_hhc_doctors_consultants',on_delete=models.CASCADE,null=True)# new added
	# eve_req_id = models.BigIntegerField(null=True)
	srv_prof_id = models.ForeignKey('agg_hhc_service_professionals',on_delete=models.CASCADE,null=True)
	# service_date = models.DateField(null=True)# this field for fields stor  time
	# service_date_to = models.DateField(null=True)# this field for fields stor time
	start_date = models.DateTimeField(null=True)
	end_date = models.DateTimeField(null=True)
	service_cost = models.FloatField(null=True)
	prof_prefered = enum.EnumField(pt_gender_enum,null=True) # updated
	status = enum.EnumField(status_enum,null=True)
	added_by = models.BigIntegerField(null=True)
	added_date = models.DateField(default=timezone.now,null=True)
	remark = models.CharField(max_length=200, null=True)# newly added
	last_modified_by = models.BigIntegerField(null=True)
	last_modified_date = models.DateField(null=True)

class agg_hhc_event_professional(models.Model):#16 To store professional available details
	eve_prof_id = models.AutoField(primary_key = True)
	eve_id = models.BigIntegerField(null=True)
	eve_req_id = models.BigIntegerField(null=True)
	srv_prof_id = models.BigIntegerField(null=True)
	eve_poc_id = models.BigIntegerField(null=True)
	srv_id = models.BigIntegerField(null=True)
	service_closed = enum.EnumField(yes_no_enum,null=True)
	status = enum.EnumField(status_enum,null=True)
	added_by = models.BigIntegerField(null=True)
	added_date = models.DateField(default=timezone.now,null=True)
	modified_by = models.BigIntegerField(null=True)
	last_modified_date = models.DateField(null=True)

# class agg_hhc_event_requirements(models.Model):#17
# 	# eve_req_id = models.AutoField(primary_key = True)
# 	# eve_id = models.BigIntegerField(null=True)
# 	srv_id = models.BigIntegerField(null=True)
# 	sub_srv_id = models.BigIntegerField(null=True)
# 	srv_prof_id = models.BigIntegerField(null=True)
# 	status = enum.EnumField(status_enum,null=True) 
# 	hosp_id = models.BigIntegerField(null=True)
# 	Consultant = models.BigIntegerField(null=True)
# 	added_by = models.BigIntegerField(null=True)
# 	added_date = models.DateField(null=True)
# 	last_modified_by = models.BigIntegerField(null=True)
# 	last_modified_date = models.DateField(null=True)

class agg_hhc_event_share_hcm(models.Model):#18
	eve_share_hcm_id = models.AutoField(primary_key = True)
	eve_id = models.BigIntegerField(null=True)
	assigned_to = models.BigIntegerField(null=True)
	assigned_by = models.BigIntegerField(null=True)
	status = enum.EnumField(status_enum,null=True)
	added_by = models.BigIntegerField(null=True)
	added_date = models.DateField(default=timezone.now,null=True)
	modified_by = models.BigIntegerField(null=True)
	last_modified_date = models.DateField(null=True)

class agg_hhc_log_for_event(models.Model):#19
	log_for_eve_id = models.AutoField(primary_key = True)
	Role_id = enum.EnumField(Role_id_enum,null=True)
	srv_prof_id = models.BigIntegerField(null=True)
	logged_from = models.CharField(max_length=50,null=True)
	logStatement = models.CharField(max_length=200,null=True)
	Added_date = models.DateField(default=timezone.now,null=True)


class agg_hhc_caller_relation(models.Model):#21
	caller_rel_id = models.AutoField(primary_key = True)
	relation = models.CharField(max_length=240,null=True)
	status = enum.EnumField(status_enum,null=True)
	def __str__(self):
		return self.relation

class agg_hhc_conference_call(models.Model):#22
	conf_call_id = models.AutoField(primary_key = True)
	caller_id = models.CharField(max_length=50,null=True)
	call_agentid = models.CharField(max_length=50,null=True)
	call_mobile = models.CharField(max_length=50,null=True)
	call_extension = models.CharField(max_length=50,null=True)
	# call_status = enum.EnumField(call_status_enum,null=True)
	call_type = models.CharField(max_length=20,null=True)
	call_datetime = models.DateField(null=True)
	is_deleted = enum.EnumField(yes_no_enum,null=True)

class agg_hhc_sp_incoming_call(models.Model):#23
	inc_call_id = models.AutoField(primary_key = True)
	calling_phone_no = models.CharField(max_length=100,null=True)
	agent_no = models.CharField(max_length=100,null=True)
	ext_no = models.CharField(max_length=50,null=True)
	caller_id = models.CharField(max_length=50,null=True)
	status = models.CharField(max_length=500,null=True)
	call_Type = models.CharField(max_length=10,null=True)
	message = models.CharField(max_length=500,null=True)
	dis_conn_massage = models.CharField(max_length=500,null=True)
	call_datetime = models.DateField(null=True)
	call_rinning_datetime = models.DateField(null=True)
	call_connect_datetime = models.DateField(null=True)
	call_disconnect_datetime = models.DateField(null=True)
	avaya_call_time = models.CharField(max_length=50,null=True)
	call_audio = models.CharField(max_length=500,null=True)
	# cl_status = enum.EnumField(cl_status_enum,null=True)
	is_deleted = enum.EnumField(yes_no_enum,null=True)

class agg_hhc_outgoing_call(models.Model):#24
	out_g_call_id = models.AutoField(primary_key = True)
	caller_id = models.CharField(max_length=50,null=True)
	call_agentid = models.CharField(max_length=50,null=True)
	call_mobile = models.CharField(max_length=50,null=True)
	call_extension = models.CharField(max_length=50,null=True)
	# call_status = enum.EnumField(call_status_enum,null=True)
	call_datetime = models.DateField(null=True)
	call_disconnect_datetime = models.DateField(null=True)
	is_deleted = enum.EnumField(yes_no_enum,null=True)
        
class agg_hhc_purpose_call(models.Model):#25
	purp_call_id = models.AutoField(primary_key = True)
	name = models.CharField(max_length=255,null=True)
	status = enum.EnumField(status_enum,null=True)
	added_by = models.BigIntegerField(null=True)
	added_date = models.DateField(default=timezone.now,null=True)
	modified_by = models.BigIntegerField(null=True)
	modified_date = models.DateField(null=True)
	def __str__(self):
		return f"{self.name}"

class agg_hhc_extend_service(models.Model):#26
	ext_srv_id = models.AutoField(primary_key = True)
	eve_poc_id = models.BigIntegerField(null=True)
	eve_id = models.BigIntegerField(null=True)
	service_date = models.DateField(null=True)
	service_date_to = models.DateField(null=True)
	startTime = models.CharField(max_length=50,null=True)
	endTime = models.CharField(max_length=50,null=True)
	estimate_cost = models.BigIntegerField(null=True)
	OTP = models.CharField(max_length=11,null=True)
	status = enum.EnumField(srv_status_enum,null=True)
	added_date = models.DateField(default=timezone.now,null=True)
	OTP_count = models.IntegerField(null=True)
	otp_expire_time = models.DateField(null=True)

class agg_hhc_no_reason_for_service(models.Model):#27
	no_res_for_srv_id = models.AutoField(primary_key = True)
	reason_title = models.CharField(max_length=255,null=True)
	is_deleted = enum.EnumField(yes_no_enum,null=True)
	added_by = models.BigIntegerField(null=True)
	added_date = models.DateField(default=timezone.now,null=True)
	last_modified_by = models.BigIntegerField(null=True)
	last_modified_date = models.DateField(null=True)

class agg_hhc_professional_services(models.Model):#28
	prof_srv_id = models.AutoField(primary_key = True)
	srv_id = models.BigIntegerField(null=True)
	sub_srv_id = models.BigIntegerField(null=True)
	professional_type = enum.EnumField(professional_type_enum,null=True)
	srv_prof_id = models.BigIntegerField(null=True)
	vender_id = models.BigIntegerField(null=True)
	availability = models.CharField(max_length=255,null=True)
	status = enum.EnumField(status_enum,null=True)
	added_by = models.BigIntegerField(null=True)
	added_date = models.DateField(default=timezone.now,null=True)
	modified_by = models.BigIntegerField(null=True)
	last_modified_date = models.DateField(null=True)

class agg_hhc_professional_sub_services(models.Model):#29
	prof_sub_srv_id = models.AutoField(primary_key = True)
	srv_prof_id = models.BigIntegerField(null=True)
	srv_id = models.CharField(max_length=11,null=True)
	sub_srv_id = models.BigIntegerField(null=True)
	prof_cost = models.FloatField(null=True)

	def __str__(self):
		return f'{self.srv_id}'


class agg_hhc_services(models.Model):#30
	srv_id = models.AutoField(primary_key = True)
	service_title = models.CharField(max_length=255,null=True)
	is_hd_access = enum.EnumField(yes_no_enum,null=True)
	status = enum.EnumField(status_enum,null=True)
	added_by = models.BigIntegerField(null=True)
	added_date = models.DateField(default=timezone.now,null=True)
	last_modified_by = models.BigIntegerField(null=True)
	last_modified_date = models.DateField(null=True)
	# flag = enum.EnumField(flag_enum,null=True)##########################################
	tf = enum.EnumField(Tf_enum,null=True)
	package_status = enum.EnumField(package_status_enum,null=True)
	image_path = models.ImageField(null=True)
	info = models.CharField(max_length=500,null=True)
	info_image_path = models.CharField(max_length=300,null=True)
	ser_order = models.CharField(max_length=10,null=True)
	dash_order = models.CharField(max_length=10,null=True)

	def __str__(self):
	    return f"{self.srv_id},{self.service_title}"
	
class agg_hhc_sub_services(models.Model):#34
	sub_srv_id = models.AutoField(primary_key = True)
	recommomded_service = models.CharField(max_length=255,null=True)
	srv_id = models.ForeignKey(agg_hhc_services,on_delete=models.CASCADE, related_name='service', null=True)
	cost = models.FloatField(null=True)
	tax = models.FloatField(null=True)
	deposit = models.CharField(max_length=240,null=True)
	supplied_by = models.CharField(max_length=240,null=True)
	UOM = models.CharField(max_length=50,null=True)
	status = enum.EnumField(status_enum,null=True)
	added_by = models.BigIntegerField(null=True)
	added_date = models.DateField(default=timezone.now,null=True)
	last_modified_by = models.BigIntegerField(null=True)
	last_modified_date = models.DateField(null=True)
	# flag = enum.EnumField(flag_enum,null=True)
	tf = enum.EnumField(Tf_enum,null=True)
	Instruction = models.CharField(max_length=500,null=True)
	Specimen = models.CharField(max_length=100,null=True)
	
	def __str__(self):
	    return f"{self.recommomded_service}"
	

class agg_hhc_service_membership_registration(models.Model):#31
	srv_member_reg_id = models.AutoField(primary_key = True)
	membership_id = models.CharField(max_length=50,null=True)
	sp_pt_id = models.BigIntegerField(null=True)
	pt_name = models.CharField(max_length=50,null=True)
	pt_gender = enum.EnumField(pt_gender_enum,null=True)
	pt_age = models.CharField(max_length=10,null=True)
	pt_contact = models.CharField(max_length=20,null=True)
	pt_contact2 = models.CharField(max_length=20,null=True)
	pt_email = models.CharField(max_length=50,null=True)
	pt_address = models.CharField(max_length=100,null=True)
	pt_ref_form = models.CharField(max_length=30,null=True)
	pt_past_history = models.CharField(max_length=200,null=True)
	pt_curr_prob = models.CharField(max_length=200,null=True)
	pt_allergies = models.CharField(max_length=200,null=True)
	pt_med_company = models.CharField(max_length=50,null=True)
	pt_med_policy = models.CharField(max_length=10,null=True)
	pt_med_exp_date = models.DateField(null=True)
	occupation = models.CharField(max_length=20,null=True)
	rel_contact = models.CharField(max_length=20,null=True)
	rel_name = models.CharField(max_length=50,null=True)
	rel_address = models.CharField(max_length=100,null=True)
	rel_relation = models.CharField(max_length=10,null=True)
	pt_consultant = enum.EnumField(yes_no_enum,null=True)
	pt_consultant_name = models.CharField(max_length=50,null=True)
	pt_consultant_hos = models.CharField(max_length=50,null=True)
	pt_consultant_contact = models.CharField(max_length=20,null=True)
	reg_status = enum.EnumField(reg_status_enum,null=True)
	added_date = models.DateField(default=timezone.now,null=True)
	last_modified_date = models.DateField(null=True)
	status = enum.EnumField(status_enum,null=True)
	# membership_approval = enum.EnumField(membership_approval_enum,null=True)
	membership_note = models.CharField(max_length=100,null=True)
	# membership = enum.EnumField(membership_enum,null=True)
	membership_id_path = models.CharField(max_length=100,null=True)
	modified_by = models.CharField(max_length=20,null=True)



class agg_hhc_service_professionals(models.Model):#32
	srv_prof_id = models.AutoField(primary_key = True)
	professional_code = models.CharField(max_length=255,null=True)
	reference_type = enum.EnumField(reference_type_enum,null=True)
	title = models.CharField(max_length=500,null=True)
	skill_set=models.CharField(max_length=200,null=True)#BHMS
	Job_type = models.CharField(max_length=10,null=True)
	first_name = models.CharField(max_length=255,null=True)
	last_name = models.CharField(max_length=50,null=True)
	middle_name = models.CharField(max_length=50,null=True)
	email_id = models.CharField(max_length=255,null=True)
	phone_no = models.CharField(max_length=20,null=True)
	mobile_no = models.CharField(max_length=20,null=True)
	dob = models.DateField(null=True)
	doj = models.DateField(null=True)
	address = models.CharField(max_length=500,null=True)
	work_email_id = models.CharField(max_length=255,null=True)
	work_phone_no = models.CharField(max_length=20,null=True)
	work_address = models.CharField(max_length=500,null=True)
	prof_zone_id= models.ForeignKey('agg_hhc_professional_zone',on_delete=models.CASCADE,null=True)
	loc_id = models.CharField(max_length=240,null=True)
	set_location = enum.EnumField(set_location_enum,null=True)
	status = enum.EnumField(status_enum,null=True)
	isDelStatus = models.BigIntegerField(null=True)
	added_by = models.BigIntegerField(null=True)
	added_date = models.DateField(default=timezone.now,null=True)
	last_modified_by = models.BigIntegerField(null=True)
	last_modified_date = models.DateField(null=True)
	lattitude = models.CharField(max_length=240,null=True)
	langitude = models.CharField(max_length=240,null=True)
	google_home_location = models.CharField(max_length=240,null=True)
	google_work_location = models.CharField(max_length=240,null=True)
	Physio_Rate = models.FloatField(null=True)
	police_varification = models.CharField(max_length=10,null=True)
	apron_charges = models.CharField(max_length=10,null=True)
	document_status = enum.EnumField(document_status_enum,null=True)
	APP_password = models.CharField(max_length=50,null=True)
	OTP = models.CharField(max_length=4,null=True)
	OTP_count = models.BigIntegerField(null=True)
	otp_expire_time = models.DateTimeField(null=True)
	Profile_pic = models.CharField(max_length=100,null=True)
	Ratings = models.FloatField(null=True)
	Reviews = models.IntegerField(null=True)
	Description = models.CharField(max_length=200,null=True)
	OTP_verification = enum.EnumField(yes_no_enum,null=True)
	reg_source = enum.EnumField(reg_source_enum,null=True)
	availability_status = enum.EnumField(yes_no_enum,null=True)
	location_status = enum.EnumField(yes_no_enum,null=True)
	Services = models.ForeignKey('agg_hhc_professional_sub_services',on_delete=models.CASCADE,null=True)
	Experience = models.IntegerField(null=True)
	Calendar = models.DateField(auto_now=False, auto_now_add=False, null=True)

class agg_hhc_service_professional_details(models.Model):#33
	srv_prof_dt_id = models.AutoField(primary_key = True)
	srv_prof_id = models.BigIntegerField(null=True)
	qualification = models.CharField(max_length=255,null=True)
	specialization = models.CharField(max_length=255,null=True)
	skill_set = models.CharField(max_length=255,null=True)
	work_experience = models.FloatField(null=True)
	hospital_attached_to = models.CharField(max_length=255,null=True)
	pancard_no = models.CharField(max_length=20,null=True)
	service_tax = models.FloatField(null=True)
	status = enum.EnumField(status_enum,null=True)
	added_by = models.BigIntegerField(null=True)
	added_date = models.DateField(default=timezone.now,null=True)
	last_modified_by = models.BigIntegerField(null=True)
	last_modified_date = models.DateField(null=True)
	designation = models.CharField(max_length=50,null=True)
	reference_1 = models.CharField(max_length=100,null=True)
	reference_2 = models.CharField(max_length=100,null=True)
	reference_1_contact_num = models.CharField(max_length=11,null=True)
	reference_2_contact_num = models.CharField(max_length=11,null=True)

class agg_hhc_jobclosure_detail_datewise(models.Model):#35
	jcolse_dt_d_wise_id = models.AutoField(primary_key = True)
	event_id = models.BigIntegerField(null=True)
	srv_id = models.BigIntegerField(null=True)
	sub_srv_id = models.BigIntegerField(null=True)
	service_date = models.DateField(null=True)
	actual_service_date = models.DateField(null=True)
	job_closure_detail = models.CharField(max_length=200,null=True)
	StartTime = models.CharField(max_length=240,null=True)
	Endtime = models.CharField(max_length=240,null=True)
	added_by = models.BigIntegerField(null=True)
	added_by_type = enum.EnumField(reg_source_enum,null=True)
	status = enum.EnumField(status_enum,null=True)
	added_date = models.DateField(default=timezone.now,null=True)

# class agg_hhc_jobclosure_detail_datewise_old(models.Model):#36
# 	jclose_dt_d_wise_old_id = models.AutoField(primary_key = True)
# 	eve_id = models.BigIntegerField(null=True)
# 	srv_id = models.BigIntegerField(null=True)
# 	sub_srv_id = models.BigIntegerField(null=True)
# 	service_date = models.DateField(null=True)
# 	actual_service_date = models.DateField(null=True)
# 	job_closure_detail = models.CharField(max_length=200,null=True)
# 	StartTime = models.CharField(max_length=240,null=True)
# 	Endtime = models.CharField(max_length=240,null=True)
# 	added_by = models.BigIntegerField(null=True)
# 	status = enum.EnumField(status_enum,null=True)
# 	added_date = models.DateField(default=timezone.now,null=True)

class agg_hhc_job_closure(models.Model):#37
	jclose_id = models.AutoField(primary_key = True)
	eve_id = models.BigIntegerField(null=True)
	srv_prof_id = models.BigIntegerField(null=True)
	srv_id = models.BigIntegerField(null=True)
	service_render = enum.EnumField(yes_no_enum,null=True)
	service_date = models.DateField(null=True)
	medicine_id = models.BigIntegerField(null=True)
	cons_id = models.BigIntegerField(null=True)
	temprature = models.FloatField(null=True)
	bsl = models.FloatField(null=True)
	pulse = models.BigIntegerField(null=True)
	spo2 = models.FloatField(null=True)
	rr = models.BigIntegerField(null=True)
	gcs_total = models.BigIntegerField(null=True)
	high_bp = models.CharField(max_length=5,null=True)
	low_bp = models.CharField(max_length=5,null=True)
	skin_perfusion = enum.EnumField(skin_perfusion_enum,null=True)
	airway = enum.EnumField(airway_enum,null=True)
	breathing = enum.EnumField(breathing_enum,null=True)
	circulation = enum.EnumField(circulation_enum,null=True)
	baseline = enum.EnumField(baseline_enum,null=True)
	summary_note = models.CharField(max_length=500,null=True)
	job_closure_file = models.CharField(max_length=255,null=True)
	# status = enum.EnumField(status_enum,null=True)
	added_by = models.BigIntegerField(null=True)
	added_date = models.DateField(default=timezone.now,null=True)
	modified_by = models.BigIntegerField(null=True)
	last_modified_date = models.DateField(null=True)

class agg_hhc_job_closure_consumption_mapping(models.Model):#38
	jclose_cons_map_id = models.AutoField(primary_key = True)
	jclose_id = models.BigIntegerField(null=True)
	consumption_type = enum.EnumField(consumption_type_enum,null=True)
	unit_id = models.BigIntegerField(null=True)
	unit_quantity = models.CharField(max_length=255,null=True)
	status = enum.EnumField(status_enum,null=True)
	added_by = models.BigIntegerField(null=True)
	added_date = models.DateField(default=timezone.now,null=True)
	modified_by = models.BigIntegerField(null=True)
	last_modified_date = models.DateField(null=True)

class agg_hhc_feedbackform1(models.Model):#39
	fb_form_1_id = models.AutoField(primary_key = True)
	event_id = models.CharField(max_length=50,null=True)
	dateAdd = models.DateField(null=True)
	name = models.CharField(max_length=100,null=True)
	mob = models.CharField(max_length=20,null=True)
	q1 = models.CharField(max_length=100,null=True)
	q2 = models.CharField(max_length=100,null=True)
	q3 = models.CharField(max_length=100,null=True)
	q4 = models.CharField(max_length=100,null=True)
	q5 = models.CharField(max_length=100,null=True)
	q6 = models.CharField(max_length=100,null=True)
	status = enum.EnumField(status_enum,null=True)

class agg_hhc_feedback_answers(models.Model):#40
	fb_ans_id = models.AutoField(primary_key = True)
	eve_id = models.ForeignKey('agg_hhc_events',on_delete=models.CASCADE,null=True)
	#fb_from_id = models.BigIntegerField(null=True)
	Ratings=models.FloatField(null=True)
	answer = models.CharField(max_length=255,null=True)
	user_id = models.BigIntegerField(null=True)
	user_type = enum.EnumField(user_type_enum,null=True)
	service_date = models.DateField(null=True)
	added_by = models.BigIntegerField(null=True)
	added_date = models.DateField(default=timezone.now,null=True)
	modified_by = models.BigIntegerField(null=True)
	last_modified_date = models.DateField(null=True)

class agg_hhc_feedback_form(models.Model):#41
	fb_from_id = models.AutoField(primary_key = True)
	question = models.CharField(max_length=500,null=True)
	option_type = enum.EnumField(option_type_enum,null=True)
	status = enum.EnumField(status_enum,null=True)
	isDelStatus = models.BigIntegerField(null=True)
	added_by = models.BigIntegerField(null=True)
	added_date = models.DateField(default=timezone.now,null=True)
	modified_by = models.BigIntegerField(null=True)
	last_modified_date = models.DateField(null=True)

class agg_hhc_feedback_for_app(models.Model):#42
	fb_for_app_id = models.AutoField(primary_key = True)
	feedback = models.CharField(max_length=200,null=True)
	professional_id = models.BigIntegerField(null=True)
	added_date = models.DateField(default=timezone.now,null=True)

class agg_hhc_feedback_options(models.Model):#43
	fb_opt_id = models.AutoField(primary_key = True)
	fb_from_id = models.BigIntegerField(null=True)
	option_value = models.CharField(max_length=20,null=True)
	status = enum.EnumField(status_enum,null=True)
	added_by = models.BigIntegerField(null=True)
	added_date = models.DateField(default=timezone.now,null=True)
	modified_by = models.BigIntegerField(null=True)
	last_modified_date = models.DateField(null=True)

class agg_hhc_assisted_living_schedule(models.Model):#44
	ass_liv_sche_id = models.AutoField(primary_key = True)
	event_id = models.BigIntegerField(null=True)
	service_date = models.DateField(null=True)
	Activity_Name = models.CharField(max_length=20,null=True)
	Cost = models.FloatField(null=True)
	Tax = models.FloatField(null=True)
	Start_time = models.CharField(max_length=20,null=True)
	End_time = models.CharField(max_length=20,null=True)
	# Status = enum.EnumField(Status_enum,null=True)
	date = models.DateField(null=True)

class agg_hhc_membership_schedule_detail(models.Model):#45
	member_sche_dt_id = models.AutoField(primary_key = True)
	pt_id = models.CharField(max_length=2,null=True)
	Doctor_Visit_1 = models.DateField(null=True)
	Doctor_Visit_2 = models.DateField(null=True)
	Telemedicine_1 = models.DateField(null=True)
	Telemedicine_2 = models.DateField(null=True)
	Telemedicine_3 = models.DateField(null=True)
	Telemedicine_4 = models.DateField(null=True)
	lab_test_1 = models.DateField(null=True)
	lab_test_2 = models.DateField(null=True)
	hos_co_ordination_1 = models.DateField(null=True)
	hos_co_ordination_2 = models.DateField(null=True)
	membership_card = models.CharField(max_length=50,null=True)
	document = models.CharField(max_length=200,null=True)
	added_by = models.CharField(max_length=10,null=True)
	added_date = models.DateField(default=timezone.now,null=True)
	modify_by = models.CharField(max_length=10,null=True)
	modify_date = models.DateField(null=True)
	status = enum.EnumField(status_enum,null=True)

class agg_hhc_professional_scheduled(models.Model):#46  THIS WILL WE USED TO STORE DATA IN CALENDAR
	prof_sche_id = models.AutoField(primary_key = True)
	srv_prof_id = models.ForeignKey('agg_hhc_service_professionals',on_delete=models.CASCADE,null=True)
	scheduled_date = models.DateField(null=True)
	from_time = models.DateTimeField(max_length=240,null=True)
	to_time = models.DateTimeField(max_length=240,null=True)
	is_night_shift = enum.EnumField(yes_no_enum,null=True)
	status = enum.EnumField(status_enum,null=True)
	added_by = models.BigIntegerField(null=True)
	added_date = models.DateField(default=timezone.now,null=True)
	modified_by = models.BigIntegerField(null=True)
	modified_date = models.DateField(null=True)

class agg_hhc_reschedule_session(models.Model):#47
	re_sche_session_id = models.AutoField(primary_key = True)
	event_id = models.BigIntegerField(null=True)
	detail_plan_of_care_id = models.BigIntegerField(null=True)
	professional_id = models.BigIntegerField(null=True)
	professional_type = enum.EnumField(professional_types_enum,null=True)
	session_start_date = models.DateField(null=True)
	session_end_date = models.DateField(null=True)
	reschedule_start_date = models.DateField(null=True)
	reschedule_start_time = models.DateField(null=True)
	reschedule_end_date = models.DateField(null=True)
	reschedule_end_time = models.DateField(null=True)
	reschedule_reason = models.CharField(max_length=255,null=True)
	professional_acceptance_status = enum.EnumField(acceptance_status_enum,null=True)
	professional_acceptance_narration = models.CharField(max_length=255,null=True)
	patient_acceptance_status = enum.EnumField(acceptance_status_enum,null=True)
	patient_acceptance_narration = models.CharField(max_length=255,null=True)
	added_user_id = models.BigIntegerField(null=True)
	added_user_type = enum.EnumField(user_types_enum,null=True)
	added_date = models.DateField(default=timezone.now,null=True)
	modified_user_id = models.BigIntegerField(null=True)
	modified_user_type = enum.EnumField(user_types_enum,null=True)
	modified_date = models.DateField(null=True)
	status = enum.EnumField(status_enum,null=True)

class agg_hhc_payments_received_by_professional(models.Model):#48
	pay_recived_by_prof_id = models.AutoField(primary_key = True)
	event_id = models.BigIntegerField(null=True)
	eve_req_id = models.BigIntegerField(null=True)
	Session_id = models.BigIntegerField(null=True)
	cheque_DD_NEFT_no = models.CharField(max_length=50,null=True)
	cheque_DD_NEFT_date = models.DateField(null=True)
	cheque_path_id = models.BigIntegerField(null=True)
	party_bank_name = models.CharField(max_length=50,null=True)
	srv_prof_id = models.BigIntegerField(null=True)
	professional_name = models.CharField(max_length=50,null=True)
	Transaction_Type = models.CharField(max_length=50,null=True)
	amount = models.BigIntegerField(null=True)
	types = models.CharField(max_length=50,null=True)
	added_by = models.BigIntegerField(null=True)
	added_by_type = enum.EnumField(reg_source_enum,null=True)
	Card_Number = models.BigIntegerField(null=True)
	Transaction_ID = models.CharField(max_length=11,null=True)
	date_time = models.DateField(null=True)
	Comments = models.CharField(max_length=250,null=True)
	branch = models.CharField(max_length=50,null=True)
	payment_receipt_no_voucher_no = models.BigIntegerField(null=True)
	status = enum.EnumField(status_enum,null=True)
	payment_status = enum.EnumField(payment_status_enum,null=True)
	Payment_type = enum.EnumField(Payment_type_enum,null=True)
	Payment_mode = enum.EnumField(Payment_mode_enum,null=True)
	OTP_verifivation = enum.EnumField(OTP_verifivation_enum,null=True)

class agg_hhc_professional_availability(models.Model):#49
	professional_avaibility_id = models.AutoField(primary_key = True)
	prof_srv_id = models.IntegerField(null=True) #agg_hhc_professional_services
	day = models.CharField(max_length=8,null=True)

# ------------------------------------------------------------------------------------------------------------------
class prof_enum(enum.Enum): 
    Pending=1
    Accepted=2
    Rejected=3
    Expired=4

class Package_status_enum(enum.Enum):
    Servcie=1
    Package=2

class flag_enum(enum.Enum):
    HD_systems=1
    Mobile_App=2

class is_delet_enum(enum.Enum):
    Yes=1
    No=2

class active_enum(enum.Enum):
	Active=0
	
class type_enum(enum.Enum):
    Doctor=1
    Consultant=2

class consultant_status_enum(enum.Enum):
    Active=1
    Inactive=2
    Delete=3
    Pending=4


class documents_enum(enum.Enum):
    Verified=1
    need_more_details=2
    Rejected=3
    In_Progress=4
    
class truefalse_enum(enum.Enum):
    true=1
    false=2

class pic_enum(enum.Enum):
    Photo=1
    Video=2
class Leave_Conflit_enum(enum.Enum):
    Conflit=1
    Not_conflite=2

class Leave_status_enum(enum.Enum):
    Applied=1
    Approve=2
    pending=3
    Rejected=4
    Cancle=5
class desk_type_enum(enum.Enum):
    SuperAdmin=1
    Admin=2
    HRManager=3
class patient_bed_location_enum(enum.Enum):
    hall1=1
    hall2=2
    bedroom1=3
    bedroom2=4

class Facility_type_enum(enum.Enum):
    Day_care=1
    Reguler=2
    Luxury=3

class consumable_type_enum(enum.Enum):
    Unit=1
    NonUnit=2

class content_type_enum(enum.Enum):
    header=1
    footer=2

class employee_type_enum(enum.Enum):
    HCM=1
    HD=2
    Accountant=3
    Office_Assistant=4
    Trainer=5
    Hospital=6
    dashbaord=7
    caller = 8

class event_by_professional_enum(enum.Enum):
    Started_Route=1
    Started_Session=2
    Completed_Session=3

class Add_through_enum(enum.Enum):
    HD=1
    Professional=2
    Community_App=3

class Pause_Ready_enum(enum.Enum):
    Pause=1
    Ready=2
class session_status_enum(enum.Enum):
    Active=1
    inactive=2
    Device_removed=3

class reciver_enum(enum.Enum):
    Patient=1
    Prof=2
    Consultant=3
    Caller=4

class user_admin_enum(enum.Enum):
    User=1
    Admin=2

class added_by_type_enum(enum.Enum):
    Employee=1
    Professional=2
    Admin=3

class agg_hhc_professional_availability_detail(models.Model):#50
    prof_avaib_dt_id=models.AutoField(primary_key=True)
    #prof_avaib_id=models.ForeignKey(agg_hhc_professional_availability,on_delete=models.CASCADE,null=True)
    start_time=models.TimeField(null=True)
    end_time=models.TimeField(null=True)
    #professional_zone_id=models.ForeignKey(agg_hhc_professional_zone,on_delete=models.CASCADE,null=True)

class agg_hhc_professional_device_info(models.Model):#51
    prof_devi_info_id=models.AutoField(primary_key=True)
    OSVersion=models.CharField(max_length=100,null=True)
    OSName=models.CharField(max_length=100,null=True)
    DevicePlatform=models.CharField(max_length=100,null=True)
    AppVersion=models.CharField(max_length=100,null=True)
    DeviceTimezone=models.CharField(max_length=100,null=True)
    DeviceCurrentTimestamp=models.DateTimeField(null=True)
    Token=models.CharField(max_length=1000,null=True)
    ModelName=models.CharField(max_length=100,null=True)
    added_date=models.DateTimeField(default=timezone.now,null=True)

class agg_hhc_professional_documents(models.Model):#52
    prof_doc_id=models.AutoField(primary_key=True)
    #professional_id=models.ForeignKey(agg_hhc_service_professionals,on_delete=models.CASCADE,null=True)
    #doc_li_id=models.ForeignKey(agg_hhc_documetns_list,on_delete=models.CASCADE,null=True)
    url_path=models.CharField(max_length=1000,null=True)
    rejection_reason=models.CharField(max_length=200,null=True,blank=True)
    status=enum.EnumField(documents_enum,null=True)
    isVerified=enum.EnumField(truefalse_enum,null=True)



class agg_hhc_professional_location_details(models.Model):#54
    prof_loc_dt_id=models.AutoField(primary_key=True)
    lattitude=models.FloatField(null=True)
    longitude=models.FloatField(null=True)
    location_name=models.TextField(null=True)
    prof_zone_id=models.ForeignKey('agg_hhc_professional_zone',on_delete=models.CASCADE,null=True)

class agg_hhc_professional_location_preferences(models.Model):#55
    prof_loc_pref_id=models.AutoField(primary_key=True)
    #srv_prof_id=models.ForeignKey(agg_hhc_service_professionals,on_delete=models.CASCADE,null=True)
    prof_zone_id=models.ForeignKey('agg_hhc_professional_zone',on_delete=models.CASCADE,null=True)
    max_latitude=models.FloatField(null=True)
    min_latitude=models.FloatField(null=True)
    max_longitude=models.FloatField(null=True)
    min_longitude=models.FloatField(null=True)

class agg_hhc_professional_media(models.Model):#56
    prof_media_id=models.AutoField(primary_key=True)
    srv_id=models.ForeignKey(agg_hhc_services,on_delete=models.CASCADE,null=True)
    #sub_srv_id=models.ForeignKey(agg_hhc_sub_services,on_delete=models.CASCADE,null=True)
    Service_day=models.IntegerField(null=True)
    types=enum.EnumField(pic_enum,null=True)
    path=models.CharField(max_length=200,null=True)
    added_by=models.IntegerField(null=True)
    added_date=models.DateTimeField(default=timezone.now,null=True)
    thumbnail_path=models.CharField(max_length=200,null=True)

class agg_hhc_professional_notification(models.Model):#57
    prof_noti_id=models.AutoField(primary_key=True)
    #professional_id=models.ForeignKey(agg_hhc_service_professionals,on_delete=models.CASCADE,null=True)
    types=models.CharField(max_length=100,null=True)
    title=models.CharField(max_length=100,null=True)
    #notification_detail_id=models.IntegerField(null=True)
    message=models.CharField(max_length=1000,null=True)
    Acknowledged=enum.EnumField(prof_enum,null=True)
    added_date=models.DateTimeField(null=True)
    added_by=models.IntegerField(null=True)
    last_modify_date=models.DateTimeField(default=timezone.now,null=True,blank=True)
    last_modify_by=models.IntegerField(null=True,blank=True)

class agg_hhc_professional_password(models.Model):#58
    prof_passwd_id=models.AutoField(primary_key=True)
    #srv_id=models.ForeignKey(agg_hhc_services,on_delete=models.CASCADE,null=True)
    #srv_prof_id=models.ForeignKey(agg_hhc_service_professionals,on_delete=models.CASCADE,null=True)
    professional_password=models.CharField(max_length=50,null=True)
    status=models.IntegerField(null=True)

class agg_hhc_professional_weekoff(models.Model):#59
    prof_woff_id=models.AutoField(primary_key=True)
    #srv_prof_id=models.ForeignKey(agg_hhc_service_professionals,on_delete=models.CASCADE,null=True)
    date_form=models.DateTimeField(null=True)
    date_to=models.DateTimeField(null=True)
    Note=models.CharField(max_length=50,null=True)
    date=models.DateTimeField(null=True)
    Leave_Conflit=enum.EnumField(Leave_Conflit_enum,null=True)
    Leave_status=enum.EnumField(Leave_Conflit_enum,null=True)
    rejection_reason=models.CharField(max_length=200,null=True)
    status=enum.EnumField(truefalse_enum,null=True)

class agg_hhc_admin_users(models.Model):#60
    ad_usr_id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=50,null=True)
    last_name=models.CharField(max_length=50,null=True)
    middle_name=models.CharField(max_length=50,null=True)
    email_id=models.EmailField(null=True)
    password=models.CharField(max_length=255,null=True)
    #landline_no=
    mobile_no=models.IntegerField(null=True)
    alternate_email_id=models.EmailField(null=True,blank=True)
    types=enum.EnumField(desk_type_enum,null=True)
    status=enum.EnumField(status_enum,null=True)
    isDelStatus=models.IntegerField(null=True)
    added_by=models.IntegerField(null=True)
    added_date=models.DateTimeField(default=timezone.now,null=True)
    last_modified_by=models.IntegerField(null=True,blank=True)
    last_modified_date=models.DateTimeField(null=True,blank=True)
    last_login_time=models.DateTimeField(null=True,blank=True)

class agg_hhc_admin_users_modules(models.Model):#61
    ad_usr_model_id=models.AutoField(primary_key=True)
    ad_usr_id=models.ForeignKey(agg_hhc_admin_users,on_delete=models.CASCADE,null=True)
    #module_id=models.ForeignKey(agg_hhc_modules,on_delete=models.CASCADE,null=True)
    status=enum.EnumField(status_enum,null=True)
    added_by=models.IntegerField(null=True)
    added_date=models.DateTimeField(default=timezone.now,null=True)
    last_modified_by=models.IntegerField(null=True,blank=True)
    last_modified_date=models.DateTimeField(null=True,blank=True)

class agg_hhc_admin_user_hospital_mapping(models.Model):#62
    ad_usr_hos_map_id=models.AutoField(primary_key=True)
    #ad_usr_id=models.ForeignKey(agg_hhc_admin_users,on_delete=models.CASCADE,null=True)
    #hosp_id=models.ForeignKey(agg_hhc_hospitals,on_delete=models.CASCADE,null=True)
    added_by=models.IntegerField(null=True)
    added_date=models.DateTimeField(default=timezone.now,null=True)
    last_modified_by=models.IntegerField(null=True,blank=True)
    last_modified_date=models.DateTimeField(null=True,blank=True)

class agg_hhc_assisted_living_booking(models.Model):#63
    ass_liv_book_id=models.AutoField(primary_key=True)
    Flat_Number=models.BigIntegerField(null=True)
    Patient_location=enum.EnumField(patient_bed_location_enum,null=True)
    Facility_type=enum.EnumField(Facility_type_enum,null=True)
    #agg_sp_pt_id=models.ForeignKey(agg_hhc_patients,on_delete=models.CASCADE,null=True)
    status=enum.EnumField(is_delet_enum,null=True)
    date=models.DateTimeField(null=True)

class agg_hhc_attendance_details(models.Model):#64
    att_dt_id=models.AutoField(primary_key=True)
    #Professional_id=models.ForeignKey(agg_hhc_service_professionals,on_delete=models.CASCADE,null=True)
    attnd_date=models.DateField(null=True)
    attnd_type=models.CharField(max_length=30,null=True)
    attnd_status=models.CharField(max_length=10,null=True)
    attnd_Note=models.CharField(max_length=500,null=True)
    added_by_type=models.CharField(max_length=20,null=True)
    ad_usr_id=models.ForeignKey(agg_hhc_admin_users,on_delete=models.CASCADE,null=True)
    added_by_date=models.DateTimeField(null=True)
    status=enum.EnumField(is_delet_enum,null=True)

class agg_hhc_avaya_extensions(models.Model):#65
    avaya_ext_id=models.AutoField(primary_key=True)
    ext_type=models.CharField(max_length=100,null=True)
    ext_ip=models.CharField(max_length=100,null=True)
    ext_no=models.CharField(max_length=100,null=True)
    is_deleted=enum.EnumField(is_delet_enum,null=True)

class agg_hhc_bank_details(models.Model):#66
    bank_dt_id=models.AutoField(primary_key=True)
    #Professional_id=models.ForeignKey(agg_hhc_service_professionals,on_delete=models.CASCADE,null=True)
    Account_name=models.CharField(max_length=100,null=True)
    Account_number=models.CharField(max_length=50,null=True)
    Bank_name=models.CharField(max_length=100,null=True)
    Branch=models.CharField(max_length=50,null=True)
    IFSC_code=models.CharField(max_length=20,null=True)
    Account_type=models.CharField(max_length=20,null=True)
    Amount_with_spero=models.IntegerField(null=True)
    Amount_with_me=models.IntegerField(null=True)

class agg_hhc_cancellation_history(models.Model):#67
    canc_his_id=models.AutoField(primary_key=True)
    #eve_id=models.ForeignKey(agg_hhc_events,on_delete=models.CASCADE,null=True)
    event_code=models.CharField(max_length=50,null=True)
    cancelled_date=models.DateTimeField(null=True)
    can_amt=models.IntegerField(null=True)
    reason=models.CharField(max_length=100,null=True)
    status=enum.EnumField(is_delet_enum,null=True)

class agg_hhc_change_status(models.Model):#68
    cng_stat_id=models.IntegerField(null=True)
    #prof_id=models.ForeignKey(agg_hhc_service_professionals,on_delete=models.CASCADE,null=True)
    status=models.CharField(max_length=20,null=True)
    reason=models.CharField(max_length=100,null=True)
    date=models.DateTimeField(null=True)

class agg_hhc_cheque_images(models.Model):#69
    cq_img_id=models.AutoField(primary_key=True)
    #agg_sp_dt_eve_poc_id=models.ForeignKey(agg_hhc_detailed_event_plan_of_care,on_delete=models.CASCADE,null=True)
    Url_path=models.CharField(max_length=200,null=True)
    Added_date=models.DateTimeField(default=timezone.now,null=True)

class agg_hhc_city(models.Model):#70
    city_id=models.AutoField(primary_key=True)
    city_name=models.CharField(max_length=100,null=True,unique=True)
    state_name=models.ForeignKey('agg_hhc_state',on_delete=models.CASCADE,null=True,to_field='state_name')
    status=enum.EnumField(status_enum,null=True)
    Added_by=models.IntegerField(null=True)
    Added_date=models.DateTimeField(default=timezone.now,null=True)
    def __str__(self):
	    return self.city_name

class agg_hhc_consent_agree_form(models.Model):#71
    consent_agree_form_id=models.AutoField(primary_key=True)
    #eid=models.ForeignKey(agg_hhc_events,on_delete=models.CASCADE,null=True)
    p_name=models.CharField(max_length=100,null=True)
    que=models.CharField(max_length=50,null=True)
    note=models.CharField(max_length=100,null=True)
    added_date=models.DateTimeField(default=timezone.now,null=True)
    status=enum.EnumField(is_delet_enum,null=True)

class agg_hhc_consumables(models.Model):#72
    cons_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255,null=True)
    types=enum.EnumField(consumable_type_enum,null=True)
    manufacture_name=models.CharField(max_length=255,null=True)
    rate=models.FloatField(null=True)#monthly rate
    manufa_name=models.CharField(max_length=11,null=True)#sale manufacture
    sale_price=models.FloatField(null=True)
    status=enum.EnumField(status_enum,null=True)
    added_by=models.IntegerField(null=True)
    added_date=models.DateTimeField(default=timezone.now,null=True)
    last_modified_by=models.IntegerField(null=True,blank=True)
    last_modified_date=models.DateTimeField(null=True,blank=True)

class agg_hhc_content(models.Model):#73
    content_id=models.AutoField(primary_key=True)
    #hosp_id=models.ForeignKey(agg_hhc_hospitals,on_delete=models.CASCADE,null=True)
    content_type=enum.EnumField(content_type_enum,null=True)
    content_value=models.CharField(max_length=500,null=True)
    status=enum.EnumField(status_enum,null=True)
    added_date=models.DateTimeField(default=timezone.now,null=True)
    added_user_id=models.IntegerField(null=True)
    modified_date=models.DateTimeField(null=True,blank=True)
    modified_user_id=models.IntegerField(null=True,blank=True)

class agg_hhc_dash_count_details(models.Model):#74
    dash_count_dt_id=models.AutoField(primary_key=True)
    till_total_count=models.IntegerField(null=True)
    till_month_total_count=models.IntegerField(null=True)
    till_today_total_count=models.IntegerField(null=True)
    till_org_count=models.CharField(max_length=50,null=True)
    till_dia_count=models.CharField(max_length=50,null=True)
    till_month_org_count=models.CharField(max_length=50,null=True)
    till_month_dia_count=models.CharField(max_length=50,null=True)
    added_date=models.DateTimeField(default=timezone.now,null=True)
    status=enum.EnumField(active_inactive_enum,null=True)

class agg_hhc_device_version_info(models.Model):#75
    devi_version_info_id=models.AutoField(primary_key=True)
    osName=models.CharField(max_length=50,null=True)
    osVersion=models.CharField(max_length=50,null=True)
    location_path=models.CharField(max_length=200,null=True)
    compulsory_version=models.CharField(max_length=20,null=True)
    status=enum.EnumField(active_inactive_enum,null=True)
    Added_date=models.DateTimeField(default=timezone.now,null=True)

class agg_hhc_doctors_consultants(models.Model):#76
    doct_cons_id=models.AutoField(primary_key=True)
    #hosp_id=models.ForeignKey(agg_hhc_hospitals,on_delete=models.CASCADE,null=True)
    hos_nm=models.CharField(max_length=100,null=True)
    first_name=models.CharField(max_length=100,null=True)
    last_name=models.CharField(max_length=100,null=True)
    middle_name=models.CharField(max_length=100,null=True,blank=True)
    email_id=models.EmailField(null=True)
    #phone_no=models.IntegerField(null=True)
    mobile_no=models.IntegerField(null=True)
    weblogin_password=models.CharField(max_length=100,null=True)
    work_email_id=models.EmailField(null=True,blank=True)
    work_phone_no=models.IntegerField(null=True,blank=True)
    work_address=models.TextField(null=True)
    speciality=models.CharField(max_length=255,null=True)
    type=enum.EnumField(type_enum,null=True)
    telephonic_consultation_fees=models.IntegerField(null=True,blank=True)
    approved_by=models.CharField(max_length=20,null=True,blank=True)
    reject_by=models.CharField(max_length=20,null=True,blank=True)
    reject_reason=models.CharField(max_length=100,null=True,blank=True)
    status=enum.EnumField(consultant_status_enum,null=True)
    #isDelStatus=models.IntegerField(null=True)
    added_by=models.IntegerField(null=True)
    added_date=models.DateTimeField(default=timezone.now,null=True)
    last_modified_by=models.IntegerField(null=True,blank=True)
    last_modified_date=models.DateTimeField(null=True,blank=True)

class agg_hhc_documetns_list(models.Model):#77
    doc_li_id=models.AutoField(primary_key=True)
    professional_type=models.IntegerField(null=True)
    Documents_name=models.CharField(max_length=50,null=True)
    Added_date=models.DateTimeField(default=timezone.now,null=True)
    isManadatory=enum.EnumField(truefalse_enum,null=True)
    gracePeriod=models.IntegerField(null=True)

class agg_hhc_doc_con(models.Model):#78
    doc_cons_presc_id=models.AutoField(primary_key=True)
    #emp_id=models.ForeignKey(agg_hhc_service_professionals,on_delete=models.CASCADE,null=True)
    presc=models.CharField(max_length=500,null=True)
    doctor=models.CharField(max_length=100,null=True)
    redg_no=models.CharField(max_length=100,null=True)
    sug=models.CharField(max_length=100,null=True)
    note=models.CharField(max_length=100,null=True)
    complaints=models.CharField(max_length=100,null=True)
    added_date=models.DateTimeField(default=timezone.now,null=True)
    status=enum.EnumField(is_delet_enum,null=True)

class agg_hhc_employees(models.Model):#79
    emp_id=models.AutoField(primary_key=True)
    employee_code=models.CharField(max_length=255,null=True)
    types=enum.EnumField(employee_type_enum,null=True)
    #hosp_id=models.ForeignKey(agg_hhc_hospitals,null=True)
    first_name=models.CharField(max_length=50,null=True)
    last_name=models.CharField(max_length=50,null=True)
    middle_name=models.CharField(max_length=50,null=True)
    designation=models.CharField(max_length=255,null=True)
    email_id=models.EmailField(null=True)
    password=models.CharField(max_length=255,null=True)
    mobile_no=models.IntegerField(null=True)
    dob=models.DateField(null=True)
    address=models.CharField(max_length=500,null=True)
    work_phone_no=models.IntegerField(null=True,blank=True)
    work_email_id=models.EmailField(null=True,blank=True)
    loc_id=models.IntegerField(null=True)
    qualification=models.CharField(max_length=255,null=True)
    specialization=models.CharField(max_length=255,null=True)
    work_experience=models.CharField(max_length=255,null=True)
    status=enum.EnumField(status_enum,null=True)
    avaya_agentid=models.ForeignKey(agg_hhc_avaya_extensions,on_delete=models.CASCADE,null=True)
    is_login=enum.EnumField(is_delet_enum,null=True)
    isDelStatus=models.IntegerField(null=True)
    added_by=models.IntegerField(null=True)
    added_date=models.DateTimeField(default=timezone.now,null=True)
    last_modified_by=models.IntegerField(null=True,blank=True)
    last_modified_date=models.DateTimeField(null=True,blank=True)
    last_login=models.DateTimeField(null=True,blank=True)

class agg_hhc_emp_spero(models.Model):#80
    emp_sp_id=models.AutoField(primary_key=True)
    fname=models.CharField(max_length=50,null=True)
    designation=models.CharField(max_length=50,null=True)
    mobile_no=models.IntegerField(null=True)
    birth_date=models.DateField(null=True)
    DOJ=models.DateField(null=True)
    status=enum.EnumField(is_delet_enum,null=True)
    added_by=models.CharField(max_length=10,null=True)
    last_modified_by=models.CharField(max_length=10,null=True,blank=True)
    last_modified_date=models.DateTimeField(null=True,blank=True)
    added_date=models.DateField(default=timezone.now,null=True)
    bitrthday_greeting=models.CharField(max_length=200,null=True)
    anniversary_greeting=models.CharField(max_length=200,null=True)

class agg_hhc_enquiry_follow_up(models.Model):#81
    enq_follow_up_id=models.AutoField(primary_key=True)
    #event_id=models.ForeignKey(agg_hhc_events,on_delete=models.CASCADE,null=True)
    follow_up_date=models.DateField(null=True)
    follow_up_time=models.CharField(max_length=255,null=True)
    follow_up_desc=models.CharField(max_length=500,null=True)
    follow_up_status=enum.EnumField(status_enum,null=True)
    follow_up_next_date=models.DateField(null=True,blank=True)
    added_by=models.IntegerField(null=True)
    added_date=models.DateTimeField(default=timezone.now,null=True)
    last_modified_by=models.IntegerField(null=True,blank=True)
    last_modified_date=models.DateTimeField(null=True,blank=True)
    is_read_status=enum.EnumField(is_delet_enum,null=True)

class agg_hhc_enquiry_requirements(models.Model):#82
    enq_requi_id=models.AutoField(primary_key=True)
    #event_id=models.ForeignKey(agg_hhc_events,on_delete=models.CASCADE,null=True)
    #srv_id=models.ForeignKey(agg_hhc_services,on_delete=models.CASCADE,null=True)
    #sub_srv_id=models.ForeignKey(agg_hhc_sub_services,on_delete=models.CASCADE)

class agg_hhc_hospitals(models.Model):#83
    hosp_id=models.AutoField(primary_key=True)
    branch=models.CharField(max_length=100,null=True)
    hospital_name=models.CharField(max_length=255,null=True)
    hospital_short_code=models.CharField(max_length=5,null=True)
    phone_no=models.IntegerField(null=True)
    website_url=models.CharField(max_length=70,null=True)
    #loc_id=models.ForeignKey(agg_hhc_locations,on_delete=models.CASCADE)
    address=models.TextField(null=True)
    status=enum.EnumField(status_enum,null=True)
    #isDelStatus=
    added_by=models.IntegerField(null=True)
    added_date=models.DateTimeField(default=timezone.now,null=True)
    last_modified_by=models.IntegerField(null=True,blank=True)
    last_modified_date=models.DateTimeField(null=True,blank=True)
    
    # def __str__(self):
    #     return f"{self.hosp_id}"

class agg_hhc_hospital_ips(models.Model):#84
    hosp_ips_id=models.AutoField(primary_key=True)
    #hosp_id=models.ForeignKey(agg_hhc_hospitals,on_delete=models.CASCADE,null=True)
    hospital_ip=models.CharField(max_length=240)
    status=enum.EnumField(status_enum,null=True)
    added_by=models.IntegerField(null=True)
    added_date=models.DateTimeField(default=timezone.now,null=True)
    last_modified_by=models.IntegerField(null=True,blank=True)
    last_modified_date=models.DateTimeField(null=True,blank=True)

class agg_hhc_knowledge_base_documents(models.Model):#85
    know_b_doc_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255,null=True)
    document_file=models.CharField(max_length=255,null=True)
    status=enum.EnumField(status_enum,null=True)
    isDelStatus=models.IntegerField(null=True)
    added_by=models.IntegerField(null=True)
    added_date=models.DateTimeField(default=timezone.now,null=True)
    last_modified_by=models.IntegerField(null=True,blank=True)
    last_modified_date=models.DateTimeField(null=True,blank=True)

class agg_hhc_recived_hospitals(models.Model):#83
    recived_hosp_id=models.AutoField(primary_key=True)
    branch=models.CharField(max_length=100,null=True)
    hospital_name=models.CharField(max_length=255,null=True)
    hospital_short_code=models.CharField(max_length=5,null=True)
    phone_no=models.IntegerField(null=True)
    website_url=models.CharField(max_length=70,null=True)
    address=models.TextField(null=True)
    status=enum.EnumField(status_enum,null=True)
    added_by=models.IntegerField(null=True)
    added_date=models.DateTimeField(default=timezone.now,null=True)
    last_modified_by=models.IntegerField(null=True,blank=True)
    last_modified_date=models.DateTimeField(null=True,blank=True)

class agg_hhc_locations(models.Model):#86 locality
    loc_id=models.AutoField(primary_key=True)
    location=models.CharField(max_length=255,null=True)
    pin_code=models.CharField(max_length=240,null=True)
    status=enum.EnumField(status_enum,null=True)
    #isDelStatus=
    added_by=models.IntegerField(null=True)
    added_date=models.DateTimeField(default=timezone.now,null=True)
    last_modified_by=models.IntegerField(blank=True,null=True)
    last_modified_date=models.DateTimeField(null=True,blank=True)
    


class agg_hhc_log_location_for_session(models.Model):#87
    log_loc_for_session_id=models.AutoField(primary_key=True)
    #Session_id=models.ForeignKey(agg_hhc_detailed_event_plan_of_care,on_delete=models.CASCADE,null=True)
    event_by_professional=enum.EnumField(event_by_professional_enum,null=True)
    #professional_id=models.ForeignKey(agg_hhc_service_professionals,on_delete=models.CASCADE,null=True)
    latitude=models.FloatField(null=True)
    longitude=models.FloatField(null=True)
    Added_date=models.DateTimeField(default=timezone.now,null=True)

class agg_hhc_manager_spero(models.Model):#88
    man_sp_id=models.AutoField(primary_key=True)
    Man_name=models.CharField(max_length=50,null=True)
    mob=models.IntegerField(null=True)
    status=enum.EnumField(is_delet_enum,null=True)
"""
class agg_hhc_medicines(models.Model):#89
    med_id
    pt_id
    doctor_visit1_BP
    doctor_visit1_pulse
    doctor_visit1_temp
    doctor_visit1_SPO2
    doctor_visit1_weight
    doctor_visit1_height
    doctor_visit1_prof
    doctor_visit1_complaint
    doctor_visit1_lab
    doctor_visit1_diet
    doctor_visit1_rx
    added_by
    status
    added_date
    modify_date
    modify_by
class agg_hhc_membership_pat_basic_detail(models.Model):#90
    member_pat_b_dt_id
    pt_id
    doctor_visit1_BP
    doctor_visit1_pulse
    doctor_visit1_temp
    doctor_visit1_SPO2
    doctor_visit1_weight
    doctor_visit1_height
    doctor_visit1_prof
    doctor_visit1_complaint
    doctor_visit1_lab
    doctor_visit1_diet
    doctor_visit1_rx
    added_by
    status
    added_date
    modify_date
    modify_by

"""
class agg_hhc_modules(models.Model):#91
    module_id=models.AutoField(primary_key=True)
    module_name=models.CharField(max_length=255,null=True)
    status=enum.EnumField(status_enum,null=True)
    added_by=models.IntegerField(null=True)
    added_date=models.DateTimeField(default=timezone.now,null=True)
    last_modified_by=models.IntegerField(null=True,blank=True)
    last_modified_date=models.DateTimeField(null=True,blank=True)

class agg_hhc_ongoing_remark_history(models.Model):#92
    ong_remark_his_id=models.AutoField(primary_key=True)
    #eid=models.ForeignKey(agg_hhc_employees,on_delete=models.CASCADE,null=True)
    pat_nm=models.CharField(max_length=100,null=True)
    mobile=models.IntegerField(null=True)
    remark=models.CharField(max_length=100,null=True)
    added_date=models.DateTimeField(default=timezone.now,null=True)
    added_by=models.CharField(max_length=100,null=True)
    status=enum.EnumField(is_delet_enum,null=True)

class agg_hhc_payments(models.Model):#93
    pay_id=models.AutoField(primary_key=True)
    event_id=models.ForeignKey(agg_hhc_events,on_delete=models.CASCADE,null=True)
    cheque_DD_NEFT_no=models.CharField(max_length=50,null=True)
    cheque_DD_NEFT_date=models.DateField(null=True)
    party_bank_name=models.CharField(max_length=50,null=True)
    professional_name=models.CharField(max_length=50,null=True)
    Transaction_Type=models.CharField(max_length=50,null=True)
    amount=models.IntegerField(null=True)
    types=models.CharField(max_length=50,null=True)
    added_by=models.IntegerField(null=True)
    Add_through=enum.EnumField(Add_through_enum,null=True)
    Card_Number=models.BigIntegerField(null=True)
    Transaction_ID=models.CharField(max_length=11,null=True)
    date_time=models.DateTimeField(null=True)
    Comments=models.CharField(max_length=255,null=True)
    payment_receipt_no_voucher_no=models.BinaryField(null=True)
    #hosp_id=models.ForeignKey(agg_hhc_hospitals,on_delete=models.CASCADE)
    status=enum.EnumField(status_enum,null=True)

class agg_hhc_payment_details(models.Model):#94
    pay_dt_id=models.AutoField(primary_key=True)
    #eve_id=models.ForeignKey(agg_hhc_events,on_delete=models.CASCADE,null=True)
    #event_requrement_id=models.ForeignKey(agg_hhc_event_requirements,on_delete=models.CASCADE,null=True)
    amount=models.IntegerField(null=True)
    pay_recived_by_prof_id= models.ForeignKey(agg_hhc_payments,on_delete=models.CASCADE,null=True)
    hosp_id=models.ForeignKey(agg_hhc_hospitals,on_delete=models.CASCADE,null=True)
    date=models.DateTimeField(null=True)
    status=enum.EnumField(is_delet_enum,null=True)

"""
class sp_payment_response(models.Model):#95
    pay_resp_id
    transaction_id
    bank_transaction_id
    order_id
    transcation_amount
    status
    transcation_type
    gateway_name
    response_code
    response_msg
    bank_name
    MID
    payment_mode
    refund_amount
    transcation_date

class sp_payment_transaction(models.Model):#96
    pay_trans_id=
    mId
    channelId
    professional_id
    mobileNo
    email
    transaction_Amount
    website
    industryTypeId
    callbackUrl
    checksumHash
    pay_status
    added_date
"""
class sp_ready_pause_history(models.Model):#97
    ready_paus_his_id=models.AutoField(primary_key=True)
    ext_no=models.CharField(max_length=10,null=True)
    #CallUniqueID=models.ForeignKey(agg_hhc_callers,on_delete=models.CASCADE,null=True)
    #user_id=models.ForeignKey(agg_hhc_incomming,on_delete=models.CASCADE,null=True) Question
    mode_status=enum.EnumField(Pause_Ready_enum,null=True)
    date_time=models.DateField(null=True)
    is_deleted=enum.EnumField(is_delet_enum,null=True)

class agg_hhc_restriction_for_session_complete(models.Model):#98
    restri_for_session_comp_id=models.AutoField(primary_key=True)
    #distance=models.IntegerField(null=True)
    duration=models.IntegerField(null=True)
    added_by=models.IntegerField(null=True)
    added_date=models.DateTimeField(default=timezone.now,null=True)
    status=enum.EnumField(active_inactive_enum,null=True)

class agg_hhc_session(models.Model):#99
    session_id=models.AutoField(primary_key=True)
    #prof_devi_info_id=models.ForeignKey(agg_hhc_professional_device_info,on_delete=models.CASCADE,null=True)
    #srv_prof_id=models.ForeignKey(agg_hhc_service_professionals,on_delete=models.CASCADE,null=True)
    added_date=models.DateField(default=timezone.now,null=True)
    last_modify_date=models.DateField(null=True,blank=True)
    status=enum.EnumField(session_status_enum,null=True)

class agg_hhc_sms_response(models.Model):#100
    sms_resp_id=models.AutoField(primary_key=True)
    sms_event_code=models.CharField(max_length=20,null=True,blank=True)
    sms_mobile_no=models.IntegerField(null=True)
    sms_text=models.CharField(max_length=500,null=True)
    sms_datetime=models.DateTimeField(null=True)
    sms_response=models.CharField(max_length=500,null=True)

class agg_hhc_source_of_enquiry(models.Model):#101
    sor_of_enq_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255,null=True)
    status=enum.EnumField(status_enum,null=True)
    added_by=models.IntegerField(null=True)
    added_date=models.DateTimeField(default=timezone.now,null=True)
    modified_by=models.IntegerField(null=True,blank=True)
    modified_date=models.DateTimeField(null=True,blank=True)

class agg_hhc_specialty(models.Model):#102
    spec_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255,null=True)
    abbreviation=models.CharField(max_length=255,null=True)
    description=models.CharField(max_length=500,null=True)
    added_by=models.IntegerField(null=True)
    added_date=models.DateField(default=timezone.now,null=True)
    last_modified_by=models.IntegerField(null=True,blank=True)
    last_modified_date=models.DateTimeField(null=True,blank=True)
    status=enum.EnumField(status_enum,null=True)
    isDelStatus=models.IntegerField(null=True)

class agg_hhc_tc_examination(models.Model):#103
    id=models.AutoField(primary_key=True)
    #event_id=models.ForeignKey(agg_hhc_events,on_delete=models.CASCADE,null=True)
    patient_id=models.ForeignKey(agg_hhc_patients,on_delete=models.CASCADE,null=True)
    pulse_beat=models.CharField(max_length=50,null=True)
    bp=models.CharField(max_length=50,null=True)
    rr=models.CharField(max_length=50,null=True)
    o2_sat=models.CharField(max_length=50,null=True)
    temp=models.CharField(max_length=50,null=True)
    abdomen=models.CharField(max_length=100,null=True)
    chest=models.CharField(max_length=100,null=True)
    extremity=models.CharField(max_length=100,null=True)
    skin=models.CharField(max_length=100,null=True)
    CNS=models.CharField(max_length=100,null=True)
    ENT=models.CharField(max_length=100,null=True)
    phy_note=models.CharField(max_length=100,null=True)
    sys_note=models.CharField(max_length=100,null=True)
    psy_note=models.CharField(max_length=100,null=True)
    added_date=models.DateTimeField(default=timezone.now,null=True)
    mod_date=models.DateField(null=True,blank=True)
    status=enum.EnumField(is_delet_enum,null=True)

class agg_hhc_teleconsultation_enquiry(models.Model):#104
    tc_enq_id=models.AutoField(primary_key=True)
    #doc_id=models.ForeignKey(agg_hhc_service_professional,on_delete=models.CASCADE,null=True)
    #event_id=models.ForeignKey(sp_events,on_delete=models.CASCADE,null=True)
    #receiver_id=models.ForeignKey(on_delete=,null=True)Question
    receiver=enum.EnumField(reciver_enum,null=True)
    new_event=models.IntegerField(null=True)
    added_by=models.IntegerField(null=True)
    added_date=models.IntegerField(default=timezone.now,null=True)
    status=enum.EnumField(is_delet_enum,null=True)

class agg_hhc_user_activity(models.Model):#105
    usr_acti_id=models.AutoField(primary_key=True)
    module_type=enum.EnumField(user_admin_enum,null=True)
    #module_id=models.ForeignKey(agg_hhc_modules,on_delete=models.CASCADE,null=True)
    module_name=models.CharField(max_length=255,null=True)
    #purp_call_id=models.ForeignKey(agg_hhc_purpose,on_delete=models.CASCADE,null=True)
    #event_id=models.ForeignKey(agg_hhc_events,on_delete=models.CASCADE,null=True)
    activity_description=models.CharField(max_length=500,null=True)
    added_by_type=enum.EnumField(added_by_type_enum,null=True)
    #added_by_id=models.ForeignKey(agg_hhc_employee,on_delete=models.CASCADE,null=True)
    added_by_date=models.DateTimeField(null=True)

class agg_hhc_vc_diagnosis(models.Model):#106
    uvc_diagno_id=models.AutoField(primary_key=True)
    #event_id=models.ForeignKey(agg_hhc_events,on_delete=models.CASCADE,null=True)
    agg_sp_pt_id=models.ForeignKey(agg_hhc_patients,on_delete=models.CASCADE,null=True)
    diagno=models.CharField(max_length=500,null=True)
    phy_assessment=models.CharField(max_length=100,null=True)
    added_date=models.DateTimeField(default=timezone.now,null=True)
    mod_date=models.DateTimeField(null=True,blank=True)
    status=enum.EnumField(is_delet_enum,null=True)

class agg_hhc_vc_fam_his(models.Model):#107
    vc_fam_his_id=models.AutoField(primary_key=True)
    #event_id=models.ForeignKey(agg_hhc_events,on_delete=models.CASCADE,null=True)
    agg_sp_pt_id=models.ForeignKey(agg_hhc_patients,on_delete=models.CASCADE,null=True)
    PH_mother=models.CharField(max_length=50,null=True)
    PH_father=models.CharField(max_length=50,null=True)
    note=models.CharField(max_length=100,null=True)
    added_date=models.DateTimeField(default=timezone.now,null=True)
    mod_date=models.DateTimeField(null=True,blank=True)
    status=enum.EnumField(is_delet_enum,null=True)

class agg_hhc_vc_investigation(models.Model):#108
    vc_inve_id=models.AutoField(primary_key=True)
    #event_id=models.ForeignKey(agg_hhc_events,on_delete=models.CASCADE,null=True)
    #agg_sp_pt_id=models.ForeignKey(agg_hhc_patients,on_delete=models.CASCADE,null=True)
    lab=models.CharField(max_length=100,null=True)
    MRI=models.CharField(max_length=100,null=True)
    CT_scan=models.CharField(max_length=100,null=True)
    USG=models.CharField(max_length=100,null=True)
    Xray=models.CharField(max_length=100,null=True)
    ECG=models.CharField(max_length=100,null=True)
    added_date=models.DateTimeField(default=timezone.now,null=True)
    mod_date=models.DateTimeField(null=True,blank=True)
    status=enum.EnumField(is_delet_enum,null=True)

class agg_hhc_vc_med_his(models.Model):#109
    vc_med_his_id=models.AutoField(primary_key=True)
    #event_id=models.ForeignKey(agg_hhc_events,on_delete=models.CASCADE,null=True)
    #agg_sp_pt_id=models.ForeignKey(agg_hhc_patients,on_delete=models.CASCADE,null=True)
    que1=models.CharField(max_length=100,null=True)
    que2=models.CharField(max_length=100,null=True)
    que3=models.CharField(max_length=100,null=True)
    que4=models.CharField(max_length=100,null=True)
    que5=models.CharField(max_length=100,null=True)
    que6=models.CharField(max_length=100,null=True)
    added_date=models.DateTimeField(default=timezone.now,null=True)
    mod_date=models.DateTimeField(null=True,blank=True)
    status=enum.EnumField(is_delet_enum,null=True)

class sp_vc_prescription(models.Model):#110
    vc_prescri_id=models.AutoField(primary_key=True)
    #event_id=models.ForeignKey(agg_hhc_events,on_delete=models.CASCADE,null=True)
    #agg_sp_pt_id=models.ForeignKey(agg_hhc_patients,on_delete=models.CASCADE,null=True)
    medicine=models.CharField(max_length=500,null=True)
    remark=models.CharField(max_length=100,null=True)
    added_date=models.DateTimeField(default=timezone.now,null=True)
    mod_date=models.DateTimeField(null=True,blank=True)
    status=enum.EnumField(is_delet_enum,null=True)

class agg_hhc_video_consulting(models.Model):#111
    vc_conslt_id=models.AutoField(primary_key=True)
    #event_id=models.ForeignKey(agg_hhc_events,on_delete=models.CASCADE,null=True)
    #agg_sp_pt_id=models.ForeignKey(agg_hhc_patients,on_delete=models.CASCADE,null=True)
    #prof_id=models.ForeignKey(null=True)
    room_id=models.CharField(max_length=100,null=True)
    app_date=models.DateTimeField(null=True)
    app_time=models.CharField(max_length=100,null=True)
    status=enum.EnumField(is_delet_enum,null=True)
    
class agg_hhc_gender(models.Model):#112
	gender_id=models.AutoField(primary_key=True)
	name=models.CharField(max_length=20,null=True)
	status=enum.EnumField(status_enum,null=True)

	

#_____________________________________Android Application_________________#

"""

class agg_hhc_app_family_details(models.Model):
	family_member_id = models.AutoField(primary_key=True)
	phone = models.BigIntegerField(null=True)
	otp = models.IntegerField(null=True)
	otp_expire_time = models.DateTimeField(null=True)
	fname = models.CharField(max_length=50, null=True)
	lname = models.CharField(max_length=50, null=True)
	age = models.IntegerField(null=True)
	gender = models.CharField(max_length=20, null=True)
	email = models.EmailField(null=True)
	contact = models.BigIntegerField(null=True)
	alter_contact = models.BigIntegerField(null=True)
	Address = models.CharField(max_length=250, null=True)
	save_this_add = models.CharField(max_length=250, null=True)
	added_date = models.DateField(default=timezone.now,null=True)
	app_user_id = models.IntegerField(null=True)
	relation = models.ForeignKey(agg_hhc_caller_relation, on_delete=models.SET_NULL, null=True)
	status = enum.EnumField(status_enum,null=True)
"""
class agg_hhc_app_add_address(models.Model):
	address_id = models.AutoField(primary_key=True)
	address = models.CharField(max_length=500, null=True)
	city = models.CharField(max_length=250, null=True)
	locality = models.CharField(max_length=250, null=True)
	sate = models.CharField(max_length=250, null=True)
	pincode = models.CharField(max_length=250, null=True)
	Address_type = models.CharField(max_length=250, null=True)
	#app_call_reg_id = models.ForeignKey(agg_hhc_app_caller_register, on_delete=models.SET_NULL,null=True)
	caller_id=models.ForeignKey(agg_hhc_callers,on_delete=models.SET_NULL,null=True)
	patient_id=models.ForeignKey(agg_hhc_patients,on_delete=models.CASCADE,null=True)
	
class agg_hhc_patient_documents(models.Model):
	doc_id = models.AutoField(primary_key=True)
	agg_sp_pt_id = models.ForeignKey(agg_hhc_patients,null=True, on_delete=models.CASCADE)
	doc_name = models.CharField(max_length=100, null=True)
	doucment = models.FileField(null=True)
	verification_status = enum.EnumField(Leave_status_enum,null=True)
	added_at_time = models.DateTimeField(null=True)

class agg_hhc_state(models.Model):
	state_id=models.AutoField(primary_key=True)
	state_name=models.CharField(max_length=100,null=True,unique=True)
	def __str__(self):
		return f"{self.state_name}"

class agg_hhc_app_patient_documents(models.Model):
	pt_id = models.AutoField(primary_key=True)
	agg_sp_pt_id = models.IntegerField(null=True)
	doc_type_name = models.CharField(max_length=100, null=True)
	path = models.CharField(max_length=500, null=True)
	added_date = models.DateTimeField(default=timezone.now,null=True)
	status = enum.EnumField(Tf_enum, null=True)

#class agg_hhc_city(models.Model):
#	city_id=models.AutoField(primary_key=True)
#	city_name=models.CharField(max_length=255,null=True)
	

class agg_hhc_pincode(models.Model):
	pincode_id=models.AutoField(primary_key=True)
	state_name=models.ForeignKey('agg_hhc_state',on_delete=models.CASCADE,null=True,to_field='state_name')
	city_id=models.ForeignKey('agg_hhc_city',on_delete=models.CASCADE,null=True,to_field='city_name')
	pincode_number=models.PositiveIntegerField(null=True)

class agg_hhc_professional_zone(models.Model):#53 Zones 
    prof_zone_id=models.AutoField(primary_key=True)
    city_id=models.ForeignKey('agg_hhc_city',on_delete=models.CASCADE,null=True)
	#prof_srv_id=models.ForeignKey(agg_hhc_professional_services,on_delete=models.CASCADE,null=True)
    Name=models.CharField(max_length=50,null=True)
    def __str__(self):
	    return f'{self.Name}'


class agg_hhc_professional_cancled_resson(models.Model):
	cancle_reason_id=models.AutoField(primary_key=True)
	srv_prof_id=models.ForeignKey('agg_hhc_service_professionals',on_delete=models.CASCADE,null=True)
	reason=models.TextField(null=True)
	added_date=models.DateTimeField(default=timezone.now,null=True)
	





















#___________________JWT_tables-------------------------------  


class agg_mas_group(models.Model):
    grp_id = models.AutoField(primary_key=True, auto_created=True)
    grp_name = models.CharField(max_length=30, null=True)
    grp_code = models.CharField(max_length=15, null=True)
    grp_level = enum.EnumField(level, null=True)
    grp_parent = models.CharField(max_length=15, null=True)
    grp_status = enum.EnumField(status_enum, null=True)
    grp_added_by = models.IntegerField(null=True)
    grp_added_date = models.DateField(null=True)
    grp_modify_by = models.IntegerField(null=True)
    grp_modify_date = models.DateField(null=True)

    def __str__(self):
        return '%s' %(self.grp_id)




# Custom User Manager
class agg_colleague_manager(BaseUserManager):

    def create_user(self, clg_ref_id, clg_first_name, clg_mid_name ,clg_last_name ,grp_id , clg_email ,clg_mobile_no ,clg_gender ,clg_address ,clg_is_login ,clg_designation ,clg_state ,clg_division ,clg_district ,clg_break_type ,clg_senior ,clg_hos_id ,clg_agency_id ,clg_status ,clg_added_by ,clg_modify_by ,clg_Date_of_birth ,clg_Work_phone_number ,clg_work_email_id ,clg_Emplyee_code ,clg_qualification,clg_avaya_agentid ,clg_Aadhar_no,clg_specialization ,clg_profile_photo_path ,clg_joining_date ,clg_marital_status, password=None, password2=None):
        """
        Creates and saves a User with the given email, name, tc and password.
        """
        if not clg_ref_id:
            raise ValueError('User must have an user id')

        user = self.model(
            clg_email=self.normalize_email(clg_email),
            clg_ref_id = clg_ref_id,
            clg_Emplyee_code = clg_Emplyee_code,
            clg_hos_id = clg_hos_id,
            clg_avaya_agentid = clg_avaya_agentid,
            clg_agency_id = clg_agency_id,
            clg_first_name = clg_first_name,
            clg_mid_name = clg_mid_name, 
            clg_last_name = clg_last_name,
            grp_id = grp_id,
            clg_mobile_no = clg_mobile_no,
            clg_Work_phone_number = clg_Work_phone_number,
            clg_work_email_id = clg_work_email_id,
            clg_gender = clg_gender,
            clg_Date_of_birth = clg_Date_of_birth,
            clg_designation = clg_designation,
            clg_qualification = clg_qualification,
            clg_specialization = clg_specialization,
            clg_senior = clg_senior,
            clg_address = clg_address,
            clg_state = clg_state,
            clg_division = clg_division,
            clg_district = clg_district,
            clg_is_login = clg_is_login,
            clg_break_type = clg_break_type,
            clg_Aadhar_no = clg_Aadhar_no,
            clg_profile_photo_path = clg_profile_photo_path,
            clg_joining_date = clg_joining_date,
            clg_status = clg_status,
            clg_marital_status = clg_marital_status,
            clg_added_by = clg_added_by ,
            clg_modify_by = clg_modify_by
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, clg_ref_id, clg_first_name, clg_mid_name ,clg_last_name, grp_id ,clg_email ,clg_mobile_no ,clg_gender ,clg_address ,clg_is_login ,clg_designation ,clg_state ,clg_division ,clg_district ,clg_break_type ,clg_senior ,clg_hos_id ,clg_agency_id ,clg_status ,clg_added_by ,clg_modify_by ,clg_Date_of_birth ,clg_Work_phone_number ,clg_work_email_id ,clg_Emplyee_code ,clg_qualification,clg_avaya_agentid ,clg_Aadhar_no,clg_specialization, clg_profile_photo_path ,clg_joining_date ,clg_marital_status, password=None):
        """Creates and saves a superuser with the given email, name, tc and password."""
        user = self.create_user(
            clg_email=clg_email,
            password=password,
            clg_ref_id = clg_ref_id,
            clg_Emplyee_code = clg_Emplyee_code,
            clg_hos_id = clg_hos_id,
            clg_avaya_agentid = clg_avaya_agentid,
            clg_agency_id = clg_agency_id,
            clg_first_name = clg_first_name,
            clg_mid_name = clg_mid_name, 
            clg_last_name = clg_last_name,
            grp_id = grp_id,
            clg_mobile_no = clg_mobile_no,
            clg_Work_phone_number = clg_Work_phone_number,
            clg_work_email_id = clg_work_email_id,
            clg_gender = clg_gender,
            clg_Date_of_birth = clg_Date_of_birth,
            clg_designation = clg_designation,
            clg_qualification = clg_qualification,
            clg_specialization = clg_specialization,
            clg_senior = clg_senior,
            clg_address = clg_address,
            clg_state = clg_state,
            clg_division = clg_division,
            clg_district = clg_district,
            clg_is_login = clg_is_login,
            clg_break_type = clg_break_type,
            clg_Aadhar_no = clg_Aadhar_no,
            clg_profile_photo_path = clg_profile_photo_path,
            clg_joining_date = clg_joining_date,
            clg_status = clg_status,
            clg_marital_status = clg_marital_status,
            clg_added_by = clg_added_by ,
            clg_modify_by = clg_modify_by
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class agg_com_colleague(AbstractBaseUser):
    # clg_id = models.AutoField(primary_key=True, auto_created=True)
    clg_ref_id = models.CharField(max_length=15,unique=True, null=True)
    clg_email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        null= True
    )
    clg_work_email_id =	models.EmailField(max_length=100, null=True)
    clg_hos_id = models.IntegerField(null=True)
    clg_agency_id =	models.IntegerField(null=True)
    clg_Emplyee_code =	models.CharField(max_length=15, null=True)
    clg_avaya_agentid =	models.IntegerField(null=True)
    clg_first_name = models.CharField(max_length=15, null=True)
    clg_mid_name =	models.CharField(max_length=15, null=True)
    clg_last_name =	models.CharField(max_length=15, null=True)
    # grp_id = models.IntegerField(null=True)
    grp_id = models.ForeignKey(agg_mas_group,related_name='clg_group', on_delete=models.CASCADE, null=True, default=None)
    clg_gender = models.CharField(max_length=15, null=True)
    clg_mobile_no =	models.IntegerField(null=True)
    clg_Work_phone_number =	models.IntegerField(null=True)
    clg_Date_of_birth =	models.DateField(null=True)
    clg_Aadhar_no =	models.BigIntegerField(null=True)
    clg_designation = models.CharField(max_length=15, null=True)
    clg_qualification =	models.CharField(max_length=15, null=True)
    clg_specialization = models.CharField(max_length=15, null=True)
    clg_address = models.CharField(max_length=100, null=True)
    clg_state =	models.IntegerField(null=True)
    clg_division =	models.IntegerField(null=True)
    clg_district =	models.IntegerField(null=True)
    clg_senior = models.CharField(max_length=15, null=True)
    clg_break_type = models.IntegerField(null=True)
    clg_status = models.CharField(max_length=15, default=True, null=True)    
    clg_profile_photo_path = models.CharField(max_length=100, null=True)
    clg_joining_date =	models.CharField(max_length=30, null=True)
    clg_marital_status = models.CharField(max_length=15, null=True)
    is_active = models.BooleanField(default=True)
    clg_is_login =	models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    clg_added_by =	models.IntegerField(null=True)
    clg_added_date = models.DateField(auto_now_add=True)
    clg_modify_by =	models.IntegerField(null=True)
    clg_modify_date = models.DateField(auto_now=True, null=True)

    username = None
    email = None

    objects = agg_colleague_manager()

    EMAIL_FIELD = 'clg_email'
    GROUP_FIELD = 'grp_id'
    USERNAME_FIELD = 'clg_ref_id'

    REQUIRED_FIELDS = ['grp_id','clg_first_name', 'clg_mid_name' ,'clg_last_name' ,'clg_email' ,'clg_mobile_no', 'clg_gender' ,'clg_address' ,'clg_is_login' ,'clg_designation' ,'clg_state' ,'clg_division' ,'clg_district' ,'clg_break_type' ,'clg_senior' ,'clg_hos_id' ,'clg_agency_id' ,'clg_status' ,'clg_added_by' ,'clg_modify_by' ,'clg_Date_of_birth' ,'clg_Work_phone_number' ,'clg_work_email_id' ,'clg_Emplyee_code' ,'clg_qualification','clg_avaya_agentid' ,'clg_Aadhar_no','clg_specialization', 'clg_profile_photo_path' ,'clg_joining_date' ,'clg_marital_status',]

    def __str__(self):
        return self.clg_ref_id

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin