#!/usr/bin/env python
import os
import sys



if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "timetable_generator.settings")
   

    execute_from_command_line(sys.argv)
