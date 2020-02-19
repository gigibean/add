from .models import Tracks, Posts, Users, Comments


class TrackPost:

    track = Tracks()
    user = Users()
    post = Posts()
    comments = []
    url = ''
    hashtags = []

    def __init__(self, track, user, post):
        self.track = track
        self.user = user
        self.post = post
        self.setHashTagList()

    def setHashTagList(self):
        if(self.post.tags):
            taglist = self.post.tags.split(' ')
            self.hashtags = []                  # initiate
            for tag in taglist:
                self.hashtags.append("#"+tag)

        print(self.hashtags)

    def setForSummarizedTrack(self, comment_count):
        self.post.comment_count = comment_count

    def setComment(self):
        self.comments = []
        qs = Comments.objects.filter(posts_idx=self.post)
        comments = qs.order_by('-created_dt')
        for comment in comments:
            self.comments.append(comment)





'''
    # track info
    title = ''
    track_type = 0
    played_count = 0
    moods = ''       # mood tags if MR
    genre = ''       # genre if song
    track_source =''
    image = ''

    # post info
    tags = []        # additional tags by author
    desc = ''
    comment_count = 0
    likes_count = 0
    created_dt = ''
    updated_dt = ''

    # user info
    author_name = ''
    follower_count = 0
    track_count = 0
     def __init__(self, title, track_type, played_count,
                 moods, genre, track_source, image,
                 tags, contents, comment_count, likes_count,
                 author_name, follower_count, created_dt, updated_dt):

        self.follower_count = follower_count
        self.desc = contents
     '''