name: GHES/GHEC repos to GitHub migration [GEI]
description: Perform a migration of repositories from GitHub Enterprise Server or Cloud to GitHub using GEI
title: "GHES/GHEC repos to GitHub migration [GEI]: "
labels: ["migration", "GEI"]
assignees: []
body:
  - type: markdown
    attributes:
      value: |
        Thanks for initiating a repository migration. Please fill out the information below to get started.

  - type: textarea
    id: repositories
    attributes:
      label: Repositories
      description: Please enter the repositories you would like to migrate from GitHub Enterprise Server to GitHub Enterprise Cloud.
      placeholder: |
        https://github.com/your-org/your-repository-1
        https://github.com/your-org/your-repository-2
    validations:
      required: true

  - type: dropdown
    id: organization
    attributes:
      label: Target Organization
      description: Please select the Target Organization
      options:
        - mgmri-commerce
        - mgmri-source
    validations:
      required: true

  - type: dropdown
    id: visibility
    attributes:
      label: Target repository visibility
      description: Please select the visibility for the repositories on GitHub Enterprise Cloud after they have been migrated.
      options:
        - Private
        - Internal
        - Mirror
    validations:
      required: true

  - type: markdown
    attributes:
      value: |
        ## Workflow Trigger
        After submitting this issue, you can trigger specific workflows by commenting with the workflow file name. Valid workflow files are:
        - bootstrap.yml
        - migration-delete-gei-repositories.yml
        - migration-github-repos-gei.yml
        - migration-prepare.yml
        - shared-github-enterprise-cloud-gei.yml
        - stale.yml

  - type: checkboxes
    id: terms
    attributes:
      label: Code of Conduct
      description: By submitting this issue, you agree to follow our [Code of Conduct](https://example.com/coc)
      options:
        - label: I agree to follow this project's Code of Conduct
          required: true
