## BN_lyric_gen 

This repository builds a neural network for creating lyrics based on the band
[Brand New](https://www.fightoffyourdemons.com). We scrape lyrics, clean them
up, feed them in, and enjoy the ridiculousness that comes out.

#### Preprocessing

The scraping is done with [scrapy](https://scrapy.org) through
[lyrics.com](www.lyrics.com). The spider in `BN_scrape\spiders` scrapes each
(unique) track for the lyrics. Unfortunately, essentially every word in every
song is linked to a definition on a different website. So all these links need
to be removed using regex.

#### Training

Using a sliding window of 50 words, we train a three layer RNN on the data. The
specific architecture was chosen for the problem at hand, but also to test some
older hardware I had lying around.

#### Generalizability

The above code can be used for any band, but the spider would need to be
modified. The list of albums and their enumeration would need to be updated
based on a different artists' page. 

This code could potentially be improved by sentiment analysis. I haven't tried this yet, but it is on my list of things to do.

