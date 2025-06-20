# GitHub API Documentation Summary

This file documents the GitHub API endpoints used in the project

# 1. Search Repositories
  * Endpoint: `GET https://api.github.com/search/repositories?q={query}`  
  * Purpose: Retrieves public repositories matching a search term (in this case python was used)

# 2. Get Repository Commits
  * Endpoint: `GET https://api.github.com/repos/{owner}/{repo}/commits`  
  * Purpose: Fetches a list of commits for a specific repository (for this request, octocat/Hello-World repository)

# 3. Get Repository Contents
  * Endpoint: `GET https://api.github.com/repos/{owner}/{repo}/contents/{path}`  
  * Purpose: Retrieves the file and folder structure of a given path (for this request, octocat/Hello-World repository)

# Pagination
  * All endpoints supporting lists return 30 results per page by default
  * To retrieve additional pages:  
    `?page=2`, `?per_page=100`, etc

# Rate Limits
  * Authenticated: 5,000 requests/hour
  * Unauthenticated: 60 requests/hour
