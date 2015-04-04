#!/usr/bin/env bash
epydoc --html ./* -o api --name NewAppearances
http-server ./api/ -p 9999 -a localhost
