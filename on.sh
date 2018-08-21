#!/bin/bash
flag=/root/ruter/ruter.flag
touch $flag

while [ -f $flag ]; do
        nextbus=$(/root/ruter/31_s.py)
        echo "Neste buss om $nextbus sek"
if [[ $nextbus -lt 300 && $nextbus -gt 220 ]]; then
                echo 'Passe tid. Setter gul farge i gang'
                /root/ruter/lights.py yellow
        elif [[ $nextbus -lt 220 && $nextbus -gt 130 ]]; then
                echo 'Skynde seg. Setter rød farge i gang'
                /root/ruter/lights.py red
        else
                echo 'Kan vente litt. Setter normal farge i gang'
                /root/ruter/lights.py normal
        fi
        sleep 30
done
