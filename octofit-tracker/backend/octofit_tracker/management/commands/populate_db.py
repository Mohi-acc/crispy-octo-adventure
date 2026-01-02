
from django.core.management.base import BaseCommand
from octofit_tracker import models as app_models
from django.conf import settings
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Deleting existing data...'))
        # Try to clear via ORM, fallback to direct MongoDB drop if needed
        try:
            app_models.Activity.objects.all().delete()
            app_models.User.objects.all().delete()
            app_models.Leaderboard.objects.all().delete()
            app_models.Workout.objects.all().delete()
            app_models.Team.objects.all().delete()
        except Exception as e:
            self.stdout.write(self.style.WARNING(f'ORM deletion failed: {e}. Dropping collections directly.'))
            client = MongoClient(settings.DATABASES['default']['CLIENT']['host'])
            db = client[settings.DATABASES['default']['NAME']]
            for col in ['activity', 'user', 'leaderboard', 'workout', 'team']:
                db[col].drop()

        # Create Teams
        marvel = app_models.Team.objects.create(name='Team Marvel')
        dc = app_models.Team.objects.create(name='Team DC')

        # Create Users
        ironman = app_models.User.objects.create(email='ironman@marvel.com', name='Iron Man', team=marvel)
        captain = app_models.User.objects.create(email='captain@marvel.com', name='Captain America', team=marvel)
        batman = app_models.User.objects.create(email='batman@dc.com', name='Batman', team=dc)
        superman = app_models.User.objects.create(email='superman@dc.com', name='Superman', team=dc)

        # Create Activities
        app_models.Activity.objects.create(user=ironman, type='Run', duration=30, distance=5)
        app_models.Activity.objects.create(user=batman, type='Swim', duration=45, distance=2)
        app_models.Activity.objects.create(user=superman, type='Cycle', duration=60, distance=20)
        app_models.Activity.objects.create(user=captain, type='Walk', duration=20, distance=2)

        # Create Workouts
        app_models.Workout.objects.create(name='Morning Cardio', description='Cardio for all heroes', duration=40)
        app_models.Workout.objects.create(name='Strength Training', description='Strength for all heroes', duration=60)

        # Create Leaderboard
        app_models.Leaderboard.objects.create(team=marvel, points=100)
        app_models.Leaderboard.objects.create(team=dc, points=90)

        self.stdout.write(self.style.SUCCESS('Database populated with test data!'))
