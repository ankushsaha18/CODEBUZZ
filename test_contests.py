#!/usr/bin/env python
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hackIDE_project.settings')
django.setup()

from hackIDE.models import Contest, ContestProblem

print("=== Testing Contest System ===")

# Check contests
contests = Contest.objects.all()
print(f"Total contests in database: {contests.count()}")

for contest in contests:
    print(f"\nContest: {contest.title}")
    print(f"  Active: {contest.is_active}")
    print(f"  Start: {contest.start_time}")
    print(f"  End: {contest.end_time}")
    print(f"  Problems: {contest.problems.count()}")
    
    # Check problems
    for problem in contest.problems.all():
        print(f"    - {problem.title} ({problem.difficulty}) - {problem.points} pts")

# Check active contests
active_contests = Contest.objects.filter(is_active=True)
print(f"\nActive contests: {active_contests.count()}")

# Test the query from the view
from django.utils import timezone
now = timezone.now()
print(f"Current time: {now}")

# This is the exact query from the view
view_contests = Contest.objects.filter(is_active=True).order_by('-start_time')
print(f"View query result: {view_contests.count()} contests")

print("\n=== Test Complete ===")
