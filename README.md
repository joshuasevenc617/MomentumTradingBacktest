# Momentum Trading Strategy Project
### Objective:
Build and backtest a momentum trading strategy using historical stock data.

### Key Outcomes:
- Implement a data-driven trading algorithm.
- Evaluate performance using metrics such as the Sharpe ratio and drawdowns.
- Document your approach and findings in a reproducible format (e.g., GitHub, Jupyter Notebooks).

### Tools:
- Python (pandas, numpy, matplotlib)
- A backtesting library (Backtrader or Zipline)
- Data source: Yahoo Finance API

### Data Source:
- Yahoo Finance API: https://pypi.org/project/yfinance/
    - Apple stock data from 2020-01-01 to 2021-01-01, reasons of choise:
        - Demonstrative Purposes:
            It’s often helpful to start with a fixed, known period so you can see how your code behaves with a complete dataset.
        - Volatile and Calm Periods:
            The 2020–2021 period includes both volatility (e.g., during the COVID-19 market crash) and recovery phases, offering a varied market environment to test your strategy.
        - Historical Testing:
            Backtesting typically uses historical data to evaluate how a strategy would have performed under real market conditions.
