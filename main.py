from flask import Flask, render_template_string
import tweepy

app = Flask(__name__)

# Twitter API setup
auth = tweepy.OAuthHandler('MGECNsdKf5jpLov3Hd9z58D0I', 'aPQ96YhFqtRK9V4PBYsPVp6JlBvIx4tp360kjPQaZA59Gder4L')
auth.set_access_token('1688677003590008832-WQwDFBrUpfqkOEtwdLN4VShUv9hq1S', 'EPg33KTkkhwEb5rMQFK9Ka1qNQsvTos2cudtBZ5hkRwdf')
api = tweepy.API(auth)

@app.route('/')
def get_user():
    username = 'elonmusk' # Input Twitter Username Here
    user = api.get_user(screen_name=username)

    # HTML template
    template = '''
    <h1>User Details</h1>
    <p>User ID: {{ user.id }}</p>
    <p>User Name: {{ user.name }}</p>
    <p>Screen Name: {{ user.screen_name }}</p>
    <p>Location: {{ user.location }}</p>
    <p>Followers Count: {{ user.followers_count }}</p>
    <p>Friends Count: {{ user.friends_count }}</p>
    <p>Created at: {{ user.created_at }}</p>
    <p>Bio: {{ user.description }}</p>
    '''

    # Render HTML with user data
    return render_template_string(template, user=user)

if __name__ == "__main__":
    app.run(debug=True)
