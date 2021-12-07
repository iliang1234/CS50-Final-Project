import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="5143c26fbbcd46918a5fa549ce3199d4",
                                                           client_secret="2f1ac0c2c08a4226a9a88b111b2fa3cf"))

sample_sentence = input("Enter a sentence: ")
sentence_list = sample_sentence.split(" ")

# Print track names that contains each word from the sentence input
for word in sentence_list:
    results = sp.search(q=word, type="artist", limit=1)
    for artist in enumerate(results['artists']['items']):
        name = artist[1]['name']