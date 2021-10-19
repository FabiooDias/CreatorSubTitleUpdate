import re
import datetime
class Calculator_time:
    def line_time_update(self, time_old, value: float) -> re.compile(r'\d{2}:\d{2}:\d{2},\d{3}' + ' --> ' + r'\d{2}:\d{2}:\d{2},\d{3}'):
        new_time = []
        for time in time_old:
            new_time.append(self.update_time(time, value))
        return new_time[0] + ' --> ' + new_time[1] + '\n'

    def update_time(self, time, value):
        time = datetime.datetime.strptime(time, '%H:%M:%S,%f')
        increased_time = time + datetime.timedelta(seconds=value)
        return increased_time.strftime('%H:%M:%S,%f')[0:12]