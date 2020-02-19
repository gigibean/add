# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Comments(models.Model):
    idx = models.AutoField(primary_key=True)
    contents = models.CharField(max_length=225)
    users_idx = models.ForeignKey('Users', models.DO_NOTHING, db_column='users_idx', related_name='fk_comments_1')
    posts_idx = models.ForeignKey('Posts', models.DO_NOTHING, db_column='posts_idx', related_name='fk_comments_2')
    created_dt = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'comments'


class Friends(models.Model):
    idx = models.AutoField(primary_key=True)
    sender_idx = models.ForeignKey('Users', models.DO_NOTHING, db_column='sender_idx', related_name='fk_friends_1')
    receiver_idx = models.ForeignKey('Users', models.DO_NOTHING, db_column='receiver_idx', related_name='fk_friends_2')
    created_dt = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'friends'


class Likes(models.Model):
    idx = models.AutoField(primary_key=True)
    users_idx = models.ForeignKey('Users', models.DO_NOTHING, db_column='users_idx', related_name='fk_likes_1')
    posts_idx = models.ForeignKey('Posts', models.DO_NOTHING, db_column='posts_idx', related_name='fk_likes_2')
    created_dt = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'likes'


class Messages(models.Model):
    idx = models.AutoField(primary_key=True)
    contents = models.TextField()
    sender_idx = models.ForeignKey('Users', models.DO_NOTHING, db_column='sender_idx', related_name='fk_messages_1')
    receiver_idx = models.ForeignKey('Users', models.DO_NOTHING, db_column='receiver_idx', related_name='fk_messages_2')
    room_idx = models.ForeignKey('Rooms', models.DO_NOTHING, db_column='room_idx')
    created_dt = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'messages'


class MonthlyChart(models.Model):
    idx = models.AutoField(primary_key=True)
    created_dt = models.DateTimeField()
    ranked_set = models.CharField(max_length=225, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'monthly_chart'


class Notifications(models.Model):
    idx = models.AutoField(primary_key=True)
    users_idx = models.ForeignKey('Users', models.DO_NOTHING, db_column='users_idx')
    contents = models.CharField(max_length=225)
    url = models.CharField(max_length=225)
    flag = models.IntegerField()
    created_dt = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'notifications'


class Posts(models.Model):
    idx = models.AutoField(primary_key=True)
    contents = models.CharField(max_length=500)
    users_idx = models.ForeignKey('Users', models.DO_NOTHING, db_column='users_idx')
    created_dt = models.DateTimeField()
    track_idx = models.ForeignKey('Tracks', models.DO_NOTHING, db_column='track_idx', blank=True, null=True)
    tags = models.CharField(max_length=255, blank=True, null=True)
    comments_count = models.IntegerField(blank=True, null=True)
    likes_count = models.IntegerField(blank=True, null=True)
    updated_dt = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'posts'


class Rooms(models.Model):
    idx = models.AutoField(primary_key=True)
    users_idx_1 = models.ForeignKey('Users', models.DO_NOTHING, db_column='users_idx_1', related_name='fk_rooms_1')
    users_idx_2 = models.ForeignKey('Users', models.DO_NOTHING, db_column='users_idx_2', related_name='fk_rooms_2')
    last_message = models.TextField()
    created_dt = models.DateTimeField()
    updated_dt = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rooms'


class TrackGenres(models.Model):
    idx = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'track_genres'


class TrackTypes(models.Model):
    idx = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'track_types'


class Tracks(models.Model):
    idx = models.AutoField(primary_key=True)
    title = models.CharField(max_length=45)
    genre_idx = models.ForeignKey(TrackGenres, models.DO_NOTHING, db_column='genre_idx', blank=True, null=True)
    type_idx = models.ForeignKey(TrackTypes, models.DO_NOTHING, db_column='type_idx')
    track_source = models.CharField(max_length=80)
    image = models.CharField(max_length=225, blank=True, null=True)
    flag = models.IntegerField(blank=True, null=True)
    users_idx = models.CharField(max_length=255)
    created_dt = models.DateTimeField()
    played_count = models.IntegerField(blank=True, null=True)
    moods = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tracks'


class Users(models.Model):
    idx = models.AutoField(primary_key=True)
    user_id = models.CharField(unique=True, max_length=45)
    pw = models.CharField(max_length=80)
    nickname = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=45)
    profile = models.CharField(max_length=500, blank=True, null=True)
    salt = models.CharField(max_length=64)
    follower_count = models.IntegerField(blank=True, null=True)
    following_count = models.IntegerField(blank=True, null=True)
    tracks_count = models.IntegerField(blank=True, null=True)
    grade = models.IntegerField()
    status = models.IntegerField()
    created_dt = models.DateTimeField()
    access_dt = models.DateTimeField(blank=True, null=True)
    updated_dt = models.DateTimeField(blank=True, null=True)
    refresh_token = models.CharField(max_length=225, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class UsersHasTracks(models.Model):
    idx = models.AutoField(primary_key=True)
    users_idx = models.ForeignKey(Users, models.DO_NOTHING, db_column='users_idx')
    tracks_idx = models.ForeignKey(Tracks, models.DO_NOTHING, db_column='tracks_idx')
    created_dt = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'users_has_tracks'


class WeeklyChart(models.Model):
    idx = models.AutoField(primary_key=True)
    created_dt = models.DateTimeField()
    ranked_set = models.CharField(max_length=225, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'weekly_chart'
