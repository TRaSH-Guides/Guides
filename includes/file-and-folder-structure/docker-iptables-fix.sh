#!/bin/bash
currentAttempt=0
totalAttempts=10
delay=15

while [ $currentAttempt -lt $totalAttempts ]; do
    currentAttempt=$(($currentAttempt + 1))

    echo "Attempt $currentAttempt of $totalAttempts..."

    result=$(iptables-save)

    if [[ $result =~ "-A DOCKER -i docker0 -j RETURN" ]]; then
        echo "Docker rules found! Modifying..."

        iptables -t nat -A PREROUTING -m addrtype --dst-type LOCAL -j DOCKER
        iptables -t nat -A PREROUTING -m addrtype --dst-type LOCAL ! --dst 127.0.0.0/8 -j DOCKER

        echo "Done!"

        break
    fi

    echo "Docker rules not found! Sleeping for $delay seconds..."

    sleep $delay
done
