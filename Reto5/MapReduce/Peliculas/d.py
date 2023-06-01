from mrjob.job import MRJob
from mrjob.step import MRStep

class MovieRatingsMR(MRJob):

    def mapper(self, _, line):
        fields = line.split(',')
        
        # Extrae el ID de la película y el rating de la línea
        movie_id = fields[1]
        rating = float(fields[2])
        yield movie_id, (1, rating)# ID de la película como clave y una tupla (1, rating) como valor

    def reducer(self, movie_id, values):
        user_count = 0
        rating_sum = 0
        
        # Recorre los valores y realiza la sumatoria de usuarios y ratings
        for value in values:
            user_count += value[0]
            rating_sum += value[1]
        
        average_rating = rating_sum / user_count
        yield movie_id, (user_count, average_rating)# ID de la película junto con el número de usuarios y el rating promedio


    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducer)
        ]

if __name__ == '__main__':
    MovieRatingsMR.run()
