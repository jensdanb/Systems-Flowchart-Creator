""" Hettinger:
- Hold det konsist. Bruk innebygde funskjoner, eller lag egne for å korte ned og forenkle kode.
- Ikke planlegg inheritance. Skriv hver klasse manuelt, oppdag inheritance etter behov
- Løs det enkleste først. Alternativt, løs et annet, lignende problem før det faktiske problem.
"""

import matplotlib.pyplot as plt
import random
# import matplotlib.animation as animation
# from matplotlib import style


# Parent class
class Node:
    def __init__(self, name, gain):
        self.name = name

        self.current_value = 0
        self.gain = gain  # In most cases this is gain. Default should be 1.

        # Keeps a list of other nodes it is connected to. They are either upstream and downstream in the flowchart.
        self.downstream = []
        self.upstream = []

        self.ticker = 0  # System clock. += 1 and equal among all nodes for each loop of the whole system.

    # Connections come in pairs. To add or break a connection, call these on the upstream partner.
    # It also removes itself from its partner's list of upstream connections.
    def add_connection(self, downstream_partner):
        self.downstream.append(downstream_partner)
        downstream_partner.add_me(self)

    def break_connection(self, downstream_partner):
        self.downstream.remove(downstream_partner)
        downstream_partner.remove_me(self)

    # Used by upstream partner to remove itself. Don't call from elsewhere.
    def add_me(self, sender_to_add):
        self.upstream.append(sender_to_add)

    def remove_me(self, sender_to_remove):
        self.upstream.remove(sender_to_remove)

    def all_buckets_received(self):
        upstream_tickers = [partner.ticker for partner in self.upstream]  # List of upstream tickers
        return upstream_tickers.count(upstream_tickers[0]) == len(upstream_tickers)  # Checks they're all equal


class Source(Node):
    def send_constant(self, amplitude):
        print(f"{self.name} pass {amplitude} downstream")  # For testing only
        for connection in self.downstream:
            connection.pass_the_bucket(amplitude * self.gain)
        self.ticker += 1

    def send_random(self, rand_limit):
        bucket = rand_limit * random.random()
        print(f"{self.name} pass {bucket} downstream")  # For testing only
        for connection in self.downstream:
            connection.pass_the_bucket(bucket)
        self.ticker += 1


# "Gain" is a synonym for multiplication.
class Gain(Node):
    def pass_the_bucket(self, signal_in):
        self.current_value += signal_in

        if not self.all_buckets_received():
            print(f"{self.name} got {signal_in} and store {self.current_value} in bucket.")  # For testing only
            pass

        elif self.all_buckets_received():
            self.ticker += 1
            bucket = self.current_value * self.gain  # The gain happens here
            self.current_value = 0
            for connection in self.downstream:
                print(f"{self.name} got {signal_in} and pass {bucket} downstream")
                connection.pass_the_bucket(bucket)


class Sink(Node):
    def __init__(self, name, gain):
        super().__init__(name, gain)
        self.sunk = [0]             # History starts in origo. Remove both 0's to not
        self.tick_history = [0]

    def pass_the_bucket(self, signal_in):
        self.current_value += signal_in
        if not self.all_buckets_received():
            pass
        elif self.all_buckets_received():
            bucket = self.current_value * self.gain
            self.current_value = 0
            print(f'{self.name} received {signal_in} and stores {bucket} in sink.')  # For testing only
            self.sunk.append(bucket)
            self.tick_history.append(self.ticker + 1)
            self.ticker += 1

    def plot_sink(self):
        plt.plot(self.tick_history, self.sunk)
        plt.show()





"""
# Tidligere forsøk starter her
class Source(type):
    # Basic properties: Generates a signal. Has one output.
    # Comes in various types: [constant, sine, pwm, step, ramp]

    output_vector =


def source(signal_class, amplitude, frequency):
    output = True

    # Initial condition of the signal
    if signal_class in ['sine', 'step', 'ramp']:
        signal = 0
    elif signal_class in ['constant', 'cosine', 'pwm']:
        signal = amplitude
    else:
        print('Invalid signal_class. Try again')
        output = False

    update_interval = 0.001
    while output:
        print(signal)

"""
