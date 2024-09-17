# final_project/transcriptions/models.py


from django.db import models

class Transcription(models.Model):
    CALLER_ID_MAX_LENGTH = 255
    SENTIMENT_CHOICES = [
        ('Positive', 'Positive'),
        ('Negative', 'Negative'),
        ('Neutral', 'Neutral'),  # Optional: If you want to add a Neutral option
    ]
    caller_id = models.CharField(max_length=CALLER_ID_MAX_LENGTH)
    hindi_transcription = models.TextField(null=True, blank=True)
    english_transcription = models.TextField(null=True, blank=True)
    hindi_translation = models.TextField(null=True, blank=True)
    english_translation = models.TextField(null=True, blank=True)
    hindi_sentiment = models.CharField(max_length=10, choices=SENTIMENT_CHOICES, null=True, blank=True)
    english_sentiment = models.CharField(max_length=10, choices=SENTIMENT_CHOICES, null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    analysis_hindi = models.TextField(null=True, blank=True)
    analysis_english = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'transcriptions'  # Make sure this matches the actual table name
