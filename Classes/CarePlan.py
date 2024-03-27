class CarePlan:
    def __init__(self, assessment, planning, diagnosis, post_evaluation, date_added, frequency,
                 frequency_type, end_date):
        self._assessment = assessment
        self._planning = planning
        self._diagnosis = diagnosis
        self._post_evaluation = post_evaluation
        self._date_added = date_added
        self._frequency = frequency
        self._frequency_type = frequency_type
        self._end_date = end_date

    def get_assessment(self):
        return self._assessment

    def set_assessment(self, assessment):
        self._assessment = assessment

    def get_planning(self):
        return self._planning

    def set_planning(self, planning):
        self._planning = planning

    def get_diagnosis(self):
        return self._diagnosis

    def set_diagnosis(self, diagnosis):
        self._diagnosis = diagnosis

    def get_post_evaluation(self):
        return self._post_evaluation

    def set_post_evaluation(self, post_evaluation):
        self._post_evaluation = post_evaluation

    def get_date_added(self):
        return self._date_added

    def set_date_added(self, date_added):
        self._date_added = date_added

    def get_frequency(self):
        return self._frequency

    def set_frequency(self, frequency):
        self._frequency = frequency

    def get_frequency_type(self):
        return self._frequency_type

    def set_frequency_type(self, frequency_type):
        self._frequency_type = frequency_type

    def get_end_date(self):
        return self._end_date

    def set_end_date(self, end_date):
        self._end_date = end_date
