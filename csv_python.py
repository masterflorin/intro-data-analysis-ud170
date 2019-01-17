import unicodecsv

enrollments_filename = './data/enrollments.csv'
engagement_filename = './data/daily_engagement.csv'
submissions_filename = './data/project_submissions.csv'

def read_csv(filename):
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)

enrollments = read_csv(engagement_filename)
print('enrollments loaded succesfully')
daily_engagement = read_csv(engagement_filename)
print('daily engagement loaded succesfully')
project_submissions = read_csv(submissions_filename)
print('submissions loaded succesfully')
