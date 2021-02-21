class TMDB_URL_Maker:
    url = 'https://api.themoviedb.org/3'

    def __init__(self):
        self.api_key = '0bd0f25bbc346f3c9ea7effba6fb6710'
        self.language = 'ko'
    
    def get_url(self, opt=''):
        return f'{self.url}/{opt}'