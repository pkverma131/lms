from django.db import models


class Users(models.Model):
    userID = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    userType = models.CharField(max_length=20)

class LearningPaths(models.Model):
    pathID = models.AutoField(primary_key=True)
    pathName = models.CharField(max_length=255)

class Courses(models.Model):
    courseID = models.AutoField(primary_key=True)
    courseName = models.CharField(max_length=255)
    pathID = models.ForeignKey(LearningPaths, on_delete=models.CASCADE)

class Modules(models.Model):
    moduleID = models.AutoField(primary_key=True)
    moduleName = models.CharField(max_length=255)
    courseID = models.ForeignKey(Courses, on_delete=models.CASCADE)

class Chapters(models.Model):
    chapterID = models.AutoField(primary_key=True)
    chapterName = models.CharField(max_length=255)
    moduleID = models.ForeignKey(Modules, on_delete=models.CASCADE)

class Topics(models.Model):
    topicID = models.AutoField(primary_key=True)
    topicName = models.CharField(max_length=255)
    chapterID = models.ForeignKey(Chapters, on_delete=models.CASCADE)

class AdminCourses(models.Model):
    adminID = models.ForeignKey(Users, on_delete=models.CASCADE)
    courseID = models.ForeignKey(Courses, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)

class MembersCourses(models.Model):
    memberID = models.ForeignKey(Users, on_delete=models.CASCADE)
    courseID = models.ForeignKey(Courses, on_delete=models.CASCADE)

class Comments(models.Model):
    commentID = models.AutoField(primary_key=True)
    memberID = models.ForeignKey(Users, on_delete=models.CASCADE)
    chapterID = models.ForeignKey(Chapters, on_delete=models.CASCADE)
    commentText = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class CourseRatings(models.Model):
    ratingID = models.AutoField(primary_key=True)
    memberID = models.ForeignKey(Users, on_delete=models.CASCADE)
    courseID = models.ForeignKey(Courses, on_delete=models.CASCADE)
    rating = models.IntegerField()

class Notifications(models.Model):
    notificationID = models.AutoField(primary_key=True)
    memberID = models.ForeignKey(Users, on_delete=models.CASCADE)
    notificationType = models.CharField(max_length=20)  # CommunityPost or Mail
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class JoinCourseRequests(models.Model):
    requestID = models.AutoField(primary_key=True)
    memberID = models.ForeignKey(Users, on_delete=models.CASCADE)
    courseID = models.ForeignKey(Courses, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)  # Pending, Approved, Rejected
