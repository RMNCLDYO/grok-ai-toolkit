# Changelog

All notable changes to the project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2024-12-28

### Added
- Support for image detail parameter in vision mode
- File size validation (10MiB limit) for image uploads
- Proper message structure formatting for xAI Vision API

### Changed
- Updated FileHandler to handle image detail parameter:
  - `process_files()` now accepts detail parameter
  - `process_file()` passes detail to appropriate processing functions
  - `handle_upload_command()` supports detail parameter
- Modified base GrokBase class:
  - `handle_user_input()` now accepts image_detail parameter
- Updated Vision class to properly handle image parameters
- Improved message content structure to match xAI API specifications

### Fixed
- Fixed argument mismatch in `process_files()`
- Corrected message structure for text-only responses in vision mode
- Standardized image URL and base64 message formatting

### Technical Details
- Image detail parameter defaults to "high"
- File size limit enforced at 10MiB (10 * 1024 * 1024 bytes)
- Message content now properly structured as array of type-specific objects

## [1.0.1] - 10/28/2024

### Changed
- Changed repo name to 'grok-ai-toolkit'.

## [1.0.0] - 10/23/2024

### Added
- Initial release.
