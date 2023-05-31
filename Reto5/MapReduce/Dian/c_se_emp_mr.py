from mrjob.job import MRJob
from mrjob.step import MRStep

class SectorCountMR(MRJob):

    def mapper(self, _, line):
        fields = line.split(',')   
        # Extrae el ID del empleado y el sector económico de la línea
        id_emp = fields[0]
        sector = fields[1]
        # Emite el ID del empleado como clave y el sector económico como valor
        yield id_emp, sector

    def reducer(self, id_emp, sectors):
        # Calcula el número de sectores económicos únicos para cada empleado
        unique_sectors = set(sectors)
        num_sectors = len(unique_sectors)
        
        # Emite el ID del empleado y el número de sectores económicos como resultado final
        yield id_emp, num_sectors

    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducer)
        ]

if __name__ == '__main__':
    SectorCountMR.run()
