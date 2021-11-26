import csv
from courses.models import Course

from django.utils import timezone

csvfile_path = "/Users/weicongxie/Developer/tusclass/class_ri.csv"
with open(csvfile_path) as f:
    reader = csv.reader(f)
    for row in reader:
        Course.objects.update_or_create(
            course_name=str(row[0]),
            teacher_name=str(row[1]),
            class_hours=str(row[2]),
            Department=str(row[3]),
            course_form=str(row[4]),
            year_semester=str(row[5]),
            pub_date=timezone.now()
        )