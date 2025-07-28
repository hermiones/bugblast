# 🔬 FUTURE TEST CASES for BugBlast

This document outlines the upcoming testing ideas and scenarios to evaluate and enhance the effectiveness, stability, and usability of BugBlast — a simple fuzzing tool for security testing.

---

## 🛠 FUNCTIONAL TEST CASES

### ✅ TC-001: Basic GET URL Fuzzing
- **Pre-condition**: Valid URL provided
- **Steps**: Run fuzzer with basic SQL payloads
- **Expected**: Payloads get appended; tool prints response codes

---

### ✅ TC-002: Empty Payload List
- **Steps**: Provide an empty or missing payload file
- **Expected**: Tool handles it gracefully with a warning

---

### ✅ TC-003: Invalid URL Format
- **Steps**: Give malformed URLs (e.g., `htp:/badlink`)
- **Expected**: Tool throws validation error, doesn’t crash

---

### ✅ TC-004: URL with Existing Query Params
- **Steps**: Use `https://site.com/page?search=test`
- **Expected**: Payload is injected properly after the query param

---

### ✅ TC-005: URL with Fragment (#)
- **Steps**: URL with a fragment like `site.com/page#section`
- **Expected**: Payload should not be added after fragment

---

## 🔐 SECURITY-AWARE TEST CASES

### 🚨 TC-010: SQL Error Injection Check
- **Steps**: Inject `' OR '1'='1`, `'--`, etc.
- **Expected**: Tool captures any SQL-related errors (e.g. `syntax`, `database`)

---

### 🚨 TC-011: XSS Reflected Payload Test
- **Steps**: Inject `<script>alert(1)</script>`
- **Expected**: Look for reflection in HTML body

---

### 🚨 TC-012: 403/401 Auth Required Page
- **Steps**: Fuzz an endpoint requiring login
- **Expected**: Ensure tool handles/ignores unauthorized pages cleanly

---

## 📉 NEGATIVE TEST CASES

### ❌ TC-020: Nonexistent Domain
- **Steps**: Try `http://fakedomain.abc`
- **Expected**: Tool catches connection error without breaking loop

---

### ❌ TC-021: No Internet Connection
- **Steps**: Disable internet and run tool
- **Expected**: Print retry message or exit gracefully

---

### ❌ TC-022: Long Payload
- **Steps**: Use a 10,000-char string as a payload
- **Expected**: Tool doesn’t crash or truncate it silently

---

## 🔁 STRESS & PERFORMANCE TEST CASES

### 💣 TC-030: 1000 URLs in One Go
- **Steps**: Feed a list of 1000 test URLs
- **Expected**: Tool handles memory, doesn’t leak or freeze

---

### 💣 TC-031: 500 Payloads on One URL
- **Steps**: Add 500+ payloads in the list
- **Expected**: It completes fuzzing all inputs without error

---

### 💣 TC-032: Slow Server Response
- **Steps**: Fuzz an intentionally slow API (5+ seconds)
- **Expected**: Tool respects timeout settings or handles delays

---

## 🧩 EDGE CASES

### 🤯 TC-040: Payloads with Special Characters
- **Steps**: Add payloads with unicode, emoji, etc.
- **Expected**: Tool URL-encodes where needed or handles safely

---

### 🤯 TC-041: URLs Ending with Slash
- **Steps**: `https://site.com/`
- **Expected**: Tool appends payload correctly without breaking path

---

## 📦 FILE & LOG TEST CASES

### 📁 TC-050: Log File Creation
- **Steps**: Run tool and verify output logs created
- **Expected**: Logs include timestamp, URL, payload used, status code

---

### 📁 TC-051: Duplicate Payload Handling
- **Steps**: Add repeated payloads in list
- **Expected**: Tool skips or handles them without redundant requests

---

### 📁 TC-052: Unicode Response Handling
- **Steps**: Fuzz a multilingual site
- **Expected**: No crashes from unexpected character encodings

---

## 🔮 FUTURE INTEGRATION TESTS

### 🤖 TC-060: Integrate with Selenium
- **Steps**: Fuzz input fields instead of just URL
- **Expected**: Payloads auto-fill and submit forms

---

### 🔐 TC-061: Authenticated Session Testing
- **Steps**: Pass headers/cookies/token
- **Expected**: Tool uses session info to access protected routes

---

### 🧠 TC-062: Response Diffing/Alerting
- **Steps**: Run fuzzing twice on same URL
- **Expected**: Tool shows differences in responses, highlights anomaly

---

## 🏁 TO-DO

- [ ] Add test data generator
- [ ] Implement unit tests for core methods (input, payload injection)
- [ ] Add test cases for CLI flags & user errors
