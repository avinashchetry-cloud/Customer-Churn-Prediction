
import pandas as pd
from ydata_profiling import ProfileReport


df = pd.read_csv('C:\\Users\\hp\\Downloads\\SpotifyFeatures\\SpotifyFeatures.csv')

profile = ProfileReport(df, title="Spotify Music Analysis")

profile.to_file("spotify_report.html")

