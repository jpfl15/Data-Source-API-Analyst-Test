# Data-Source-API-Analyst-Test

This repository contains the solution to the Improvado Data Source API Analyst assignment.  
It demonstrates API exploration, data extraction, troubleshooting, and documentation using GitHub's public REST API.

# Repository Structure

  - Content/
      * API_Documentation.md
      * github_api_auth.py
      * github_api_utils.py
      * troubleshooting.md
  - Postman_Collection
      * github_api_collection.json
      * github_api_test.ipynb
  - README.md

# Assignment Overview

  The goal of this assignment was to:
    - Explore the GitHub API and identify endpoints
    - Extract data from:
      * Repository search
      * Commits
      * Contents
    - Handle authentication, pagination, and rate limits
    - Test requests using Postman and Google Colab
    - Provide reusable scripts and documentation

# Postman Collection

  Located in /Postman_Collection/github_api_collection.json

  Included requests:
    * Search repositories with query 'Python'
    * Fetch commits from 'octocat/Hello-world'
    * Retrieve contents from 'octocat/Hello-world'

  All requests include necessary headers and are authenticated using a GitHub token.

# Google Colab Notebook

  Located in /Postman_Collection/github_api_test.ipynb

  Includes:
  - GitHub token setup using getpass() for security
  - Headers setup with 'Bearer' authorization
  - API requests to search repositories, get commits, and list contents
  - Pagination support across multiple pages of search results
  - Error handling for unauthorized access and invalid requests
  - Response formatting using 'json.dumps(..., indent=2)' for readability

# Content Folder

Includes Python scripts and documentation:

  * github_api_auth.py: Sets up GitHub API headers using a token 
  * github_api_utils.py: Contains reusable functions for safe requests, pagination, and endpoint-specific calls 
  * API_Documentation.md: Summary of GitHub API endpoints used 
  * troubleshooting.md: Common error cases and how they were resolved

# Reflections

Working on this assignment, I gained practical experience working with real-world APIs. What I can highlight from what I learned is:

- Learning the difference between 'path', 'query', and 'body' parameters, and when each is used in REST APIs.
- Understanding how to use 'authorization tokens' to securely access GitHub's REST API.
- Implementing request 'headers', such as 'Authorization' and 'Accept', to ensure proper authentication and response formats.
- Handling 'rate limits' imposed by APIs and how to check or avoid exceeding them.
- Creating reusable Python functions and troubleshooting common HTTP errors like 401 and 404.

# Technologies Used

- Postman
- Python (requests, json)
- Google Colab
- GitHub REST API
