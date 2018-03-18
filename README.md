# 2-by-2-rubik-cube-solver

* Naming convention is explained in details in rubik.py. Refer the following pictures to understand better. 

    * Naming of 6 surfaces: 
    
      ![img1](https://github.com/gov-vj/2-by-2-rubik-cube-solver/blob/master/images/surface%20name.jpg)
      
    * Naming of cubie positions:
    
      ![img2](https://github.com/gov-vj/2-by-2-rubik-cube-solver/blob/master/images/cubie%20position.jpg)
      
    * Naming of cubie surfaces:
    
      ![img3](https://github.com/gov-vj/2-by-2-rubik-cube-solver/blob/master/images/cubie%20surface.jpg)
    
    
*  There are 6 unique operations (Explanation is given in details in rubik.py. Here is only the exapmles to make things more clear)

      I(initial position)=((flu, luf, ufl), (fur, urf, rfu), (fdl, dlf, lfd), (frd, rdf, dfr), (bul, ulb, lbu), (bru, rub, ubr), (bld, ldb, dbl), (bdr, drb, rbd))
      
      See last picture to form I. Note that each cubie has 3 visible surface and they will stay together after rotating the cube. Example: flu, luf, ufl are the surfaces name of cube FLU and after rotating front face clockwise it will come in 2nd position as shown below.
    
    * Front face rotated clockwise.
        
        F=((fdl, dlf, lfd), (flu, luf, ufl), (frd, rdf, dfr), (fur, urf, rfu), (bul, ulb, lbu), (bru, rub, ubr), (bld, ldb, dbl), (bdr, drb, rbd))
        
    * Front face rotated anti clockwise (Fi)
    * Left face rotated clockwise (L)
    * Left face rotated anti clockwise (Li)
    * Upper face rotated clockwise (U)
    * Upper face rotated anti clockwise (Ui)
    
    ### perm_apply method example:
    
    Let's rotate the front face clockwise from position I and then rotate the left face clockwise.
    
       middle = perm_apply(perm=F, position=I)
              = [position[i] for i in perm] = [I[i] for i in F]
              = [I[i] for i in (fdl, dlf, lfd, flu, ...)]
              = [I[fdl] I[dlf] I[lfd] I[flu] ...]
              = [I[6] I[7] I[8] I[0] ...]   (refer lines 40-70 in rubik.py)
              = [fdl dlf lfd flu ...] 
              = F
                                                                           
                                                                          
       end = perm_apply(perm=L, position=middle)
           = [middle[i] for i in L]
           = [middle[i] for i in (ulb, lbu, bul, fur, ...)]
           = [middle[i] for i in (13, 14, 12, 3, ...)]
           = [middle[13] middle[14] middle[12] middle[3] ...]
           = [F[13] F[14] F[12] F[3] ...]
           = [ulb lbu bul flu ...]
                                              
    
    Fi, Li, and Ui is calclauted using perm_inverse. F and Fi operation should cancel each other and therefore we can find the permutaion of Fi by applying inverse (logic is explained in rubik.py) on F. Similarly for Li, and Ui.
    
    
    ## Algorithm
    
      * Reduction to graph problem:
      
          We treat every possible combination of our rubik cube as a node in the graph and an undirected edge exist between 2 nodes if we can reach one node from the another node by applying only single operation from the set of 6 operations defined above.
          
          So, now our problem is reduced to find the shortest path from the start position (or node) to the final position. Since there are no weights on an edge we can find the shortest path using BFS.
          
      * Challenges:
      
          Number of possible configuration for our rubik cube is 24!. Note that some of the configuration state is not acheivable. But still number of nodes are huge and therefore we cannot define the full graph initially. Instead we will use perm_apply method to find the neighboring nodes at run time. 
          
          Also to reduce the average time of the algo we will use 2 way BSF to find the shortest path otherwise we may end up visiting 24! nodes.
          
      * Termination:
      
          The maximum number of turns required to solve the cube is up to 14 quarter turns only. So, if the algo hadn't found the answer in 14 turns then we can terminate the code and return "this configuration of rubik cube cannot be solve" otherwise it will return the answer. Since, we are using 2 way BSF we will terminate the code at 16th iteration.
          
    
    
    
        
