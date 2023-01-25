# If you on a Windows machine with any Python version 
# or an M1 mac with any Python version
# or an Intel Mac with Python > 3.7
# the multi-threaded version does not work
# so instead, you can use this version. 

import unittest
import population
import simulation 
import genome 
import creature 
import numpy as np
import csv 

class TestGA(unittest.TestCase):
    def testBasicGA(self):
        popsize = 100
        pop = population.Population(pop_size=100, 
                                    gene_count=5)
        #sim = simulation.ThreadedSim(pool_size=1)
        sim = simulation.Simulation()

        testname = "best_test"

        header = ['iteration', 'fittest', 'mean fit', 'mean links', 'max links', 'tot pop']

        with open('best_test.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)

            for iteration in range(50):
                # this is a non-threaded version 
                # where we just call run_creature instead
                # of eval_population
                for cr in pop.creatures:
                    sim.run_creature(cr, 2400)            
                #sim.eval_population(pop, 2400)
                fits = [cr.get_distance_travelled() 
                        for cr in pop.creatures]
                links = [len(cr.get_expanded_links()) 
                        for cr in pop.creatures]

                #calculate total population in each generation         
                tot_creat = len(pop.creatures)*iteration + popsize

                print(iteration, "fittest:", np.round(np.max(fits), 3), 
                    "mean:", np.round(np.mean(fits), 3), "mean links:", np.round(np.mean(links)), "max links:", np.round(np.max(links)), "total creatures:", tot_creat)    

                #data to include in csv 
                data = [iteration, np.round(np.max(fits),3), np.round(np.mean(fits),3), np.round(np.mean(links)), np.round(np.max(links)), tot_creat]

                writer.writerow(data)

                fit_map = population.Population.get_fitness_map(fits)
                new_creatures = []
                for i in range(len(pop.creatures)):
                    p1_ind = population.Population.select_parent(fit_map)
                    p2_ind = population.Population.select_parent(fit_map)
                    p1 = pop.creatures[p1_ind]
                    p2 = pop.creatures[p2_ind]
                    # now we have the parents!
                    dna = genome.Genome.crossover(p1.dna, p2.dna)
                    dna = genome.Genome.point_mutate(dna, rate=0.35, amount=0.5)
                    dna = genome.Genome.shrink_mutate(dna, rate=0.25)
                    dna = genome.Genome.grow_mutate(dna, rate=0.1)
                    cr = creature.Creature(1)
                    cr.update_dna(dna)
                    new_creatures.append(cr)
                # elitism
                max_fit = np.max(fits)
                for cr in pop.creatures:
                    if cr.get_distance_travelled() == max_fit:
                        new_cr = creature.Creature(1)
                        new_cr.update_dna(cr.dna)
                        new_creatures[0] = new_cr
                        #filename = "elite_"+str(iteration)+".csv"
                        #genome.Genome.to_csv(cr.dna, filename)
                        break

                if iteration == 49:
                    filename = "elite_"+str(testname)+".csv"
                    genome.Genome.to_csv(cr.dna, filename)

                pop.creatures = new_creatures
                            
        self.assertNotEqual(fits[0], 0)

unittest.main()
