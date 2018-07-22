#!/bin/bash

set -e

python -m rasa_core.server -d $NUROBOT_HOME/Chatbots/projects/Lambton/models/dialogue -u $NUROBOT_HOME/Chatbots/projects/Lambton/models/nlu/default/current -p 5000 --debug -o $NUROBOT_HOME/Chatbots/projects/Lambton/logs/nuRobot-out.log --cors
