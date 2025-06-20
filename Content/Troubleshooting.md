# Troubleshooting Guide

# 1. 401 Unauthorized
  * Cause: Missing or invalid GitHub token.  
  * Solution: Ensure the token is valid, has correct permissions, and is passed in the Authorization header.

# 2. Rate Limit Exceeded
  * Cause: Too many requests without authentication.  
  * Solution: Use an authenticated request with a personal access token.

# 3. 404 Not Found
  * Cause: Wrong repository name or path.  
  * Solution: Double-check the `owner/repo` and endpoint formatting.
