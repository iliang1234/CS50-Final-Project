<<<<<<< Updated upstream
=======
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
'''
from flask import Flask, flash, redirect, render_template, request, session


# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/submit", methods=["GET", "POST"])
def index():
    # TODO
'''

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="5143c26fbbcd46918a5fa549ce3199d4",
                                                           client_secret="2f1ac0c2c08a4226a9a88b111b2fa3cf"))

sample_sentence = input("Enter a sentence: ")
sentence_list = sample_sentence.split(" ")

# Print track names that contains each word from the sentence input
for word in sentence_list:
    results = sp.search(q=word, type="track", limit=1)
    for track in enumerate(results['tracks']['items']):
        # Print track name and track artist(s) -- holy shit this part took too fucking long
        artists = (track[1]['artists'])[0]['name']
        track_name = track[1]['name']
        print(track_name + " by " + artists)

"""
    TODO FOR HTML/PYTHON LINK:
        Highlight the word in the track titles (they might not be words on their own; i.e. 'is' being apart of 'island')
        Hyperlink each song (I can get the link from python but Silas needs to implement it to the HTML)
"""
>>>>>>> Stashed changes
