# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [v1.0.0] - 2025-08-27
### 🚀 Added
- Core real-time trip matching system.
- API v1 routes (`/rides`, `/metrics`).
- API key authentication middleware.
- Database manager with connection handling.
- Schemas for request, ride, and user validation.
- Cost calculation engine (active providers, cost matrix, destination checks).
- Firebase + socket notification system.
- Matching algorithm + queue worker.
- Ride matcher + route distance service.
- Error handling, logging, and Sentry integration.
- Gunicorn production configuration.

### 🐛 Fixed
- N/A (first stable release).

### 🔧 Notes
- First official stable release, ready for production.
