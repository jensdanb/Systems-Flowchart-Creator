# For now, this is a test lab. Will move that to separate file and put actual main code here later.

from flowchart import *


def print_tickers(nodes):
    print([f"{node.name} is at {node.ticker}" for node in nodes])


# Setup the blocks
source1a = Source('Source 1a', 1)
gain2a = Gain('Gain 2a', 2)
sink3a = Sink('Sink 3a', 1 / 2)  # Back to gain of 1 for the system as a whole

# Connect the blocks to a system
print(f"{source1a.name} has receivers {source1a.downstream}")
source1a.add_connection(gain2a)
gain2a.add_connection(sink3a)
print(f"{source1a.name} has receivers {source1a.downstream}")
print(f"{gain2a.name} has {gain2a.upstream} upstream.")
print(f"{gain2a.name} has {gain2a.downstream} downstream.")

print("------")
# Run and print output
while source1a.ticker <= 1:
    source1a.send_random(7)
    print("------")

# Check some things and plot the sink's history
print(f"Source 1a has {source1a.downstream} downstream.")
source1a.break_connection(gain2a)
print(f"{source1a.name} has {source1a.downstream} downstream.")
print(sink3a.sunk)
sink3a.plot_sink()
