docker build -t arm . -q > /dev/null
result=$(docker run --platform linux/arm64/v8 -i arm | grep -oE 'Result: [0-9a-fA-F]+' | cut -d' ' -f2)
result=$(echo "obase=16; $result" | bc | tr '[:upper:]' '[:lower:]')
echo 'picoCTF{'$result'}'

