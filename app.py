import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

from flask import Flask, flash, redirect, render_template, request, session
# Configure application
app = Flask(__name__)
# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True
@app.route("/", methods=["GET", "POST"])
def songs():
    if request.method == "POST":
        sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="5143c26fbbcd46918a5fa549ce3199d4",
                                                                client_secret="2f1ac0c2c08a4226a9a88b111b2fa3cf"))

        sample_sentence = request.form.get("sentence")
        sentence_list = sample_sentence.split(" ")
        songs = []
        # Print track names that contains each word from the sentence input
        for word in sentence_list:
            results = sp.search(q=word, type="track", limit=1)
            for track in enumerate(results['tracks']['items']):
                # Print track name and track artist(s) -- holy shit this part took too fucking long
                artist = (track[1]['artists'])[0]['name']
                track_name = track[1]['name']
                song_info = {"name":track_name, "artist":artist}
                songs.append(song_info)
                #print(track_name + " by " + artists)
        return render_template("playlist_songs.html", songs=songs)
    else:
        return render_template("songs.html")

@app.route("/artists", methods=["GET", "POST"])
def artists():
    if request.method == "POST":
        sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="5143c26fbbcd46918a5fa549ce3199d4",
                                                                client_secret="2f1ac0c2c08a4226a9a88b111b2fa3cf"))

        sample_sentence = request.form.get("sentence")
        sentence_list = sample_sentence.split(" ")
        names = []
        # Print track names that contains each word from the sentence input
        for word in sentence_list:
            results = sp.search(q=word, type="artist", limit=1)
            for artist in enumerate(results['artists']['items']):
                name = artist[1]['name']
                names.append(name)
        return render_template("playlist_artists.html", names=names)
    else:
        return render_template("artists.html")
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
'''
"""
    TODO FOR HTML/PYTHON LINK:
        Highlight the word in the track titles (they might not be words on their own; i.e. 'is' being apart of 'island')
        Hyperlink each song (I can get the link from python but Silas needs to implement it to the HTML)
"""