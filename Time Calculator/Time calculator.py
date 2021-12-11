class Node:
    def __init__(self,day ,nxt_day = None):
        self.day = day
        self.next = nxt_day
    def __str__(self):
        return self.day
    
class CircularLinkedList:
    def __init__(self, r = None ):
        self.root = r
        self.size = 0

    def add(self, d):
        if self.size == 0:
            self.root = Node(d)
            self.root.next = self.root
        else:
            new_node = Node(d, self.root.next)
            self.root.next = new_node
        self.size += 1

    def find(self,day):
        this_node = self.root
        while True:
            if this_node.get_data() == d:
                return d
            elif this_node.get_next() == self.root:
                return "False: could not find {}".format(d)
            this_node = this_node.get_next()

    def next_day(self, day, n = 1 ):
        curr = self.root
        new_day = None
        while curr:
            if curr.day == day:
                break
            curr = curr.next
        for i in range(n):
            curr = curr.next
        return curr.day

week = CircularLinkedList()
days = ['monday','sunday','saturday','friday','thursday', 'wednesday', 'tuesday']
for day in days:
    week.add(day)
day = week.root

def add_time(start, duration, day = None):
    start_time, period = start.split()
    start_hrs, start_mins = start_time.split(':')
    add_hrs, add_mins = duration.split(':')

    start_hrs = int(start_hrs)
    start_mins = int(start_mins)
    add_hrs = int(add_hrs)
    add_mins = int(add_mins)

    old_period = period
    new_period = None
    days_later = None
    end_hrs = None
    end_mins = None

    duration_time = add_hrs + add_mins/60
    if duration_time < 24:
        end_hrs = start_hrs + add_hrs
        end_mins = start_mins + add_mins

    else: # duration_time >= 24
        if duration_time % 24 == 0:
            days_later = add_hrs // 24
        else:
            days_later = (add_hrs // 24 )+ 1
        add_hrs = add_hrs % 24
        end_hrs = start_hrs + add_hrs
        end_mins = start_mins + add_mins

    if end_mins > 60:
        end_mins = end_mins - 60
        end_hrs = end_hrs + 1

    total_endTime = end_hrs + end_mins / 60
    if period in ['AM'] and total_endTime > 12:
        period = 'PM'
        if end_hrs > 12:
            end_hrs = end_hrs - 12
    elif period in ['PM'] and total_endTime > 12:
        period = 'AM'
        if end_hrs > 12:
            end_hrs = end_hrs - 12
    if len(str(end_mins)) == 1:
        end_mins = '0' + str(end_mins)

    output = None
    if not day:
        if old_period in ['PM'] and period in ['AM'] and not days_later:
            output = str(end_hrs) + ':' + str(end_mins) + ' ' + f"{period}" + ' ' + '(next day)'
        elif old_period == period and not days_later:
            output = str(end_hrs) + ':' + str(end_mins) + ' ' + f"{period}"
        elif old_period != period and not days_later:
            output = str(end_hrs) + ':' + str(end_mins) + ' ' + f"{period}"
        elif old_period == period or old_period != period and days_later == 1:
            output = str(end_hrs) + ':' + str(end_mins) + ' ' + f"{period}" + ' ' + '(next day)'
        else:
            output = str(end_hrs) + ':' + str(end_mins) + ' ' + f"{period}" + ' ' + f"({days_later} days later)"
        return output
    else:
        if old_period in ['PM'] and period in ['AM'] and not days_later:
            day = week.next_day(day.lower())
            output = str(end_hrs) + ':' + str(end_mins) + ' ' + f"{period}" + ',' + ' ' + f"{day.capitalize()}" + ' ' + '(next day)'
        elif old_period != period and not days_later:
            output = str(end_hrs) + ':' + str(end_mins) + ' ' + f"{period}" + ',' + ' ' + f"{day.capitalize()}"
        elif old_period == period and not days_later:
            output = str(end_hrs) + ':' + str(end_mins) + ' ' + f"{period}" + ',' + ' ' + f"{day.capitalize()}"
        elif old_period == period or old_period != period and days_later == 1:
            day = week.next_day(day.lower(), days_later)
            output = str(end_hrs) + ':' + str(end_mins) + ' ' + f"{period}" + ',' + ' ' + f"{day.capitalize()}" + ' ' + '(next day)'
        else:
            day = week.next_day(day.lower(),days_later)
            output = str(end_hrs) + ':' + str(end_mins) + ' ' + f"{period}" + ',' + ' ' + f"{day.capitalize()}" + ' ' + f"({days_later} days later)"
        return output

#print(add_time("11:43 PM", "24:20", "tueSday"))
#add_time("10:10 PM", "3:30")
#print(add_time("3:00 PM", "3:10"))
#print(add_time("6:30 PM", "205:12"))
#print(add_time("3:00 PM", "24:10"))
#print(add_time("8:30 PM", "2:32", "Monday"))
print(add_time("2:59 AM", "24:00", "tueSday"))
