# The heart of async, Think of it as a manager.
# Task A
# Task B
# Task C
# Manager checks:
# Is A waiting?
# → Run B
# Is B waiting?
# → Run C
# Is C waiting?
# → Run A
# Keeps switching intelligently.
# This manager is called: Event Loop

