from django.contrib import admin
from .models import Users, LearningPaths, Courses, Modules, Chapters, Topics, AdminCourses, MembersCourses, Comments, CourseRatings, Notifications, JoinCourseRequests

class UsersAdmin(admin.ModelAdmin):
    list_display = ['userID', 'username', 'password', 'userType']

class LearningPathsAdmin(admin.ModelAdmin):
    list_display = ['pathID', 'pathName']

class CoursesAdmin(admin.ModelAdmin):
    list_display = ['courseID', 'courseName', 'pathID']

class ModulesAdmin(admin.ModelAdmin):
    list_display = ['moduleID', 'moduleName', 'courseID']

class ChaptersAdmin(admin.ModelAdmin):
    list_display = ['chapterID', 'chapterName', 'moduleID']

class TopicsAdmin(admin.ModelAdmin):
    list_display = ['topicID', 'topicName', 'chapterID']

class AdminCoursesAdmin(admin.ModelAdmin):
    list_display = ['adminID', 'courseID', 'status']

class MembersCoursesAdmin(admin.ModelAdmin):
    list_display = ['memberID', 'courseID']

class CommentsAdmin(admin.ModelAdmin):
    list_display = ['commentID', 'memberID', 'chapterID', 'commentText', 'timestamp']

class CourseRatingsAdmin(admin.ModelAdmin):
    list_display = ['ratingID', 'memberID', 'courseID', 'rating']

class NotificationsAdmin(admin.ModelAdmin):
    list_display = ['notificationID', 'memberID', 'notificationType', 'content', 'timestamp']

class JoinCourseRequestsAdmin(admin.ModelAdmin):
    list_display = ['requestID', 'memberID', 'courseID', 'status']

# Register your models with the custom admin classes
admin.site.register(Users, UsersAdmin)
admin.site.register(LearningPaths, LearningPathsAdmin)
admin.site.register(Courses, CoursesAdmin)
admin.site.register(Modules, ModulesAdmin)
admin.site.register(Chapters, ChaptersAdmin)
admin.site.register(Topics, TopicsAdmin)
admin.site.register(AdminCourses, AdminCoursesAdmin)
admin.site.register(MembersCourses, MembersCoursesAdmin)
admin.site.register(Comments, CommentsAdmin)
admin.site.register(CourseRatings, CourseRatingsAdmin)
admin.site.register(Notifications, NotificationsAdmin)
admin.site.register(JoinCourseRequests, JoinCourseRequestsAdmin)
