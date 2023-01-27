# AI Evolution

<p float="left">
  <img src="https://user-images.githubusercontent.com/84393679/215149585-4282f01c-dd29-417b-a5ee-79723172fb86.png" width=500 height=300/>
  <img src="https://user-images.githubusercontent.com/84393679/215149709-75aa0723-a8f8-48b6-b397-c743f597620e.png" width=500 height=300/>
</p>

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
