from django.shortcuts import render
from .forms import ArousalForm
from django.shortcuts import redirect
# Create your views here.
from .models import GameSession
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
from django.http import HttpResponse



def get_emotion(valence, arousal, intensity):
   emotion_table = {
        ('1', '1', '1'): "Despair, Deep Sadness",
        ('1', '1', '2'): "Gloom, Dejection",
        ('1', '1', '3'): "Sadness, Disappointment",
        ('1', '1', '4'): "Distress",
        ('1', '1', '5'): "Severe Distress",
        ('1', '2', '1'): "Uncomfortable, Unease",
        ('1', '2', '2'): "Tension",
        ('1', '2', '3'): "Anxiety",
        ('1', '2', '4'): "Fear",
        ('1', '2', '5'): "Panic",
        ('1', '3', '1'): "Mild Discomfort",
        ('1', '3', '2'): "Annoyance",
        ('1', '3', '3'): "Frustration",
        ('1', '3', '4'): "Anger",
        ('1', '3', '5'): "Rage",
        ('1', '4', '1'): "Unease",
        ('1', '4', '2'): "Tension",
        ('1', '4', '3'): "Nervousness",
        ('1', '4', '4'): "Anxiety",
        ('1', '4', '5'): "High Anxiety",
        ('1', '5', '1'): "Severe Unease",
        ('1', '5', '2'): "Panic",
        ('1', '5', '3'): "Intense Fear",
        ('1', '5', '4'): "Extreme Anger",
        ('1', '5', '5'): "Terror",
        ('2', '1', '1'): "Discontent",
        ('2', '1', '2'): "Mild Unhappiness",
        ('2', '1', '3'): "Disappointment",
        ('2', '1', '4'): "Regret",
        ('2', '1', '5'): "Strong Regret",
        ('2', '2', '1'): "Mild Annoyance",
        ('2', '2', '2'): "Frustration",
        ('2', '2', '3'): "Anger",
        ('2', '2', '4'): "Strong Anger",
        ('2', '2', '5'): "Intense Anger",
        ('2', '3', '1'): "Unease",
        ('2', '3', '2'): "Nervousness",
        ('2', '3', '3'): "Anxiety",
        ('2', '3', '4'): "Fear",
        ('2', '3', '5'): "High Fear",
        ('2', '4', '1'): "Frustration",
        ('2', '4', '2'): "Anger",
        ('2', '4', '3'): "Strong Anger",
        ('2', '4', '4'): "Rage",
        ('2', '4', '5'): "Extreme Rage",
        ('2', '5', '1'): "Anxiety",
        ('2', '5', '2'): "Fear",
        ('2', '5', '3'): "High Anxiety",
        ('2', '5', '4'): "Intense Fear",
        ('2', '5', '5'): "Panic",
        ('3', '1', '1'): "Indifference",
        ('3', '1', '2'): "Slight Unhappiness",
        ('3', '1', '3'): "Boredom",
        ('3', '1', '4'): "Mild Displeasure",
        ('3', '1', '5'): "Displeasure",
        ('3', '2', '1'): "Mild Indifference",
        ('3', '2', '2'): "Boredom",
        ('3', '2', '3'): "Displeasure",
        ('3', '2', '4'): "Frustration",
        ('3', '2', '5'): "Annoyance",
        ('3', '3', '1'): "Neutral",
        ('3', '3', '2'): "Slight Displeasure",
        ('3', '3', '3'): "Indifference",
        ('3', '3', '4'): "Mild Annoyance",
        ('3', '3', '5'): "Annoyance",
        ('3', '4', '1'): "Indifference",
        ('3', '4', '2'): "Boredom",
        ('3', '4', '3'): "Mild Frustration",
        ('3', '4', '4'): "Frustration",
        ('3', '4', '5'): "Annoyance",
        ('3', '5', '1'): "Displeasure",
        ('3', '5', '2'): "Annoyance",
        ('3', '5', '3'): "High Annoyance",
        ('3', '5', '4'): "Frustration",
        ('3', '5', '5'): "Anger",
        ('4', '1', '1'): "Contentment",
        ('4', '1', '2'): "Satisfaction",
        ('4', '1', '3'): "Calm Happiness",
        ('4', '1', '4'): "Happiness",
        ('4', '1', '5'): "Joy",
        ('4', '2', '1'): "Mild Happiness",
        ('4', '2', '2'): "Happiness",
        ('4', '2', '3'): "Joy",
        ('4', '2', '4'): "High Joy",
        ('4', '2', '5'): "Excitement",
        ('4', '3', '1'): "Happiness",
        ('4', '3', '2'): "Joy",
        ('4', '3', '3'): "Excitement",
        ('4', '3', '4'): "High Excitement",
        ('4', '3', '5'): "Thrill",
        ('4', '4', '1'): "Joy",
        ('4', '4', '2'): "Excitement",
        ('4', '4', '3'): "High Excitement",
        ('4', '4', '4'): "Thrill",
        ('4', '4', '5'): "Ecstasy",
        ('4', '5', '1'): "High Joy",
        ('4', '5', '2'): "Thrill",
        ('4', '5', '3'): "Ecstasy",
        ('4', '5', '4'): "Bliss",
        ('4', '5', '5'): "Euphoria",
        ('5', '1', '1'): "Calm Delight",
        ('5', '1', '2'): "Happiness",
        ('5', '1', '3'): "Joy",
        ('5', '1', '4'): "High Joy",
        ('5', '1', '5'): "Bliss",
        ('5', '2', '1'): "Joy",
        ('5', '2', '2'): "High Joy",
        ('5', '2', '3'): "Bliss",
        ('5', '2', '4'): "Euphoria",
        ('5', '2', '5'): "Ecstasy",
        ('5', '3', '1'): "Happiness",
        ('5', '3', '2'): "Joy",
        ('5', '3', '3'): "High Joy",
        ('5', '3', '4'): "Thrill",
        ('5', '3', '5'): "Ecstasy",
        ('5', '4', '1'): "Joy",
        ('5', '4', '2'): "High Joy",
        ('5', '4', '3'): "Ecstasy",
        ('5', '4', '4'): "Bliss",
        ('5', '4', '5'): "Euphoria",
        ('5', '5', '1'): "High Joy",
        ('5', '5', '2'): "Ecstasy",
        ('5', '5', '3'): "Bliss",
        ('5', '5', '4'): "Euphoria",
        ('5', '5', '5'): "Ultimate Bliss",
    }
   return emotion_table.get((valence, arousal, intensity), "Unknown Emotion")

# def home(request):
def home(request,id):
   form = ArousalForm()
   msg = ""
   if(request.method == 'POST'):
      ArousalVal = request.POST['Arousal']
      ValenceVal = request.POST['Valence']
      IntensityVal = request.POST['Intensity']
      msg = ValenceVal+ArousalVal+IntensityVal+get_emotion(ArousalVal, ValenceVal, IntensityVal)
      session = GameSession(gameid=id, arousal=ArousalVal, valence=ValenceVal, intensity=IntensityVal)
      session.save()
   context = {
      'form': form,
      'msg': msg,
      'game_id':id
   }
   # print(form)
   return render(request, 'home.html',context)

def game(request):
   if(request.method == 'POST'):
      gameid = request.POST['gameid']
      return redirect('home', gameid)
   return render(request, 'game.html')


def erase(request):
   if request.method == 'POST':
        GameSession.objects.all().delete()
        return redirect('game')  # Redirect to the home view or any other view you prefer
   # return render(request, 'confirm_delete.html')
   # return redirect('game')
   
   
def report(request):
    sessions = GameSession.objects.all()
    game_sessions = {}

    for session in sessions:
        if session.gameid not in game_sessions:
            game_sessions[session.gameid] = {'valence': [], 'arousal': [], 'intensity': []}
        game_sessions[session.gameid]['valence'].append(int(session.valence))
        game_sessions[session.gameid]['arousal'].append(int(session.arousal))
        game_sessions[session.gameid]['intensity'].append(int(session.intensity))

    averaged_sessions = []
    for gameid, values in game_sessions.items():
        # avg_valence = np.mean(values['valence'])
        avg_valence = "{:.2f}".format(np.mean(values['valence']))
        avg_arousal = "{:.2f}".format(np.mean(values['arousal']))
        avg_intensity = "{:.2f}".format(np.mean(values['intensity']))
        averaged_sessions.append({
            'gameid': gameid,
            'avg_valence': avg_valence,
            'avg_arousal': avg_arousal,
            'avg_intensity': avg_intensity,
        })

    context = {
        'sessions': averaged_sessions
    }
    return render(request, 'report.html', context)


def generate_graph(request):
    sessions = GameSession.objects.all()
    game_sessions = {}

    for session in sessions:
        if session.gameid not in game_sessions:
            game_sessions[session.gameid] = {'valence': [], 'arousal': [], 'intensity': []}
        game_sessions[session.gameid]['valence'].append(int(session.valence))
        game_sessions[session.gameid]['arousal'].append(int(session.arousal))
        game_sessions[session.gameid]['intensity'].append(int(session.intensity))

    averaged_sessions = []
    for gameid, values in game_sessions.items():
        avg_valence = np.mean(values['valence'])
        avg_arousal = np.mean(values['arousal'])
        avg_intensity = np.mean(values['intensity'])
        averaged_sessions.append({
            'gameid': gameid,
            'avg_valence': avg_valence,
            'avg_arousal': avg_arousal,
            'avg_intensity': avg_intensity,
        })

    game_ids = [session['gameid'] for session in averaged_sessions]
    avg_valences = [session['avg_valence'] for session in averaged_sessions]
    avg_arousals = [session['avg_arousal'] for session in averaged_sessions]
    avg_intensities = [session['avg_intensity'] for session in averaged_sessions]

    plt.figure(figsize=(10, 10))

    scatter = plt.scatter(avg_valences, avg_arousals, c=avg_intensities, cmap='viridis', alpha=0.6, edgecolors='w', s=100)
    plt.colorbar(scatter, label='Intensity')
    plt.xlabel('Average Valence')
    plt.ylabel('Average Arousal')
    plt.title('2D Graph of Average Valence and Arousal')

    plt.axhline(y=0, color='k', linestyle='--')  # Add horizontal line at y=0
    plt.axvline(x=0, color='k', linestyle='--')  # Add vertical line at x=0

    for i, game_id in enumerate(game_ids):
        plt.annotate(game_id, (avg_valences[i], avg_arousals[i]))

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    return HttpResponse(buffer.getvalue(), content_type='image/png')