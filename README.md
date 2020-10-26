# my_scripts
 Collection of programs of various complexity I find useful.
 
##### [alarm_clock](https://github.com/Jac08H/my_scripts/tree/master/alarm_clock)
* Language: Python3
* Description: Plays an alarm sound after specified time period.
* Usage: `./alarm_clock.py [-s SECONDS] [-m MINUTES]`
* Example: `./alarm_clock.py -s 0 -m 5`
##### [crypto_price](https://github.com/Jac08H/my_scripts/tree/master/crypto_price)
* Language: Python3
* Description: Gets price of cryptocurrencies using [Cryptocompare's](https://www.cryptocompare.com/) API. 
* Usage: `./crypto_price.py [from_symbols] [to_symbols]`
* Example: `./crypto_price.py btc usd,eur`
##### [sms_parser](https://github.com/Jac08H/my_scripts/tree/master/sms_parser)
* Language: Python3
* Description: Parse an .xml file containing text messages
* Usage: `./sms_parser.py`
* Example:
```
$ ./sms_parser.py
Enter filename[xml filename]
Enter sender's name[sender's name]
Enter receiver's name[receiver's name]
```
##### [wma2mp3](https://github.com/Jac08H/my_scripts/tree/master/wma2mp3)
* Language: Python3
* Description: Converts wma files to mp3 inplace and removes wma files. 
* Usage: `./wma2mp3.py [path]`
##### [youtube_download](https://github.com/Jac08H/my_scripts/tree/master/youtube_download)
* Language: Bash
* Description: Downloads mp3 from youtube videos using [youtube-dl](https://github.com/rg3/youtube-dl).
* Usage: `./youtube_dl.sh` 
* Example:

```
$ ./youtube_dl.sh
URL:
[youtube URL]
name:
[name]
```
