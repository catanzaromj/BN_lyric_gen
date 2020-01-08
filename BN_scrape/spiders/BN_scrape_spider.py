import scrapy

class LyricsSpider(scrapy.Spider):
    name = "lyrics"
    start_urls = [
            'https://www.lyrics.com/artist/Brand-New/511016'
        ]

    ## parse links through all the songs
    def parse(self, response):
        for i in [3,4,5,7,8,9,11]:##only consider unique albums
            for song in response.css("div.clearfix")[i].css("tbody").css("strong a::attr(href)").getall():
                url = response.urljoin(song)
                yield scrapy.Request(url, callback = self.parse_song)

### parse song reads through lyrics 
    def parse_song(self, response):
        for lyric in response.css("pre.lyric-body").getall():
            yield {
                    'title' : response.css("title::text").get(),
                    'lyric' : response.css("pre.lyric-body").getall()
            }
