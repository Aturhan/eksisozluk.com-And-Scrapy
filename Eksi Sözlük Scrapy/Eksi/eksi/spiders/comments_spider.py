#Abdullah Turhan 14.09.2022



import scrapy


class CommentsSpider(scrapy.Spider):
    name = "comments"
    comment_counter = 1
    file = open("eksi_comments.txt","a",encoding="UTF-8")
    start_urls = [

            "https://eksisozluk.com/afyonkarahisar--73870?p=1"

        ] # You can add here url address that you want to use



        

    def parse(self, response):
        comment_content = response.css("div.content::text").extract()
        comment_author = response.css("a.entry-author::text").extract() 

        i = 0
        while(i < len(comment_content)):
            """yield{
                "content" : comment_content[i],
                "author" : comment_author[i]
            }"""
            self.file.write("------------------------------------\n")
            self.file.write(str(self.comment_counter) + "\n")
            self.file.write("Comment Content: " + comment_content[i] + "\n")
            self.file.write("Comment Author: " + comment_author[i] + "\n")
            self.file.write("------------------------------------\n")
            self.comment_counter += 1
            
            i += 1
