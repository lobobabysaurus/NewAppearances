#!/usr/bin/env bash
epydoc --html ../* -o api --name NewAppearances
../node_modules/.bin/http-server ./api/ -p 9999 -a localhost
