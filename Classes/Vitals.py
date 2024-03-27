class Vitals:
    def __init__(self, temperature, systolic_blood_pressure, diastolic_blood_pressure, respiration_rate,
                 pulse_rate="", blood_oxygen_levels=""):
        self._temperature = temperature
        self._systolic_blood_pressure = systolic_blood_pressure
        self._diastolic_blood_pressure = diastolic_blood_pressure
        self._respiration_rate = respiration_rate
        self._pulse_rate = pulse_rate
        self._blood_oxygen_levels = blood_oxygen_levels

    def get_temperature(self):
        return self._temperature

    def set_temperature(self, temperature):
        self._temperature = temperature

    def get_systolic_blood_pressure(self):
        return self._systolic_blood_pressure

    def set_systolic_blood_pressure(self, systolic_blood_pressure):
        self._systolic_blood_pressure = systolic_blood_pressure

    def get_diastolic_blood_pressure(self):
        return self._diastolic_blood_pressure

    def set_diastolic_blood_pressure(self, diastolic_blood_pressure):
        self._diastolic_blood_pressure = diastolic_blood_pressure

    def get_pulse_rate(self):
        return self._pulse_rate

    def set_pulse_rate(self, pulse_rate):
        self._pulse_rate = pulse_rate

    def get_respiration_rate(self):
        return self._respiration_rate

    def set_respiration_rate(self, respiration_rate):
        self._respiration_rate = respiration_rate

    def get_blood_oxygen_levels(self):
        return self._blood_oxygen_levels

    def set_blood_oxygen_levels(self, blood_oxygen_levels):
        self._blood_oxygen_levels = blood_oxygen_levels
