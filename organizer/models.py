from django.db import models

# a model for a tag to tag a blogpost
class Tag(models.Model):
    name = models.CharField(max_length = 50, unique = True)
    slug = models.SlugField(max_length = 31, unique = True, help_text='A label for URL config.')
    class Meta:
        ordering =['name']

    def __str__(self):
        return self.name.title()

class Startup(models.Model):
    name = models.CharField(max_length = 50, db_index = True)
    slug = models.SlugField(max_length = 31, unique = True, help_text='A label for URL config.')
    description = models.TextField()
    founded_date = models.DateField('date founded')
    contact_email = models.EmailField()
    website = models.URLField(max_length = 255)
    tags = models.ManyToManyField(Tag)
    class Meta:
        ordering =['name']
        get_latest_by = 'founded_date'

    def __str__(self):
        return self.name

class NewsLink(models.Model):
    title = models.CharField(max_length = 100)
    link = models.URLField(max_length = 255)
    pub_date = models.DateField('date published')
    startup = models.ForeignKey('Startup', on_delete=models.CASCADE)
    class Meta:
        verbose_name = ' news article'
        ordering = ['-pub_date']
        get_latest_by = 'pub_date'

    def __Str__(self):
        return "{}:{}".format(self.startup, self.title)