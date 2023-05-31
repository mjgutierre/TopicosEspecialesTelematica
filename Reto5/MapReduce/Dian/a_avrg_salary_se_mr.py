#Bibl para trabajar con Hadoop y definir el proceso de Map/Reduce
from mrjob.job import MRJob
from mrjob.step import MRStep

class SalaryAverageSeMR(MRJob):

    def mapper(self, _, line):
        fields = line.split(',')
        # Extrae el sector económico y el salario de la línea
        sector = fields[1]
        salary = int(fields[2])
        # Emite el sector económico y el salario como clave-valor
        yield sector, salary

    def reducer(self, sector, salaries):
        # Calcula el salario promedio para cada sector económico
        total_salary = 0
        num_salaries = 0
        for salary in salaries:
            total_salary += salary
            num_salaries += 1
        
        avg_salary = total_salary / num_salaries
        
        # Emite el sector económico y el salario promedio como resultado final
        yield sector, avg_salary

    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducer)
        ]

if __name__ == '__main__':
    SalaryAverageSeMR.run()


