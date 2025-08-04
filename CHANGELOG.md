# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.0.4] - 2025-08-05

### Added
- Changelog with comprehensive project history
- Python 3.12 and 3.13 support
- Manual PyPI release pipeline with version input
- Renovate dependency management
- Automated changelog generation based on conventional commits
- Author information in project metadata

### Changed
- Modernized packaging to be PEP 621 compliant
- Modernized GitHub Actions workflow for releases
- Updated to use trusted publishing for PyPI
- Updated actions/setup-python to v5
- Updated renovatebot/github-action to v43

### Fixed
- ActualGenerator: fix dc_2_power

## [0.0.2] - 2024-12-10

### Added
- Individual classes for each inverter domain
- More explicit implementations for inverter properties
- Support for multiple values per request
- Inverter make and name information

### Changed
- Refactored constants to use classes for better auto completion
- Improved example implementations
- Removed status code printing for cleaner output

## [0.0.1] - Initial Release

### Added
- Initial implementation of pykostal
- Basic communication with Kostal Piko inverters
- Core API functionality
