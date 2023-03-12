.. image::
    :target:
    :align: center
    :alt: Enigmatic | Catalyst

|version tag|
|version status|
|forum|
|discord|
|twitter|

=========  ===============           ================
Service    Master                    Develop
---------  ---------------           ----------------
CI Badge   |travis-master|           |travis-develop|
=========  ===============           ================

Builds on Catalyst.
Catalyst is an algorithmic trading library for crypto-assets written in Python.
It allows trading strategies to be easily expressed and backtested against 
historical data (with daily and minute resolution), providing analytics and 
insights regarding a particular strategy's performance. Catalyst also supports
live-trading of crypto-assets starting with four exchanges (Binance, Bitfinex, Bittrex,
and Poloniex) with more being added over time. Catalyst empowers users to share 
and curate data and build profitable, data-driven investment strategies. Please 
visit `catalystcrypto.io <https://www.catalystcrypto.io>`_ to learn more about Catalyst.

Catalyst builds on top of the well-established 
`Zipline <https://github.com/quantopian/zipline>`_ project. We did our best to 
minimize structural changes to the general API to maximize compatibility with 
existing trading algorithms, developer knowledge, and tutorials. Join us on the 
`Catalyst Forum <https://forum.catalystcrypto.io/>`_ for questions around Catalyst,
algorithmic trading and technical support. We also have a 
`Discord <https://discord.gg/SJK32GY>`_ group with the *#catalyst_dev* and 
*#catalyst_setup* dedicated channels.

Overview
========

-  Ease of use: Catalyst tries to get out of your way so that you can 
   focus on algorithm development. See 
   `examples of trading strategies <https://github.com/enigmampc/catalyst/tree/master/catalyst/examples>`_ 
   provided.
-  Support for several of the top crypto-exchanges by trading volume:
   `Bitfinex <https://www.bitfinex.com>`_, `Bittrex <http://www.bittrex.com>`_,
   `Poloniex <https://www.poloniex.com>`_ and `Binance <https://www.binance.com/>`_.
-  Secure: You and only you have access to each exchange API keys for your accounts.
-  Input of historical pricing data of all crypto-assets by exchange, 
   with daily and minute resolution. See 
   `Catalyst Market Coverage Overview <https://www.enigma.co/catalyst/status>`_.
-  Backtesting and live-trading functionality, with a seamless transition
   between the two modes.
-  Output of performance statistics are based on Pandas DataFrames to 
   integrate nicely into the existing PyData eco-system.
-  Statistic and machine learning libraries like matplotlib, scipy, 
   statsmodels, and sklearn support development, analysis, and 
   visualization of state-of-the-art trading systems.
-  Addition of Bitcoin price (btc_usdt) as a benchmark for comparing 
   performance across trading algorithms.

Go to our `Documentation Website <https://enigmampc.github.io/catalyst/>`_.




.. |version tag| image::
   :target:

.. |version status| image::
   :target:
   
.. |forum| image::
   :target:

.. |discord| image::
   :target:

.. |twitter| image::
   :target:

.. |travis-develop| image::
   :target:

.. |travis-master| image::
   :target:




