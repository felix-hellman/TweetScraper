IFS=$'\n'
set -f
for i in $(cat < "twitterlist"); do
	wget -O- $i  2>/dev/null | python tweetscraper.py
done



