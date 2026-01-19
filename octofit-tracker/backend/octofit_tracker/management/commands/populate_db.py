from django.core.management.base import BaseCommand
from octofit_tracker.models import Team, User, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Create users
        users = [
            User(name='Spider-Man', email='spiderman@marvel.com', team=marvel, is_superhero=True),
            User(name='Iron Man', email='ironman@marvel.com', team=marvel, is_superhero=True),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team=dc, is_superhero=True),
            User(name='Batman', email='batman@dc.com', team=dc, is_superhero=True),
        ]
        User.objects.bulk_create(users)

        # Refresh users from DB to get IDs
        users = list(User.objects.all())

        # Create activities
        Activity.objects.create(user=users[0], activity_type='Running', duration_minutes=30, date=timezone.now().date())
        Activity.objects.create(user=users[1], activity_type='Cycling', duration_minutes=45, date=timezone.now().date())
        Activity.objects.create(user=users[2], activity_type='Swimming', duration_minutes=60, date=timezone.now().date())
        Activity.objects.create(user=users[3], activity_type='Yoga', duration_minutes=40, date=timezone.now().date())

        # Create workouts
        w1 = Workout.objects.create(name='Super Strength', description='Strength workout for superheroes')
        w2 = Workout.objects.create(name='Agility Training', description='Agility and speed workout')
        w1.suggested_for.set(users)
        w2.suggested_for.set(users)

        # Create leaderboards
        Leaderboard.objects.create(team=marvel, total_points=100, rank=1)
        Leaderboard.objects.create(team=dc, total_points=90, rank=2)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data!'))
