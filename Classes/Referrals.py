class Referrals:
    def __init__(self, referral_num, referral_reason, referral_provider="", provider_npi="", referral_date="",
                 referral_expiration_date="", patient_condition="", status=""):
        self._referral_num = referral_num
        self._referral_reason = referral_reason
        self._referral_provider = referral_provider
        self._provider_npi = provider_npi
        self._referral_date = referral_date
        self._referral_expiration_date = referral_expiration_date
        self._patient_condition = patient_condition
        self._status = status

    def get_referral_num(self):
        return self._referral_num

    def set_referral_num(self, referral_num):
        self._referral_num = referral_num

    def get_referral_provider(self):
        return self._referral_provider

    def set_referral_provider(self, referral_provider):
        self._referral_provider = referral_provider

    def get_provider_npi(self):
        return self._provider_npi

    def set_provider_npi(self, provider_npi):
        self._provider_npi = provider_npi

    def get_referral_date(self):
        return self._referral_date

    def set_referral_date(self, referral_date):
        self._referral_date = referral_date

    def get_referral_expiration_date(self):
        return self._referral_expiration_date

    def set_referral_expiration_date(self, referral_expiration_date):
        self._referral_expiration_date = referral_expiration_date

    def get_referral_reason(self):
        return self._referral_reason

    def set_referral_reason(self, referral_reason):
        self._referral_reason = referral_reason

    def get_patient_condition(self):
        return self._patient_condition

    def set_patient_condition(self, patient_condition):
        self._patient_condition = patient_condition

    def get_status(self):
        return self._status

    def set_status(self, status):
        self._status = status
