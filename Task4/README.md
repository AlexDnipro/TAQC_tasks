This module calculates project estimates using https://en.wikipedia.org/wiki/Three-point_estimation.
It asks a user for providing available tasks (at least one) with 3 required estimates (a, m, b). After, it
calculates an estimate (E) and a standard deviation (SD) for each task using the following formulae:

E(task) = (a + 4m + b) / 6
SD(task) = (b − a) / 6
Finally, it calculates the 95% confidence interval (CI) for the project based on
https://en.wikipedia.org/wiki/Three-point_estimation#Project_management. It means that E(project) and SE (project) (SE(task) is equal to SD(task) above) have to be calculated before making the final evaluation of
CI(project) = E(project) ± 2 × SE(project). 

The final values have to be printed like:

Project's 95% confidence interval: 100 ... 120 points
where 100 and 120 are values of Min and Max CI(project).