# Systems-Flowchart-Creator

Overview / analogy

The program's job is to simulate systems that can be described with differential equations, as a flowchart through function blocks.
Values pass from one node (the "upstream" node) to the next ("downstream"), and only in that direction. 

The analogy is 'passing buckets', with each node doing something to the bucket content. Nodes come in three categories: 

'Source' nodes create a bucket, add initial content and pass it on.
'Function' nodes contain functions that it applies to each bucket before passing on downstream. Includes addition when buckets come from multiple upstream nodes. 
'Sink' nodes are end stations and/or passive measurement tools, recording all buckets received in chronological order. Can plot the list for you, so you can see a plot of the output that goes into that sink. Put these at the main system output and anywhere else you want to inspect system behaviour. As end stations, they are 'passive' and cannot affect any other nodes. 


Future plans after making the basics work with a GUI: 
- Ability to automatically generate the equivalent PDE matrix for the system you have created. 
  - Iterate over that matrix with Numpy instead of actually passing buckets between node classes, for better performance. 
  - Retain ability to 'manually' run the system, and compare results between the two methods. 
- As alternative to PDE matrix, generate the equivalent Transfer Function (Laplace domain). 
  - For many systems, gives even more accurate and performant result than the PDE matrix, especially for longer timescales. 
  - Compare output with bucket-passing and PDE matrix outputs. Can also view output in Laplace domain. 
- Functions to give the user automatically generated system properties, such as the mentioned PDE matrix, Transfer Function, but also Impulse Response, stability domains...
