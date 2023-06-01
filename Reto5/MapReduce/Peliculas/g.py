from mrjob.job import MRJob
from mrjob.step import MRStep

class BWRating(MRJob):
    def mapper(self, _, line):
        fields = line.split(',')
        
        genre = fields[3]# Extrae el género, el título de la película y el rating 
        movie = fields[1]
        rating = float(fields[2])
        
        yield genre, (rating, movie)

    def reducer(self, genre, values):
        best_movie = None
        best_rating = float('-inf')
        worst_movie = None
        worst_rating = float('inf')
        
        # Recorre los valores y encuentra la mejor y peor película por género
        for value in values:
            rating, movie = value
            if rating > best_rating:
                best_rating = rating
                best_movie = movie
            if rating < worst_rating:
                worst_rating = rating
                worst_movie = movie
        
        yield genre, (best_movie, worst_movie) # Emite el género junto con la mejor y peor película


    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducer)
        ]

if __name__ == '__main__':
    BWRating.run()


    

    
