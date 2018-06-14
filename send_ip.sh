IP=`ifconfig | grep broadcast`

curl -XPOST -d "token=xoxp-token xxxxxxx" -d "pretty=1" -d "channel=@d.kanai" -d "username=Bot" "https://slack.com/api/chat.postMessage" -d "text=$IP"
