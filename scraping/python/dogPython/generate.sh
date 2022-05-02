#!/bin/bash

BUFF=
SELECTOR=
FULL=0
NAME="myelem"
URL=$1
shift


while [[ $# -gt 0 ]]; do
    key=$1

    case $key in
    -h|--help)
        echo "USAGE: ./generate.sh [URL]"
        echo "      -s|--selector [Selector]  Define the precise selector to get instead of getting the full data"
        echo "      -n|--name [Name]          Define file's name before generation (default = myelem.html)"
        exit
        ;;
    -s|--selector)
        SELECTOR=$2
        shift
        shift
        ;;
    -n|--name)
        NAME=$2
        shift
        shift
        ;;
    -f|--full)
        FULL=1
        shift
        shift
        ;;
    *) #unknown
        BUFF+=$1
        shift
        ;;
    esac
done

echo "SELECTOR = $SELECTOR"
echo "NAME = $NAME"

if [[ -n $1 ]]; then
    echo "Error while getting arguments, $1 not recognized"
fi


if [[ -n $SELECTOR ]]; then
    echo "Executing scrappy with selector"
    scrapy crawl arg -a link="$URL" -a container="$SELECTOR" -a name="$NAME"
elif [[ $FULL == 1 ]]; then
    echo "Executing scrappy to scrape the whole page"
    scrapy crawl full -a link="$URL" -a name="$NAME"
else
    echo "Executing scrappy without selector"
    scrapy crawl fullSplit -a link="$URL" -a name="$NAME"
fi