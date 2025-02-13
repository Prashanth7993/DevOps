import scrapy

class ExtractUrls(scrapy.Spider):
    name = "Prashanth"

    def start_requests(self):
        urls = ["https://economictimes.indiatimes.com"]
        for u in urls:
            yield scrapy.Request(url=u, callback=self.parse)

    def parse(self, response):
        # Extract all URLs from the page
        links = response.css("a::attr(href)").getall()

        # Print extracted URLs
        for link in links:
            self.log(f"Found URL: {link}")

        # Optionally, yield results
        yield {"Extracted Links": links}
