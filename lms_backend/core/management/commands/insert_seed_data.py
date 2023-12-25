# core/management/commands/insert_seed_data.py

import json
from django.core.management.base import BaseCommand
from core.models import LearningPaths, Courses, Modules, Chapters, Topics

class Command(BaseCommand):
    help = 'Insert seed data into the database'

    def handle(self, *args, **kwargs):
        json_file_path = '/home/rahul/lms/lms_feeds.json'

        try:
            with open(json_file_path, 'r') as file:
                seed_data = json.load(file)
                self.insert_data(seed_data)
                self.stdout.write(self.style.SUCCESS('Seed data inserted successfully!'))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'JSON file not found at path: {json_file_path}'))
        except json.JSONDecodeError:
            self.stdout.write(self.style.ERROR('Invalid JSON format in the file'))

    def insert_data(self, seed_data):
        learning_path_data = seed_data.get('learning_path', {})
        path_name = learning_path_data.get('path_name', '')
        courses_data = learning_path_data.get('courses', [])

        # Insert learning path
        learning_path = LearningPaths.objects.create(pathName=path_name)

        # Insert courses
        for course_data in courses_data:
            course_name = course_data.get('course_name', '')
            modules_data = course_data.get('modules', [])

            course = Courses.objects.create(courseName=course_name, pathID=learning_path)

            # Insert modules
            for module_data in modules_data:
                module_name = module_data.get('module_name', '')
                chapters_data = module_data.get('chapters', [])

                module = Modules.objects.create(moduleName=module_name, courseID=course)

                # Insert chapters
                for chapter_data in chapters_data:
                    chapter_name = chapter_data.get('chapter_name', '')
                    topics_data = chapter_data.get('topics', [])

                    chapter = Chapters.objects.create(chapterName=chapter_name, moduleID=module)

                    # Insert topics
                    for topic_data in topics_data:
                        topic_name = topic_data.get('topic_name', '')
                        Topics.objects.create(topicName=topic_name, chapterID=chapter)
