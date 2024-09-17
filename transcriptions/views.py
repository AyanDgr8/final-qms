# final_project/transcriptions/views.py

from django.http import JsonResponse
from django.shortcuts import get_list_or_404
from .models import Transcription
from django.db.models import Q


def get_word_groups(request):
    word_groups = {
        "positive": ["happy", "good", "joyful", "amazing", "best"],
        "negative": ["angry", "hate", "bad", "terrible", "abusive", "not"],
        "neutral": ["okay", "fine", "average", "normal"]
    }
    return JsonResponse(word_groups)

# Get all transcriptions
def get_transcriptions(request):
    transcriptions = Transcription.objects.all()
    data = list(transcriptions.values())
    return JsonResponse(data, safe=False)


# Search transcriptions with spokenWords, addWords, and additional query parameters
def search_transcriptions(request):
    # Extract query parameters from the URL's query string
    spoken_words = request.GET.get('spokenWords', '').strip()
    add_words = request.GET.get('addWords', '').strip()

    # You can expand to more query string parameters here, like timeBasis
    # Example: time_basis = request.GET.get('timeBasis', '').strip()

    # Start with all transcriptions
    transcriptions = Transcription.objects.all()

    # Apply filters based on the search terms
    if spoken_words:
        transcriptions = transcriptions.filter(
            Q(customer_translation__icontains=spoken_words) |
            Q(agent_translation__icontains=spoken_words)
        )

    if add_words:
        transcriptions = transcriptions.filter(
            Q(customer_translation__icontains=add_words) |
            Q(agent_translation__icontains=add_words)
        )

    # Serialize the filtered transcriptions
    data = list(transcriptions.values(
        'id', 'caller_id', 
        'hindi_transcription', 'english_transcription', 
        'hindi_translation', 'english_translation',
        'hindi_sentiment', 'english_sentiment',
        'created_at','analysis_hindi', 'analysis_english'
    ))

    return JsonResponse(data, safe=False)
