# Penn Internet Analysis

This is an in-depth analysis of the internet connection speed at the University of Pennsylvania.

## Methodology

Metrics were collected from 2 computers, a laptop on AirPennNet (thinkpad) and one on the LAN network in Harnwell (desktop).
Both computers run Linux with a stable kernel and no modifications to the network stack.

The speed tests are performed against speedtest.net using the speedtest-cli python utility and cron.

### Flaws

Currently, the speedtest-cli script being used autoselects the server to test against, so it may change from test to test, though it's not as serious because many webservers and globally distributed so it may be more accurate despite being less precise.

Another issue is that the script only runs when my computer is running.
While my desktop remains on almost all the time, my laptop only stays on during normal waking hours, though that's when it matters most to me so not a huge problem.

## Reasoning
After experiencing annoying connection issues on my desktop on AirPennNet which nobody was able to resolve, I began recording the internet connection speed and ping every 15 minutes on both my computers.
Now that I have about a year's worth of data from 2 computers, I'll start doing some analysis to find problematic patterns.
