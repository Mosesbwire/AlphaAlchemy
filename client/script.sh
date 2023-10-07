#!/bin/sh

touch .env

echo "VITE_HOST=$HOST" >> .env
echo "VITE_PORT=$PORT" >> .env