import scrapy


class SongsSpider(scrapy.Spider):
    name = 'songs'
    allowed_domains = ['vgmusic.com']
    start_urls = ['https://www.vgmusic.com/music/console/nintendo/nes/']

    def parse(self, response):
        hrefs = response.css('tr > td > a::attr(href)').extract()
        midi_links = [href for href in hrefs if '.mid' in href]

        with open('downloaded.txt', 'r') as f:
            downloaded_lines = f.readlines()
            already_downloaded = [line.replace(
                '\n', '') for line in downloaded_lines]

        not_downloaded = [
            link for link in midi_links if link not in already_downloaded]

        for link in not_downloaded:
            file = MidiFile()
            file['file_urls'] = [response.urljoin(link)]

            yield file


class MidiFile(scrapy.Item):
    file_urls = scrapy.Field()
    files = scrapy.Field()
