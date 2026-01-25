class Codec:
    def __init__(self):
        self.d={}
        self.id=0
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.d[self.id]=longUrl
        self.id+=1
        return "https://tinyurl.com/"+str(self.id-1)
    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        key=shortUrl.split("https://tinyurl.com/")[1]
        return self.d[int(key)]
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))