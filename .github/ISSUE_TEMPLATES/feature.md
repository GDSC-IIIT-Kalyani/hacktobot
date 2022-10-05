name: Feature Request
description: File a feature request
title: "[Request]: "
labels: ["request"]
body:
  - type: markdown
    attributes:
      value: |
        Any advice is well recieved!
      required: false
  - type: textarea
    id: explain-request
    attributes:
      label: Explain the request!
    validations:
      required: true
  - type: textarea
    id: additional
    attributes:
      label: Additional info
      description: Anything else we need to know?
	validations:
      required: false