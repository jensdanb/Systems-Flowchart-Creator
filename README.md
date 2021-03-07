# Systems-Flowchart-Creator

Overview / analogy

The program's job is to simulate systems that can be described with differential equations, as a flowchart through function blocks.
Values pass from one node to the next, always the same direction. Different nodes can create, change, and/or sum values, before passing it downstream.
A connection is a one-way street: Information is passed only one way, from the upstream node to the downstream.

The analogy is 'passing buckets', with each node doing something to the bucket content. Nodes come in three categories: 

'Source' nodes create a bucket, add initial content and pass it on.
'Function' nodes do most of the mathematical functions, changing the content or combining multiple buckets before passing on their output. 
'Sink' nodes are end stations, keeping a list of the buckets received. Your system should produce some dynamic output, so put a sink at the main output to see what you got. Add other places if you want to. They don't affect the system. 
