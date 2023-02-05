# Wikipedia2Anki scraper
Scraper converting Wikipedia tables with images to Anki cards format. My motivation to create that was to learn things such as countries crest or flags, as these are the kind of information that often appear on [PubQuizes](https://pubquiz.pl/).
I've chosen Anki as an effective way to learn new things, but didn't want to bother myself with creating cards for it manually, therefore that script.

# Current usage
Currently, this script supports only scraping tables of the [polish Wikipedia page with crests](https://pl.wikipedia.org/wiki/Herby_i_god%C5%82a_pa%C5%84stw_%C5%9Bwiata), I'll try to make the script more generic, if I decide to scrap more pages.
At this moment, it can be adjusted by updating the `url` passed to the `scrap_page` function, and adjusting properties/tags that are scrapped by the `BeautifulSoup`.

# How to import Anki cards?
The output of the script is added to the parent folder of the script. It consists of the csv file called `herby.csv`, which contains information about the name of the Anki card and image represented by that card, and `media` folder which contains images that are part of each card.
In order to use the output in Anki you need to move the content of the `media` directory to the Anki's `collection.media` (you can find info about directory location in [the documentation](https://docs.ankiweb.net/files.html)) and import the csv file

# How does it look in Anki?
![ankidroid_scraper_example](https://user-images.githubusercontent.com/20254121/216839765-4bce2edb-c26d-4249-9a9e-eb45239a8bc8.png)


# Worth mentions
According to [that page](https://meta.wikimedia.org/wiki/User-Agent_policy), Wikimedia sites are rejecting requests without `user-agent` header send, or bots that are using browser's `user-agent` - such request are rejected with 403 error. 
