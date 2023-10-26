from quiz.models import Questions, Subjects
import csv


def run():
    with open('sejarah question sets.csv', encoding='utf8') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        Questions.objects.all().delete()
        Subjects.objects.all().delete()

        

        for row in reader:
            print(row)
            subject,_ = Subjects.objects.get_or_create(subject = 'Sejarah')

            questionaire = Questions(
                question = row[0],
                option_1 = row[4],
                option_2 = row[5],
                option_3 = row[6],
                option_4 = row[7],
                answer = row[3],
                subject = subject,
                image = None

            )
            questionaire.save()