#!/usr/bin/env python3
"""
twitter-app.py

01 July 2018     - Written by Robert Preuss (preuss93@students.rowan.edu)
05 February 2020 - Updates from Connor Hornibrook (hornibrookc@rowan.edu) 
"""
import argparse
import configparser
import twitter


class TwitterApp:
    """
    Helper class for initializing the API and making calls to it.
    """

    def __init__(self, filename):
        """
        Constructor, sets up configuration and API object
        """
        # Parse values from configuration file
        config = configparser.ConfigParser()
        config.read(filename)
        self.api = twitter.Api(consumer_key=config['TWITTER']['consumerKey'],
                               consumer_secret=config['TWITTER']['consumerSecret'],
                               access_token_key=config['TWITTER']['accessToken'],
                               access_token_secret=config['TWITTER']['accessTokenSecret'],
                               tweet_mode='extended')

    def write_followers(self, screen_name):
        """
        Write the the newest 200 followers of the specified user name in a 
        file named Twitter_Followers.txt
        """
        results = self.api.GetFollowersPaged(screen_name=screen_name)
        followers = results[2]

        with open("Twitter_Followers.txt", 'w', encoding="utf-8") as file:
            file.write("{} is followed by:\n".format(screen_name))
            for follower in followers:
                file.write("\t{}\n".format(follower.screen_name))

    def write_timeline(self, screen_name):
        """
        Write the last 10 tweets of the specified user to a file named Twitter_Timeline.txt
        """

        with open("Twitter_Timeline.txt", 'w', encoding="utf-8") as file:
            timeline = self.api.GetUserTimeline(screen_name=screen_name, count=10)

            file.write("Latest tweets from {}:\n\n".format(screen_name))
            for status in timeline:
                file.write("Url:  https://twitter.com/i/web/status/{}\n".format(status.id))
                file.write("Created at: {}\n".format(status.created_at))
                file.write("Tweet: {}\n\n".format(status.full_text))


def main():
    """
    Main method logic
    """
    # Parse command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('screen_name', help='Twitter screen_name to print information on')
    parser.add_argument("-c", "--config-file",
                        help="Path to configuration file containing API information.",
                        required=True)
    args = parser.parse_args()

    # Construct class for interacting with Twitter API
    app = TwitterApp(args.config_file)

    # Write latest tweets/followers to output files
    screen_name = args.screen_name
    app.write_timeline(screen_name)
    app.write_followers(screen_name)


# Run the program
if __name__ == '__main__':
    main()
