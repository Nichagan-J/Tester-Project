#!/bin/bash

echo "Running Postman Collections using Newman..."

# Run Restful-Booker using Dev Environment
newman run ../collections/Restful-Booker.postman_collection.json \
  -e ../environments/dev.postman_environment.json \
  -r cli,json,htmlextra \
  --reporter-json-export ../reports/newman-result.json \
  --reporter-htmlextra-export ../reports/newman-report.html
  
echo "Tests Execution Completed!"