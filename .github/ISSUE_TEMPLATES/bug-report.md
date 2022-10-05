name: Bug Report
description: File a bug report
title: "[Bug]: "
labels: ["bug"]
body:
  - type: markdown
    attributes:
      value: |
        Any bug report is well appreciated!
      required: false
  - type: textarea
    id: explain-bug
    attributes:
      label: Explain the bug!
      description: Also tell us, what did you expect to happen?
      placeholder: What happened?
      value: "A bug happened!"
    validations:
      required: true
  - type: textarea
    id: reproduce-bug
    attributes:
      label: How do you recreate this bug?
      description: Any and all steps are appreciated!
      placeholder: How did the bug occurr?
      value: "First you..."
    validations:
      required: true
  - type: textarea
    id: logs
    attributes:
      label: Relevant log output
      description: Please copy and paste any relevant log output. This will be automatically formatted into code, so no need for backticks.
      render: shell