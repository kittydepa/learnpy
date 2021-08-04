# Task

Create a command line tool for converting between universally unique identifiers (UUIDs) and a proprietary representation known as a "device identifier". The format is described in an appendix at the end of this document.

The tool should allow a user to specify and provide a UUID or device ID, and the tool should convert the input to the appropriate output, and print it to the terminal for the end user to consume.

## Requirements

### For juniors or interns

- The application should use a command line parsing library or module
- The application should have separate flags or subcommands for the two required functions
- Help text should briefly describe how to use the tool

### For intermediates

- Everything in the previous section, and:
- The application should validate that the input is a valid device identifier
- The application should allow printing either input as an unsigned 128-bit integer
  - In decimal
  - In hexadecimal
- The application should allow taking an unsigned 128-bit integer as an input
  - In decimal
  - In hexadecimal
- The application should be able to print a richer output describing the meaning of each of the fields of the identifier

## Test cases

You can use the following test cases to confirm your understanding of the problem and confirm that your tool behaves as required.

Note: the capitalisation in UUIDs does not matter, but **device identifiers are case-sensitive, capital letters matter.**

### Device identifier to UUID

- `E0-010FAB-0A-210521-00010A` → `00000000-00E0-010F-AB0A-21052100010A`
- `F0-405B97-50-121212-FBFD53` → `00000000-00F0-405B-9750-121212FBFD53`

### UUID to Device Identifier

- `00000000-0080-47E9-85B2-20010119E272` → `80-47E985-B2-200101-19E272`
- `00000000-00A9-4D19-BAF9-99123149DBE9` → `A9-4D19BA-F9-991231-49DBE9`


# Appendix: Device Identifier Specification

## Purpose

The problems that this device identifier scheme solves are as follows:

- Identifying what "object" the number is an identifier for
- Its production date
- The semantic version of the object
- The factory code for the object (ie, a known identifier for a factory or office where production of the object occurred; this value is contextual)
- The sequence number (ie the iterating counter of item production order)

## Structure of a device identifier

All values (except date/month/year) are in hexadecimal, and the count is the number of these hexadecimal values.

Date/month/year is encoded in ["binary encoded decimal"](https://en.wikipedia.org/wiki/Binary-coded_decimal) – ie it's just decimal. Don't overthink it.

| Placeholder | Count (characters) | Count (bytes) | Purpose | Valid Values |
| --- | --- | --- | --- | --- |
| O | 2 | 1 | Object identifier | 00 .. FF (hex) |
| X | 2 | 1 | Major version | 00 .. FF (hex) |
| Y | 2 | 1 | Minor version | 00 .. FF (hex) |
| Z | 2 | 1 | Patch version | 00 .. FF (hex) |
| F | 2 | 1 | Factory identifier | 00 .. FF (hex) |
| y | 2 | 1 | Two-digit year | 00 .. 99 (decimal) |
| m | 2 | 1 | Two-digit month | 01 .. 12 (decimal) |
| d | 2 | 1 | Two-digit day | 01 .. 31 (decimal) |
| S | 6 | 3 | Sequence number | 000000 .. FFFFFF (hex) |

Total bytes of data: 11 – (88 bits of data, leaving 40 more bits for future extension)

## Parsing the device identifier

The rules for parsing the device identifier in a certain way are determined by the object identifier portion of the device identifier and must be the prefix of the device identifier. A corollary of this rule is that a device identifier format change necessitates a change in object identifier prefix.

This is the pattern for how a device identifier is represented when printed:

`OO-XXYYZZ-FF-yymmdd-SSSSSS`

Example:

`E0-010FAB-0A-210521-00010A`

If we break this example down into fields:

- Object identifier: 0xE0 (224)
- Major version: 0x01 (1)
- Minor version: 0x0F (15)
- Patch version: 0xAB (171)
- Factory identifier: 0x0A (10)
- Production year: 2021
- Production month: 5 (May)
- Production day: 21
- Sequence number: 0x10A (266)

### Alternative representations

Where supported and efficient, the identifier SHOULD be stored and interchanged as a binary blob (or sequence of bytes, if this is your preferred phrase for the same thing).

For certain database and interchange purposes, the data MAY be stored as a UUID for data storage and interchange purposes only, and is to be treated as if it were a 128-bit integer.

You MUST NOT display a device identifier in any other representation than described in this appendix. UUID and other representations exist only for the purposes of compatibility with other systems (such as databases) and for efficient transfer of data over-the-wire.

## Future changes to the device identifier specification

The rules for device identifier changes are as follows:

- A device identifier may not ever encode more than 128-bits of representable data, meaning no more than 32 hexadecimal characters
- We may change the length of the device identifier at any time, provided the previous rule is still met

