#!/bin/bash
cd /home/kavia/workspace/code-generation/event-management-api-7e972b0f/event_management_backend
source venv/bin/activate
flake8 .
LINT_EXIT_CODE=$?
if [ $LINT_EXIT_CODE -ne 0 ]; then
  exit 1
fi

