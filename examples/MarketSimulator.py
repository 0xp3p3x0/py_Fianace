from datetime import datetime
import matplotlib.pyplot as plt
from finance.utils.BasicUtils import *
from finance.sim import MarketSimulator

sim = MarketSimulator('./data')
sim.initial_cash = 1000000
sim.load_trades("MarketSimulator_orders.csv")
sim.simulate()

print(sim.portfolio[0:10])

print('Total Return:', total_return(sim.portfolio))
print(sharpe_ratio(sim.portfolio))

sim.portfolio.plot()
plt.show()