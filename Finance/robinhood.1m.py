#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

# <xbar.title>Robinhood</xbar.title>
# <xbar.version>v1.0</xbar.version>
# <xbar.author>Jonathan Grant</xbar.author>
# <xbar.author.github>jonathangrant</xbar.author.github>
# <xbar.desc>Shows your total portfolio value.</xbar.desc>
# <xbar.dependencies>python,robin_stocks</xbar.dependencies>

from robin_stocks import robinhood as me


me.login(username="yourusername", password="yourpassword")
data = me.profiles.load_portfolio_profile
start = data("equity_previous_close")
now = data("equity")
+color = 'white'
difference = float(now) - float(start)
if difference > 0:
    color = 'green'
elif difference < 0:
    color = 'red'
print('${:,.2f}|color={}'.format(float(now), color))
print('---')
print('Start of Day: ${:,.2f}|color={}'.format(float(start), 'white'))
print('Difference: ${:,.2f}|color={}'.format(float(difference), color))
