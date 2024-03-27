class FollowUp:
    def __init__(self, needed, follow_up_frequency, follow_up_frequency_type):
        self._needed = needed
        self._follow_up_frequency = follow_up_frequency
        self._follow_up_frequency_type = follow_up_frequency_type

    def get_needed(self):
        return self._needed

    def set_needed(self, needed):
        self._needed = needed

    def get_follow_up_frequency(self):
        return self._follow_up_frequency

    def set_follow_up_frequency(self, follow_up_frequency):
        self._follow_up_frequency = follow_up_frequency

    def get_follow_up_frequency_type(self):
        return self._follow_up_frequency_type

    def set_follow_up_frequency_type(self, follow_up_frequency_type):
        self._follow_up_frequency_type = follow_up_frequency_type
