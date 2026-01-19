from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.user = User.objects.create(name='Test User', email='test@example.com', team=self.team)
        self.workout = Workout.objects.create(name='Test Workout')
        self.activity = Activity.objects.create(user=self.user, activity_type='Test', duration_minutes=10, date='2023-01-01')
        self.leaderboard = Leaderboard.objects.create(team=self.team, total_points=10, rank=1)
        self.workout.suggested_for.set([self.user])

    def test_user(self):
        self.assertEqual(self.user.name, 'Test User')

    def test_team(self):
        self.assertEqual(self.team.name, 'Test Team')

    def test_activity(self):
        self.assertEqual(self.activity.activity_type, 'Test')

    def test_workout(self):
        self.assertEqual(self.workout.name, 'Test Workout')

    def test_leaderboard(self):
        self.assertEqual(self.leaderboard.rank, 1)
