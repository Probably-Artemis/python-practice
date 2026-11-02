"""
Objective: run this file, and notice that importing greetings outputs test messages, which a module should not do. Edit greetings.py so its test code only runs when greetings.py itself is run, not when it is imported. Running this file should then output only "Hello, Sam!".
Restriction: you may not edit this file.
"""

import greetings

print(greetings.greet("Sam"))