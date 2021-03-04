#!/usr/bin/env bash

docker=$(which docker)

$docker build . -t feature-flag/python:dev
