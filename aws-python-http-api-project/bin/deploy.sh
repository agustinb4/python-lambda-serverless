#!/bin/bash

ENV=$1

case $ENV in
  local)
    echo Deploying to local
    npx serverless offline --stage $ENV
    ;;
  dev)
    echo Deploying to dev
    npx serverless deploy --stage $ENV
    ;;
  pre-prod)
    echo Deploying to pre-prod
    npx serverless deploy --stage $ENV
    ;;
  prod)
    echo Deploying to prod
    npx serverless deploy --stage $ENV
    ;;
  *)
    echo "Env not found: $ENV, try ./deploy.sh (local|dev|prod)"
    ;;
esac

