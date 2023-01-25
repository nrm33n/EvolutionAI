# AI Evolution
Teaching creatures how to walk using a genetic algorithm 

This is a study based on Karl Sims' <a href="https://www.karlsims.com/papers/siggraph94.pdf">paper</a> on evolving virtual creatures. 
Uses python, physics engine <a href="https://pybullet.org/wordpress/">PyBullet</a>. Built using test-driven development methods. 

distance calculated using basic euclidean distance:
```
[np.linalg.norm(a-b)]
 ```
 
For effectively evolution, the genetic algorithm supports: 
 * crossover mutation
 * point mutation
 * shrink mutation 
 * grow mutation 
 * elitism 

Hyperparameters in the URDF file were changed and compared, results can be seen in the "elites" folder
Files containing the hyperparameters of each test are the test_x.URDF files. 
