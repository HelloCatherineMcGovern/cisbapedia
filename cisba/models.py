from django.db import models

# Create your models here.

class Category(models.Model):
#Categories of CISBA knowledge(i.e., Python, Cybersecurity, Object-oriented Programming
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        """Return a string representation of the model."""
        return self.text

class Author(models.Model):
#The name of the person who wrote the article
    text = models.CharField(max_length=200)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text

class Tag(models.Model):
    tag_text = models.CharField(max_length=30)

    def __str__(self):
        return self.title

class Article(models.Model):
    # The name of the person who wrote the article
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    text = models.TextField()
    tag = models.ManyToManyField(Tag)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'articles'

    def __str__(self):
        """Return a string representation of the model"""
        return f"{self.text[:50]}..."