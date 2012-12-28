from datetime import datetime
from finance.utils.BasicUtils import *
from finance.sim import MarketSimulator

sim = MarketSimulator('./data')
sim.initial_cash = 1000000
sim.simulate("MarketSimulator_orders.csv")

print(sim.portfolio[0:10])

print('Total Return:', total_return(sim.portfolio))
print(sharpe_ratio(sim.portfolio, extraAnswers=True))

import matplotlib
matplotlib.use('Qt4Agg') # Probably most people dont need this line
import matplotlib.pyplot as plt
sim.portfolio.plot()
plt.show()